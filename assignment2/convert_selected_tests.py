#!/usr/bin/env python3
"""Convert all test files in selected_mbpp_seed42 to pytest format."""
import re
from pathlib import Path


def extract_assertions(content):
    """Extract all assertion lines from content."""
    assertions = []
    for line in content.split('\n'):
        line = line.strip()
        if line.startswith('assert '):
            assertions.append(line[7:])  # Remove 'assert ' prefix
    return assertions


def get_function_name_from_solution(solution_file):
    """Get function name from solution file."""
    if not solution_file.exists():
        return None
    content = solution_file.read_text()
    match = re.search(r'^def (\w+)\(', content, re.MULTILINE)
    if match:
        return match.group(1)
    return None


def convert_test_file(test_file_path, solution_file_path):
    """Convert a test file to pytest format."""
    test_file = Path(test_file_path)
    solution_file = Path(solution_file_path)
    
    if not test_file.exists():
        print(f"Test file not found: {test_file_path}")
        return False
    
    content = test_file.read_text()
    
    # Extract assertions
    assertions = extract_assertions(content)
    if not assertions:
        print(f"No assertions found in {test_file_path}")
        return False
    
    # Get function name from solution file
    func_name = get_function_name_from_solution(solution_file)
    
    # Fallback: get from first assertion
    if not func_name:
        match = re.search(r'(\w+)\(', assertions[0])
        if match:
            func_name = match.group(1)
        else:
            func_name = 'test_function'
    
    # Build new test file content
    lines = [
        '"""Test cases using pytest."""',
        '',
        'import pytest',
        'import sys',
        'from pathlib import Path',
        '',
        '# Add parent directory to path to import solution',
        "sys.path.insert(0, str(Path(__file__).parent))",
        'import solution',
        '',
    ]
    
    # Create test functions
    for i, assert_line in enumerate(assertions, 1):
        # Replace function name in assertion with solution.func_name
        modified_assert = assert_line.replace(f'{func_name}(', f'solution.{func_name}(')
        lines.append(f'def test_{func_name}_{i}():')
        lines.append(f'    """Test {func_name} case {i}."""')
        lines.append(f'    assert {modified_assert}')
        lines.append('')
    
    # Write new content
    test_file.write_text('\n'.join(lines))
    print(f"Converted {test_file_path} ({len(assertions)} test cases)")
    return True


if __name__ == '__main__':
    base_dir = Path('selected_mbpp_seed42')
    
    if not base_dir.exists():
        print(f"Directory not found: {base_dir}")
        exit(1)
    
    # Get all subdirectories
    subdirs = [d for d in base_dir.iterdir() if d.is_dir() and not d.name.startswith('.')]
    
    converted = 0
    failed = 0
    
    for subdir in sorted(subdirs):
        test_file = subdir / 'tests.py'
        solution_file = subdir / 'solution.py'
        
        if test_file.exists() and solution_file.exists():
            if convert_test_file(test_file, solution_file):
                converted += 1
            else:
                failed += 1
        else:
            print(f"Skipping {subdir.name}: missing tests.py or solution.py")
    
    print(f"\nConversion complete: {converted} files converted, {failed} failed")

