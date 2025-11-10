#!/usr/bin/env python3
"""Rename folders from xxx/xxx copy/xxx copy 2/xxx copy 3 to xxx_1/xxx_2/xxx_3/xxx_4."""
import os
from pathlib import Path
import re

def rename_folders(base_dir):
    """Rename folders following the pattern: xxx -> xxx_1, xxx copy -> xxx_2, etc."""
    base_path = Path(base_dir)
    
    # Find all folders that match the patterns
    folders_to_rename = {}
    
    for item in base_path.iterdir():
        if not item.is_dir():
            continue
        
        name = item.name
        
        # Pattern 1: exact match (e.g., "375")
        if re.match(r'^\d+$', name):
            base_name = name
            if base_name not in folders_to_rename:
                folders_to_rename[base_name] = {}
            folders_to_rename[base_name][1] = item
        
        # Pattern 2: "xxx copy" -> _2
        elif re.match(r'^(\d+) copy$', name):
            match = re.match(r'^(\d+) copy$', name)
            base_name = match.group(1)
            if base_name not in folders_to_rename:
                folders_to_rename[base_name] = {}
            folders_to_rename[base_name][2] = item
        
        # Pattern 3: "xxx copy 2" -> _3
        elif re.match(r'^(\d+) copy 2$', name):
            match = re.match(r'^(\d+) copy 2$', name)
            base_name = match.group(1)
            if base_name not in folders_to_rename:
                folders_to_rename[base_name] = {}
            folders_to_rename[base_name][3] = item
        
        # Pattern 4: "xxx copy 3" -> _4
        elif re.match(r'^(\d+) copy 3$', name):
            match = re.match(r'^(\d+) copy 3$', name)
            base_name = match.group(1)
            if base_name not in folders_to_rename:
                folders_to_rename[base_name] = {}
            folders_to_rename[base_name][4] = item
    
    # Rename folders
    # We need to rename in reverse order to avoid conflicts
    # First, rename to temporary names, then to final names
    temp_renames = []
    final_renames = []
    
    for base_name, folders in folders_to_rename.items():
        # Sort by the number (1, 2, 3, 4)
        for num in sorted(folders.keys(), reverse=True):
            old_path = folders[num]
            new_name = f"{base_name}_{num}"
            new_path = base_path / new_name
            
            # Skip if already correctly named
            if old_path.name == new_name:
                print(f"Skipping {old_path.name} (already correctly named)")
                continue
            
            # Check if target already exists
            if new_path.exists():
                print(f"Warning: Target {new_name} already exists. Skipping {old_path.name}")
                continue
            
            # First rename to temporary name to avoid conflicts
            temp_name = f"{base_name}_TEMP_{num}"
            temp_path = base_path / temp_name
            temp_renames.append((old_path, temp_path))
            final_renames.append((temp_path, new_path))
    
    # Execute renames in two phases
    print("Phase 1: Renaming to temporary names...")
    for old_path, temp_path in temp_renames:
        print(f"  {old_path.name} -> {temp_path.name}")
        old_path.rename(temp_path)
    
    print("\nPhase 2: Renaming to final names...")
    for temp_path, new_path in final_renames:
        print(f"  {temp_path.name} -> {new_path.name}")
        temp_path.rename(new_path)
    
    print(f"\nRenamed {len(final_renames)} folder(s)")

if __name__ == '__main__':
    # Get the directory where this script is located
    script_dir = Path(__file__).parent
    rename_folders(script_dir)

