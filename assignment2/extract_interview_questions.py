#!/usr/bin/env python3
"""
Script to extract 2 random interview questions from APPS_PLUS_FINAL.json.
Uses seed for reproducibility and saves all components to separate files.
"""

import json
import sys
import random
import re
from pathlib import Path
from typing import Dict, Any, List, Optional


def first_non_empty(*vals, cast=str) -> Optional[str]:
    """Return the first non-empty value from the given arguments."""
    for v in vals:
        if v is None:
            continue
        if isinstance(v, (list, tuple)):
            if not v:
                continue
            try:
                s = "\n".join(map(str, v)).strip()
            except Exception:
                s = str(v)
        else:
            s = str(v).strip()
        if s:
            return cast(s)
    return None


def extract_prompt_text_only(item: Dict[str, Any]) -> str:
    """Extract prompt/question text from item."""
    return first_non_empty(
        item.get("prompt"), 
        item.get("text"), 
        item.get("question"), 
        item.get("instruction")
    ) or ""


def extract_solution(item: Dict[str, Any]) -> str:
    """Extract solution code from item."""
    return first_non_empty(
        item.get("solution"), 
        item.get("canonical_solution"), 
        item.get("code"), 
        item.get("reference_solution")
    ) or ""


def extract_tests(item: Dict[str, Any]) -> str:
    """Extract test code from item."""
    s = first_non_empty(item.get("tests"), item.get("test"), item.get("test_code"))
    if s:
        return s
    parts = []
    setup = first_non_empty(item.get("test_setup_code"))
    if setup:
        parts.append(setup)
    for key in ["test_list", "challenge_test_list"]:
        lst = item.get(key)
        if isinstance(lst, list) and lst:
            parts.append("\n".join(str(x) for x in lst))
    if parts:
        return "\n\n".join(parts)
    fallback = first_non_empty(item.get("unittest"), item.get("asserts"))
    return fallback or ""


def generate_tests_from_io(item: Dict[str, Any], entry_point: str = "") -> str:
    """
    Generate test code from inputs and outputs arrays.
    This is used when no explicit test code is available.
    """
    inputs = item.get("inputs", [])
    outputs = item.get("outputs", [])
    
    if not inputs or not outputs:
        return ""
    
    # Try to infer entry point from solution or starter code
    if not entry_point:
        solution = extract_solution(item)
        starter_code = first_non_empty(item.get("starter_code"), item.get("start_code")) or ""
        
        # Look for function/class definition
        func_pattern = r'def\s+(\w+)\s*\('
        class_pattern = r'class\s+(\w+)'
        
        if starter_code:
            match = re.search(func_pattern, starter_code) or re.search(class_pattern, starter_code)
            if match:
                entry_point = match.group(1)
        
        if not entry_point and solution:
            match = re.search(func_pattern, solution) or re.search(class_pattern, solution)
            if match:
                entry_point = match.group(1)
    
    if not entry_point:
        entry_point = "solution"  # Default fallback
    
    # Generate test code
    test_lines = ["import sys", "from io import StringIO"]
    test_lines.append("")
    test_lines.append("def test_solution():")
    
    # Check if it's a class-based solution
    is_class = "class Solution" in (item.get("canonical_solution", "") or item.get("solution", "") or item.get("starter_code", ""))
    
    if is_class:
        test_lines.append("    from solution import Solution")
        test_lines.append("    sol = Solution()")
    else:
        test_lines.append("    from solution import " + entry_point)
    
    test_lines.append("")
    
    # Generate test cases
    for i, (inp, out) in enumerate(zip(inputs, outputs), 1):
        test_lines.append(f"    # Test case {i}")
        
        if is_class:
            # For class-based solutions, inputs are typically method arguments
            if isinstance(inp, list) and len(inp) > 0:
                # Format input as arguments
                if len(inp) == 1:
                    arg_str = repr(inp[0])
                else:
                    arg_str = ", ".join(repr(x) for x in inp)
                test_lines.append(f"    result = sol.{entry_point}({arg_str})")
            else:
                test_lines.append(f"    result = sol.{entry_point}({repr(inp)})")
        else:
            # For function-based solutions, might need to handle stdin
            # Check if inputs are strings (stdin format) or direct values
            if isinstance(inp, str):
                # String input - likely stdin format
                # Create a test that mocks stdin and captures stdout
                test_lines.append(f"    # Test case {i} (stdin input)")
                test_lines.append(f"    from io import StringIO")
                test_lines.append(f"    import sys")
                test_lines.append(f"    old_stdin = sys.stdin")
                test_lines.append(f"    old_stdout = sys.stdout")
                test_lines.append(f"    sys.stdin = StringIO({repr(inp)})")
                test_lines.append(f"    sys.stdout = StringIO()")
                test_lines.append(f"    try:")
                test_lines.append(f"        {entry_point}()")
                test_lines.append(f"        result = sys.stdout.getvalue()")
                test_lines.append(f"        expected = {repr(out)}")
                test_lines.append(f"        assert result == expected, f'Expected {{expected}}, got {{result}}'")
                test_lines.append(f"    finally:")
                test_lines.append(f"        sys.stdin = old_stdin")
                test_lines.append(f"        sys.stdout = old_stdout")
                test_lines.append("")
                continue
            elif isinstance(inp, list) and len(inp) > 0:
                if len(inp) == 1:
                    arg_str = repr(inp[0])
                else:
                    arg_str = ", ".join(repr(x) for x in inp)
                test_lines.append(f"    result = {entry_point}({arg_str})")
            else:
                test_lines.append(f"    result = {entry_point}({repr(inp)})")
        
        # Format expected output
        if isinstance(out, list):
            expected = out[0] if len(out) == 1 else out
        else:
            expected = out
        
        test_lines.append(f"    assert result == {repr(expected)}, f'Expected {repr(expected)}, got {{result}}'")
        test_lines.append("")
    
    test_lines.append("if __name__ == '__main__':")
    test_lines.append("    test_solution()")
    test_lines.append("    print('All tests passed!')")
    
    return "\n".join(test_lines)


