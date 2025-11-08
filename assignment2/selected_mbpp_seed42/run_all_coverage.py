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
    has_branch_header = False
    for line in lines:
        if 'Name' in line and 'Stmts' in line and 'Miss' in line:
            in_table = True
            # Check if branch coverage is included in header
            has_branch_header = 'Branch' in line or 'BrPart' in line or 'BrMiss' in line
            continue
        if in_table and line.strip().startswith('---'):
            continue
        if in_table and line.strip() and not line.strip().startswith('TOTAL'):
            # Skip empty lines and separator lines
            if not line.strip() or line.strip().startswith('---'):
                continue
            
            # Try parsing with branch coverage first if header indicates it
            if has_branch_header:
                # Format with branch: "filepath  stmts  miss  branch  brpart  cover%  missing"
                # Example: "54_4/solution.py      13      1      6      1    89%   3"
                match = re.match(r'(\S+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)%\s*(.*)', line.strip())
                if match:
                    filepath, stmts, miss, branches, brpart, cover, missing = match.groups()
                    # Only include solution.py files
                    if 'solution.py' in filepath:
                        branches_int = int(branches)
                        brpart_int = int(brpart)
                        # Calculate branch coverage percentage
                        if branches_int > 0:
                            branch_coverage = int((branches_int - brpart_int) / branches_int * 100)
                        else:
                            branch_coverage = 100
                        
                        coverage_data[filepath] = {
                            'statements': int(stmts),
                            'missing': int(miss),
                            'coverage': int(cover),
                            'missing_lines': missing.strip() if missing.strip() else '-',
                            'branches': branches_int,
                            'branch_missing': brpart_int,
                            'branch_coverage': branch_coverage
                        }
                    continue
            
            # Try parsing without branch coverage (fallback or when no branch header)
            # Format: "filepath  stmts  miss  cover%  missing"
            # More flexible: allow for missing lines to be optional or empty
            match = re.match(r'(\S+)\s+(\d+)\s+(\d+)\s+(\d+)%\s*(.*)', line.strip())
            if match:
                filepath, stmts, miss, cover, missing = match.groups()
                # Only include solution.py files
                if 'solution.py' in filepath:
                    coverage_data[filepath] = {
                        'statements': int(stmts),
                        'missing': int(miss),
                        'coverage': int(cover),
                        'missing_lines': missing.strip() if missing.strip() else '-',
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
            '--cov-branch',  # Enable branch coverage
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
    
    # Debug: print if no coverage data was parsed
    if not coverage_data:
        # Try to find coverage section in output
        if 'Name' in result.stdout and 'Stmts' in result.stdout:
            print(f"\nDEBUG: Found coverage table header but no data parsed for {directory}")
            # Print a sample of the coverage output for debugging
            lines = result.stdout.split('\n')
            for i, line in enumerate(lines):
                if 'Name' in line and 'Stmts' in line:
                    print(f"DEBUG: Header line: {line}")
                    # Print next 10 lines after header
                    for j in range(i+1, min(i+11, len(lines))):
                        if lines[j].strip() and not lines[j].strip().startswith('==='):
                            print(f"DEBUG: Line {j-i}: {lines[j]}")
                    break
    
    return result.returncode == 0, coverage_data

def print_summary_table(all_coverage_data):
    """Print a summary table of all coverage data."""
    # Check if any file has branch coverage data
    has_branch = any(data.get('branches') is not None for data in all_coverage_data.values())
    
    print(f"\n{'='*110}")
    print("COVERAGE SUMMARY")
    print(f"{'='*110}")
    
    if has_branch:
        print(f"{'File':<25} {'Statements':<12} {'Missing':<10} {'Coverage':<10} {'Branches':<10} {'Branch%':<10} {'Missing Lines'}")
        print(f"{'-'*110}")
    else:
        print(f"{'File':<25} {'Statements':<12} {'Missing':<10} {'Coverage':<10} {'Missing Lines'}")
        print(f"{'-'*110}")
    
    total_stmts = 0
    total_miss = 0
    total_branches = 0
    total_br_miss = 0
    
    for filepath in sorted(all_coverage_data.keys()):
        data = all_coverage_data[filepath]
        total_stmts += data['statements']
        total_miss += data['missing']
        missing_lines = data['missing_lines'] if data['missing_lines'] else '-'
        
        if has_branch:
            if data.get('branches') is not None:
                total_branches += data['branches']
                total_br_miss += data['branch_missing']
                print(f"{filepath:<25} {data['statements']:<12} {data['missing']:<10} {data['coverage']:>5}%     {data['branches']:<10} {data['branch_coverage']:>5}%     {missing_lines}")
            else:
                print(f"{filepath:<25} {data['statements']:<12} {data['missing']:<10} {data['coverage']:>5}%     {'-':<10} {'-':<10} {missing_lines}")
        else:
            print(f"{filepath:<25} {data['statements']:<12} {data['missing']:<10} {data['coverage']:>5}%     {missing_lines}")
    
    print(f"{'-'*110}")
    if total_stmts > 0:
        total_coverage = int((total_stmts - total_miss) / total_stmts * 100)
        if has_branch and total_branches > 0:
            total_br_coverage = int((total_branches - total_br_miss) / total_branches * 100)
            print(f"{'TOTAL':<25} {total_stmts:<12} {total_miss:<10} {total_coverage:>5}%     {total_branches:<10} {total_br_coverage:>5}%")
        else:
            print(f"{'TOTAL':<25} {total_stmts:<12} {total_miss:<10} {total_coverage:>5}%")
    print(f"{'='*110}\n")

if __name__ == '__main__':
    base_dir = Path(__file__).parent
    # List of prefixes to include in coverage
    prefixes = [54, 151, 222, 290, 375, 410, 491, 596, 677, 944]
    
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
    
    # Print summary table (always print, even if empty)
    print_summary_table(all_coverage_data)
    
    print(f"{'='*60}")
    if all_passed:
        print("All tests passed!")
    else:
        print("Some tests failed!")
        sys.exit(1)

