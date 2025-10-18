"""
Grid Layouts with DrawBotGrid
=============================
Using the DrawBotGrid library for professional layouts.

What you'll learn:
- Column and row grids
- Baseline grids for typography
- Combined grid systems
- Responsive layouts
- Magazine-style compositions
"""

import sys
import os

# Add the project root to Python path to find the local drawBot module
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import drawBot as db
from drawBotGrid import Grid, ColumnGrid, RowGrid, BaselineGrid

# PAGE 1: Column Grid Basics
db.newPage(800, 1000)

# Background
db.fill(0.98)
db.rect(0, 0, 800, 1000)

# Title
db.fill(0)
db.font("Helvetica-Bold")
db.fontSize(28)
db.text("Column Grid Layouts", (50, 930))

# Create a column grid with margins
columns = ColumnGrid.from_margins((50, 50, 50, 50), subdivisions=12, gutter=20)

# Draw the grid for visualization
db.stroke(0.85)
db.strokeWidth(0.5)
columns.draw()
db.stroke(None)

# Example 1: Simple column layout
y_pos = 800

# Span across different columns
db.fill(0.2, 0.4, 0.8)
# Single column
db.rect(columns[0], columns.bottom, columns.column_width, 100)

# Three columns
db.fill(0.8, 0.2, 0.4)
db.rect(columns[3], columns.bottom, columns.span(3), 100)

# Remaining columns
db.fill(0.4, 0.8, 0.2)
db.rect(columns[6], columns.bottom, columns.span(6), 100)

# Labels
db.fill(0)
db.font("Helvetica")
db.fontSize(12)
db.text("1 column", (columns[0] + 10, 780))
db.text("3 columns", (columns[3] + 10, 780))
db.text("6 columns", (columns[6] + 10, 780))

# Example 2: Magazine-style layout
y_pos = 600

# Main content area (8 columns)
db.fill(0.95)
db.stroke(0.6)
db.strokeWidth(1)
db.rect(columns[0], y_pos - 400, columns.span(8), 400)

# Sidebar (4 columns)
db.fill(0.9)
db.rect(columns[8], y_pos - 400, columns.span(4), 400)

# Text placeholders
db.fill(0.3)
db.stroke(None)
# Main headline
db.rect(columns[0] + 20, y_pos - 60, columns.span(8) - 40, 40)
# Body text lines
for i in range(10):
    db.rect(columns[0] + 20, y_pos - 120 - i * 25, columns.span(8) - 40, 15)

# Sidebar elements
db.fill(0.5)
db.rect(columns[8] + 15, y_pos - 60, columns.span(4) - 30, 60)
db.rect(columns[8] + 15, y_pos - 150, columns.span(4) - 30, 60)
db.rect(columns[8] + 15, y_pos - 240, columns.span(4) - 30, 60)

# PAGE 2: Row Grid and Combined Grids
db.newPage(800, 1000)

# Background
db.fill(0.98)
db.rect(0, 0, 800, 1000)

# Title
db.fill(0)
db.font("Helvetica-Bold")
db.fontSize(28)
db.text("Row Grid & Combined Grids", (50, 930))

# Create a combined grid
grid = Grid.from_margins((50, 50, 50, 50), 
                        column_subdivisions=6, 
                        row_subdivisions=8,
                        column_gutter=20,
                        row_gutter=20)

# Draw the grid
db.stroke(0.85)
db.strokeWidth(0.5)
grid.draw()
db.stroke(None)

# Example 1: Grid cells
# Access grid cells using tuple indexing
colors = [
    (0.9, 0.2, 0.2),
    (0.2, 0.9, 0.2),
    (0.2, 0.2, 0.9),
    (0.9, 0.9, 0.2),
    (0.9, 0.2, 0.9),
    (0.2, 0.9, 0.9)
]

# Place elements in specific grid cells
for i in range(6):
    col = i % 3
    row = i // 3
    db.fill(*colors[i], 0.5)
    # Get position from grid
    x = grid.columns[col * 2]
    y = grid.rows[row + 2]
    width = grid.columns.span(2)
    height = grid.rows.span(1)
    db.rect(x, y, width, height)

# Example 2: Complex layout using grid
# Header spanning full width
db.fill(0.2)
x = grid.columns[0]
y = grid.rows[0]
width = grid.columns.span(6)
height = grid.rows.span(1)
db.rect(x, y, width, height)

# Main content area
db.fill(0.95)
db.stroke(0.4)
db.strokeWidth(1)
x = grid.columns[0]
y = grid.rows[5]
width = grid.columns.span(4)
height = grid.rows.span(3)
db.rect(x, y, width, height)

# Sidebar elements
db.fill(0.85)
x = grid.columns[4]
y = grid.rows[5]
width = grid.columns.span(2)
height = grid.rows.span(1)
db.rect(x, y, width, height - 10)

y = grid.rows[6]
db.rect(x, y, width, height - 10)

y = grid.rows[7]
db.rect(x, y, width, height - 10)

db.stroke(None)

# PAGE 3: Baseline Grid for Typography
db.newPage(800, 1000)

# Background
db.fill(0.98)
db.rect(0, 0, 800, 1000)

# Title
db.fill(0)
db.font("Helvetica-Bold")
db.fontSize(28)
db.text("Baseline Grid Typography", (50, 930))

# Create baseline grid
baseline = BaselineGrid.from_margins((50, 50, 50, 50), line_height=24)

# Visualize the baseline grid
db.stroke(0.9, 0.4, 0.4, 0.3)
db.strokeWidth(0.5)
baseline.draw()
db.stroke(None)

