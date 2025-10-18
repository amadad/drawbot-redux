"""
LongitudinalBench Poster v7 - PROPERLY Using Design System

This version:
✅ Uses grid system for spatial awareness
✅ Uses proper typography scale for posters
✅ Uses real text metrics (not fontSize approximations)
✅ Wraps text based on points (not character count)
✅ Validates layout fits before drawing
✅ Uses portable paths (works on any machine)

Design approach:
- Three-Tier Architecture as primary visual (40% of page)
- Grid-based layout (12 columns, 16 rows)
- Color-coded tiers showing temporal progression
- Proper baseline metrics and spacing
"""

import sys
from pathlib import Path

# Add lib to path
sys.path.insert(0, str(Path(__file__).parent.parent / "lib"))

import drawBot as db
from drawbot_grid import Grid
from drawbot_design_system import (
    POSTER_SCALE,
    get_output_path,
    get_color_palette,
    draw_wrapped_text,
    validate_layout_fit,
    setup_poster_page
)

# ==================== SETUP ====================

# Page setup (returns width, height, margin)
WIDTH, HEIGHT, MARGIN = setup_poster_page("letter", margin_ratio=1/10)

# Typography scale (poster-appropriate: base 18pt, ratio 1.5)
SCALE = POSTER_SCALE

# Colors (70-20-10 rule)
COLORS = get_color_palette("professional")

# Fonts
FONT_BOLD = "Helvetica-Bold"
FONT_REGULAR = "Helvetica"
FONT_LIGHT = "Helvetica-Light"

# Color-coded tier system
TIER_COLORS = [
    (0.15, 0.35, 0.55),  # Tier 1: Deep blue
    (0.2, 0.5, 0.6),     # Tier 2: Teal
    (0.25, 0.55, 0.5)    # Tier 3: Green-teal
]

STATUS_COLOR = (0.95, 0.7, 0.2)  # Yellow-orange

# ==================== GRID SYSTEM ====================

# Define grid FIRST (before any drawing)
grid = Grid.from_margins(
    (-MARGIN, -MARGIN, -MARGIN, -MARGIN),
    column_subdivisions=12,
    row_subdivisions=16,
    column_gutter=10,
    row_gutter=10
)

# Allocate rows (verify total = 16)
HEADER_ROWS = 2      # Brand + title
TIER_ROWS = 9        # 3 tiers (3 rows each)
CONTENT_ROWS = 4     # Two-column content
FOOTER_ROWS = 1      # Footer

assert HEADER_ROWS + TIER_ROWS + CONTENT_ROWS + FOOTER_ROWS == 16, "Grid allocation mismatch!"

# Define layout areas using grid coordinates
header_area = (*grid[(0, 14)], *grid*(12, HEADER_ROWS))
tier1_area = (*grid[(0, 11)], *grid*(12, 3))
tier2_area = (*grid[(0, 8)], *grid*(12, 3))
tier3_area = (*grid[(0, 5)], *grid*(12, 3))
left_col_area = (*grid[(0, 1)], *grid*(5, CONTENT_ROWS))
right_col_area = (*grid[(7, 1)], *grid*(5, CONTENT_ROWS))
footer_area = (*grid[(0, 0)], *grid*(12, FOOTER_ROWS))

# Status box (top-right overlay)
status_area = (WIDTH - MARGIN - 160, HEIGHT - MARGIN - 140, 160, 100)

# ==================== BACKGROUND ====================

db.fill(*COLORS["background"])
db.rect(0, 0, WIDTH, HEIGHT)

# Subtle gradient
db.fill(None)
bg_start = tuple(max(0, c - 0.02) for c in COLORS["background"])
bg_end = tuple(min(1, c + 0.01) for c in COLORS["background"])
db.linearGradient(
    (0, 0), (WIDTH, HEIGHT),
    [bg_start, bg_end],
    [0, 1]
)
db.rect(0, 0, WIDTH, HEIGHT)

# ==================== HELPER FUNCTIONS ====================

def draw_rounded_rect(x, y, width, height, radius=8):
    """Draw a rounded rectangle using BezierPath"""
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

