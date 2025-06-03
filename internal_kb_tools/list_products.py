#!/usr/bin/env python
"""
List Available Products

Script to list available products for the KB tool.
"""

import os
import argparse
import sys
from pathlib import Path

print(f"Python executable: {sys.executable}")
print(f"Current working directory: {os.getcwd()}")

# Add the parent directory to sys.path
script_path = os.path.abspath(__file__)
print(f"Script path: {script_path}")
current_dir = os.path.dirname(script_path)
print(f"Current dir: {current_dir}")
parent_dir = os.path.dirname(current_dir)
print(f"Parent dir: {parent_dir}")

if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)
    print(f"Added {parent_dir} to sys.path")

# Import the utility function
try:
    print("Attempting to import kb_utils...")
    # First try direct import
    sys.path.insert(0, current_dir)
    from kb_utils import print_available_products
    print("Successfully imported kb_utils directly")
except ImportError as e:
    print(f"Direct import failed: {e}")
    try:
        # Try package import
        from internal_kb_tools.kb_utils import print_available_products
        print("Successfully imported kb_utils from package")
    except ImportError as e:
        print(f"Package import failed: {e}")
        print("Available modules in sys.path:")
        for path in sys.path:
            print(f"  {path}")
            if os.path.exists(path):
                for item in os.listdir(path):
                    print(f"    {item}")
        
        # Last resort - try to import manually
        kb_utils_path = os.path.join(current_dir, 'kb_utils.py')
        if os.path.exists(kb_utils_path):
            print(f"Found kb_utils.py at {kb_utils_path}")
            # Use spec to load module
            import importlib.util
            spec = importlib.util.spec_from_file_location("kb_utils", kb_utils_path)
            kb_utils = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(kb_utils)
            print_available_products = kb_utils.print_available_products
            print("Loaded kb_utils.py manually")
        else:
            print(f"kb_utils.py not found at {kb_utils_path}")
            sys.exit(1)

def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(
        description="List available products for the KB tool"
    )
    
    parser.add_argument(
        "--stage",
        type=int,
        choices=[1, 2],
        required=True,
        help="Stage to list products for: 1=data, 2=summaries"
    )
    
    args = parser.parse_args()
    
    # Determine data type based on stage
    data_type = "data" if args.stage == 1 else "summaries"
    
    try:
        # Print available products
        print_available_products(parent_dir, data_type)
    except Exception as e:
        print(f"Error: {e}")
        print(f"Current working directory: {os.getcwd()}")
        print(f"Script directory: {current_dir}")
        print(f"Parent directory: {parent_dir}")
        
        # Check if directories exist
        if data_type == "data":
            check_dir = os.path.join(parent_dir, "internal_kb_tools", "ticket_processing", "collated_ticket_data")
            print(f"Checking if {check_dir} exists: {os.path.exists(check_dir)}")
            if os.path.exists(check_dir):
                print(f"Contents of {check_dir}:")
                for item in os.listdir(check_dir):
                    print(f"  {item}")
        elif data_type == "summaries":
            check_dir = os.path.join(parent_dir, "internal_kb_tools", "ticket_processing", "ticket_summaries")
            print(f"Checking if {check_dir} exists: {os.path.exists(check_dir)}")
            if os.path.exists(check_dir):
                print(f"Contents of {check_dir}:")
                for item in os.listdir(check_dir):
                    print(f"  {item}")
        
        sys.exit(1)

if __name__ == "__main__":
    main() 