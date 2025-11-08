#!/usr/bin/env python3
"""Convert test files to pytest format."""
import re
from pathlib import Path

def is_already_pytest_format(content):
    """Check if the file is already in pytest format."""
    # Check for pytest imports and test function definitions
    has_pytest_import = 'import pytest' in content
    has_test_function = re.search(r'^def test_\w+\(\):', content, re.MULTILINE)
    has_solution_import = 'import solution' in content
    
    # If it has pytest imports and test functions, it's already converted
    if has_pytest_import and has_test_function and has_solution_import:
        return True
    
    # Also check if it doesn't have the old format (multiple function definitions)
    # Old format typically has multiple 'def counting_sort' definitions
    counting_sort_defs = len(re.findall(r'^def counting_sort\(', content, re.MULTILINE))
    if counting_sort_defs > 1:
        return False  # Old format with multiple definitions
    
    return False

def convert_test_file(test_file_path):
    test_file = Path(test_file_path)
    content = test_file.read_text()
    
    # Check if already in pytest format
    if is_already_pytest_format(content):
        print(f'Skipping {test_file_path} (already in pytest format)')
        return False
    
    # Extract assertions
    assertions = [line[7:].strip() for line in content.split('\n') if line.strip().startswith('assert ')]
    
    if not assertions:
        print(f'No assertions found in {test_file_path}')
        return False
    
    # Try to detect function name from first assertion
    func_name = 'counting_sort'  # default
    if assertions:
        match = re.search(r'(\w+)\(', assertions[0])
        if match:
            func_name = match.group(1)
    
    lines = [
        '"""Test cases using pytest."""',
        '',
        'import pytest',
        'import sys',
        'from pathlib import Path',
        '',
        '# Add parent directory to path to import solution',
        'sys.path.insert(0, str(Path(__file__).parent))',
        'import solution',
        '',
    ]
    
    for i, assert_line in enumerate(assertions, 1):
        modified_assert = assert_line.replace(f'{func_name}(', f'solution.{func_name}(')
        lines.append(f'def test_{func_name}_{i}():')
        lines.append(f'    """Test {func_name} case {i}."""')
        lines.append(f'    assert {modified_assert}')
        lines.append('')
    
    test_file.write_text('\n'.join(lines))
    print(f'Converted {test_file_path} ({len(assertions)} test cases)')
    return True

if __name__ == '__main__':
    import sys
    
    # If directories are specified as arguments, use those
    if len(sys.argv) > 1:
        test_files = [Path(arg) for arg in sys.argv[1:]]
    else:
        # Default: convert all directories with these prefixes
        prefixes = [54, 151, 222]
        test_files = []
        for prefix in prefixes:
            for num in [1, 2, 3, 4]:
                test_files.append(Path(f'{prefix}_{num}/tests.py'))
    
    converted = 0
    skipped = 0
    
    for test_file in test_files:
        if test_file.exists():
            if convert_test_file(test_file):
                converted += 1
            else:
                skipped += 1
        else:
            print(f'File not found: {test_file}')
    
    print(f'\nSummary: {converted} converted, {skipped} skipped')