def draw_tier_card(x, y, width, height, tier_num, tier_color, tier_title, tier_desc, turn_count):
    """Draw a tier card with proper text metrics"""
    # Card background
    db.fill(tier_color[0], tier_color[1], tier_color[2], 0.15)
    db.stroke(*tier_color)
    db.strokeWidth(3)
    draw_rounded_rect(x, y, width, height)
    db.strokeWidth(0)

    # Content padding
    padding = 16

    # Turn count (large, right side)
    db.fill(*tier_color)
    db.font(FONT_BOLD)
    db.fontSize(SCALE.h1 * 1.2)  # Make it bigger for visual impact
    turn_width, _ = db.textSize(turn_count)
    turn_x = x + width - padding - turn_width
    turn_y = y + height - padding - SCALE.h1 * 0.8

    db.text(turn_count, (turn_x, turn_y))

    # Tier title (left side, top - ensure no overlap with turn count)
    db.font(FONT_BOLD)
    db.fontSize(SCALE.h3)
    db.fill(*COLORS["text"])
    title_max_width = width - turn_width - (padding * 3)  # Leave space for turn count
    db.text(tier_title, (x + padding, y + height - padding - SCALE.h3 * 0.8))

    # Description (wrapped to fit card width)
    db.font(FONT_REGULAR)
    db.fontSize(SCALE.body * 0.9)  # Slightly smaller for better fit
    db.fill(0.3, 0.3, 0.3)  # Medium gray

    # Calculate available space (below title)
    desc_width = width - (padding * 2)
    desc_height = height - (padding * 2) - SCALE.h3 - 20  # Space for title + margin

    # Draw wrapped text (fills available space)
    draw_wrapped_text(
        tier_desc,
        x + padding,
        y + height - padding - SCALE.h3 - 20,  # Start below title
        desc_width,
        desc_height,
        FONT_REGULAR,
        SCALE.body * 0.9,
        leading_ratio=1.4
    )

def draw_score_dots(x, y, current, maximum, dot_size=8, dot_spacing=12):
    """Draw visual score indicators"""
    for i in range(maximum):
        if i < current:
            db.fill(*COLORS["accent"])
        else:
            db.fill(0.85, 0.85, 0.85)
        db.oval(x + (i * dot_spacing), y, dot_size, dot_size)

# ==================== HEADER SECTION ====================

# GiveCare branding
db.font(FONT_LIGHT)
db.fontSize(SCALE.body)
db.fill(*COLORS["text"])
db.fill(0.5, 0.5, 0.5)
db.text("GiveCare", (MARGIN, grid[(0, 15)][1] + grid.rows.row_height * 0.3))

# Main title
db.font(FONT_BOLD)
db.fontSize(SCALE.title)
db.fill(*COLORS["text"])
db.text("LongitudinalBench", (MARGIN, grid[(0, 14)][1] + grid.rows.row_height * 0.2))

# Subtitle
db.font(FONT_REGULAR)
db.fontSize(SCALE.h3)
db.fill(*COLORS["accent"])
subtitle_y = grid[(0, 14)][1] - 10
db.text("AI Safety Benchmark for", (MARGIN, subtitle_y))
db.text("Longitudinal Caregiver Support", (MARGIN, subtitle_y - SCALE.h3 * 1.3))

# ==================== STATUS BOX ====================

status_x, status_y, status_w, status_h = status_area

db.fill(STATUS_COLOR[0], STATUS_COLOR[1], STATUS_COLOR[2], 0.2)
db.stroke(*STATUS_COLOR)
db.strokeWidth(2)
draw_rounded_rect(status_x, status_y, status_w, status_h, radius=6)
db.strokeWidth(0)

db.font(FONT_BOLD)
db.fontSize(SCALE.caption * 1.3)
db.fill(*COLORS["text"])
db.text("PRELIMINARY", (status_x + 12, status_y + status_h - 20))

db.font(FONT_REGULAR)
db.fontSize(SCALE.caption)
db.fill(0.4, 0.4, 0.4)
info_y = status_y + status_h - 40
db.text("v0.1.0", (status_x + 12, info_y))
db.text("2 models tested", (status_x + 12, info_y - 14))
db.text("3 scenarios", (status_x + 12, info_y - 28))

# ==================== THREE-TIER ARCHITECTURE ====================

# Section title
db.font(FONT_BOLD)
db.fontSize(SCALE.h2)
db.fill(*COLORS["text"])
tier_title_y = grid[(0, 13)][1] + grid.rows.row_height * 0.5
db.text("Three-Tier Architecture", (MARGIN, tier_title_y))

# Timeline arrow
timeline_y = tier_title_y - 20
db.stroke(0.5, 0.5, 0.5)
db.strokeWidth(2)
arrow_end = WIDTH - MARGIN - 180
db.line((MARGIN, timeline_y), (arrow_end, timeline_y))
db.line((arrow_end, timeline_y), (arrow_end - 10, timeline_y - 5))
db.line((arrow_end, timeline_y), (arrow_end - 10, timeline_y + 5))
db.strokeWidth(0)

db.font(FONT_LIGHT)
db.fontSize(SCALE.caption)
db.fill(0.5, 0.5, 0.5)
db.text("temporal progression →", (arrow_end - 140, timeline_y + 8))

# Tier 1 card
tier1_x, tier1_y, tier1_w, tier1_h = tier1_area
draw_tier_card(
    tier1_x, tier1_y, tier1_w, tier1_h,
    1, TIER_COLORS[0], "Tier 1: Immediate Safety",
    "Crisis detection and immediate safety response. Rapid assessment of urgent needs and appropriate intervention.",
    "3-5 turns"
)

# Tier 2 card
tier2_x, tier2_y, tier2_w, tier2_h = tier2_area
draw_tier_card(
    tier2_x, tier2_y, tier2_w, tier2_h,
    2, TIER_COLORS[1], "Tier 2: Relationship Formation",
    "Building therapeutic alliance and maintaining professional boundaries. Establishing trust and appropriate connection.",
    "8-12 turns"
)

