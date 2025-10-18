"""
LongitudinalBench Poster v2 - Improved Design

Design approach:
- Hero section: Three-Tier Architecture as PRIMARY visual focal point (40% of page)
- Asymmetric golden ratio layout (38%/62% split)
- Color-coded tiers showing temporal progression
- Visual score indicators for eight dimensions using dot system
- Dramatic typography scale using golden ratio (1.618)
- Subtle gradient background for depth
- Compressed supporting context to prioritize methodology
"""

try:
    # Try drawbot-skia first (cross-platform)
    from drawBot import *
    import drawBot as db
    USE_SKIA = True
except ImportError:
    # Fall back to macOS DrawBot
    import drawBot as db
    USE_SKIA = False

import textwrap

# ==================== CANVAS & SYSTEM ====================

# Letter size canvas
WIDTH = 612  # 8.5 inches
HEIGHT = 792  # 11 inches

db.newPage(WIDTH, HEIGHT)

# Design system variables
MARGIN = WIDTH / 10  # 61.2pt - generous margins
GUTTER = 24
BASE_LINE = 6  # Baseline grid unit

# Golden ratio typography scale
SCALE_RATIO = 1.618
BASE_SIZE = 11
SIZE_CAPTION = BASE_SIZE / SCALE_RATIO  # ~6.8pt
SIZE_BODY = BASE_SIZE  # 11pt
SIZE_H3 = BASE_SIZE * SCALE_RATIO  # ~18pt
SIZE_H2 = BASE_SIZE * (SCALE_RATIO ** 2)  # ~29pt
SIZE_H1 = BASE_SIZE * (SCALE_RATIO ** 3)  # ~47pt
SIZE_TITLE = BASE_SIZE * (SCALE_RATIO ** 4)  # ~76pt

# Font weights
FONT_BOLD = "Helvetica-Bold"
FONT_REGULAR = "Helvetica"
FONT_LIGHT = "Helvetica-Light"

# Color palette
BG_COLOR = (0.98, 0.98, 0.97)  # Off-white
TEXT_DARK = (0.1, 0.1, 0.1)  # Near black
TEXT_MEDIUM = (0.3, 0.3, 0.3)  # Medium gray
ACCENT_COLOR = (0.2, 0.45, 0.7)  # Professional blue

# Color-coded tier system (blue to teal progression)
TIER_1_COLOR = (0.15, 0.35, 0.55)  # Deep blue
TIER_2_COLOR = (0.2, 0.5, 0.6)  # Teal
TIER_3_COLOR = (0.25, 0.55, 0.5)  # Green-teal

STATUS_COLOR = (0.95, 0.7, 0.2)  # Yellow-orange for "preliminary"

# Layout dimensions
usable_width = WIDTH - (MARGIN * 2)
usable_height = HEIGHT - (MARGIN * 2)

# Golden ratio layout proportions
LEFT_COL_WIDTH = usable_width * 0.382  # ~38%
RIGHT_COL_WIDTH = usable_width * 0.618  # ~62%

# ==================== BACKGROUND LAYER ====================

# Solid background
db.fill(*BG_COLOR)
db.rect(0, 0, WIDTH, HEIGHT)

# Subtle gradient for depth
db.fill(None)
db.linearGradient(
    (0, 0), (WIDTH, HEIGHT),
    [(BG_COLOR[0] - 0.02, BG_COLOR[1] - 0.02, BG_COLOR[2] - 0.02),
     (BG_COLOR[0] + 0.01, BG_COLOR[1] + 0.01, BG_COLOR[2] + 0.01)],
    [0, 1]
)
db.rect(0, 0, WIDTH, HEIGHT)

# ==================== HELPER FUNCTIONS ====================

def draw_score_dots(x, y, current, maximum, dot_size=8, dot_spacing=12):
    """Draw visual score indicators as filled/unfilled dots"""
    for i in range(maximum):
        if i < current:
            db.fill(*ACCENT_COLOR)
        else:
            db.fill(0.85)
        db.oval(x + (i * dot_spacing), y, dot_size, dot_size)

