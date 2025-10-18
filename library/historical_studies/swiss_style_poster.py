"""
Swiss International Style Poster Study
======================================
Design Principle: Objectivity, clarity, and systematic design
Historical Context: 1950s-1970s Switzerland, Josef Müller-Brockmann, Armin Hofmann
Key Concepts: Grid systems, sans-serif typography, photographic imagery, minimal color
DrawBot Features Used: Precise grid alignment, Helvetica, mathematical positioning
Study Reference: "Der Film" poster by Josef Müller-Brockmann (1960)
"""

import math

# Import DrawBot
try:
    import drawBot as db
except ImportError:
    import sys
    import os
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    sys.path.insert(0, project_root)
    import drawBot as db

# Swiss Style Constants
GRID_UNIT = 10  # Base unit for grid
MARGIN_RATIO = 0.067  # Classic Swiss margin proportion

def create_swiss_grid(width, height, units_x=12, units_y=16):
    """Create a Swiss-style modular grid"""
    margin = width * MARGIN_RATIO
    
    # Calculate module size
    content_width = width - (2 * margin)
    content_height = height - (2 * margin)
    
    module_width = content_width / units_x
    module_height = content_height / units_y
    
    # Draw grid lines (subtle)
    db.stroke(0.9, 0.9, 0.9)
    db.strokeWidth(0.5)
    
    # Vertical lines
    for i in range(units_x + 1):
        x = margin + i * module_width
        db.line((x, 0), (x, height))
    
    # Horizontal lines
    for i in range(units_y + 1):
        y = margin + i * module_height
        db.line((0, y), (width, y))
    
    # Margin lines (stronger)
    db.stroke(0.8, 0.2, 0.2, 0.5)
    db.strokeWidth(1)
    db.rect(margin, margin, content_width, content_height)
    
    db.stroke(None)
    
    return margin, module_width, module_height

def recreate_der_film_poster():
    """Recreate Josef Müller-Brockmann's 'der Film' poster"""
    # A2 poster size
    width, height = 420, 594
    
    db.newPage(width, height)
    
    # Background
    db.fill(0.95, 0.95, 0.95)  # Slight off-white
    db.rect(0, 0, width, height)
    
    # Create grid
    margin, module_w, module_h = create_swiss_grid(width, height, 8, 12)
    
    # Title: "der Film"
    db.fill(0, 0, 0)
    db.font("Helvetica-Bold")
    db.fontSize(72)
    
    # Position text on grid
    x = margin
    y = height - margin - module_h * 2
    
    db.text("der Film", (x, y))
    
    # Geometric elements representing film frames
    # Create diagonal rhythm
    frame_width = module_w * 1.5
    frame_height = module_h * 1
    
    # Black frames in diagonal arrangement
    positions = [
        (2, 4), (3, 5), (4, 6), (5, 7),
        (1, 7), (2, 8), (3, 9)
    ]
    
    for col, row in positions:
        x = margin + col * module_w
        y = height - margin - row * module_h
        
        db.fill(0, 0, 0)
        db.rect(x, y - frame_height, frame_width, frame_height)
        
        # Add perforation holes
        db.fill(0.95, 0.95, 0.95)
        hole_size = 3
        for i in range(4):
            db.oval(x + 3, y - frame_height + 5 + i * 8, hole_size, hole_size)
            db.oval(x + frame_width - 6, y - frame_height + 5 + i * 8, hole_size, hole_size)
    
    # Information text
    db.fill(0, 0, 0)
    db.font("Helvetica")
    db.fontSize(10)
    
    info_y = margin + module_h * 2
    line_height = 14
    
    info_text = [
        "Ausstellung",
        "Kunstgewerbemuseum Zürich", 
        "10. Juni bis 31. Juli 1960",
        "Täglich geöffnet"
    ]
    
    for i, line in enumerate(info_text):
        db.text(line, (margin, info_y - i * line_height))