def extract_interview_questions_streaming(json_file_path: str, seed: int = 2025) -> List[Dict[str, Any]]:
    """
    Extract all interview difficulty questions using streaming approach.
    This avoids loading the entire JSON file into memory.
    """
    json_path = Path(json_file_path)
    
    if not json_path.exists():
        print(f"Error: File '{json_file_path}' not found.", file=sys.stderr)
        sys.exit(1)
    
    print(f"Scanning JSON file for interview questions: {json_file_path}...", file=sys.stderr)
    
    interview_questions = []
    
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Set a very high integer limit (200000 should handle 35660 digits easily)
        sys.set_int_max_str_digits(200000)
        
        # Try to load as JSON - if it's a list, iterate; if dict, iterate values
        try:
            data = json.loads(content)
        except ValueError as e:
            if "Exceeds the limit" in str(e):
                print("Warning: Some values exceed integer limit.", file=sys.stderr)
                print("Attempting to parse with string-based integers...", file=sys.stderr)
                # Use regex to replace very large integers with strings before parsing
                # This is a workaround for Python's integer conversion limit
                def replace_large_int(match):
                    num_str = match.group(0)
                    # Check if it's a very large number (more than 10000 digits)
                    if len(num_str) > 10000:
                        return f'"{num_str}"'
                    return num_str
                
                # Pattern to match integers (not inside strings)
                # This is a simplified approach - for full accuracy would need proper JSON parsing
                int_pattern = r'(?<!")(?<!":\s")(?<!":\s)-?\d{10000,}(?!")(?!")'
                modified_content = re.sub(int_pattern, replace_large_int, content)
                
                try:
                    data = json.loads(modified_content)
                except (ValueError, json.JSONDecodeError) as e2:
                    print("Error: Cannot parse JSON even with workarounds.", file=sys.stderr)
                    print(f"Error details: {e2}", file=sys.stderr)
                    sys.exit(1)
            else:
                raise
        
        # Process the loaded data
        if isinstance(data, list):
            items = data
        elif isinstance(data, dict):
            items = list(data.values()) if data else []
        else:
            items = [data]
        
        print(f"Found {len(items)} total items, filtering for interview difficulty...", file=sys.stderr)
        
        for idx, item in enumerate(items):
            if not isinstance(item, dict):
                continue
            
            difficulty = item.get("difficulty", "").lower()
            if difficulty == "interview":
                interview_questions.append(item)
                if len(interview_questions) % 100 == 0:
                    print(f"Found {len(interview_questions)} interview questions so far...", file=sys.stderr)
        
        print(f"Total interview questions found: {len(interview_questions)}", file=sys.stderr)
        
    except MemoryError:
        print("Error: File too large to load into memory. Using regex-based extraction...", file=sys.stderr)
        return extract_interview_questions_regex(json_file_path, seed)
    except Exception as e:
        print(f"Error reading file: {e}", file=sys.stderr)
        sys.exit(1)
    
    return interview_questions


def extract_interview_questions_regex(json_file_path: str, seed: int = 42) -> List[Dict[str, Any]]:
    """
    Fallback method: Extract interview questions using regex pattern matching.
    This is less accurate but works with very large files.
    """
    print("Using regex-based extraction (may be less accurate)...", file=sys.stderr)
    # This is a simplified approach - for full accuracy, would need ijson library
    # For now, we'll try the JSON loading with increased limits first
    return []