def draw_tier_card(x, y, width, height, tier_num, tier_color, tier_title, tier_desc, turn_count):
    """Draw a large horizontal tier card"""
    # Card background with rounded corners
    db.fill(tier_color[0], tier_color[1], tier_color[2], 0.15)  # 15% opacity
    db.stroke(*tier_color)
    db.strokeWidth(3)

    # Draw rounded rectangle using path
    path = db.BezierPath()
    radius = 8
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

    db.strokeWidth(0)

    # Turn count (large, prominent)
    db.fill(*tier_color)
    db.font(FONT_BOLD)
    db.fontSize(SIZE_H1)
    turn_y = y + height - 48
    db.text(turn_count, (x + 16, turn_y))

    # Tier label
    db.font(FONT_BOLD)
    db.fontSize(SIZE_H3)
    db.fill(*TEXT_DARK)
    db.text(tier_title, (x + 16, turn_y - 26))

    # Description text (wrapped manually)
    db.font(FONT_REGULAR)
    db.fontSize(SIZE_BODY)
    db.fill(*TEXT_MEDIUM)

    # Wrap text manually
    wrapped_lines = textwrap.wrap(tier_desc, width=70)
    desc_y = y + 16
    for line in wrapped_lines[:2]:  # Max 2 lines
        db.text(line, (x + 16, desc_y))
        desc_y -= 14

def draw_dimension_row(x, y, dimension_name, current_score, max_score):
    """Draw a single evaluation dimension with score dots"""
    # Dimension name
    db.font(FONT_REGULAR)
    db.fontSize(SIZE_BODY)
    db.fill(*TEXT_DARK)
    db.text(dimension_name, (x, y))

    # Score dots to the right
    dots_x = x + 200
    draw_score_dots(dots_x, y + 2, current_score, max_score)

def wrap_text_lines(text, y, width_chars=60):
    """Helper to wrap and draw multi-line text"""
    wrapped_lines = textwrap.wrap(text, width=width_chars)
    for line in wrapped_lines:
        db.text(line, (MARGIN, y))
        y -= 14
    return y

# ==================== CONTENT LAYERS ====================

# Current Y position tracker
current_y = HEIGHT - MARGIN

# === HEADER SECTION ===

# GiveCare branding (small, top-left)
db.font(FONT_LIGHT)
db.fontSize(SIZE_BODY)
db.fill(*TEXT_MEDIUM)
db.text("GiveCare", (MARGIN, current_y))
current_y -= 30

# Main title (bold, large)
db.font(FONT_BOLD)
db.fontSize(SIZE_TITLE)
db.fill(*TEXT_DARK)
db.text("LongitudinalBench", (MARGIN, current_y))
current_y -= 90

# Subtitle (wrapped)
db.font(FONT_REGULAR)
db.fontSize(SIZE_H3)
db.fill(*ACCENT_COLOR)
db.text("AI Safety Benchmark for", (MARGIN, current_y))
current_y -= 24
db.text("Longitudinal Caregiver Support", (MARGIN, current_y))
current_y -= 60

# === STATUS BOX (small colored sidebar) ===
status_box_width = 160
status_box_height = 80
status_x = WIDTH - MARGIN - status_box_width
status_y = HEIGHT - MARGIN - 140

# Status box background
db.fill(STATUS_COLOR[0], STATUS_COLOR[1], STATUS_COLOR[2], 0.2)
db.stroke(*STATUS_COLOR)
db.strokeWidth(2)

# Rounded rect for status
status_path = db.BezierPath()
radius = 6
status_path.moveTo((status_x + radius, status_y))
status_path.lineTo((status_x + status_box_width - radius, status_y))
status_path.curveTo((status_x + status_box_width, status_y), (status_x + status_box_width, status_y),
                    (status_x + status_box_width, status_y + radius))
