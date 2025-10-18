"""
Typography Systems in DrawBot
=============================
Design Principle: Typographic Hierarchy and Rhythm
Historical Context: Based on Emil Ruder's Typographie and Jan Tschichold's principles
Key Concepts: Scale, weight, spacing, alignment, and contrast
DrawBot Features Used: FormattedString, font(), fontSize(), tracking(), baselineShift()
Parameters to Experiment With: type_scale, baseline_unit, tracking_values
"""

import math

# Import DrawBot using the helper
import sys
import os
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_root)
import drawBot as db

# Design System Constants
GOLDEN_RATIO = 1.618
MUSICAL_SCALE = 1.25  # Major third
CLASSIC_SCALE = 1.333  # Perfect fourth
BASELINE_UNIT = 8  # Points

# Color Palette
BLACK = (0, 0, 0)
GRAY_DARK = (0.2, 0.2, 0.2)
GRAY_MID = (0.5, 0.5, 0.5)
GRAY_LIGHT = (0.8, 0.8, 0.8)
RED_ACCENT = (0.9, 0.1, 0.1)

def calculate_type_scale(base_size, ratio, steps):
    """Generate a modular type scale"""
    return [base_size * (ratio ** i) for i in range(steps)]

def draw_baseline_grid(width, height, unit):
    """Draw a baseline grid for vertical rhythm"""
    db.stroke(*GRAY_LIGHT)
    db.strokeWidth(0.5)
    for y in range(0, int(height), unit):
        db.line((0, y), (width, y))
    db.stroke(None)

def demonstrate_hierarchy():
    """Show good vs bad typographic hierarchy"""
    # Page setup
    page_width, page_height = 595, 842  # A4
    margin = 60
    column_width = (page_width - margin * 3) / 2
    
    db.newPage(page_width, page_height)
    
    # Draw baseline grid
    draw_baseline_grid(page_width, page_height, BASELINE_UNIT)
    
    # Title
    db.fill(*BLACK)
    db.font("Helvetica-Bold")
    db.fontSize(32)
    db.text("Typography Systems", (margin, page_height - margin))
    
    # Good Example Column
    x_good = margin
    y_pos = page_height - margin - 80
    
    db.fill(*RED_ACCENT)
    db.font("Helvetica")
    db.fontSize(14)
    db.text("GOOD: Clear Hierarchy", (x_good, y_pos))
    
    # Type scale using golden ratio
    sizes = calculate_type_scale(10, GOLDEN_RATIO, 5)
    
    y_pos -= 40
    # Demonstrate hierarchy with clear differentiation
    db.fill(*BLACK)
    db.font("Helvetica-Bold")
    db.fontSize(sizes[3])  # 26pt
    db.text("Main Heading", (x_good, y_pos))
    
    y_pos -= sizes[3] + BASELINE_UNIT
    db.font("Helvetica")
    db.fontSize(sizes[2])  # 16pt
    db.text("Subheading Level", (x_good, y_pos))
    
    y_pos -= sizes[2] + BASELINE_UNIT
    db.fontSize(sizes[1])  # 10pt
    db.fill(*GRAY_DARK)
    body_text = """This demonstrates proper hierarchy
through size, weight, and color contrast.
Notice the clear distinction between levels."""
    db.textBox(body_text, (x_good, y_pos - 60, column_width, 60))
    
    # Bad Example Column
    x_bad = margin * 2 + column_width
    y_pos = page_height - margin - 80
    
    db.fill(*RED_ACCENT)
    db.fontSize(14)
    db.text("BAD: Weak Hierarchy", (x_bad, y_pos))
    
    y_pos -= 40
    # Demonstrate poor hierarchy
    db.fill(*BLACK)
    db.font("Helvetica")
    db.fontSize(16)  # Too similar sizes
    db.text("Main Heading", (x_bad, y_pos))
    
    y_pos -= 20
    db.fontSize(14)  # Not enough contrast
    db.text("Subheading Level", (x_bad, y_pos))
    
    y_pos -= 18
    db.fontSize(12)  # Minimal difference
    bad_text = """This shows poor hierarchy with
insufficient size contrast between levels.
The distinctions are unclear and weak."""
    db.textBox(bad_text, (x_bad, y_pos - 60, column_width, 60))
    
    # Typography Rules Section
    y_pos = page_height / 2
    
    db.fill(*BLACK)
    db.font("Helvetica-Bold")
    db.fontSize(20)
    db.text("Core Principles", (margin, y_pos))
    
    # Demonstrate tracking (letter spacing)
    y_pos -= 60
    db.fontSize(14)
    db.text("1. Tracking for Different Sizes", (margin, y_pos))
    
    y_pos -= 30
    # Large text needs tighter tracking
    fs = db.FormattedString()
    fs.font("Helvetica")
    fs.fontSize(36)
    fs.tracking(-1)  # Tighter
    fs.append("DISPLAY")
    db.text(fs, (margin, y_pos))
    
    # Small text needs looser tracking
    fs = db.FormattedString()
    fs.font("Helvetica")
    fs.fontSize(8)
    fs.tracking(1)  # Looser
    fs.append("SMALL CAPTION TEXT")
    db.text(fs, (margin + 200, y_pos + 10))
    
    # Line height demonstration
    y_pos -= 80
    db.font("Helvetica-Bold")
    db.fontSize(14)
    db.text("2. Line Height (Leading)", (margin, y_pos))
    
    y_pos -= 30
    db.font("Helvetica")
    db.fontSize(10)
    
    # Good line height
    fs = db.FormattedString()
    fs.font("Helvetica")
    fs.fontSize(10)
    fs.lineHeight(16)  # 1.6x
    fs.append("Good: Comfortable line height\nallows easy reading and\ncreates breathing room.")
    db.text(fs, (margin, y_pos - 50))
    
    # Bad line height
    fs = db.FormattedString()
    fs.font("Helvetica")
    fs.fontSize(10)
    fs.lineHeight(10)  # 1.0x - too tight
    fs.append("Bad: Cramped line height\nmakes reading difficult\nand feels compressed.")
    db.text(fs, (margin + 150, y_pos - 50))
    
    # Alignment demonstration
    y_pos -= 120
    db.font("Helvetica-Bold")
    db.fontSize(14)
    db.text("3. Alignment Creates Order", (margin, y_pos))
    
    y_pos -= 40
    # Strong left alignment
    db.font("Helvetica")
    db.fontSize(10)
    align_text = "Strong alignment creates\nvisual connection between\nelements and improves\nreadability significantly."
    db.text(align_text, (margin, y_pos - 60))
    
    # Visual alignment line
    db.stroke(*RED_ACCENT)
    db.strokeWidth(1)
    db.line((margin - 5, y_pos), (margin - 5, y_pos - 60))
    db.stroke(None)

