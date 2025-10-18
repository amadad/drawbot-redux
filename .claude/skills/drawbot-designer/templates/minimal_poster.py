"""
Minimal Poster Template

Copy this file to start a new poster. Modify the content sections marked with # TODO
"""

import sys
from pathlib import Path
# From .claude/skills/drawbot-designer/templates/ go up to repo root, then into lib/
repo_root = Path(__file__).resolve().parent.parent.parent.parent.parent
sys.path.insert(0, str(repo_root / "lib"))

import drawBot as db
from drawbot_grid import Grid
from drawbot_design_system import (
    POSTER_SCALE,
    get_output_path,
    get_color_palette,
    draw_wrapped_text,
    setup_poster_page
)

# ==================== SETUP ====================

# Page setup
WIDTH, HEIGHT, MARGIN = setup_poster_page("letter", margin_ratio=1/10)

# Grid (12 columns × 8 rows)
grid = Grid.from_margins(
    (-MARGIN, -MARGIN, -MARGIN, -MARGIN),
    column_subdivisions=12,
    row_subdivisions=8
)

# Typography
scale = POSTER_SCALE  # or MAGAZINE_SCALE, BOOK_SCALE, REPORT_SCALE

# Colors
colors = get_color_palette("professional")  # or "warm", "cool", "high_contrast"

# ==================== BACKGROUND ====================

db.fill(*colors["background"])
db.rect(0, 0, WIDTH, HEIGHT)

# ==================== CONTENT ====================

# TODO: Update with your content

# Title (top 2 rows)
db.font("Helvetica-Bold")
db.fontSize(scale.title)
db.fill(*colors["text"])
db.text("Your Title Here", (MARGIN, grid[(0, 7)][1] + 20))

# Subtitle
db.fontSize(scale.h2)
db.fill(*colors["accent"])
db.text("Your Subtitle", (MARGIN, grid[(0, 6)][1] + 10))

# Body text (rows 1-5)
body_text = """
Replace this with your body text. It will automatically wrap to fit the
available width using proper point-based measurements.
"""

db.font("Helvetica")
db.fontSize(scale.body)
db.fill(*colors["text"])

draw_wrapped_text(
    body_text.strip(),
    MARGIN,
    grid[(0, 5)][1] - 10,
    (grid * (12, 1))[0] - MARGIN * 2,
    (grid * (4, 1))[1],
    "Helvetica",
    scale.body,
    leading_ratio=1.5
)

# Footer (row 0)
db.fontSize(scale.caption)
db.fill(0.5, 0.5, 0.5)
db.text("Footer text", (MARGIN, grid[(0, 0)][1] + 10))

# ==================== DEBUG (optional) ====================

# Uncomment to visualize grid during development:
# grid.draw(show_index=True)

# ==================== SAVE ====================

# TODO: Change filename
output = get_output_path("my_poster.pdf")
db.saveImage(str(output))
print(f"✓ Saved to {output}")