status_path.lineTo((status_x + status_box_width, status_y + status_box_height - radius))
status_path.curveTo((status_x + status_box_width, status_y + status_box_height),
                    (status_x + status_box_width, status_y + status_box_height),
                    (status_x + status_box_width - radius, status_y + status_box_height))
status_path.lineTo((status_x + radius, status_y + status_box_height))
status_path.curveTo((status_x, status_y + status_box_height), (status_x, status_y + status_box_height),
                    (status_x, status_y + status_box_height - radius))
status_path.lineTo((status_x, status_y + radius))
status_path.curveTo((status_x, status_y), (status_x, status_y), (status_x + radius, status_y))
status_path.closePath()
db.drawPath(status_path)
db.strokeWidth(0)

db.font(FONT_BOLD)
db.fontSize(SIZE_CAPTION * 1.2)
db.fill(*TEXT_DARK)
db.text("PRELIMINARY", (status_x + 12, status_y + 55))

db.font(FONT_REGULAR)
db.fontSize(SIZE_CAPTION)
db.fill(*TEXT_MEDIUM)
db.text("v0.1.0", (status_x + 12, status_y + 42))
db.text("2 models tested", (status_x + 12, status_y + 30))
db.text("3 scenarios", (status_x + 12, status_y + 18))

# === THREE-TIER ARCHITECTURE (HERO SECTION - 40% of page) ===

tier_section_height = usable_height * 0.42
tier_card_height = (tier_section_height - (GUTTER * 2)) / 3

# Section title
db.font(FONT_BOLD)
db.fontSize(SIZE_H2)
db.fill(*TEXT_DARK)
db.text("Three-Tier Architecture", (MARGIN, current_y))
current_y -= 40

# Timeline arrow (horizontal line showing progression)
timeline_y = current_y + 10
db.stroke(*TEXT_MEDIUM)
db.strokeWidth(2)
db.line((MARGIN, timeline_y), (WIDTH - MARGIN - status_box_width - 20, timeline_y))
# Arrow head
db.line((WIDTH - MARGIN - status_box_width - 20, timeline_y),
        (WIDTH - MARGIN - status_box_width - 30, timeline_y - 5))
db.line((WIDTH - MARGIN - status_box_width - 20, timeline_y),
        (WIDTH - MARGIN - status_box_width - 30, timeline_y + 5))
db.strokeWidth(0)

db.font(FONT_LIGHT)
db.fontSize(SIZE_CAPTION)
db.fill(*TEXT_MEDIUM)
db.text("temporal progression", (WIDTH - MARGIN - status_box_width - 150, timeline_y + 8))

current_y -= 30

# Tier 1 card
draw_tier_card(
    MARGIN, current_y - tier_card_height, usable_width, tier_card_height,
    1, TIER_1_COLOR, "Tier 1: Immediate Safety",
    "Crisis detection and immediate safety response. Rapid assessment of urgent needs and appropriate intervention.",
    "3-5 turns"
)
current_y -= (tier_card_height + GUTTER)

# Tier 2 card
draw_tier_card(
    MARGIN, current_y - tier_card_height, usable_width, tier_card_height,
    2, TIER_2_COLOR, "Tier 2: Relationship Formation",
    "Building therapeutic alliance and maintaining professional boundaries. Establishing trust and appropriate connection.",
    "8-12 turns"
)
current_y -= (tier_card_height + GUTTER)

# Tier 3 card
draw_tier_card(
    MARGIN, current_y - tier_card_height, usable_width, tier_card_height,
    3, TIER_3_COLOR, "Tier 3: Longitudinal Consistency",
    "Multi-session coherence and memory integrity. Maintaining consistent support across extended timeframes.",
    "20+ turns"
)
current_y -= (tier_card_height + GUTTER + 30)

# === ASYMMETRIC TWO-COLUMN LAYOUT (38%/62% split) ===

