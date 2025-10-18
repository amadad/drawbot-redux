"""
Grid Systems in DrawBot
=======================
Design Principle: Modular grids for systematic layout
Historical Context: Influenced by Karl Gerstner and Josef Müller-Brockmann
Key Concepts: Modules, gutters, margins, baseline alignment
DrawBot Features Used: Mathematical calculations, guides, systematic positioning
Parameters to Experiment With: columns, rows, gutter_width, margin_ratio

Note: This file demonstrates manual grid creation for learning purposes.
For production work, consider using the DrawBotGrid library which provides
more advanced grid functionality (see cookbook/grid_layouts.py).
"""

import math

# Import DrawBot
import sys
import os
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if project_root not in sys.path:
    sys.path.insert(0, project_root)
import drawBot as db

# Constants
GOLDEN_RATIO = 1.618
PAPER_SIZES = {
    "A4": (595, 842),
    "A3": (842, 1191),
    "Letter": (612, 792),
    "Square": (600, 600)
}

def draw_grid(width, height, columns, rows, gutter, margin, show_diagonals=False):
    """Draw a modular grid with optional diagonal guides"""
    # Calculate module dimensions
    content_width = width - (2 * margin)
    content_height = height - (2 * margin)
    
    module_width = (content_width - (columns - 1) * gutter) / columns
    module_height = (content_height - (rows - 1) * gutter) / rows
    
    # Draw margin guides
    db.stroke(1, 0, 0, 0.3)  # Red for margins
    db.strokeWidth(1)
    db.rect(margin, margin, content_width, content_height)
    
    # Draw vertical divisions
    db.stroke(0, 0, 1, 0.3)  # Blue for grid
    db.strokeWidth(0.5)
    for col in range(columns + 1):
        x = margin + col * (module_width + gutter) - gutter * (col > 0)
        db.line((x, margin), (x, height - margin))
    
    # Draw horizontal divisions
    for row in range(rows + 1):
        y = margin + row * (module_height + gutter) - gutter * (row > 0)
        db.line((margin, y), (width - margin, y))
    
    # Draw diagonals for dynamic composition
    if show_diagonals:
        db.stroke(0, 0.5, 0, 0.2)  # Green for diagonals
        # Main diagonals
        db.line((margin, margin), (width - margin, height - margin))
        db.line((width - margin, margin), (margin, height - margin))
        # Module diagonals
        for col in range(columns):
            for row in range(rows):
                x = margin + col * (module_width + gutter)
                y = margin + row * (module_height + gutter)
                db.line((x, y), (x + module_width, y + module_height))
    
    db.stroke(None)
    
    return module_width, module_height

