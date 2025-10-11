#!/usr/bin/env python3
"""
Automated assessment script for Weather Advisor projects.
This script:
1. Clones student repositories
2. Exports notebooks to Python scripts
3. Runs basic tests on functionality
4. Generates a report on code quality and functionality
"""

import os
import sys
import subprocess
import json
import re
from pathlib import Path
import nbformat
from nbconvert import PythonExporter
import pylint.lint
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend for headless execution

# Configuration
GITHUB_USERNAME = "michael-adci"
STUDENT_REPOS_FILE = "student_repos.txt"
OUTPUT_DIR = "assessment_results"
TEST_CITIES = ["Sydney", "London", "New York", "Tokyo", "Paris"]
TEST_QUESTIONS = [
    "What's the weather like in Sydney today?",
    "Will it rain tomorrow in London?",
    "Do I need a jacket in New York?",
    "What's the temperature in Tokyo this weekend?",
    "Is it going to be sunny in Paris next Tuesday?"
]

def clone_repositories():
    """Clone each student repository listed in the student_repos.txt file"""
    if not os.path.exists(STUDENT_REPOS_FILE):
        print(f"Error: {STUDENT_REPOS_FILE} not found")
        return False
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    with open(STUDENT_REPOS_FILE, 'r') as f:
        repos = [line.strip() for line in f if line.strip()]
    
    for repo in repos:
        # Extract student ID or name from repo URL
        student_id = repo.split('/')[-1].replace('.git', '')
        student_dir = os.path.join(OUTPUT_DIR, student_id)
        
        if os.path.exists(student_dir):
            print(f"Updating repository for {student_id}...")
            subprocess.run(['git', '-C', student_dir, 'pull'], check=True)
        else:
            print(f"Cloning repository for {student_id}...")
            subprocess.run(['git', 'clone', repo, student_dir], check=True)
    
    return True

def convert_notebooks_to_scripts():
    """Convert all Jupyter notebooks to Python scripts for analysis"""
    python_exporter = PythonExporter()
    
    for student_dir in os.listdir(OUTPUT_DIR):
        student_path = os.path.join(OUTPUT_DIR, student_dir)
        if not os.path.isdir(student_path):
            continue
        
        # Find all notebook files
        notebook_files = list(Path(student_path).glob('**/*.ipynb'))
        
        for notebook_file in notebook_files:
            try:
                # Convert to Python script
                with open(notebook_file, 'r', encoding='utf-8') as f:
                    notebook_content = nbformat.read(f, as_version=4)
                
                python_code, _ = python_exporter.from_notebook_node(notebook_content)
                
                # Save to .py file
                script_path = notebook_file.with_suffix('.py')
                with open(script_path, 'w', encoding='utf-8') as f:
                    f.write(python_code)
                
                print(f"Converted {notebook_file} to {script_path}")
            except Exception as e:
                print(f"Error converting {notebook_file}: {e}")

def analyze_code_quality():
    """Run static code analysis on all Python files"""
    results = {}
    
    for student_dir in os.listdir(OUTPUT_DIR):
        student_path = os.path.join(OUTPUT_DIR, student_dir)
        if not os.path.isdir(student_path):
            continue
        
        # Find all Python files
        python_files = list(Path(student_path).glob('**/*.py'))
        if not python_files:
            print(f"No Python files found for {student_dir}")
            continue
        
        print(f"Analyzing code quality for {student_dir}...")
        
        # Run pylint on all Python files
        try:
            pylint_output = subprocess.check_output(
                ['pylint', '--output-format=json'] + [str(f) for f in python_files],
                stderr=subprocess.STDOUT,
                universal_newlines=True
            )
            pylint_data = json.loads(pylint_output)
            
            # Process pylint results
            results[student_dir] = {
                'score': calculate_pylint_score(pylint_data),
                'issues': categorize_issues(pylint_data)
            }
        except subprocess.CalledProcessError as e:
            # Pylint returns non-zero exit code if there are any issues
            try:
                pylint_data = json.loads(e.output)
                results[student_dir] = {
                    'score': calculate_pylint_score(pylint_data),
                    'issues': categorize_issues(pylint_data)
                }
            except:
                results[student_dir] = {
                    'score': 0,
                    'issues': {'error': str(e)}
                }
    
    # Save results
    with open(os.path.join(OUTPUT_DIR, 'code_quality_results.json'), 'w') as f:
        json.dump(results, f, indent=2)
    
    return results