def demonstrate_advanced_features():
    """Show advanced FormattedString capabilities"""
    page_width, page_height = 595, 842
    margin = 60
    
    db.newPage(page_width, page_height)
    
    # Title
    db.fill(*BLACK)
    db.font("Helvetica-Bold")
    db.fontSize(32)
    db.text("Advanced Typography", (margin, page_height - margin))
    
    # Mixed formatting in one line
    y_pos = page_height - 150
    fs = db.FormattedString()
    fs.font("Helvetica")
    fs.fontSize(16)
    fs.append("Combine ")
    fs.font("Helvetica-Bold")
    fs.fill(*RED_ACCENT)
    fs.append("multiple ")
    fs.font("Helvetica-Oblique")
    fs.fill(*BLACK)
    fs.append("styles ")
    fs.font("Helvetica")
    fs.fontSize(12)
    fs.baselineShift(4)
    fs.append("with ease")
    
    db.text(fs, (margin, y_pos))
    
    # Baseline shift for superior/inferior
    y_pos -= 60
    fs = db.FormattedString()
    fs.font("Helvetica")
    fs.fontSize(16)
    fs.append("E = mc")
    fs.fontSize(12)
    fs.baselineShift(6)
    fs.append("2")
    fs.fontSize(16)
    fs.baselineShift(0)
    fs.append(" demonstrates baseline shift")
    
    db.text(fs, (margin, y_pos))
    
    # Variable tracking within text
    y_pos -= 60
    fs = db.FormattedString()
    fs.font("Helvetica")
    fs.fontSize(14)
    fs.append("Normal ")
    fs.tracking(5)
    fs.append("EXPANDED ")
    fs.tracking(-1)
    fs.append("CONDENSED ")
    fs.tracking(0)
    fs.append("tracking")
    
    db.text(fs, (margin, y_pos))
    
    # OpenType features (if available)
    y_pos -= 60
    fs = db.FormattedString()
    fs.font("Helvetica")
    fs.fontSize(14)
    fs.append("OpenType features: ")
    # Note: OpenType features syntax may vary by DrawBot version
    # fs.openTypeFeatures({"smcp": True})  # Small caps
    fs.append("Small Caps")
    
    db.text(fs, (margin, y_pos))

def create_type_specimen():
    """Create a type specimen showing scale relationships"""
    page_width, page_height = 595, 842
    margin = 60
    
    db.newPage(page_width, page_height)
    
    # Background
    db.fill(0.98, 0.98, 0.98)
    db.rect(0, 0, page_width, page_height)
    
    # Title
    db.fill(*BLACK)
    db.font("Helvetica-Bold")
    db.fontSize(32)
    db.text("Modular Type Scale", (margin, page_height - margin))
    
    # Show three different scales
    scales = [
        ("Golden Ratio (1.618)", GOLDEN_RATIO, RED_ACCENT),
        ("Musical Scale (1.25)", MUSICAL_SCALE, (0.1, 0.5, 0.9)),
        ("Classic Scale (1.333)", CLASSIC_SCALE, (0.1, 0.7, 0.3))
    ]
    
    x_pos = margin
    for scale_name, ratio, color in scales:
        y_pos = page_height - 150
        
        db.fill(*color)
        db.font("Helvetica")
        db.fontSize(12)
        db.text(scale_name, (x_pos, y_pos))
        
        # Generate and display scale
        sizes = calculate_type_scale(8, ratio, 6)
        y_pos -= 20
        
        for i, size in enumerate(sizes):
            y_pos -= size + 5
            db.fill(*BLACK)
            db.font("Helvetica")
            db.fontSize(size)
            db.text(f"Aa {int(size)}pt", (x_pos, y_pos))
        
        x_pos += 160

# Main execution
if __name__ == "__main__":
    # Create all demonstrations
    demonstrate_hierarchy()
    demonstrate_advanced_features()
    create_type_specimen()
    
    # Save the output
    db.saveImage("typography_systems.pdf")
    print("Typography systems guide created successfully!")