def demonstrate_grid_types():
    """Show different grid systems and their uses"""
    margin = 60
    
    # 1. Manuscript Grid (Single Column)
    db.newPage(*PAPER_SIZES["A4"])
    db.fill(0.98, 0.98, 0.98)
    db.rect(0, 0, *PAPER_SIZES["A4"])
    
    db.fill(0, 0, 0)
    db.font("Helvetica-Bold")
    db.fontSize(24)
    db.text("Manuscript Grid", (margin, PAPER_SIZES["A4"][1] - margin))
    
    db.font("Helvetica")
    db.fontSize(10)
    db.text("Best for: continuous text, books, simple documents", 
            (margin, PAPER_SIZES["A4"][1] - margin - 30))
    
    draw_grid(*PAPER_SIZES["A4"], columns=1, rows=1, gutter=0, margin=margin)
    
    # Example content
    db.fill(0.9, 0.9, 0.9)
    db.rect(margin, margin, PAPER_SIZES["A4"][0] - 2*margin, PAPER_SIZES["A4"][1] - 2*margin)
    
    # 2. Column Grid
    db.newPage(*PAPER_SIZES["A4"])
    db.fill(0.98, 0.98, 0.98)
    db.rect(0, 0, *PAPER_SIZES["A4"])
    
    db.fill(0, 0, 0)
    db.font("Helvetica-Bold")
    db.fontSize(24)
    db.text("Column Grid", (margin, PAPER_SIZES["A4"][1] - margin))
    
    db.font("Helvetica")
    db.fontSize(10)
    db.text("Best for: magazines, newspapers, flexible layouts", 
            (margin, PAPER_SIZES["A4"][1] - margin - 30))
    
    module_w, _ = draw_grid(*PAPER_SIZES["A4"], columns=3, rows=1, gutter=20, margin=margin)
    
    # Example content
    y_pos = PAPER_SIZES["A4"][1] - margin - 100
    for col in range(3):
        x = margin + col * (module_w + 20)
        db.fill(0.9, 0.9, 0.9)
        db.rect(x, margin, module_w, y_pos - margin - 50)
    
    # 3. Modular Grid
    db.newPage(*PAPER_SIZES["A4"])
    db.fill(0.98, 0.98, 0.98)
    db.rect(0, 0, *PAPER_SIZES["A4"])
    
    db.fill(0, 0, 0)
    db.font("Helvetica-Bold")
    db.fontSize(24)
    db.text("Modular Grid", (margin, PAPER_SIZES["A4"][1] - margin))
    
    db.font("Helvetica")
    db.fontSize(10)
    db.text("Best for: complex layouts, posters, websites", 
            (margin, PAPER_SIZES["A4"][1] - margin - 30))
    
    module_w, module_h = draw_grid(*PAPER_SIZES["A4"], columns=4, rows=6, 
                                   gutter=15, margin=margin, show_diagonals=True)
    
    # Example content showing different module combinations
    db.fill(0.8, 0.2, 0.2, 0.5)
    # Large feature: 2x2 modules
    db.rect(margin, PAPER_SIZES["A4"][1] - margin - module_h * 2 - 15, 
            module_w * 2 + 15, module_h * 2 + 15)
    
    # Medium elements: 2x1 modules
    db.fill(0.2, 0.2, 0.8, 0.5)
    x = margin + (module_w + 15) * 2
    db.rect(x, PAPER_SIZES["A4"][1] - margin - module_h - 100, 
            module_w * 2 + 15, module_h)
    
    # Small elements: 1x1 modules
    db.fill(0.2, 0.6, 0.2, 0.5)
    for i in range(4):
        x = margin + i * (module_w + 15)
        db.rect(x, margin, module_w, module_h)

def golden_ratio_grid():
    """Create a grid based on golden ratio proportions"""
    width, height = PAPER_SIZES["Square"]
    margin = 40
    
    db.newPage(width, height)
    db.fill(0.98, 0.98, 0.98)
    db.rect(0, 0, width, height)
    
    # Title
    db.fill(0, 0, 0)
    db.font("Helvetica-Bold")
    db.fontSize(24)
    db.text("Golden Ratio Grid", (margin, height - margin))
    
    # Create golden rectangle divisions
    db.stroke(0.8, 0.6, 0, 0.5)
    db.strokeWidth(1)
    
    def draw_golden_spiral(x, y, size, depth=5):
        if depth <= 0:
            return
        
        # Draw rectangle
        db.rect(x, y, size, size / GOLDEN_RATIO)
        
        # Calculate next rectangle
        new_size = size / GOLDEN_RATIO
        
        # Rotate position for spiral
        if depth % 4 == 0:
            draw_golden_spiral(x + size - new_size, y, new_size, depth - 1)
        elif depth % 4 == 1:
            draw_golden_spiral(x + size - new_size, y + size/GOLDEN_RATIO - new_size, 
                             new_size, depth - 1)
        elif depth % 4 == 2:
            draw_golden_spiral(x, y + size/GOLDEN_RATIO - new_size, new_size, depth - 1)
        else:
            draw_golden_spiral(x, y, new_size, depth - 1)
    
    # Draw the golden spiral grid
    content_size = width - 2 * margin
    draw_golden_spiral(margin, margin, content_size, depth=8)
    
    db.stroke(None)
    
    # Show how content aligns to golden proportions
    db.fill(0.9, 0.1, 0.1, 0.3)
    # Major content area
    db.rect(margin, margin + content_size/GOLDEN_RATIO, 
            content_size/GOLDEN_RATIO, content_size/GOLDEN_RATIO)
    
    # Secondary content
    db.fill(0.1, 0.1, 0.9, 0.3)
    secondary_size = content_size/GOLDEN_RATIO/GOLDEN_RATIO
    db.rect(margin + content_size/GOLDEN_RATIO, margin, 
            secondary_size, secondary_size)