def create_typographic_poster():
    """Create a Swiss style typographic poster"""
    width, height = 420, 594
    
    db.newPage(width, height)
    
    # White background
    db.fill(1, 1, 1)
    db.rect(0, 0, width, height)
    
    # Grid
    margin, module_w, module_h = create_swiss_grid(width, height, 6, 9)
    
    # Color accent - typical Swiss red
    swiss_red = (0.9, 0.1, 0.1)
    
    # Main typography
    db.font("Helvetica")
    
    # Large number as graphic element
    db.fill(*swiss_red)
    db.fontSize(320)
    db.text("5", (margin + module_w * 3, height - margin - module_h * 5))
    
    # Overlapping text
    db.fill(0, 0, 0)
    db.fontSize(48)
    db.text("MUSIK", (margin, height - margin - module_h * 2.5))
    
    db.fontSize(36)
    db.text("KONZERT", (margin, height - margin - module_h * 3.5))
    
    # Date and venue
    db.fontSize(14)
    y_pos = height - margin - module_h * 7
    
    details = [
        "Tonhalle Zürich",
        "Samstag 25. Mai",
        "20.00 Uhr"
    ]
    
    for detail in details:
        db.text(detail, (margin, y_pos))
        y_pos -= 20
    
    # Bottom alignment text
    db.fontSize(10)
    db.text("Eintritt Fr. 8.—", (margin, margin + module_h))

def demonstrate_swiss_principles():
    """Show key Swiss design principles"""
    width, height = 595, 842  # A4
    
    db.newPage(width, height)
    db.fill(1, 1, 1)
    db.rect(0, 0, width, height)
    
    margin = 50
    
    # Title
    db.fill(0, 0, 0)
    db.font("Helvetica-Bold")
    db.fontSize(32)
    db.text("Swiss Design Principles", (margin, height - margin))
    
    # 1. Objectivity
    y_section = height - 150
    db.font("Helvetica-Bold")
    db.fontSize(18)
    db.text("1. Objectivity", (margin, y_section))
    
    db.font("Helvetica")
    db.fontSize(12)
    db.text("Clear, universal communication without decoration", (margin, y_section - 25))
    
    # Example: objective vs decorative
    y_example = y_section - 60
    
    # Good - objective
    db.fill(0, 0.6, 0)
    db.text("GOOD", (margin, y_example))
    db.fill(0, 0, 0)
    db.font("Helvetica")
    db.fontSize(24)
    db.text("Information", (margin, y_example - 35))
    
    # Bad - decorative
    db.fill(0.8, 0, 0)
    db.text("BAD", (margin + 200, y_example))
    db.fill(0, 0, 0)
    
    # Decorative text (simulated with multiple styles)
    fs = db.FormattedString()
    fs.font("Times-Italic")
    fs.fontSize(24)
    fs.append("I")
    fs.font("Helvetica-Bold")
    fs.append("nfor")
    fs.font("Times-Roman")
    fs.append("mation")
    db.text(fs, (margin + 200, y_example - 35))
    
    # 2. Grid System
    y_section -= 150
    db.font("Helvetica-Bold")
    db.fontSize(18)
    db.text("2. Mathematical Grid", (margin, y_section))
    
    db.font("Helvetica")
    db.fontSize(12)
    db.text("Systematic organization creates order and consistency", (margin, y_section - 25))
    
    # Show mini grid
    grid_demo_size = 150
    y_example = y_section - 60
    
    db.stroke(0.8, 0.8, 0.8)
    db.strokeWidth(0.5)
    for i in range(7):
        x = margin + i * 25
        db.line((x, y_example - grid_demo_size), (x, y_example))
    for i in range(7):
        y = y_example - i * 25
        db.line((margin, y), (margin + 150, y))
    
    # Elements aligned to grid
    db.stroke(None)
    db.fill(0, 0, 0)
    db.rect(margin, y_example - 150, 50, 50)
    db.rect(margin + 75, y_example - 100, 75, 25)
    db.rect(margin + 100, y_example - 50, 50, 25)
    
    # 3. Sans-serif Typography
    y_section -= 150
    db.font("Helvetica-Bold")
    db.fontSize(18)
    db.text("3. Sans-serif Typography", (margin, y_section))
    
    db.font("Helvetica")
    db.fontSize(12)
    db.text("Helvetica: neutral, legible, modern", (margin, y_section - 25))
    
    # Type specimen
    y_example = y_section - 50
    sizes = [8, 12, 18, 24, 36]
    
    for size in sizes:
        db.fontSize(size)
        db.text(f"Helvetica {size}pt", (margin, y_example))
        y_example -= size + 10
    
    # 4. Asymmetric Layout
    y_section = height - 500
    x_section = width / 2 + 20
    
    db.font("Helvetica-Bold")
    db.fontSize(18)
    db.text("4. Dynamic Asymmetry", (x_section, y_section))
    
    db.font("Helvetica")
    db.fontSize(12)
    db.text("Creates visual tension and movement", (x_section, y_section - 25))
    
    # Example layout
    y_example = y_section - 60
    
    # Asymmetric composition
    db.fill(0, 0, 0)
    db.rect(x_section, y_example - 100, 120, 40)
    db.fill(0.7, 0.7, 0.7)
    db.rect(x_section + 140, y_example - 80, 40, 60)
    db.fill(0.4, 0.4, 0.4)
    db.rect(x_section + 60, y_example - 40, 80, 20)
    
    # 5. Minimal Color
    y_section -= 150
    db.font("Helvetica-Bold")
    db.fontSize(18)
    db.text("5. Restrained Color", (x_section, y_section))
    
    db.font("Helvetica")
    db.fontSize(12)
    db.text("Black, white, and one accent color", (x_section, y_section - 25))
    
    # Color palette
    y_example = y_section - 50
    colors = [(0, 0, 0), (1, 1, 1), (0.9, 0.1, 0.1)]
    labels = ["Black", "White", "Red"]
    
    for i, (color, label) in enumerate(zip(colors, labels)):
        db.fill(*color)
        if color == (1, 1, 1):
            db.stroke(0, 0, 0)
            db.strokeWidth(1)
        db.rect(x_section + i * 60, y_example, 50, 30)
        db.stroke(None)
        
        db.fill(0, 0, 0)
        db.font("Helvetica")
        db.fontSize(10)
        db.text(label, (x_section + i * 60, y_example - 15))

