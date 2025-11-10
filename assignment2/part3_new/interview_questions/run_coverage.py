#!/usr/bin/env python3
"""Run pytest with coverage (line and branch coverage) for interview questions."""
import subprocess
import sys
from pathlib import Path

def run_coverage_for_dir(directory):
    """Run pytest with coverage for a single directory."""
    print(f"\n{'='*60}")
    print(f"Testing {directory.name}")
    print(f"{'='*60}")
    
    result = subprocess.run(
        [
            sys.executable, '-m', 'pytest',
            '--import-mode=importlib',
            '--cov=.',
            '--cov-report=term-missing',
            '--cov-branch',
            'tests.py',
            '-v'
        ],
        cwd=directory,
        capture_output=True,
        text=True
    )
    
    print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)
    
    return result.returncode == 0

def main():
    """Run pytest with coverage for each question directory."""
    base_dir = Path(__file__).parent
    
    # Find all question directories
    question_dirs = [d for d in base_dir.iterdir() 
                    if d.is_dir() and d.name.startswith('question_')]
    question_dirs = sorted(question_dirs)
    
    if not question_dirs:
        print("No question directories found!")
        sys.exit(1)
    
    all_passed = True
    for question_dir in question_dirs:
        passed = run_coverage_for_dir(question_dir)
        if not passed:
            all_passed = False
    
    print(f"\n{'='*60}")
    if all_passed:
        print("All tests passed!")
    else:
        print("Some tests failed!")
        sys.exit(1)

if __name__ == '__main__':
    main()
