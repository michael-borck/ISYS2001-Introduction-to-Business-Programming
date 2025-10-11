#!/usr/bin/env python3
"""Automated Workflow with Validation and Remediation.

This script runs a complete CurriculumCreator workflow with automatic validation
and content consolidation. It detects issues like content similarity
and either merges similar content or regenerates it based on configuration.

Usage:
    python automated_workflow.py \
        --title "Course Title" \
        --week 1 \
        --topic "Course Topic" \
        --output-dir ./output \
        --similarity-threshold 0.7 \
        --auto-remediate

Requirements:
    - CurriculumCreator package installed
    - Anthropic API key set (for merging content)
    - Alternatively, OpenAI API key if --use-openai is specified
"""

import argparse
import sys
import logging
from pathlib import Path
import json
import shutil
from typing import Optional, Any

# Import CurriculumCreator components
try:
    from curriculumcreator.workflow import run_full_workflow
    from curriculumcreator.slide_linter import analyze_slide_modules
    from curriculumcreator.worksheet_linter import lint_worksheets
    from curriculumcreator.config import load_config, Settings
except ImportError as e:
    print(f"Error importing CurriculumCreator components: {e}")
    print("\nPossible solutions:")
    print("1. Install the package with all dependencies: pip install -e .")
    print(
        "2. Install missing dependencies manually: pip install tiktoken openai anthropic"
    )
    print("3. Make sure you're using the correct Python environment")
    sys.exit(1)

# Try to import Anthropic first (preferred)
try:
    import anthropic

    has_anthropic = True
except ImportError as e:
    print(f"Warning: Anthropic package not installed ({e}).")
    print("To enable content merging with Claude, install with: pip install anthropic")
    has_anthropic = False

# Fallback to OpenAI if Anthropic is not available
try:
    import openai

    has_openai = True
except ImportError as e:
    print(f"Warning: OpenAI package not installed ({e}).")
    print(
        "To enable content merging with OpenAI, install with: pip install openai tiktoken"
    )
    has_openai = False

if not has_anthropic and not has_openai:
    print(
        "WARNING: Neither Anthropic nor OpenAI packages are installed. Content merging will not be available."
    )
    print("Install at least one with: pip install anthropic openai")
    anthropic = None
    openai = None

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
    ],
)
logger = logging.getLogger("automated_workflow")

# Constants
DEFAULT_SIMILARITY_THRESHOLD = 0.7  # High similarity threshold for auto-remediation
AUTO_MERGE_THRESHOLD = 0.9  # Very high similarity for direct merging
ANTHROPIC_MODEL = (
    "claude-3-sonnet-20240229"  # Default Anthropic model for content merging
)
OPENAI_MODEL = "gpt-4"  # Default OpenAI model for content merging


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Run CurriculumCreator workflow with automatic validation and remediation"
    )
    # Basic workflow parameters
    parser.add_argument("--title", type=str, required=True, help="Course title")
    parser.add_argument("--week", type=int, required=True, help="Week number")
    parser.add_argument("--topic", type=str, required=True, help="Week topic")
    parser.add_argument("--context", type=Path, help="Optional path to context file")
    parser.add_argument(
        "--output-dir", type=Path, help="Output directory", default=Path("./output")
    )
    parser.add_argument("--config", type=Path, help="Path to configuration file")

    # Validation and remediation options
    parser.add_argument(
        "--similarity-threshold",
        type=float,
        default=DEFAULT_SIMILARITY_THRESHOLD,
        help=f"Similarity threshold for remediation (default: {DEFAULT_SIMILARITY_THRESHOLD})",
    )
    parser.add_argument(
        "--auto-remediate",
        action="store_true",
        help="Automatically remediate issues (merge similar content)",
    )
    parser.add_argument(
        "--regenerate-similar",
        action="store_true",
        help="Regenerate similar content instead of merging",
    )
    parser.add_argument(
        "--report-only",
        action="store_true",
        help="Only report issues without remediation",
    )

    # Content generation options
    parser.add_argument(
        "--skip-assessment",
        action="store_true",
        help="Skip generating assessment materials (FAQ, MCQ, etc.)",
    )
    parser.add_argument(
        "--single-format",
        action="store_true",
        help="Generate only a single format for each content type (instead of multiple formats)",
    )
    parser.add_argument(
        "--skip-slide-references",
        action="store_true",
        help="Skip including slide references in worksheets",
    )
    parser.add_argument(
        "--skip-answer-guides",
        action="store_true",
        help="Skip generating answer guides for worksheets",
    )
    parser.add_argument(
        "--combine-faqs",
        action="store_true",
        help="Combine all FAQ documents into a single file for assessment generation",
    )
    parser.add_argument(
        "--generate-html",
        action="store_true",
        help="Generate HTML versions of overview and FAQs",
    )

    # LLM options
    parser.add_argument(
        "--use-openai",
        action="store_true",
        help="Use OpenAI instead of Anthropic (Claude) for content merging",
    )
    parser.add_argument(
        "--llm-model",
        type=str,
        help="Specify a custom LLM model name (overrides defaults)",
    )

    # Output options
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    parser.add_argument(
        "--token-report",
        type=Path,
        help="Save token usage report to specified file (.json or .csv)",
    )

    return parser.parse_args()