# Left column: What & Why (compressed to 1-2 sentences each)
left_col_x = MARGIN
left_col_y = current_y

db.font(FONT_BOLD)
db.fontSize(SIZE_H3)
db.fill(*TEXT_DARK)
db.text("What is it?", (left_col_x, left_col_y))
left_col_y -= 26

db.font(FONT_REGULAR)
db.fontSize(SIZE_BODY)
db.fill(*TEXT_MEDIUM)
what_lines = [
    "A longitudinal benchmark evaluating AI safety",
    "across extended caregiver support conversations,",
    "focusing on crisis handling, relationship",
    "maintenance, and temporal consistency."
]
for line in what_lines:
    db.text(line, (left_col_x, left_col_y))
    left_col_y -= 14
left_col_y -= 20

db.font(FONT_BOLD)
db.fontSize(SIZE_H3)
db.fill(*TEXT_DARK)
db.text("Why it matters?", (left_col_x, left_col_y))
left_col_y -= 26

db.font(FONT_REGULAR)
db.fontSize(SIZE_BODY)
db.fill(*TEXT_MEDIUM)
why_lines = [
    "Ensures AI systems can safely support",
    "vulnerable caregivers over time without causing",
    "harm, maintaining boundaries, and providing",
    "consistent, culturally-sensitive guidance."
]
for line in why_lines:
    db.text(line, (left_col_x, left_col_y))
    left_col_y -= 14

# Right column: Eight Evaluation Dimensions (with visual score indicators)
right_col_x = MARGIN + LEFT_COL_WIDTH + GUTTER
right_col_y = current_y

db.font(FONT_BOLD)
db.fontSize(SIZE_H3)
db.fill(*TEXT_DARK)
db.text("Eight Evaluation Dimensions", (right_col_x, right_col_y))
right_col_y -= 30

# Draw each dimension with score dots
dimensions = [
    ("Crisis Safety", 0, 3),
    ("Regulatory Fitness", 0, 3),
    ("Trauma-Informed Flow", 0, 3),
    ("Belonging & Cultural Fitness", 0, 2),
    ("Relational Quality", 0, 3),
    ("Actionable Support", 0, 3),
    ("Longitudinal Consistency", 0, 2),
    ("Memory Hygiene", 0, 1),
]

for dim_name, current_score, max_score in dimensions:
    draw_dimension_row(right_col_x, right_col_y, dim_name, current_score, max_score)
    right_col_y -= 20

# Score legend
right_col_y -= 10
db.font(FONT_LIGHT)
db.fontSize(SIZE_CAPTION)
db.fill(*TEXT_MEDIUM)
db.text("Score range: 0 (baseline) to max per dimension", (right_col_x, right_col_y))

# ==================== FOOTER ====================

footer_y = MARGIN - 30

db.font(FONT_LIGHT)
db.fontSize(SIZE_CAPTION)
db.fill(*TEXT_MEDIUM)

# Left: GitHub
db.text("github.com/givecare/longitudinalbench", (MARGIN, footer_y))

# Center: Citation
citation = "Cite: GiveCare (2024)"
center_x = (WIDTH - 120) / 2  # Approximate centering
db.text(citation, (center_x, footer_y))

# Right: License
db.text("CC BY 4.0", (WIDTH - MARGIN - 70, footer_y))

# ==================== SAVE OUTPUT ====================

# Save as PDF
output_pdf = "/Users/amadad/Projects/tools/drawbot-redux/output/longitudinalbench_poster_v2.pdf"
db.saveImage(output_pdf)
print(f"PDF saved: {output_pdf}")

# Save as PNG
output_png = "/Users/amadad/Projects/tools/drawbot-redux/output/longitudinalbench_poster_v2.png"
db.saveImage(output_png)
print(f"PNG saved: {output_png}")

print("LongitudinalBench Poster v2 generated successfully!")
