#!/usr/bin/env python
"""Script to convert a course overview to LMS-compatible HTML format.

This script takes a course overview markdown file and converts it to HTML
that's compatible with Learning Management Systems (LMS). The HTML uses
<details> tags with inline styles for collapsible sections, ensuring
proper display even when the LMS strips out CSS or JavaScript.

Usage:
    python create_lms_overview_html.py input_overview.md [output.html]

Example:
    python create_lms_overview_html.py overview.md overview_lms.html
"""

from pathlib import Path
import sys

from curriculumcreator.overview_html import convert_overview_to_html


# Constants for argument validation
MIN_ARGS = 2
OUTPUT_ARG_INDEX = 2


def main():
    """Main function to convert overview to LMS-compatible HTML."""
    if len(sys.argv) < MIN_ARGS:
        print(
            "Usage: python create_lms_overview_html.py input_overview.md [output.html]"
        )
        sys.exit(1)

    input_path = Path(sys.argv[1])
    if not input_path.exists():
        print(f"Error: Input file {input_path} does not exist.")
        sys.exit(1)

    # Determine output path
    if len(sys.argv) >= OUTPUT_ARG_INDEX + 1:
        output_path = Path(sys.argv[OUTPUT_ARG_INDEX])
    else:
        output_path = input_path.with_name(f"{input_path.stem}_lms.html")

    # Convert overview to LMS-compatible HTML
    try:
        result_path = convert_overview_to_html(
            overview_path=input_path, output_path=output_path
        )
        print(f"LMS-compatible HTML generated at: {result_path}")
    except Exception as e:
        print(f"Error converting overview to HTML: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
