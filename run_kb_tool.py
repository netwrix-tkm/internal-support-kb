#!/usr/bin/env python
"""
KB Tool Launcher

A simple script to run the KB organizer tool from the root directory.
"""

import os
import sys
import subprocess

def main():
    """Main entry point for the launcher."""
    # Get the directory of this script
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Path to the KB organizer script
    kb_organizer_path = os.path.join(base_dir, 'internal_kb_tools', 'kb_organizer.py')
    
    if not os.path.exists(kb_organizer_path):
        print(f"Error: KB organizer script not found at {kb_organizer_path}")
        return 1
    
    # Forward all arguments to the KB organizer script
    args = [sys.executable, kb_organizer_path] + sys.argv[1:]
    
    print(f"Running: {' '.join(args)}")
    return subprocess.call(args)

if __name__ == "__main__":
    sys.exit(main()) 