def calculate_pylint_score(pylint_data):
    """Calculate a code quality score from pylint output"""
    # This is a simplified version - in practice, you'd want to customize this
    if not pylint_data:
        return 10.0  # Perfect score if no issues
    
    # Count issues by severity
    counts = {'error': 0, 'warning': 0, 'convention': 0, 'refactor': 0}
    for issue in pylint_data:
        counts[issue.get('type', 'convention')] += 1
    
    # Calculate score (simple version)
    total_issues = sum(counts.values())
    weighted_score = 10 - min(10, (
        counts['error'] * 1.0 + 
        counts['warning'] * 0.5 + 
        counts['convention'] * 0.1 + 
        counts['refactor'] * 0.2
    ))
    
    return max(0, weighted_score)

def categorize_issues(pylint_data):
    """Categorize code quality issues for reporting"""
    categories = {
        'style': [],
        'logic': [],
        'imports': [],
        'naming': [],
        'documentation': [],
        'other': []
    }
    
    for issue in pylint_data:
        msg_id = issue.get('message-id', '')
        msg = issue.get('message', '')
        
        if msg_id.startswith('C'):  # Convention
            if 'docstring' in msg:
                categories['documentation'].append(msg)
            elif 'name' in msg:
                categories['naming'].append(msg)
            else:
                categories['style'].append(msg)
        elif msg_id.startswith('R'):  # Refactor
            categories['logic'].append(msg)
        elif msg_id.startswith('W'):  # Warning
            if 'import' in msg:
                categories['imports'].append(msg)
            else:
                categories['logic'].append(msg)
        elif msg_id.startswith('E'):  # Error
            categories['logic'].append(msg)
        else:
            categories['other'].append(msg)
    
    return categories

def check_required_features():
    """Check for implementation of required project features"""
    results = {}
    
    for student_dir in os.listdir(OUTPUT_DIR):
        student_path = os.path.join(OUTPUT_DIR, student_dir)
        if not os.path.isdir(student_path):
            continue
        
        # Find main Python files
        python_files = list(Path(student_path).glob('**/*.py'))
        if not python_files:
            continue
        
        print(f"Checking features for {student_dir}...")
        
        # Read all Python code
        all_code = ""
        for py_file in python_files:
            with open(py_file, 'r', encoding='utf-8', errors='ignore') as f:
                all_code += f.read() + "\n"
        
        # Check for required components
        features = {
            'weather_data_retrieval': check_feature(all_code, [
                r'requests\.get', 
                r'wttr\.in',
                r'openweathermap',
                r'weather.*api'
            ]),
            'visualization': check_feature(all_code, [
                r'matplotlib', 
                r'plt\.', 
                r'\.plot\(',
                r'sns\.'
            ]),
            'natural_language': check_feature(all_code, [
                r'hands[-_]on[-_]ai',
                r'parse.*question',
                r'extract.*location',
                r'extract.*time',
                r'nlp'
            ]),
            'user_interface': check_feature(all_code, [
                r'pyinputplus', 
                r'inputMenu',
                r'input\(',
                r'print\('
            ]),
            'error_handling': check_feature(all_code, [
                r'try\s*:', 
                r'except',
                r'if\s+not\s+',
                r'raise'
            ]),
        }
        
        results[student_dir] = features
    
    # Save results
    with open(os.path.join(OUTPUT_DIR, 'feature_results.json'), 'w') as f:
        json.dump(results, f, indent=2)
    
    return results

def check_feature(code, patterns):
    """Check if code contains any of the given regex patterns"""
    for pattern in patterns:
        if re.search(pattern, code, re.IGNORECASE):
            return True
    return False

