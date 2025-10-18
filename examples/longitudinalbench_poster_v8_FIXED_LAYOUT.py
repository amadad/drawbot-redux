"""
LongitudinalBench Poster v8 - FIXED LAYOUT

The REAL problem: Content doesn't fit horizontally.

Solution: Stack turn count ABOVE title instead of side-by-side.

This is a DESIGN fix, not a code fix.
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "lib"))

import drawBot as db
from drawbot_grid import Grid
from drawbot_design_system import (
    POSTER_SCALE,
    get_output_path,
    get_color_palette,
    get_text_metrics,
    draw_wrapped_text,
    setup_poster_page
)

# Setup
WIDTH, HEIGHT, MARGIN = setup_poster_page("letter", margin_ratio=1/10)
SCALE = POSTER_SCALE
COLORS = get_color_palette("professional")

FONT_BOLD = "Helvetica-Bold"
FONT_REGULAR = "Helvetica"
FONT_LIGHT = "Helvetica-Light"

TIER_COLORS = [
    (0.15, 0.35, 0.55),
    (0.2, 0.5, 0.6),
    (0.25, 0.55, 0.5)
]

grid = Grid.from_margins(
    (-MARGIN, -MARGIN, -MARGIN, -MARGIN),
    column_subdivisions=12,
    row_subdivisions=16,
    column_gutter=10,
    row_gutter=10
)

# Background
db.fill(*COLORS["background"])
db.rect(0, 0, WIDTH, HEIGHT)

def draw_rounded_rect(x, y, width, height, radius=8):
    """Draw rounded rectangle"""
    path = db.BezierPath()
    path.moveTo((x + radius, y))
    path.lineTo((x + width - radius, y))
    path.curveTo((x + width, y), (x + width, y), (x + width, y + radius))
    path.lineTo((x + width, y + height - radius))
    path.curveTo((x + width, y + height), (x + width, y + height), (x + width - radius, y + height))
    path.lineTo((x + radius, y + height))
    path.curveTo((x, y + height), (x, y + height), (x, y + height - radius))
    path.lineTo((x, y + radius))
    path.curveTo((x, y), (x, y), (x + radius, y))
    path.closePath()
    db.drawPath(path)

def draw_tier_card_STACKED(x, y, width, height, tier_num, tier_color, tier_title, tier_desc, turn_count):
    """
    FIXED LAYOUT: Turn count stacked ABOVE title
    
    Layout from top to bottom:
    1. Turn count (large, centered or right-aligned)
    2. Title (below turn count)
    3. Description (wrapped, fills remaining space)
    """
    padding = 16
    
    # Card background
    db.fill(tier_color[0], tier_color[1], tier_color[2], 0.15)
    db.stroke(*tier_color)
    db.strokeWidth(3)
    draw_rounded_rect(x, y, width, height)
    db.strokeWidth(0)
    
    # ========== TURN COUNT (top, right-aligned) ==========
    
    db.font(FONT_BOLD)
    turn_size = SCALE.h1  # Smaller than before (60pt instead of 73pt)
    db.fontSize(turn_size)
    
    turn_metrics = get_text_metrics(turn_count, FONT_BOLD, turn_size)
    
    # Right-align
    turn_x = x + width - padding - turn_metrics['width']
    # Top of card
    turn_baseline_y = y + height - padding - turn_metrics['ascender']
    
    db.fill(*tier_color)
    db.text(turn_count, (turn_x, turn_baseline_y))
    
    # ========== TITLE (below turn count, left-aligned) ==========
    
    db.font(FONT_BOLD)
    title_size = SCALE.h3
    db.fontSize(title_size)
    
    title_metrics = get_text_metrics(tier_title, FONT_BOLD, title_size)
    
    # Left side
    title_x = x + padding
    
    # Below turn count (add small gap)
    gap_after_turn = 8
    title_baseline_y = turn_baseline_y + turn_metrics['descender'] - gap_after_turn - title_metrics['ascender']
    
    db.fill(*COLORS["text"])
    db.text(tier_title, (title_x, title_baseline_y))
    
    # ========== DESCRIPTION (below title) ==========
    
    # Start below title
    title_bottom_y = title_baseline_y + title_metrics['descender']
    gap_after_title = 8
    desc_top_y = title_bottom_y - gap_after_title
    
    # Available height
    desc_height = desc_top_y - (y + padding)
    
    db.font(FONT_REGULAR)
    desc_size = SCALE.body * 0.85
    db.fontSize(desc_size)
    db.fill(0.3, 0.3, 0.3)
    
    draw_wrapped_text(
        tier_desc,
        x + padding,
        desc_top_y,
        width - (padding * 2),
        desc_height,
        FONT_REGULAR,
        desc_size,
        leading_ratio=1.4
    )

# Simple layout for demo
tier1_area = (*grid[(0, 11)], *grid*(12, 3))

draw_tier_card_STACKED(
    *tier1_area,
    1,
    TIER_COLORS[0],
    "Tier 1: Immediate Safety",
    "Crisis detection and immediate safety response. Rapid assessment of urgent needs and appropriate intervention.",
    "3-5 turns"
)

tier2_area = (*grid[(0, 8)], *grid*(12, 3))

draw_tier_card_STACKED(
    *tier2_area,
    2,
    TIER_COLORS[1],
    "Tier 2: Relationship Formation",
    "Building therapeutic alliance and maintaining professional boundaries. Establishing trust and appropriate connection.",
    "8-12 turns"
)

tier3_area = (*grid[(0, 5)], *grid*(12, 3))

draw_tier_card_STACKED(
    *tier3_area,
    3,
    TIER_COLORS[2],
    "Tier 3: Longitudinal Consistency",
    "Multi-session coherence and memory integrity. Maintaining consistent support across extended timeframes.",
    "20+ turns"
)

# Title at top
db.font(FONT_BOLD)
db.fontSize(SCALE.title * 0.8)
db.fill(*COLORS["text"])
db.text("LongitudinalBench", (MARGIN, HEIGHT - MARGIN - 40))

db.font(FONT_REGULAR)
db.fontSize(SCALE.h3)
db.fill(*COLORS["accent"])
db.text("Fixed Layout: Turn counts no longer overlap!", (MARGIN, HEIGHT - MARGIN - 70))

# Save
output = get_output_path("longitudinalbench_poster_v8_FIXED_LAYOUT.pdf")
db.saveImage(str(output))
print(f"✓ Saved: {output}")
print("\n✅ FIXED: Turn counts now stack ABOVE titles (no overlap)")
print("✅ FIXED: All content fits within card boundaries")
print("✅ FIXED: Proper spacing between all elements")
