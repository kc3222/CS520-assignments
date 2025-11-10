#!/usr/bin/env python3
"""
Script to parse APPS_PLUS_FINAL.json and print unique difficulty levels.
Uses streaming approach to avoid loading entire file into memory.
"""

import json
import sys
import re
from pathlib import Path


def extract_unique_difficulties_streaming(json_file_path):
    """
    Extract unique difficulty levels by streaming through the JSON file.
    Uses regex to find difficulty values without fully parsing the JSON.
    
    Args:
        json_file_path: Path to the JSON file
        
    Returns:
        Set of unique difficulty levels
    """
    json_path = Path(json_file_path)
    
    if not json_path.exists():
        print(f"Error: File '{json_file_path}' not found.", file=sys.stderr)
        sys.exit(1)
    
    print(f"Scanning JSON file: {json_file_path}...", file=sys.stderr)
    
    difficulties = set()
    # Pattern to match "difficulty": "value" or "difficulty": value
    # This handles both string and non-string values
    pattern = r'"difficulty"\s*:\s*"([^"]+)"'
    
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                # Find all difficulty values in this line
                matches = re.findall(pattern, line)
                for match in matches:
                    if match and match.strip():
                        difficulties.add(match.strip())
                
                # Print progress every 100000 lines
                if line_num % 100000 == 0:
                    print(f"Processed {line_num:,} lines, found {len(difficulties)} unique difficulties...", 
                          file=sys.stderr)
    except Exception as e:
        print(f"Error reading file: {e}", file=sys.stderr)
        sys.exit(1)
    
    return difficulties


def extract_unique_difficulties_incremental(json_file_path):
    """
    Parse JSON file incrementally, stopping when we hit integer conversion limits.
    This method tries to parse as much as possible within the limit.
    
    Args:
        json_file_path: Path to the JSON file
        
    Returns:
        Set of unique difficulty levels
    """
    json_path = Path(json_file_path)
    
    if not json_path.exists():
        print(f"Error: File '{json_file_path}' not found.", file=sys.stderr)
        sys.exit(1)
    
    print(f"Loading JSON file incrementally: {json_file_path}...", file=sys.stderr)
    
    difficulties = set()
    
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            # Try to parse as JSON
            decoder = json.JSONDecoder()
            buffer = ""
            processed_count = 0
            
            for line in f:
                buffer += line
                try:
                    # Try to decode JSON objects from the buffer
                    while buffer:
                        obj, idx = decoder.raw_decode(buffer)
                        buffer = buffer[idx:].lstrip()
                        
                        # Extract difficulty from the object
                        if isinstance(obj, dict):
                            if 'difficulty' in obj:
                                difficulty = obj['difficulty']
                                if difficulty is not None:
                                    difficulties.add(str(difficulty))
                        elif isinstance(obj, list):
                            for item in obj:
                                if isinstance(item, dict) and 'difficulty' in item:
                                    difficulty = item['difficulty']
                                    if difficulty is not None:
                                        difficulties.add(str(difficulty))
                        
                        processed_count += 1
                        if processed_count % 1000 == 0:
                            print(f"Processed {processed_count:,} objects, found {len(difficulties)} unique difficulties...", 
                                  file=sys.stderr)
                except (json.JSONDecodeError, ValueError):
                    # Not enough data yet, continue reading
                    continue
                except ValueError as e:
                    if "Exceeds the limit" in str(e):
                        print(f"\nWarning: Hit integer conversion limit after processing {processed_count:,} objects.", 
                              file=sys.stderr)
                        print(f"Found {len(difficulties)} unique difficulties so far.", file=sys.stderr)
                        break
                    raise
    except Exception as e:
        print(f"Error reading file: {e}", file=sys.stderr)
        if not difficulties:
            sys.exit(1)
    
    return difficulties


def main():
    # Default to APPS_PLUS_FINAL.json in the same directory
    script_dir = Path(__file__).parent
    default_json = script_dir / "APPS_PLUS_FINAL.json"
    
    # Allow command line argument for JSON file path
    if len(sys.argv) > 1:
        json_file = sys.argv[1]
    else:
        json_file = str(default_json)
    
    # Use streaming approach to avoid integer conversion limits
    # This method uses regex to extract difficulty values without fully parsing JSON
    difficulties = extract_unique_difficulties_streaming(json_file)
    
    if not difficulties:
        print("No difficulty levels found in the JSON file.", file=sys.stderr)
        sys.exit(1)
    
    # Print unique difficulties, sorted for consistency
    print("\nUnique difficulty levels:")
    print("-" * 30)
    for difficulty in sorted(difficulties):
        print(difficulty)
    
    print(f"\nTotal unique difficulty levels: {len(difficulties)}")


if __name__ == "__main__":
    main()