def create_modern_swiss_poster():
    """Create a modern interpretation of Swiss style"""
    width, height = 420, 594
    
    db.newPage(width, height)
    
    # Background
    db.fill(1, 1, 1)
    db.rect(0, 0, width, height)
    
    # Grid
    margin, module_w, module_h = create_swiss_grid(width, height, 8, 12)
    
    # Modern twist: gradient as accent
    db.linearGradient(
        (margin, height - margin - module_h * 4),
        (margin + module_w * 4, height - margin),
        [(0.9, 0.1, 0.1), (0.9, 0.4, 0.1)],
        [0, 1]
    )
    db.rect(margin, height - margin - module_h * 4, module_w * 4, module_h * 4)
    
    # Typography
    db.fill(1, 1, 1)
    db.font("Helvetica-Bold")
    db.fontSize(64)
    db.text("DESIGN", (margin + module_w * 0.5, height - margin - module_h * 3))
    
    db.fill(0, 0, 0)
    db.fontSize(48)
    db.text("SYSTEM", (margin + module_w * 4.5, height - margin - module_h * 5))
    
    # Subtext
    db.font("Helvetica")
    db.fontSize(14)
    db.text("Contemporary Swiss Typography", (margin, height - margin - module_h * 8))
    
    # Grid of dots showing mathematical precision
    db.fill(0, 0, 0, 0.3)
    for col in range(8):
        for row in range(12):
            if row < 7:  # Don't overlap with gradient
                x = margin + col * module_w + module_w / 2
                y = margin + row * module_h + module_h / 2
                db.oval(x - 2, y - 2, 4, 4)
    
    # Date - bottom aligned
    db.fill(0, 0, 0)
    db.fontSize(10)
    db.text("2024", (margin, margin + module_h))

# Main execution
if __name__ == "__main__":
    recreate_der_film_poster()
    create_typographic_poster()
    demonstrate_swiss_principles()
    create_modern_swiss_poster()
    
    db.saveImage("swiss_style_poster.pdf")
    print("Swiss style poster study created successfully!")