"""
Card Layout Template

Create color-coded cards with titles and descriptions.
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

WIDTH, HEIGHT, MARGIN = setup_poster_page("letter", margin_ratio=1/10)

grid = Grid.from_margins(
    (-MARGIN, -MARGIN, -MARGIN, -MARGIN),
    column_subdivisions=12,
    row_subdivisions=12  # More rows for stacked cards
)

scale = POSTER_SCALE
colors = get_color_palette("professional")

# ==================== HELPER ====================

def draw_card(x, y, width, height, color, title, description):
    """Draw a colored card with rounded corners"""
    # Card background
    db.fill(color[0], color[1], color[2], 0.15)  # 15% opacity
    db.stroke(*color)
    db.strokeWidth(3)
    db.rect(x, y, width, height)  # Simplified (no rounded corners)
    db.strokeWidth(0)

    # Title
    db.font("Helvetica-Bold")
    db.fontSize(scale.h3)
    db.fill(*colors["text"])
    db.text(title, (x + 16, y + height - 40))

    # Description (wrapped)
    db.font("Helvetica")
    db.fontSize(scale.body)
    draw_wrapped_text(
        description,
        x + 16,
        y + height - 60,
        width - 32,
        height - 80,
        "Helvetica",
        scale.body,
        leading_ratio=1.4
    )

# ==================== BACKGROUND ====================

db.fill(*colors["background"])
db.rect(0, 0, WIDTH, HEIGHT)

# ==================== HEADER ====================

db.font("Helvetica-Bold")
db.fontSize(scale.title)
db.fill(*colors["text"])
db.text("Card Layout", (MARGIN, grid[(0, 11)][1] + 10))

# ==================== CARDS ====================

# Define card colors
card_colors = [
    (0.15, 0.35, 0.55),  # Blue
    (0.2, 0.5, 0.6),     # Teal
    (0.25, 0.55, 0.5),   # Green-teal
]

# Card 1 (rows 8-9)
card1 = (*grid[(0, 8)], *grid*(12, 2))
draw_card(
    *card1,
    card_colors[0],
    "Card 1: Title",
    "First card description. This text will wrap automatically to fit the card width."
)

# Card 2 (rows 5-6)
card2 = (*grid[(0, 5)], *grid*(12, 2))
draw_card(
    *card2,
    card_colors[1],
    "Card 2: Title",
    "Second card description with different content that also wraps automatically."
)

# Card 3 (rows 2-3)
card3 = (*grid[(0, 2)], *grid*(12, 2))
draw_card(
    *card3,
    card_colors[2],
    "Card 3: Title",
    "Third card showing the pattern. Add as many cards as needed."
)

# ==================== FOOTER ====================

db.fontSize(scale.caption)
db.fill(0.5, 0.5, 0.5)
db.text("Footer", (MARGIN, grid[(0, 0)][1] + 10))

# ==================== SAVE ====================

output = get_output_path("card_layout.pdf")
db.saveImage(str(output))
print(f"✓ Saved to {output}")