# Example text with baseline alignment
y_pos = 850

# Headline
db.font("Helvetica-Bold")
db.fontSize(36)
db.fill(0)
# Find closest baseline
headline_y = baseline.closest_line_below_coordinate(y_pos)
db.text("Typography with Baseline Grid", (50, headline_y))

# Subheadline
db.font("Helvetica")
db.fontSize(18)
db.fill(0.3)
sub_y = baseline.closest_line_below_coordinate(headline_y - 50)
db.text("Maintaining vertical rhythm across different text sizes", (50, sub_y))

# Body text
body_y = baseline.closest_line_below_coordinate(sub_y - 60)
db.fontSize(12)
db.fill(0)
body_text = """The baseline grid is fundamental to typographic design. It ensures that text aligns properly across columns and maintains consistent vertical rhythm throughout the layout. This creates a harmonious and professional appearance.

When working with different font sizes, the key is to ensure that the line height of each text style is a multiple of the baseline unit. This way, regardless of the font size, text will always align to the grid."""

# Use FormattedString for better text control
txt = db.FormattedString()
txt.append(body_text, font="Helvetica", fontSize=12, lineHeight=24)

# Text in two columns
column_width = 350
db.textBox(txt, (50, body_y - 200, column_width, 200))
db.textBox(txt, (50 + column_width + 50, body_y - 200, column_width, 200))

# Show alignment with colored bars
db.fill(0.9, 0.2, 0.2, 0.3)
for i in range(10):
    y = body_y - i * 24
    db.rect(45, y - 2, 5, 4)
    db.rect(445, y - 2, 5, 4)

# PAGE 4: Responsive Grid Layout
db.newPage(800, 1000)

# Background
db.fill(0.98)
db.rect(0, 0, 800, 1000)

# Title
db.fill(0)
db.font("Helvetica-Bold")
db.fontSize(28)
db.text("Responsive Grid Systems", (50, 930))

# Function to create responsive layout
def create_responsive_layout(x, y, width, height, breakpoint):
    """Create a layout that adapts based on width"""
    if width > breakpoint:
        # Desktop layout: 3 columns
        cols = 3
        grid = Grid((x, y, width, height), 
                   column_subdivisions=cols, 
                   row_subdivisions=2,
                   column_gutter=20,
                   row_gutter=20)
    else:
        # Mobile layout: 1 column
        cols = 1
        grid = Grid((x, y, width, height), 
                   column_subdivisions=cols, 
                   row_subdivisions=6,
                   column_gutter=20,
                   row_gutter=20)
    
    return grid, cols

# Example layouts at different sizes
layouts = [
    ("Desktop", 50, 700, 700, 180, 400),
    ("Tablet", 50, 450, 500, 180, 400),
    ("Mobile", 50, 200, 300, 180, 400)
]

for name, x, y, w, h, breakpoint in layouts:
    # Container
    db.fill(0.95)
    db.stroke(0.7)
    db.strokeWidth(1)
    db.rect(x, y, w, h)
    
    # Label
    db.fill(0)
    db.stroke(None)
    db.font("Helvetica-Bold")
    db.fontSize(14)
    db.text(f"{name} ({w}px)", (x, y + h + 10))
    
    # Create responsive grid
    grid, cols = create_responsive_layout(x, y, w, h, breakpoint)
    
    # Draw grid lightly
    db.stroke(0.85, 0.85, 0.85, 0.5)
    db.strokeWidth(0.5)
    grid.draw()
    db.stroke(None)
    
    # Place content blocks
    if cols == 3:
        # 3 column layout
        for i in range(3):
            db.fill(0.2, 0.4, 0.8, 0.5)
            x_cell = grid.columns[i]
            y_cell = grid.rows[0]
            w_cell = grid.columns.span(1)
            h_cell = grid.rows.span(1)
            db.rect(x_cell, y_cell, w_cell, h_cell)
            
            # Additional elements
            db.fill(0.6)
            y_cell = grid.rows[1]
            db.rect(x_cell, y_cell, w_cell, h_cell)
    else:
        # Single column layout
        colors = [(0.2, 0.4, 0.8), (0.8, 0.2, 0.4), (0.4, 0.8, 0.2)]
        for i in range(3):
            db.fill(*colors[i], 0.5)
            x_cell = grid.columns[0]
            y_cell = grid.rows[i * 2]
            w_cell = grid.columns.span(1)
            h_cell = grid.rows.span(2)
            db.rect(x_cell, y_cell, w_cell, h_cell - 10)

# Save the output
output_path = "output/grid_layouts.pdf"
db.saveImage(output_path)
print(f"Saved to {output_path}")

# 🎯 GRID EXERCISES:
# -----------------
# 1. Create a newspaper layout with multiple columns and baseline grid
# 2. Design a photo gallery using grid cells
# 3. Build a dashboard layout with different sized widgets
# 4. Create a book spread with margins and text columns
# 5. Design a responsive web layout that adapts to different sizes

# 💡 GRID TIPS:
# -------------
# - Always start with margins to create breathing room
# - Use consistent gutters for visual harmony
# - Baseline grids are essential for multi-column text
# - Combine different grid types for complex layouts
# - The grid is a guide, not a prison - break it purposefully

# 🔍 ADVANCED TECHNIQUES:
# ----------------------
# - Nest grids within grid cells for more control
# - Use grid.transform() for rotated layouts
# - Create asymmetric grids for dynamic compositions
# - Combine with color systems for consistent design
# - Export grid specifications for other applications