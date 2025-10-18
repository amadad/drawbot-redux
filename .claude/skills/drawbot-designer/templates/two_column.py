"""
Two-Column Layout Template

Magazine-style two-column design with automatic gutter.
"""

import sys
from pathlib import Path
# From .claude/skills/drawbot-designer/templates/ go up to repo root, then into lib/
repo_root = Path(__file__).resolve().parent.parent.parent.parent.parent
sys.path.insert(0, str(repo_root / "lib"))

import drawBot as db
from drawbot_grid import Grid
from drawbot_design_system import (
    MAGAZINE_SCALE,  # Note: Using MAGAZINE_SCALE for multi-column
    get_output_path,
    get_color_palette,
    draw_wrapped_text,
    setup_poster_page
)

# ==================== SETUP ====================

WIDTH, HEIGHT, MARGIN = setup_poster_page("letter", margin_ratio=1/10)

grid = Grid.from_margins(
    (-MARGIN, -MARGIN, -MARGIN, -MARGIN),
    column_subdivisions=12,
    row_subdivisions=8,
    column_gutter=20,  # Wider gutter for two-column
    row_gutter=10
)

scale = MAGAZINE_SCALE
colors = get_color_palette("professional")

# ==================== BACKGROUND ====================

db.fill(*colors["background"])
db.rect(0, 0, WIDTH, HEIGHT)

# ==================== HEADER ====================

db.font("Helvetica-Bold")
db.fontSize(scale.h1)
db.fill(*colors["text"])
db.text("Two-Column Layout", (MARGIN, grid[(0, 7)][1] + 10))

# ==================== COLUMNS ====================

# Define columns (5 cols each, 2 cols gutter between)
left_col = (*grid[(0, 1)], *grid*(5, 6))   # Cols 0-4, Rows 1-6
right_col = (*grid[(7, 1)], *grid*(5, 6))  # Cols 7-11, Rows 1-6
# Columns 5-6 is automatic gutter

# Left column
left_text = """
This is the left column text. It will wrap automatically to fit the column
width. Add your content here.
"""

db.font("Helvetica")
db.fontSize(scale.body)
db.fill(*colors["text"])

draw_wrapped_text(
    left_text.strip(),
    left_col[0] + 10,
    left_col[1] + left_col[3] - 10,
    left_col[2] - 20,
    left_col[3] - 20,
    "Helvetica",
    scale.body,
    leading_ratio=1.5
)

# Right column
right_text = """
This is the right column text. It will also wrap automatically. The columns
are separated by an automatic gutter.
"""

draw_wrapped_text(
    right_text.strip(),
    right_col[0] + 10,
    right_col[1] + right_col[3] - 10,
    right_col[2] - 20,
    right_col[3] - 20,
    "Helvetica",
    scale.body,
    leading_ratio=1.5
)

# ==================== FOOTER ====================

db.fontSize(scale.caption)
db.fill(0.5, 0.5, 0.5)
db.text("Footer", (MARGIN, grid[(0, 0)][1] + 10))

# ==================== SAVE ====================

output = get_output_path("two_column_layout.pdf")
db.saveImage(str(output))
print(f"✓ Saved to {output}")
