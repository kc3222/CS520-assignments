#!/usr/bin/env python3
"""
Script to parse APPS_PLUS_FINAL.json and extract 7 questions with tests, solutions, and prompts.
Each question will be saved in a separate folder within the APPS directory.
"""

import json
import random
import sys
from pathlib import Path

# Increase the limit for integer string conversion to handle large numbers in APPS dataset
sys.set_int_max_str_digits(0)  # 0 means no limit

# Set seed for reproducibility
random.seed(42)

def create_cot_prompt(problem_statement, function_signature):
    """Create a Chain of Thought prompt."""
    return f"""{function_signature}
{problem_statement}

You are a careful Python developer.
First, reason step by step privately about the algorithm and tricky cases.
Then, output ONLY valid Python code implementing `{function_signature.split('(')[0].split()[-1]}` — no comments, no prints, no tests."""

def create_self_planning_prompt(problem_statement, function_signature):
    """Create a self-planning prompt."""
    return f"""{function_signature}
{problem_statement}

You are a methodical Python engineer.
Before coding, make a brief plan in your head: inputs/outputs, edge cases, approach, and complexity.
Finally, output ONLY the final Python code implementing `{function_signature.split('(')[0].split()[-1]}` — no comments, no prints, no tests."""

def create_test_file(inputs, outputs):
    """Create a test file from inputs and outputs."""
    test_content = ""
    
    for i, (input_case, output_case) in enumerate(zip(inputs, outputs)):
        # Clean up the input and output - handle both strings and lists
        if isinstance(input_case, list):
            input_clean = '\n'.join(str(item) for item in input_case)
        else:
            input_clean = str(input_case).strip()
            
        if isinstance(output_case, list):
            output_clean = '\n'.join(str(item) for item in output_case)
        else:
            output_clean = str(output_case).strip()
        
        test_content += f"""# Test case {i+1}
# Input: {repr(input_clean)}
# Expected output: {repr(output_clean)}
# Note: This is a competitive programming problem that reads from stdin
# and writes to stdout. The test would need to be run with the input.

"""
    
    return test_content

def main():
    # Set up paths
    json_file = "APPS_PLUS_FINAL.json"
    output_dir = "./APPS"
    
    print(f"Loading data from {json_file}...")
    
    # Load the JSON data
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return
    
    print(f"Loaded {len(data)} problems from APPS dataset")
    
    # Select 7 random problems
    selected_problems = random.sample(data, min(7, len(data)))
    
    # Create output directory
    Path(output_dir).mkdir(exist_ok=True)
    
    print(f"\nSelected {len(selected_problems)} problems for processing...")
    
    # Process each problem
    for i, problem in enumerate(selected_problems, 1):
        print(f"Processing problem {i}...")
        
        # Create problem directory
        problem_dir = Path(output_dir) / f"problem_{i:02d}"
        problem_dir.mkdir(exist_ok=True)
        
        # Extract problem components
        problem_statement = problem.get('prompt', 'No description available')
        solution_code = problem.get('canonical_solution', 'No solution available')
        starter_code = problem.get('starter_code', 'def function_name():')
        inputs = problem.get('inputs', [])
        outputs = problem.get('outputs', [])
        
        # Extract function signature
        function_signature = starter_code.strip()
        
        # Create prompts
        cot_prompt = create_cot_prompt(problem_statement, function_signature)
        self_planning_prompt = create_self_planning_prompt(problem_statement, function_signature)
        
        # Create test file
        test_content = create_test_file(inputs, outputs)
        
        # Save files
        with open(problem_dir / "prompt.txt", 'w') as f:
            f.write(f"{function_signature}\n{problem_statement}")
        
        with open(problem_dir / "prompt_cot.txt", 'w') as f:
            f.write(cot_prompt)
        
        with open(problem_dir / "prompt_self_planning.txt", 'w') as f:
            f.write(self_planning_prompt)
        
        with open(problem_dir / "solution.py", 'w') as f:
            f.write(solution_code)
        
        with open(problem_dir / "tests.py", 'w') as f:
            f.write(test_content)
        
        print(f"  Saved problem {i} to {problem_dir}")
        print(f"    Function: {function_signature}")
        print(f"    Test cases: {len(inputs)}")
    
    print(f"\nCompleted! All problems saved to {output_dir}")
    print(f"Each problem folder contains:")
    print(f"  - prompt.txt: Basic problem statement")
    print(f"  - prompt_cot.txt: Chain of thought prompt")
    print(f"  - prompt_self_planning.txt: Self-planning prompt")
    print(f"  - solution.py: Canonical solution")
    print(f"  - tests.py: Test cases with inputs and expected outputs")

if __name__ == "__main__":
    main()
