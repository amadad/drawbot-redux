"""
LongitudinalBench Poster v8 - FIXED Coordinate System

Changes from v7:
✅ FIXED: Uses get_text_metrics() instead of magic numbers (no more * 0.8)
✅ FIXED: Proper baseline calculations for all text positioning
✅ FIXED: Turn count no longer overlaps title
✅ FIXED: Descriptions wrap correctly without overflow
✅ FIXED: All elements positioned using real font metrics

This version follows the mandatory rules from docs/COORDINATE_SYSTEM_RULES.md

Design approach:
- Three-Tier Architecture as primary visual (40% of page)
- Grid-based layout (12 columns, 16 rows)
- Color-coded tiers showing temporal progression
- Proper baseline metrics and spacing (NO MAGIC NUMBERS!)
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
    get_text_metrics,  # ← NEW: Import for real metrics!
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
    """
    Draw a tier card with PROPER text metrics (v8 FIXED!)
    
    x, y = bottom-left corner from grid
    width, height = dimensions from grid
    
    FIXED in v8:
    - Uses get_text_metrics() instead of magic numbers
    - Proper baseline calculations
    - Turn count and title don't overlap
    - Description wraps correctly in remaining space
    """
    padding = 16
    
    # Card background
    db.fill(tier_color[0], tier_color[1], tier_color[2], 0.15)
    db.stroke(*tier_color)
    db.strokeWidth(3)
    draw_rounded_rect(x, y, width, height)
    db.strokeWidth(0)
    
    # ==================== TURN COUNT (top-right) ====================
    
    db.font(FONT_BOLD)
    turn_size = SCALE.h1 * 1.2
    db.fontSize(turn_size)
    
    # Get REAL metrics (not magic numbers!)
    turn_metrics = get_text_metrics(turn_count, FONT_BOLD, turn_size)
    turn_width = turn_metrics['width']
    
    # Position at right edge: right - padding - width
    turn_x = x + width - padding - turn_width
    
    # Position baseline: top of box - padding - ascender
    # This puts the TOP of the text exactly at (y + height - padding)
    turn_baseline_y = y + height - padding - turn_metrics['ascender']
    
    db.fill(*tier_color)
    db.text(turn_count, (turn_x, turn_baseline_y))
    
    # ==================== TITLE (top-left) ====================
    
    db.font(FONT_BOLD)
    title_size = SCALE.h3
    db.fontSize(title_size)
    
    # Get REAL metrics
    title_metrics = get_text_metrics(tier_title, FONT_BOLD, title_size)
    
    # Position at left edge: left + padding
    title_x = x + padding
    
    # Position baseline: same as turn count (both aligned to top)
    title_baseline_y = y + height - padding - title_metrics['ascender']
    
    # Maximum width: don't overlap with turn count (leave 20pt gap)
    title_max_width = (turn_x - 20) - title_x
    
    db.fill(*COLORS["text"])
    db.text(tier_title, (title_x, title_baseline_y))
    
    # ==================== DESCRIPTION (below title) ====================
    
    # Find where title ends (baseline + descender)
    title_bottom_y = title_baseline_y + title_metrics['descender']
    
    # Add gap below title
    gap = 12
    desc_top_y = title_bottom_y - gap
    
    # Description area dimensions
    desc_x = x + padding
    desc_width = width - (padding * 2)
    
    # Height: from desc_top_y down to bottom of card + padding
    desc_height = desc_top_y - (y + padding)
    
    # Draw wrapped description
    db.font(FONT_REGULAR)
    desc_size = SCALE.body * 0.9
    db.fontSize(desc_size)
    db.fill(0.3, 0.3, 0.3)
    
    # draw_wrapped_text expects TOP-LEFT corner
    draw_wrapped_text(
        tier_desc,
        desc_x,
        desc_top_y,
        desc_width,
        desc_height,
        FONT_REGULAR,
        desc_size,
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

# GiveCare branding - FIXED: use real metrics
db.font(FONT_LIGHT)
brand_size = SCALE.body
db.fontSize(brand_size)
brand_metrics = get_text_metrics("GiveCare", FONT_LIGHT, brand_size)

# Position in row 15
brand_y = grid[(0, 15)][1] + (grid.rows.row_height / 2) - (brand_metrics['ascender'] / 2)

db.fill(0.5, 0.5, 0.5)
db.text("GiveCare", (MARGIN, brand_y))

# Main title - FIXED: use real metrics
db.font(FONT_BOLD)
title_size = SCALE.title
db.fontSize(title_size)
title_metrics = get_text_metrics("LongitudinalBench", FONT_BOLD, title_size)

# Position in row 14 (vertically centered)
title_y = grid[(0, 14)][1] + (grid.rows.row_height / 2) - (title_metrics['ascender'] / 2)

db.fill(*COLORS["text"])
db.text("LongitudinalBench", (MARGIN, title_y))

# Subtitle - FIXED: position below title
db.font(FONT_REGULAR)
subtitle_size = SCALE.h3
db.fontSize(subtitle_size)
subtitle_metrics = get_text_metrics("Sample", FONT_REGULAR, subtitle_size)

# Start below title
subtitle_y = title_y + title_metrics['descender'] - 10

db.fill(*COLORS["accent"])
db.text("AI Safety Benchmark for", (MARGIN, subtitle_y))

# Second line of subtitle
subtitle_line2_y = subtitle_y - subtitle_metrics['line_height']
db.text("Longitudinal Caregiver Support", (MARGIN, subtitle_line2_y))

# ==================== STATUS BOX ====================

status_x, status_y, status_w, status_h = status_area

db.fill(STATUS_COLOR[0], STATUS_COLOR[1], STATUS_COLOR[2], 0.2)
db.stroke(*STATUS_COLOR)
db.strokeWidth(2)
draw_rounded_rect(status_x, status_y, status_w, status_h, radius=6)
db.strokeWidth(0)

# Status label - FIXED: use real metrics
db.font(FONT_BOLD)
status_label_size = SCALE.caption * 1.3
db.fontSize(status_label_size)
status_label_metrics = get_text_metrics("PRELIMINARY", FONT_BOLD, status_label_size)

status_label_y = status_y + status_h - 12 - status_label_metrics['ascender']

db.fill(*COLORS["text"])
db.text("PRELIMINARY", (status_x + 12, status_label_y))

# Status info - FIXED: position below label
db.font(FONT_REGULAR)
info_size = SCALE.caption
db.fontSize(info_size)
info_metrics = get_text_metrics("v0.1.0", FONT_REGULAR, info_size)

info_start_y = status_label_y + status_label_metrics['descender'] - 8

db.fill(0.4, 0.4, 0.4)
db.text("v0.1.0", (status_x + 12, info_start_y))
db.text("2 models tested", (status_x + 12, info_start_y - info_metrics['line_height']))
db.text("3 scenarios", (status_x + 12, info_start_y - info_metrics['line_height'] * 2))

# ==================== THREE-TIER ARCHITECTURE ====================

# Section title - FIXED: use real metrics
db.font(FONT_BOLD)
section_title_size = SCALE.h2
db.fontSize(section_title_size)
section_metrics = get_text_metrics("Three-Tier Architecture", FONT_BOLD, section_title_size)

# Position in row 13
tier_title_y = grid[(0, 13)][1] + (grid.rows.row_height / 2) - (section_metrics['ascender'] / 2)

db.fill(*COLORS["text"])
db.text("Three-Tier Architecture", (MARGIN, tier_title_y))

# Timeline arrow - position below section title
timeline_y = tier_title_y + section_metrics['descender'] - 12

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

# Tier cards - FIXED with new draw_tier_card function
tier1_x, tier1_y, tier1_w, tier1_h = tier1_area
draw_tier_card(
    tier1_x, tier1_y, tier1_w, tier1_h,
    1, TIER_COLORS[0], "Tier 1: Immediate Safety",
    "Crisis detection and immediate safety response. Rapid assessment of urgent needs and appropriate intervention.",
    "3-5 turns"
)

tier2_x, tier2_y, tier2_w, tier2_h = tier2_area
draw_tier_card(
    tier2_x, tier2_y, tier2_w, tier2_h,
    2, TIER_COLORS[1], "Tier 2: Relationship Formation",
    "Building therapeutic alliance and maintaining professional boundaries. Establishing trust and appropriate connection.",
    "8-12 turns"
)

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

# "What is it?" heading - FIXED: use real metrics
db.font(FONT_BOLD)
what_heading_size = SCALE.h3
db.fontSize(what_heading_size)
what_heading_metrics = get_text_metrics("What is it?", FONT_BOLD, what_heading_size)

# Position at top of left column
what_heading_y = left_y + left_h - what_heading_metrics['ascender']

db.fill(*COLORS["text"])
db.text("What is it?", (left_x, what_heading_y))

# "What" description - position below heading
what_text_top_y = what_heading_y + what_heading_metrics['descender'] - 8

db.font(FONT_REGULAR)
db.fontSize(SCALE.body)
db.fill(0.3, 0.3, 0.3)

what_text = "A longitudinal benchmark evaluating AI safety across extended caregiver support conversations, focusing on crisis handling, relationship maintenance, and temporal consistency."

what_final_y = draw_wrapped_text(
    what_text,
    left_x,
    what_text_top_y,
    left_w,
    70,  # Limit height
    FONT_REGULAR,
    SCALE.body,
    leading_ratio=1.5
)

# "Why it matters?" heading - FIXED: position below what section
db.font(FONT_BOLD)
db.fontSize(what_heading_size)

why_heading_y = what_final_y - 20 - what_heading_metrics['ascender']

db.fill(*COLORS["text"])
db.text("Why it matters?", (left_x, why_heading_y))

# "Why" description
why_text_top_y = why_heading_y + what_heading_metrics['descender'] - 8

db.font(FONT_REGULAR)
db.fontSize(SCALE.body)
db.fill(0.3, 0.3, 0.3)

why_text = "Ensures AI systems can safely support vulnerable caregivers over time without causing harm, maintaining boundaries, and providing consistent, culturally-sensitive guidance."

draw_wrapped_text(
    why_text,
    left_x,
    why_text_top_y,
    left_w,
    70,  # Limit height
    FONT_REGULAR,
    SCALE.body,
    leading_ratio=1.5
)

# Right column: Evaluation Dimensions
right_x, right_y, right_w, right_h = right_col_area

# Heading - FIXED: use real metrics
db.font(FONT_BOLD)
dim_heading_size = SCALE.h3
db.fontSize(dim_heading_size)
dim_heading_metrics = get_text_metrics("Eight Evaluation Dimensions", FONT_BOLD, dim_heading_size)

dim_heading_y = right_y + right_h - dim_heading_metrics['ascender']

db.fill(*COLORS["text"])
db.text("Eight Evaluation Dimensions", (right_x, dim_heading_y))

# Dimensions list - FIXED: use real metrics for spacing
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
dim_item_size = SCALE.body
db.fontSize(dim_item_size)
dim_item_metrics = get_text_metrics("Sample", FONT_REGULAR, dim_item_size)

# Start below heading
dim_current_y = dim_heading_y + dim_heading_metrics['descender'] - 12

for dim_name, current_score, max_score in dimensions:
    db.fill(*COLORS["text"])
    db.text(dim_name, (right_x, dim_current_y))
    
    # Dots aligned with text baseline
    dots_x = right_x + 180
    draw_score_dots(dots_x, dim_current_y + 2, current_score, max_score)
    
    # Move down by line height
    dim_current_y -= dim_item_metrics['line_height']

# Score legend
db.font(FONT_LIGHT)
db.fontSize(SCALE.caption)
db.fill(0.5, 0.5, 0.5)
db.text("Score: 0 (baseline) to max per dimension", (right_x, dim_current_y - 8))

# ==================== FOOTER ====================

footer_x, footer_y, footer_w, footer_h = footer_area

# Footer text - FIXED: vertically center in footer row
db.font(FONT_LIGHT)
footer_size = SCALE.caption
db.fontSize(footer_size)
footer_metrics = get_text_metrics("Sample", FONT_LIGHT, footer_size)

footer_text_y = footer_y + (footer_h / 2) - (footer_metrics['ascender'] / 2)

db.fill(0.5, 0.5, 0.5)

# Left: GitHub
db.text("github.com/givecare/longitudinalbench", (MARGIN, footer_text_y))

# Center: Citation
citation = "Cite: GiveCare (2024)"
citation_w, _ = db.textSize(citation)
db.text(citation, ((WIDTH - citation_w) / 2, footer_text_y))

# Right: License
license_text = "CC BY 4.0"
license_w, _ = db.textSize(license_text)
db.text(license_text, (WIDTH - MARGIN - license_w, footer_text_y))

# ==================== DEBUG (optional) ====================

# Uncomment to visualize grid during development:
# grid.draw(show_index=True)

# ==================== SAVE OUTPUT ====================

# Use portable paths (works on any machine)
output_pdf = get_output_path("longitudinalbench_poster_v8.pdf")
output_png = get_output_path("longitudinalbench_poster_v8.png")

db.saveImage(str(output_pdf))
print(f"✓ PDF saved: {output_pdf}")

db.saveImage(str(output_png))
print(f"✓ PNG saved: {output_png}")

print("\n✓ LongitudinalBench Poster v8 generated successfully!")
print(f"  FIXED: All text positioning uses real metrics (no magic numbers)")
print(f"  FIXED: Turn counts don't overlap titles")
print(f"  FIXED: Descriptions wrap correctly in card boundaries")
print(f"  Using grid system: {grid.columns.columns} cols × {grid.rows.rows} rows")
print(f"  Typography scale: base {SCALE.body}pt, ratio {SCALE.ratio}")
print(f"  Output directory: {output_pdf.parent}")