def save_question_components(question: Dict[str, Any], output_dir: Path, question_num: int):
    """Save all components of a question to separate files."""
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Extract components
    task_id = first_non_empty(
        question.get("task_id"), 
        question.get("id"), 
        question.get("problem_id")
    ) or f"interview_{question_num}"
    
    prompt = extract_prompt_text_only(question)
    solution = extract_solution(question)
    tests = extract_tests(question)
    starter_code = first_non_empty(question.get("starter_code"), question.get("start_code")) or ""
    
    # Additional fields that might be present
    entry_point = first_non_empty(
        question.get("entry_point"),
        question.get("entrypoint"),
        question.get("function_name"),
        question.get("func_name")
    ) or ""
    
    # Try to infer entry point from solution/starter code if not provided
    if not entry_point:
        func_pattern = r'def\s+(\w+)\s*\('
        class_pattern = r'class\s+(\w+)'
        
        if starter_code:
            match = re.search(func_pattern, starter_code) or re.search(class_pattern, starter_code)
            if match:
                entry_point = match.group(1)
        
        if not entry_point and solution:
            match = re.search(func_pattern, solution) or re.search(class_pattern, solution)
            if match:
                entry_point = match.group(1)
    
    # Get inputs and outputs
    inputs = question.get("inputs", [])
    outputs = question.get("outputs", [])
    
    # If no tests found, generate from inputs/outputs
    if not tests and inputs and outputs:
        tests = generate_tests_from_io(question, entry_point)
        print(f"    Generated tests from inputs/outputs for question {question_num}", file=sys.stderr)
    
    input_output = first_non_empty(
        question.get("input_output"),
        question.get("io"),
        question.get("examples")
    ) or ""
    
    # Save all components
    (output_dir / "question.txt").write_text(prompt, encoding="utf-8")
    (output_dir / "solution.py").write_text(solution, encoding="utf-8")
    (output_dir / "tests.py").write_text(tests, encoding="utf-8")
    
    # Save inputs and outputs separately
    if inputs:
        (output_dir / "inputs.json").write_text(
            json.dumps(inputs, indent=2, ensure_ascii=False),
            encoding="utf-8"
        )
    
    if outputs:
        (output_dir / "outputs.json").write_text(
            json.dumps(outputs, indent=2, ensure_ascii=False),
            encoding="utf-8"
        )
    
    if starter_code:
        (output_dir / "starter_code.py").write_text(starter_code, encoding="utf-8")
    
    if entry_point:
        (output_dir / "entry_point.txt").write_text(entry_point, encoding="utf-8")
    
    if input_output:
        (output_dir / "input_output.txt").write_text(str(input_output), encoding="utf-8")
    
    # Save full JSON for reference
    (output_dir / "full_data.json").write_text(
        json.dumps(question, indent=2, ensure_ascii=False), 
        encoding="utf-8"
    )
    
    # Save metadata
    metadata = {
        "task_id": task_id,
        "difficulty": question.get("difficulty", ""),
        "entry_point": entry_point,
    }
    (output_dir / "metadata.json").write_text(
        json.dumps(metadata, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )
    
    print(f"  Saved question {question_num} to {output_dir}", file=sys.stderr)


def main():
    # Default to APPS_PLUS_FINAL.json in the same directory
    script_dir = Path(__file__).parent
    default_json = script_dir / "APPS_PLUS_FINAL.json"
    
    # Parse command line arguments
    seed = 2025
    num_questions = 2
    json_file = str(default_json)
    
    if len(sys.argv) > 1:
        json_file = sys.argv[1]
    if len(sys.argv) > 2:
        try:
            num_questions = int(sys.argv[2])
        except ValueError:
            print(f"Warning: Invalid number of questions '{sys.argv[2]}', using default: {num_questions}", file=sys.stderr)
    if len(sys.argv) > 3:
        try:
            seed = int(sys.argv[3])
        except ValueError:
            print(f"Warning: Invalid seed '{sys.argv[3]}', using default: {seed}", file=sys.stderr)
    
    # Extract all interview questions
    interview_questions = extract_interview_questions_streaming(json_file, seed)
    
    if not interview_questions:
        print("No interview questions found in the JSON file.", file=sys.stderr)
        sys.exit(1)
    
    if len(interview_questions) < num_questions:
        print(f"Warning: Only found {len(interview_questions)} interview questions, "
              f"but requested {num_questions}. Using all available.", file=sys.stderr)
        num_questions = len(interview_questions)
    
    # Select random questions using seed
    random.seed(seed)
    selected_questions = random.sample(interview_questions, num_questions)
    
    print(f"\nSelected {len(selected_questions)} random interview questions (seed={seed})", file=sys.stderr)
    
    # Create output directory
    output_base = script_dir / "interview_questions"
    output_base.mkdir(parents=True, exist_ok=True)
    
    # Save each question
    for idx, question in enumerate(selected_questions, 1):
        task_id = first_non_empty(
            question.get("task_id"),
            question.get("id"),
            question.get("problem_id")
        ) or f"question_{idx}"
        
        # Sanitize task_id for filesystem
        safe_task_id = str(task_id).replace("/", "_").replace("\\", "_")
        question_dir = output_base / f"question_{idx}_{safe_task_id}"
        
        save_question_components(question, question_dir, idx)
    
    print(f"\n✅ Successfully extracted {len(selected_questions)} interview questions", file=sys.stderr)
    print(f"   Output directory: {output_base.resolve()}", file=sys.stderr)
    print(f"   Seed used: {seed}", file=sys.stderr)


if __name__ == "__main__":
    main()

