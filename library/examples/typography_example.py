#!/usr/bin/env python3
"""
Typography Systems Example
==========================
This example demonstrates how to use the typography systems from the design library.
"""

import sys
import os

# Add the project root to Python path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_root)

import drawBot as db

# Import typography systems
sys.path.insert(0, os.path.join(project_root, 'drawbot-design-library', 'foundations'))
from typography_systems import calculate_type_scale, GOLDEN_RATIO, BASELINE_UNIT

def create_simple_typography_demo():
    """Create a simple typography demonstration"""
    
    # Page setup
    page_width, page_height = 595, 842  # A4
    margin = 60
    
    db.newPage(page_width, page_height)
    
    # Background
    db.fill(0.98, 0.98, 0.98)
    db.rect(0, 0, page_width, page_height)
    
    # Title
    db.fill(0, 0, 0)
    db.font("Helvetica-Bold")
    db.fontSize(32)
    db.text("Typography Example", (margin, page_height - margin))
    
    # Generate type scale
    sizes = calculate_type_scale(12, GOLDEN_RATIO, 5)
    
    # Demonstrate the scale
    y_pos = page_height - margin - 80
    for i, size in enumerate(sizes):
        db.font("Helvetica")
        db.fontSize(size)
        db.fill(0, 0, 0)
        db.text(f"Size {int(size)}pt - The quick brown fox", (margin, y_pos))
        y_pos -= size + BASELINE_UNIT
    
    # Demonstrate FormattedString
    y_pos -= 40
    fs = db.FormattedString()
    fs.font("Helvetica")
    fs.fontSize(16)
    fs.append("This is a ")
    fs.font("Helvetica-Bold")
    fs.fill(0.8, 0.2, 0.2)
    fs.append("FormattedString ")
    fs.font("Helvetica")
    fs.fill(0, 0, 0)
    fs.append("example with mixed styles.")
    
    db.text(fs, (margin, y_pos))
    
    # Save the output
    output_path = os.path.join(project_root, "output", "typography_example.pdf")
    db.saveImage(output_path)
    print(f"✓ Typography example created: {output_path}")

if __name__ == "__main__":
    create_simple_typography_demo() 