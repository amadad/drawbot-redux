"""
DEBUG: Tier Card - Let's see what's ACTUALLY happening
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "lib"))

import drawBot as db
from drawbot_grid import Grid
from drawbot_design_system import (
    setup_poster_page,
    get_output_path,
    get_text_metrics,
    POSTER_SCALE
)

# Setup
WIDTH, HEIGHT, MARGIN = setup_poster_page("letter", margin_ratio=1/10)

grid = Grid.from_margins(
    (-MARGIN, -MARGIN, -MARGIN, -MARGIN),
    column_subdivisions=12,
    row_subdivisions=16,
    column_gutter=10,
    row_gutter=10
)

# Background
db.fill(0.95, 0.95, 0.95)
db.rect(0, 0, WIDTH, HEIGHT)

# Get ONE tier card area
tier1_area = (*grid[(0, 11)], *grid*(12, 3))
x, y, width, height = tier1_area

print(f"\n=== TIER 1 CARD DEBUG ===")
print(f"Grid returned: x={x}, y={y}, width={width}, height={height}")
print(f"Bottom-left: ({x}, {y})")
print(f"Top-right: ({x + width}, {y + height})")
print(f"Page height: {HEIGHT}")

# Draw the card boundary (RED)
db.stroke(1, 0, 0)
db.strokeWidth(3)
db.fill(None)
db.rect(x, y, width, height)

# Mark corners
db.fill(1, 0, 0)
db.oval(x - 5, y - 5, 10, 10)  # Bottom-left (RED)
db.fill(0, 1, 0)
db.oval(x + width - 5, y + height - 5, 10, 10)  # Top-right (GREEN)

# Add labels
db.fill(0, 0, 0)
db.fontSize(10)
db.text(f"BL: ({x:.0f}, {y:.0f})", (x + 5, y + 5))
db.text(f"TR: ({x + width:.0f}, {y + height:.0f})", (x + width - 100, y + height - 15))

# Now let's try to position the turn count
padding = 16
turn_count = "3-5 turns"

db.font("Helvetica-Bold")
turn_size = POSTER_SCALE.h1 * 1.2
db.fontSize(turn_size)

# Get metrics
turn_metrics = get_text_metrics(turn_count, "Helvetica-Bold", turn_size)

print(f"\n=== TURN COUNT METRICS ===")
print(f"Text: '{turn_count}'")
print(f"Font size: {turn_size}")
print(f"Width: {turn_metrics['width']}")
print(f"Ascender: {turn_metrics['ascender']}")
print(f"Descender: {turn_metrics['descender']}")
print(f"Line height: {turn_metrics['line_height']}")

# Calculate position
turn_x = x + width - padding - turn_metrics['width']
turn_baseline_y = y + height - padding - turn_metrics['ascender']

print(f"\n=== CALCULATED POSITION ===")
print(f"Turn X: {turn_x}")
print(f"Turn baseline Y: {turn_baseline_y}")
print(f"Text top should be at: {turn_baseline_y + turn_metrics['ascender']} (should equal {y + height - padding})")
print(f"Text bottom should be at: {turn_baseline_y + turn_metrics['descender']}")

# Draw baseline line (BLUE)
db.stroke(0, 0, 1)
db.strokeWidth(1)
db.line((turn_x, turn_baseline_y), (turn_x + turn_metrics['width'], turn_baseline_y))

# Draw text top line (GREEN)
text_top_y = turn_baseline_y + turn_metrics['ascender']
db.stroke(0, 1, 0)
db.line((turn_x, text_top_y), (turn_x + turn_metrics['width'], text_top_y))

# Draw text bottom line (RED)
text_bottom_y = turn_baseline_y + turn_metrics['descender']
db.stroke(1, 0, 0)
db.line((turn_x, text_bottom_y), (turn_x + turn_metrics['width'], text_bottom_y))

# Draw the actual text
db.strokeWidth(0)
db.fill(0.15, 0.35, 0.55)
db.text(turn_count, (turn_x, turn_baseline_y))

# Now let's try the title
title = "Tier 1: Immediate Safety"
title_size = POSTER_SCALE.h3

db.font("Helvetica-Bold")
db.fontSize(title_size)

title_metrics = get_text_metrics(title, "Helvetica-Bold", title_size)

print(f"\n=== TITLE METRICS ===")
print(f"Text: '{title}'")
print(f"Font size: {title_size}")
print(f"Width: {title_metrics['width']}")
print(f"Ascender: {title_metrics['ascender']}")
print(f"Descender: {title_metrics['descender']}")

# Calculate title position (should be at same top as turn count)
title_x = x + padding
title_baseline_y = y + height - padding - title_metrics['ascender']

print(f"\n=== TITLE POSITION ===")
print(f"Title X: {title_x}")
print(f"Title baseline Y: {title_baseline_y}")
print(f"Title top: {title_baseline_y + title_metrics['ascender']} (should equal {y + height - padding})")

# Check for overlap
title_right = title_x + title_metrics['width']
gap = turn_x - title_right

print(f"\n=== OVERLAP CHECK ===")
print(f"Title right edge: {title_right}")
print(f"Turn left edge: {turn_x}")
print(f"Gap between: {gap}")
if gap < 0:
    print(f"❌ OVERLAP BY {abs(gap)} POINTS!")
else:
    print(f"✓ No overlap, {gap}pt gap")

# Draw title baseline (PURPLE)
db.stroke(0.5, 0, 0.5)
db.strokeWidth(1)
db.line((title_x, title_baseline_y), (title_x + title_metrics['width'], title_baseline_y))

# Draw title
db.strokeWidth(0)
db.fill(0, 0, 0)
db.text(title, (title_x, title_baseline_y))

# Draw the gap area (YELLOW highlight if overlap)
if gap < 0:
    db.fill(1, 1, 0, 0.3)
    db.rect(turn_x, y, abs(gap), height)
else:
    db.fill(0, 1, 0, 0.1)
    db.rect(title_right, y + height - padding - 30, gap, 30)

# Add annotations
db.fill(0, 0, 0)
db.fontSize(12)
db.text("Card boundary (red)", (x, y - 20))
db.text("Turn count baseline (blue)", (x, y - 35))
db.text("Title baseline (purple)", (x, y - 50))

# Save
output = get_output_path("DEBUG_tier_card.pdf")
db.saveImage(str(output))
print(f"\n✓ Saved to {output}")
print("\nOpen the PDF to see the visual debugging!")
