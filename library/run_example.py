#!/usr/bin/env python
"""
Run DrawBot Design Library Examples
===================================
A helper script to easily run examples from the library.

Usage:
    python run_example.py [category/filename]
    
Examples:
    python run_example.py basics/01_first_steps
    python run_example.py cookbook/pattern_generation
    python run_example.py foundations/typography_systems
"""

import sys
import os
import subprocess

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        print("\nAvailable examples:")
        print("-" * 40)
        
        # List available examples
        categories = ['basics', 'cookbook', 'foundations', 'historical_studies', 
                     'exercises', 'projects', 'interactive', 'tutorials']
        
        for category in categories:
            if os.path.exists(category):
                print(f"\n{category}/")
                for file in os.listdir(category):
                    if file.endswith('.py') and not file.startswith('__'):
                        print(f"  {file[:-3]}")
        
        sys.exit(1)
    
    # Get the example to run
    example = sys.argv[1]
    if not example.endswith('.py'):
        example += '.py'
    
    # Check if file exists
    if not os.path.exists(example):
        print(f"Error: {example} not found!")
        sys.exit(1)
    
    # Run the example
    print(f"Running {example}...")
    subprocess.run([sys.executable, example])

if __name__ == "__main__":
    main()