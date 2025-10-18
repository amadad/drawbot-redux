#!/usr/bin/env python3
"""
Runner script for typography systems
This script properly imports the local drawBot module and runs the typography demonstrations.
"""

import sys
import os

# Add the project root to Python path so we can import the local drawBot
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_root)

try:
    import drawBot as db
    print("✓ Successfully imported local drawBot module")
except ImportError as e:
    print(f"✗ Failed to import drawBot: {e}")
    sys.exit(1)

# Import and run typography systems
from typography_systems import demonstrate_hierarchy, demonstrate_advanced_features, create_type_specimen

print("Running typography systems demonstrations...")

# Run the demonstrations
demonstrate_hierarchy()
demonstrate_advanced_features()
create_type_specimen()

# Save the output
output_path = os.path.join(project_root, "output", "typography_systems_output.pdf")
db.saveImage(output_path)
print(f"✓ Typography systems completed successfully!")
print(f"✓ Output saved as '{output_path}'") 