def analyze_github_activity():
    """Analyze GitHub commits and activity"""
    results = {}
    
    for student_dir in os.listdir(OUTPUT_DIR):
        student_path = os.path.join(OUTPUT_DIR, student_dir)
        if not os.path.isdir(student_path):
            continue
        
        print(f"Analyzing GitHub activity for {student_dir}...")
        
        try:
            # Get commit count
            commit_count = subprocess.check_output(
                ['git', '-C', student_path, 'rev-list', '--count', 'HEAD'],
                universal_newlines=True
            ).strip()
            
            # Get commit dates to analyze timeline
            commit_dates = subprocess.check_output(
                ['git', '-C', student_path, 'log', '--format=%at', '--all'],
                universal_newlines=True
            ).strip().split('\n')
            
            # Convert to timestamps and sort
            commit_timestamps = sorted([int(date) for date in commit_dates if date])
            
            # Calculate time span
            time_span = 0
            if len(commit_timestamps) >= 2:
                time_span = commit_timestamps[-1] - commit_timestamps[0]
            
            results[student_dir] = {
                'commit_count': int(commit_count),
                'first_commit': commit_timestamps[0] if commit_timestamps else None,
                'last_commit': commit_timestamps[-1] if commit_timestamps else None,
                'development_days': time_span // (24 * 60 * 60),
                'commit_frequency': float(commit_count) / (time_span // (24 * 60 * 60)) if time_span > 0 else 0
            }
        except Exception as e:
            print(f"Error analyzing GitHub activity for {student_dir}: {e}")
            results[student_dir] = {'error': str(e)}
    
    # Save results
    with open(os.path.join(OUTPUT_DIR, 'github_results.json'), 'w') as f:
        json.dump(results, f, indent=2)
    
    return results

def generate_assessment_report():
    """Generate a comprehensive assessment report for each student"""
    # Load results from previous analyses
    try:
        with open(os.path.join(OUTPUT_DIR, 'code_quality_results.json'), 'r') as f:
            quality_results = json.load(f)
        
        with open(os.path.join(OUTPUT_DIR, 'feature_results.json'), 'r') as f:
            feature_results = json.load(f)
        
        with open(os.path.join(OUTPUT_DIR, 'github_results.json'), 'r') as f:
            github_results = json.load(f)
    except FileNotFoundError:
        print("Error: One or more results files not found. Run analyses first.")
        return
    
    # Create report for each student
    for student_id in quality_results:
        report_path = os.path.join(OUTPUT_DIR, f"{student_id}_report.md")
        
        with open(report_path, 'w') as f:
            f.write(f"# Assessment Report: {student_id}\n\n")
            
            # Code Quality
            f.write("## Code Quality\n\n")
            quality = quality_results.get(student_id, {})
            f.write(f"- Overall score: {quality.get('score', 'N/A')}/10\n")
            
            if 'issues' in quality:
                f.write("\n### Issues Summary\n\n")
                for category, issues in quality['issues'].items():
                    if issues:
                        f.write(f"- **{category.capitalize()}**: {len(issues)} issues\n")
            
            # Feature Implementation
            f.write("\n## Feature Implementation\n\n")
            features = feature_results.get(student_id, {})
            
            f.write("| Feature | Implemented |\n")
            f.write("|---------|-------------|\n")
            for feature, implemented in features.items():
                f.write(f"| {feature.replace('_', ' ').title()} | {'✅' if implemented else '❌'} |\n")
            
            # GitHub Activity
            f.write("\n## Development Process\n\n")
            github = github_results.get(student_id, {})
            
            if 'error' not in github:
                f.write(f"- Total commits: {github.get('commit_count', 'N/A')}\n")
                f.write(f"- Development period: {github.get('development_days', 'N/A')} days\n")
                f.write(f"- Commit frequency: {github.get('commit_frequency', 'N/A'):.2f} commits/day\n")
            else:
                f.write(f"- Error analyzing GitHub activity: {github.get('error', 'Unknown error')}\n")
            
            # Overall Assessment
            f.write("\n## Overall Assessment\n\n")
            
            # Calculate total score (customize as needed)
            quality_score = quality.get('score', 0)
            feature_score = sum(1 for impl in features.values() if impl) / len(features) * 10 if features else 0
            github_score = min(10, github.get('commit_count', 0) / 1.5) if 'commit_count' in github else 0
            
            total_score = (quality_score * 0.4) + (feature_score * 0.4) + (github_score * 0.2)
            
            f.write(f"### Total Score: {total_score:.2f}/10\n\n")
            
            # Add qualitative feedback based on scores
            if total_score >= 8.5:
                f.write("**Excellent work!** The project shows strong technical skills and development process.\n")
            elif total_score >= 7.0:
                f.write("**Good work.** The project meets requirements with some room for improvement.\n")
            elif total_score >= 5.0:
                f.write("**Satisfactory.** The project meets basic requirements but has significant areas for improvement.\n")
            else:
                f.write("**Needs improvement.** The project falls short of requirements in multiple areas.\n")
        
        print(f"Generated report for {student_id}")

def main():
    """Main function to run the assessment pipeline"""
    print("Starting automated assessment...")
    
    # Step 1: Clone repositories
    if not clone_repositories():
        return
    
    # Step 2: Convert notebooks to scripts
    convert_notebooks_to_scripts()
    
    # Step 3: Analyze code quality
    analyze_code_quality()
    
    # Step 4: Check required features
    check_required_features()
    
    # Step 5: Analyze GitHub activity
    analyze_github_activity()
    
    # Step 6: Generate assessment reports
    generate_assessment_report()
    
    print("Assessment complete. Reports generated in the assessment_results directory.")

if __name__ == "__main__":
    main()