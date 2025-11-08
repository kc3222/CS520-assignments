#!/usr/bin/env python3
"""Run pytest with coverage for each directory separately and aggregate results."""
import subprocess
import sys
import re
from pathlib import Path

def parse_coverage_output(output):
    """Parse coverage output to extract coverage data."""
    coverage_data = {}
    lines = output.split('\n')
    
    # Look for the coverage table
    in_table = False
    for line in lines:
        if 'Name' in line and 'Stmts' in line and 'Miss' in line:
            in_table = True
            # Check if branch coverage is included
            has_branch = 'Branch' in line or 'BrPart' in line
            continue
        if in_table and line.strip().startswith('---'):
            continue
        if in_table and line.strip():
            # Parse line with branch coverage: "54_1/solution.py      14      1    93%   3    10      2    80%"
            # Or without: "54_1/solution.py      14      1    93%   3"
            if 'Branch' in line or 'BrPart' in line:
                # Has branch coverage
                match = re.match(r'(\S+)\s+(\d+)\s+(\d+)\s+(\d+)%\s+(\S+)\s+(\d+)\s+(\d+)\s+(\d+)%\s*(.*)', line.strip())
                if match:
                    filepath, stmts, miss, cover, missing, branches, br_miss, br_cover, rest = match.groups()
                    # Skip __init__.py files
                    if '__init__.py' not in filepath:
                        coverage_data[filepath] = {
                            'statements': int(stmts),
                            'missing': int(miss),
                            'coverage': int(cover),
                            'missing_lines': missing.strip(),
                            'branches': int(branches),
                            'branch_missing': int(br_miss),
                            'branch_coverage': int(br_cover)
                        }
            else:
                # No branch coverage
                match = re.match(r'(\S+)\s+(\d+)\s+(\d+)\s+(\d+)%\s*(.*)', line.strip())
                if match:
                    filepath, stmts, miss, cover, missing = match.groups()
                    # Skip __init__.py files
                    if '__init__.py' not in filepath:
                        coverage_data[filepath] = {
                            'statements': int(stmts),
                            'missing': int(miss),
                            'coverage': int(cover),
                            'missing_lines': missing.strip(),
                            'branches': None,
                            'branch_missing': None,
                            'branch_coverage': None
                        }
        if in_table and line.strip().startswith('TOTAL'):
            break
    
    return coverage_data

def run_coverage_for_dir(directory):
    """Run pytest with coverage for a single directory."""
    print(f"\n{'='*60}")
    print(f"Testing {directory}")
    print(f"{'='*60}")
    
    result = subprocess.run(
        [
            sys.executable, '-m', 'pytest',
            '--import-mode=importlib',
            f'--cov={directory}',  # Use directory, not file path
            '--cov-report=term-missing',
            f'{directory}/tests.py',
            '-v'
        ],
        capture_output=True,
        text=True
    )
    
    print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)
    
    # Parse coverage data
    coverage_data = parse_coverage_output(result.stdout)
    
    return result.returncode == 0, coverage_data

def print_summary_table(all_coverage_data):
    """Print a summary table of all coverage data."""
    print(f"\n{'='*80}")
    print("COVERAGE SUMMARY")
    print(f"{'='*80}")
    print(f"{'File':<25} {'Statements':<12} {'Missing':<10} {'Coverage':<10} {'Missing Lines'}")
    print(f"{'-'*80}")
    
    total_stmts = 0
    total_miss = 0
    
    for filepath in sorted(all_coverage_data.keys()):
        data = all_coverage_data[filepath]
        total_stmts += data['statements']
        total_miss += data['missing']
        missing_lines = data['missing_lines'] if data['missing_lines'] else '-'
        print(f"{filepath:<25} {data['statements']:<12} {data['missing']:<10} {data['coverage']:>5}%     {missing_lines}")
    
    print(f"{'-'*80}")
    if total_stmts > 0:
        total_coverage = int((total_stmts - total_miss) / total_stmts * 100)
        print(f"{'TOTAL':<25} {total_stmts:<12} {total_miss:<10} {total_coverage:>5}%")
    print(f"{'='*80}\n")

if __name__ == '__main__':
    base_dir = Path(__file__).parent
    # List of prefixes to include in coverage
    prefixes = [54, 151, 222]
    
    # Find all directories matching the prefixes
    directories = []
    for prefix in prefixes:
        matching_dirs = [d.name for d in base_dir.iterdir() 
                        if d.is_dir() and d.name.startswith(f'{prefix}_')]
        directories.extend(matching_dirs)
    directories = sorted(directories)
    
    all_passed = True
    all_coverage_data = {}
    
    for directory in directories:
        passed, coverage_data = run_coverage_for_dir(directory)
        if not passed:
            all_passed = False
        
        # Merge coverage data
        all_coverage_data.update(coverage_data)
    
    # Print summary table
    if all_coverage_data:
        print_summary_table(all_coverage_data)
    
    print(f"{'='*60}")
    if all_passed:
        print("All tests passed!")
    else:
        print("Some tests failed!")
        sys.exit(1)