def run_workflow(
    title: str,
    week: int,
    topic: str,
    context_path: Optional[Path] = None,
    output_dir: Optional[Path] = None,
    settings: Optional[Settings] = None,
    skip_assessment: bool = False,
    single_format: bool = False,
    skip_slide_references: bool = False,
    skip_answer_guides: bool = False,
    combine_faqs: bool = False,
    generate_html: bool = False,
    token_report_path: Optional[Path] = None,
) -> dict[str, Any]:
    """Run the initial full workflow and return results."""
    logger.info("Starting initial content generation workflow")

    # Configure settings for comprehensive workflow
    if settings:
        # Configure slide references based on parameters
        settings.workflow.worksheet_slide_references = not skip_slide_references

        # Configure assessment types based on parameters
        if not skip_assessment:
            settings.workflow.generate_shortanswer = True
            settings.workflow.generate_fillinblanks = True
            settings.workflow.generate_answer_guides = not skip_answer_guides
        else:
            # Skip all assessment types
            settings.workflow.generate_shortanswer = False
            settings.workflow.generate_fillinblanks = False
            settings.workflow.generate_answer_guides = False
            settings.workflow.generate_mcq = False
            settings.workflow.generate_faq = False

        # Configure multiple formats
        settings.formats.generate_multiple_formats = not single_format or generate_html

        # Configure combined FAQ creation
        settings.workflow.create_all_faqs = combine_faqs

        # Configure formats based on parameters
        if generate_html:
            # Always include HTML if generate_html is specified
            settings.formats.overview_formats = ["markdown", "html"]
            settings.formats.faq_formats = ["markdown", "html"]
        elif not single_format:
            # Use multiple formats if not restricted to single format
            settings.formats.overview_formats = ["markdown", "html"]
            settings.formats.faq_formats = ["markdown", "html"]
            settings.formats.mcq_formats = ["blackboard", "traditional"]
            settings.formats.shortanswer_formats = ["blackboard", "traditional"]
            settings.formats.fillinblanks_formats = ["blackboard", "traditional"]
        else:
            # Use Blackboard format for assessments when in single format mode
            settings.formats.mcq_format = "blackboard"
            settings.formats.shortanswer_format = "blackboard"
            settings.formats.fillinblanks_format = "blackboard"

    result = run_full_workflow(
        title=title,
        week=week,
        topic=topic,
        context_path=context_path,
        output_dir=output_dir,
        settings=settings,
        show_tokens=True,
        token_output_path=token_report_path,
    )

    # Convert result to dict for easier handling
    results_dict = {
        "overview_paths": [str(p) for p in result.overview_paths],
        "slide_paths": [str(p) for p in result.slide_paths],
        "worksheet_paths": [str(p) for p in result.worksheet_paths],
        "faq_paths": [str(p) for p in result.faq_paths],
        "mcq_paths": [str(p) for p in result.mcq_paths],
        "shortanswer_paths": [str(p) for p in result.shortanswer_paths],
        "fillinblanks_paths": [str(p) for p in result.fillinblanks_paths],
        "answer_guide_paths": [str(p) for p in result.answer_guide_paths],
    }

    logger.info(
        f"Workflow completed, generated {len(result.slide_paths)} slides and {len(result.worksheet_paths)} worksheets"
    )
    return results_dict