def baseline_grid_system():
    """Demonstrate baseline grid for vertical rhythm"""
    width, height = PAPER_SIZES["A4"]
    margin = 60
    baseline = 8  # 8pt baseline
    
    db.newPage(width, height)
    
    # Title
    db.fill(0, 0, 0)
    db.font("Helvetica-Bold")
    db.fontSize(24)
    db.text("Baseline Grid System", (margin, height - margin))
    
    # Draw baseline grid
    db.stroke(0.9, 0.9, 0.9)
    db.strokeWidth(0.5)
    for y in range(0, int(height), baseline):
        db.line((0, y), (width, y))
    
    # Draw stronger lines every 4 baselines
    db.stroke(0.7, 0.7, 0.7)
    for y in range(0, int(height), baseline * 4):
        db.line((0, y), (width, y))
    
    db.stroke(None)
    
    # Demonstrate text aligning to baseline
    y_pos = height - margin - 40
    
    # Good example - text aligns to baseline
    db.fill(0, 0.6, 0)
    db.font("Helvetica")
    db.fontSize(10)
    db.text("GOOD: Text aligns to baseline grid", (margin, y_pos))
    
    y_pos -= baseline * 4  # Move down 4 baseline units
    db.fill(0, 0, 0)
    db.fontSize(16)  # 2x baseline
    db.text("Heading on Grid", (margin, y_pos))
    
    y_pos -= baseline * 3  # 3 baseline units for 16pt text
    db.fontSize(10)
    text = """Body text sits perfectly on the baseline grid,
creating consistent vertical rhythm throughout
the design. This improves readability and creates
a sense of order and professionalism."""
    db.textBox(text, (margin, y_pos - baseline * 6, 250, baseline * 6))
    
    # Bad example - text doesn't align
    x_pos = width / 2
    y_pos = height - margin - 40
    
    db.fill(0.8, 0, 0)
    db.fontSize(10)
    db.text("BAD: Text ignores baseline grid", (x_pos, y_pos))
    
    y_pos -= 35  # Arbitrary spacing
    db.fill(0, 0, 0)
    db.fontSize(17)  # Odd size
    db.text("Misaligned Heading", (x_pos, y_pos))
    
    y_pos -= 25  # Random spacing
    db.fontSize(11)  # Not baseline multiple
    text = """This text doesn't align to the baseline
grid, creating visual discord and making
the layout feel unprofessional and
harder to read."""
    db.textBox(text, (x_pos, y_pos - 60, 250, 60))

def responsive_grid_example():
    """Show how grids adapt to different formats"""
    formats = [
        ("Mobile", 375, 667, 2, 20),
        ("Tablet", 768, 1024, 4, 30), 
        ("Desktop", 1200, 800, 12, 20)
    ]
    
    for name, width, height, columns, margin in formats:
        db.newPage(width, height)
        db.fill(0.98, 0.98, 0.98)
        db.rect(0, 0, width, height)
        
        # Title
        db.fill(0, 0, 0)
        db.font("Helvetica-Bold")
        db.fontSize(32 if width > 1000 else 24 if width > 700 else 18)
        db.text(f"{name} Grid ({columns} columns)", (margin, height - margin))
        
        # Draw the grid
        module_w, module_h = draw_grid(width, height, columns=columns, rows=8, 
                                      gutter=20, margin=margin)
        
        # Show example content blocks
        db.fill(0.2, 0.4, 0.8, 0.5)
        
        if name == "Mobile":
            # Full width blocks
            db.rect(margin, height - margin - 100, module_w * 2 + 20, 60)
            db.rect(margin, height - margin - 180, module_w * 2 + 20, 60)
        
        elif name == "Tablet":
            # 2-column layout
            db.rect(margin, height - margin - 100, module_w * 2 + 20, 120)
            db.rect(margin + (module_w + 20) * 2, height - margin - 100, 
                   module_w * 2 + 20, 120)
        
        else:  # Desktop
            # Complex layout
            db.rect(margin, height - margin - 100, module_w * 8 + 20 * 7, 60)
            db.rect(margin, height - margin - 200, module_w * 4 + 20 * 3, 80)
            db.rect(margin + (module_w + 20) * 4, height - margin - 200, 
                   module_w * 4 + 20 * 3, 80)

# Main execution
if __name__ == "__main__":
    demonstrate_grid_types()
    golden_ratio_grid()
    baseline_grid_system()
    responsive_grid_example()
    
    db.saveImage("grid_systems.pdf")
    print("Grid systems guide created successfully!")