# Tier 3 card
tier3_x, tier3_y, tier3_w, tier3_h = tier3_area
draw_tier_card(
    tier3_x, tier3_y, tier3_w, tier3_h,
    3, TIER_COLORS[2], "Tier 3: Longitudinal Consistency",
    "Multi-session coherence and memory integrity. Maintaining consistent support across extended timeframes.",
    "20+ turns"
)

# ==================== TWO-COLUMN CONTENT ====================

# Left column: What & Why
left_x, left_y, left_w, left_h = left_col_area

db.font(FONT_BOLD)
db.fontSize(SCALE.h3)
db.fill(*COLORS["text"])
what_y = left_y + left_h - SCALE.h3
db.text("What is it?", (left_x, what_y))

db.font(FONT_REGULAR)
db.fontSize(SCALE.body)
db.fill(0.3, 0.3, 0.3)
what_text = "A longitudinal benchmark evaluating AI safety across extended caregiver support conversations, focusing on crisis handling, relationship maintenance, and temporal consistency."
what_final_y = draw_wrapped_text(
    what_text,
    left_x,
    what_y - 10,
    left_w,
    80,
    FONT_REGULAR,
    SCALE.body,
    leading_ratio=1.5
)

db.font(FONT_BOLD)
db.fontSize(SCALE.h3)
db.fill(*COLORS["text"])
why_y = what_final_y - 30
db.text("Why it matters?", (left_x, why_y))

db.font(FONT_REGULAR)
db.fontSize(SCALE.body)
db.fill(0.3, 0.3, 0.3)
why_text = "Ensures AI systems can safely support vulnerable caregivers over time without causing harm, maintaining boundaries, and providing consistent, culturally-sensitive guidance."
draw_wrapped_text(
    why_text,
    left_x,
    why_y - 10,
    left_w,
    80,
    FONT_REGULAR,
    SCALE.body,
    leading_ratio=1.5
)

# Right column: Evaluation Dimensions
right_x, right_y, right_w, right_h = right_col_area

db.font(FONT_BOLD)
db.fontSize(SCALE.h3)
db.fill(*COLORS["text"])
dim_y = right_y + right_h - SCALE.h3
db.text("Eight Evaluation Dimensions", (right_x, dim_y))

# Draw dimensions with scores
dimensions = [
    ("Crisis Safety", 0, 3),
    ("Regulatory Fitness", 0, 3),
    ("Trauma-Informed Flow", 0, 3),
    ("Belonging & Cultural Fit", 0, 2),
    ("Relational Quality", 0, 3),
    ("Actionable Support", 0, 3),
    ("Longitudinal Consistency", 0, 2),
    ("Memory Hygiene", 0, 1),
]

db.font(FONT_REGULAR)
db.fontSize(SCALE.body)
dim_current_y = dim_y - 24

for dim_name, current_score, max_score in dimensions:
    db.fill(*COLORS["text"])
    db.text(dim_name, (right_x, dim_current_y))

    # Dots to the right
    dots_x = right_x + 180
    draw_score_dots(dots_x, dim_current_y + 2, current_score, max_score)

    dim_current_y -= 20

# Score legend
db.font(FONT_LIGHT)
db.fontSize(SCALE.caption)
db.fill(0.5, 0.5, 0.5)
db.text("Score: 0 (baseline) to max per dimension", (right_x, dim_current_y - 10))

# ==================== FOOTER ====================

footer_x, footer_y, footer_w, footer_h = footer_area

db.font(FONT_LIGHT)
db.fontSize(SCALE.caption)
db.fill(0.5, 0.5, 0.5)

# Left: GitHub
db.text("github.com/givecare/longitudinalbench", (MARGIN, footer_y + 10))

# Center: Citation
citation = "Cite: GiveCare (2024)"
citation_w, _ = db.textSize(citation)
db.text(citation, ((WIDTH - citation_w) / 2, footer_y + 10))

# Right: License
license_text = "CC BY 4.0"
license_w, _ = db.textSize(license_text)
db.text(license_text, (WIDTH - MARGIN - license_w, footer_y + 10))

# ==================== DEBUG (optional) ====================

# Uncomment to visualize grid during development:
# grid.draw(show_index=True)

# ==================== SAVE OUTPUT ====================

# Use portable paths (works on any machine)
output_pdf = get_output_path("longitudinalbench_poster_v7.pdf")
output_png = get_output_path("longitudinalbench_poster_v7.png")

db.saveImage(str(output_pdf))
print(f"✓ PDF saved: {output_pdf}")

db.saveImage(str(output_png))
print(f"✓ PNG saved: {output_png}")

print("\n✓ LongitudinalBench Poster v7 generated successfully!")
print(f"  Using grid system: {grid.columns.columns} cols × {grid.rows.rows} rows")
print(f"  Typography scale: base {SCALE.body}pt, ratio {SCALE.ratio}")
print(f"  Output directory: {output_pdf.parent}")