def validate_slides(slide_paths: list[Path], threshold: float) -> list[dict[str, Any]]:
    """Validate slides for similarity and return issues."""
    logger.info(f"Validating {len(slide_paths)} slide modules for similarity")

    # Convert string paths to Path objects
    slide_paths = [Path(p) if isinstance(p, str) else p for p in slide_paths]

    # Analyze similarity
    similarity_results = analyze_slide_modules(slide_paths, threshold)

    # Format results for reporting
    issues = []
    for result in similarity_results:
        issues.append(
            {
                "type": "slide_similarity",
                "level": result.level,
                "score": result.similarity_score,
                "module1": str(result.module1.path),
                "module2": str(result.module2.path),
                "topics": result.overlapping_topics,
                "recommendation": result.recommendation,
            }
        )

    logger.info(
        f"Found {len(issues)} slide pairs with similarity above threshold {threshold}"
    )
    return issues


def validate_worksheets(
    worksheet_paths: list[Path], threshold: float
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Validate worksheets for similarity and content issues."""
    logger.info(f"Validating {len(worksheet_paths)} worksheets")

    # Convert string paths to Path objects
    worksheet_paths = [Path(p) if isinstance(p, str) else p for p in worksheet_paths]

    # Get worksheet directory (assuming all worksheets are in the same directory)
    if worksheet_paths:
        worksheet_dir = worksheet_paths[0].parent
    else:
        logger.warning("No worksheets to validate")
        return [], []

    # Run linting
    similarity_results, content_results = lint_worksheets(
        worksheet_dir=worksheet_dir,
        threshold=threshold,
        pattern="*.md",
        check_content=True,
    )

    # Format similarity results
    similarity_issues = []
    for result in similarity_results:
        similarity_issues.append(
            {
                "type": "worksheet_similarity",
                "level": result.level,
                "score": result.similarity_score,
                "worksheet1": str(result.worksheet1.path),
                "worksheet2": str(result.worksheet2.path),
                "topics": result.overlapping_topics,
                "recommendation": result.recommendation,
            }
        )

    # Format content issues
    content_issues = []
    for result in content_results:
        if result.has_issues:
            for issue in result.content_issues:
                content_issues.append(
                    {
                        "type": "worksheet_content",
                        "issue_type": issue.issue_type,
                        "severity": issue.severity,
                        "description": issue.description,
                        "worksheet": str(result.worksheet.path),
                    }
                )

    logger.info(
        f"Found {len(similarity_issues)} worksheet similarity issues and {len(content_issues)} content issues"
    )
    return similarity_issues, content_issues


def merge_similar_content_with_llm(
    file1: Path,
    file2: Path,
    output_path: Path,
    use_openai: bool = False,
    custom_model: Optional[str] = None,
) -> bool:
    """Merge similar content using an LLM.

    Args:
        file1: Path to first file to merge
        file2: Path to second file to merge
        output_path: Path to save merged content
        use_openai: Whether to use OpenAI instead of Anthropic
        custom_model: Custom model name to use (overrides defaults)

    Returns:
        bool: True if merge was successful, False otherwise
    """
    # Check if the requested LLM is available
    if use_openai and not has_openai:
        logger.error("OpenAI package not installed but --use-openai was specified.")
        return False

    if not use_openai and not has_anthropic:
        if has_openai:
            logger.warning("Anthropic package not installed, falling back to OpenAI.")
            use_openai = True
        else:
            logger.error(
                "Neither Anthropic nor OpenAI packages are installed. Cannot merge content."
            )
            return False

    try:
        # Read the content of both files
        with open(file1, encoding="utf-8") as f1:
            content1 = f1.read()

        with open(file2, encoding="utf-8") as f2:
            content2 = f2.read()

        # Get file types
        file_type = "slide deck" if "module" in file1.stem else "worksheet"

        # Prepare the prompt for merging
        prompt = f"""I have two {file_type} files with similar content. Please merge them into a single coherent file that:

1. Eliminates duplication
2. Preserves all unique information from both files
3. Organizes content logically
4. Maintains the same markdown format as the input files

First file: {file1.name}
```
{content1}
```

Second file: {file2.name}
```
{content2}
```

Please provide only the merged content with no additional explanation or commentary. The output should be ready to save directly as a markdown file.
"""

        # Determine which model to use
        if custom_model:
            model_name = custom_model
        elif use_openai:
            model_name = OPENAI_MODEL
        else:
            model_name = ANTHROPIC_MODEL

        # Call the appropriate API to merge the content
        if use_openai:
            logger.info(f"Using OpenAI {model_name} to merge content")
            response = openai.chat.completions.create(
                model=model_name,
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert educational content editor.",
                    },
                    {"role": "user", "content": prompt},
                ],
                temperature=0.3,
                max_tokens=4000,
            )
            merged_content = response.choices[0].message.content
        else:
            logger.info(f"Using Anthropic {model_name} to merge content")
            client = anthropic.Anthropic()
            response = client.messages.create(
                model=model_name,
                max_tokens=4000,
                temperature=0.3,
                system="You are an expert educational content editor.",
                messages=[
                    {"role": "user", "content": prompt},
                ],
            )
            merged_content = response.content[0].text

        # Save the merged content
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(merged_content)

        logger.info(f"Successfully merged similar content into {output_path}")
        return True

    except Exception as e:
        logger.error(f"Error merging content: {str(e)}")
        return False


def remediate_similarity_issues(
    issues: list[dict[str, Any]],
    output_dir: Path,
    auto_remediate: bool = False,
    regenerate: bool = False,
    use_openai: bool = False,
    custom_model: Optional[str] = None,
) -> dict[str, Any]:
    """Remediate similarity issues by merging or regenerating content."""
    logger.info(f"Remediating {len(issues)} similarity issues")

    # Track remediated files for reporting
    remediated = {
        "merged": [],
        "regenerated": [],
        "skipped": [],
    }

    for issue in issues:
        # Only auto-remediate for high or very high similarity
        if issue["level"] in ["high", "very_high"]:
            file1 = Path(
                issue["module1"] if "module1" in issue else issue["worksheet1"]
            )
            file2 = Path(
                issue["module2"] if "module2" in issue else issue["worksheet2"]
            )

            # Determine if this is a slide or worksheet
            is_slide = "module1" in issue
            content_type = "slide" if is_slide else "worksheet"

            # Get file stem for merged output
            stem1 = file1.stem
            stem2 = file2.stem

            # Create a name for the merged file that includes both source files
            if is_slide:
                # Extract module numbers
                mod1_num = int(stem1.split("module")[1].split("_")[0])
                mod2_num = int(stem2.split("module")[1].split("_")[0])

                # Get the smaller number first for consistent naming
                if mod1_num <= mod2_num:
                    merged_stem = f"module{mod1_num:02d}_{mod2_num:02d}_merged"
                else:
                    merged_stem = f"module{mod2_num:02d}_{mod1_num:02d}_merged"
            else:
                # Extract activity numbers
                act1_num = int(stem1.split("activity")[1].split("_")[0])
                act2_num = int(stem2.split("activity")[1].split("_")[0])

                # Get the smaller number first for consistent naming
                if act1_num <= act2_num:
                    merged_stem = f"activity{act1_num:02d}_{act2_num:02d}_merged"
                else:
                    merged_stem = f"activity{act2_num:02d}_{act1_num:02d}_merged"

            merged_path = file1.parent / f"{merged_stem}{file1.suffix}"

            if auto_remediate and not regenerate:
                # Merge the content
                success = merge_similar_content_with_llm(
                    file1,
                    file2,
                    merged_path,
                    use_openai=use_openai,
                    custom_model=custom_model,
                )

                if success:
                    remediated["merged"].append(
                        {
                            "merged_path": str(merged_path),
                            "source_files": [str(file1), str(file2)],
                            "similarity_score": issue["score"],
                        }
                    )

                    # Move the original files to archive directory
                    backup_dir = output_dir / "original_files" / content_type
                    backup_dir.mkdir(parents=True, exist_ok=True)

                    # Move original files to backup
                    shutil.move(file1, backup_dir / file1.name)
                    shutil.move(file2, backup_dir / file2.name)

                    logger.info(f"Moved original files to {backup_dir}")
                else:
                    remediated["skipped"].append(
                        {
                            "files": [str(file1), str(file2)],
                            "reason": "Merge failed",
                        }
                    )
            elif auto_remediate and regenerate:
                # For future: implement regeneration logic
                # This would involve calling the generator again with more specific prompts
                # For now, mark as skipped with regeneration as the intended action
                remediated["skipped"].append(
                    {
                        "files": [str(file1), str(file2)],
                        "reason": "Regeneration not implemented yet",
                    }
                )
            else:
                # Just report the issue without remediation
                remediated["skipped"].append(
                    {
                        "files": [str(file1), str(file2)],
                        "reason": "Auto-remediation disabled",
                    }
                )
        elif "module1" in issue:
            remediated["skipped"].append(
                {
                    "files": [str(issue["module1"]), str(issue["module2"])],
                    "reason": f"Similarity level ({issue['level']}) below threshold for auto-remediation",
                }
            )
        else:
            remediated["skipped"].append(
                {
                    "files": [str(issue["worksheet1"]), str(issue["worksheet2"])],
                    "reason": f"Similarity level ({issue['level']}) below threshold for auto-remediation",
                }
            )

    return remediated


def generate_report(
    workflow_results: dict[str, Any],
    slide_issues: list[dict[str, Any]],
    worksheet_similarity_issues: list[dict[str, Any]],
    worksheet_content_issues: list[dict[str, Any]],
    remediation_results: dict[str, Any],
    output_dir: Path,
) -> Path:
    """Generate a detailed validation and remediation report."""
    report = {
        "workflow_results": workflow_results,
        "validation_results": {
            "slide_similarity_issues": slide_issues,
            "worksheet_similarity_issues": worksheet_similarity_issues,
            "worksheet_content_issues": worksheet_content_issues,
        },
        "remediation_results": remediation_results,
        "summary": {
            "total_slides": len(workflow_results["slide_paths"]),
            "total_worksheets": len(workflow_results["worksheet_paths"]),
            "slide_similarity_issues": len(slide_issues),
            "worksheet_similarity_issues": len(worksheet_similarity_issues),
            "worksheet_content_issues": len(worksheet_content_issues),
            "merged_content": len(remediation_results["merged"]),
            "regenerated_content": len(remediation_results["regenerated"]),
            "skipped_remediation": len(remediation_results["skipped"]),
        },
    }

    # Generate a pretty printed report
    report_path = output_dir / "validation_report.json"
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    # Also generate a text summary
    summary_path = output_dir / "validation_summary.txt"
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write("# CurriculumCreator Validation Report\n\n")
        f.write(
            f"Generated files: {len(workflow_results['slide_paths'])} slides, {len(workflow_results['worksheet_paths'])} worksheets\n\n"
        )

        f.write("## Validation Issues\n\n")
        f.write(f"- Slide similarity issues: {len(slide_issues)}\n")
        f.write(f"- Worksheet similarity issues: {len(worksheet_similarity_issues)}\n")
        f.write(f"- Worksheet content issues: {len(worksheet_content_issues)}\n\n")

        f.write("## Remediation Summary\n\n")
        f.write(f"- Merged content: {len(remediation_results['merged'])}\n")
        f.write(f"- Regenerated content: {len(remediation_results['regenerated'])}\n")
        f.write(f"- Skipped remediation: {len(remediation_results['skipped'])}\n\n")

        if remediation_results["merged"]:
            f.write("### Merged Files\n\n")
            for merge in remediation_results["merged"]:
                f.write(
                    f"- {merge['merged_path']} (from {', '.join(merge['source_files'])}, similarity: {merge['similarity_score']:.2f})\n"
                )
            f.write("\n")

        if remediation_results["skipped"]:
            f.write("### Skipped Remediations\n\n")
            for skip in remediation_results["skipped"]:
                f.write(f"- {', '.join(skip['files'])}: {skip['reason']}\n")

    logger.info(f"Generated report at {report_path} and summary at {summary_path}")
    return report_path


def main():
    """Run the automated workflow with validation and remediation."""
    args = parse_arguments()

    # Set up logging level
    if args.verbose:
        logger.setLevel(logging.DEBUG)

    # Load configuration
    settings = load_config(args.config) if args.config else None

    # Create output directory
    output_dir = args.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    # Step 1: Run the initial workflow
    workflow_results = run_workflow(
        title=args.title,
        week=args.week,
        topic=args.topic,
        context_path=args.context,
        output_dir=output_dir,
        settings=settings,
        skip_assessment=args.skip_assessment,
        single_format=args.single_format,
        skip_slide_references=args.skip_slide_references,
        skip_answer_guides=args.skip_answer_guides,
        combine_faqs=args.combine_faqs,
        generate_html=args.generate_html,
        token_report_path=args.token_report,
    )

    # Step 2: Validate the generated content
    slide_paths = [Path(p) for p in workflow_results["slide_paths"]]
    worksheet_paths = [Path(p) for p in workflow_results["worksheet_paths"]]

    slide_issues = validate_slides(slide_paths, args.similarity_threshold)
    worksheet_similarity_issues, worksheet_content_issues = validate_worksheets(
        worksheet_paths, args.similarity_threshold
    )

    # Step 3: Remediate issues if configured
    remediation_results = {
        "merged": [],
        "regenerated": [],
        "skipped": [],
    }

    if not args.report_only:
        # Remediate slide similarity issues
        slide_remediation = remediate_similarity_issues(
            slide_issues,
            output_dir,
            auto_remediate=args.auto_remediate,
            regenerate=args.regenerate_similar,
            use_openai=args.use_openai,
            custom_model=args.llm_model,
        )

        # Remediate worksheet similarity issues
        worksheet_remediation = remediate_similarity_issues(
            worksheet_similarity_issues,
            output_dir,
            auto_remediate=args.auto_remediate,
            regenerate=args.regenerate_similar,
            use_openai=args.use_openai,
            custom_model=args.llm_model,
        )

        # Combine remediation results
        remediation_results["merged"] = (
            slide_remediation["merged"] + worksheet_remediation["merged"]
        )
        remediation_results["regenerated"] = (
            slide_remediation["regenerated"] + worksheet_remediation["regenerated"]
        )
        remediation_results["skipped"] = (
            slide_remediation["skipped"] + worksheet_remediation["skipped"]
        )

    # Step 4: Generate a report
    report_path = generate_report(
        workflow_results,
        slide_issues,
        worksheet_similarity_issues,
        worksheet_content_issues,
        remediation_results,
        output_dir,
    )

    # Print final summary
    print("\n=== Workflow and Validation Summary ===")
    print(
        f"Generated {len(workflow_results['slide_paths'])} slides and {len(workflow_results['worksheet_paths'])} worksheets"
    )
    print(f"Slide similarity issues: {len(slide_issues)}")
    print(f"Worksheet similarity issues: {len(worksheet_similarity_issues)}")
    print(f"Worksheet content issues: {len(worksheet_content_issues)}")
    print(f"Merged content: {len(remediation_results['merged'])}")
    print(f"Skipped remediation: {len(remediation_results['skipped'])}")
    print(f"Detailed report saved to: {report_path}")


if __name__ == "__main__":
    main()
