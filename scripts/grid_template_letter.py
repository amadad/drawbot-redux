"""
Letter-sized Grid Template
Just the grid visualization, no text
"""

import sys
import os

# Add the project root to Python path
project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import drawBot as db
from drawBotGrid import Grid, ColumnGrid, RowGrid, BaselineGrid

# US Letter dimensions
page_width = 612  # 8.5 inches
page_height = 792  # 11 inches

# Create page
db.newPage(page_width, page_height)

# White background
db.fill(1, 1, 1)
db.rect(0, 0, page_width, page_height)

# Grid parameters
margins = (72, 72, 72, 72)  # 1 inch margins all around

# Column grid - 12 columns with 12pt gutter
columns = ColumnGrid.from_margins(margins, subdivisions=12, gutter=12)

# Baseline grid - 8pt baseline
baseline = BaselineGrid.from_margins(margins, line_height=8)

# Draw baseline grid first (lighter)
db.stroke(0.9, 0.9, 0.9)  # Very light gray
db.strokeWidth(0.25)
baseline.draw()

# Draw stronger baseline every 8 lines (64pt)
db.stroke(0.85, 0.85, 0.85)  # Light gray
db.strokeWidth(0.5)
for i in range(0, int(page_height / 8), 8):
    y = i * 8
    if margins[2] <= y <= page_height - margins[0]:
        db.line((margins[3], y), (page_width - margins[1], y))

# Draw column grid
db.stroke(0.3, 0.5, 0.9, 0.5)  # Blue with transparency
db.strokeWidth(0.5)
columns.draw()

# Draw margins
db.stroke(1, 0, 0, 0.3)  # Red with transparency
db.strokeWidth(1)
db.fill(None)
# Top margin
db.line((0, page_height - margins[0]), (page_width, page_height - margins[0]))
# Right margin
db.line((page_width - margins[1], 0), (page_width - margins[1], page_height))
# Bottom margin
db.line((0, margins[2]), (page_width, margins[2]))
# Left margin
db.line((margins[3], 0), (margins[3], page_height))

# Reset stroke
db.stroke(None)

# Save
output_path = "output/grid_template_letter.pdf"
db.saveImage(output_path)
print(f"Grid template saved to: {output_path}")