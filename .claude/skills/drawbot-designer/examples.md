# DrawBot Designer - Examples

Practical examples showing how to use the design system. All examples are tested and working.

## Minimal Poster (80 lines)

Complete working poster in minimal code:

```python
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "lib"))

from drawbot_skia import drawbot as db
from drawbot_grid import Grid
from drawbot_design_system import (
    POSTER_SCALE,
    get_output_path,
    get_color_palette,
    draw_wrapped_text,
    setup_poster_page
)

# Setup
WIDTH, HEIGHT, MARGIN = setup_poster_page("letter", margin_ratio=1/10)
grid = Grid.from_margins((-MARGIN, -MARGIN, -MARGIN, -MARGIN),
                         column_subdivisions=12, row_subdivisions=8)
scale = POSTER_SCALE
colors = get_color_palette("professional")

# Background
db.fill(*colors["background"])
db.rect(0, 0, WIDTH, HEIGHT)

# Title (top 2 rows)
db.font("Helvetica-Bold")
db.fontSize(scale.title)
db.fill(*colors["text"])
db.text("Poster Title", (MARGIN, grid[(0, 7)][1] + 20))

# Subtitle
db.fontSize(scale.h2)
db.fill(*colors["accent"])
db.text("Subtitle Here", (MARGIN, grid[(0, 6)][1] + 10))

# Body text (rows 1-5)
body_text = """
This is body text that will automatically wrap to fit the available
width. No manual calculation needed.
""".strip()

db.font("Helvetica")
db.fontSize(scale.body)
db.fill(*colors["text"])

draw_wrapped_text(
    body_text,
    MARGIN,
    grid[(0, 5)][1] - 10,
    (grid * (12, 1))[0] - MARGIN * 2,
    (grid * (4, 1))[1],
    "Helvetica",
    scale.body,
    leading_ratio=1.5
)

# Footer
db.fontSize(scale.caption)
db.fill(0.5, 0.5, 0.5)
db.text("Footer Info", (MARGIN, grid[(0, 0)][1] + 10))

# Save
db.saveImage(str(get_output_path("minimal_poster.pdf")))
print("✓ Saved to output/minimal_poster.pdf")
```

**Run**: `uv run python examples/your_file.py`

## Two-Column Layout

Magazine-style two-column design:

```python
# ... (same setup as above)

# Define columns with automatic gutter
left_col = (*grid[(0, 1)], *grid*(5, 6))   # Cols 0-4, Rows 1-6
right_col = (*grid[(7, 1)], *grid*(5, 6))  # Cols 7-11, Rows 1-6
# Columns 5-6 is automatic gutter (20pt based on column_gutter)

# Left column content
db.font("Helvetica-Bold")
db.fontSize(scale.h2)
db.fill(*colors["text"])
db.text("Left Column", (left_col[0] + 10, left_col[1] + left_col[3] - 20))

# Right column content
db.text("Right Column", (right_col[0] + 10, right_col[1] + right_col[3] - 20))

# Optional: visualize columns during development
# db.stroke(1, 0, 0, 0.3)
# db.strokeWidth(1)
# db.rect(*left_col)
# db.rect(*right_col)
```

## Color-Coded Cards

Create colored card sections:

```python
# ... (setup)

def draw_card(x, y, width, height, color, title, description):
    """Draw a colored card with rounded corners"""
    # Card background
    db.fill(color[0], color[1], color[2], 0.15)  # 15% opacity
    db.stroke(*color)
    db.strokeWidth(3)

    # Rounded rectangle (simplified)
    radius = 8
    # ... (use BezierPath for rounded corners, see full example)
    db.rect(x, y, width, height)  # Simplified for example

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

# Use it
card1_area = (*grid[(0, 10)], *grid*(12, 2))
draw_card(
    *card1_area,
    (0.15, 0.35, 0.55),  # Blue
    "Card Title",
    "This is the card description that will wrap automatically."
)
```

## Three-Tier Architecture

Visual hierarchy with three sections:

```python
# ... (setup with 16 rows)

# Define tier areas (3 rows each)
tier1 = (*grid[(0, 11)], *grid*(12, 3))
tier2 = (*grid[(0, 8)], *grid*(12, 3))
tier3 = (*grid[(0, 5)], *grid*(12, 3))

# Tier colors (progression)
tier_colors = [
    (0.15, 0.35, 0.55),  # Deep blue
    (0.2, 0.5, 0.6),     # Teal
    (0.25, 0.55, 0.5)    # Green-teal
]

# Draw each tier
for i, (tier_area, color) in enumerate(zip([tier1, tier2, tier3], tier_colors)):
    draw_card(
        *tier_area,
        color,
        f"Tier {i+1}: Title",
        f"Description for tier {i+1}"
    )
```

## Status Badge

Small colored indicator box:

```python
# ... (setup)

# Status box (top-right)
status_w, status_h = 160, 80
status_x = WIDTH - MARGIN - status_w
status_y = HEIGHT - MARGIN - status_h - 60

# Background
db.fill(0.95, 0.7, 0.2, 0.2)  # Yellow-orange, 20% opacity
db.stroke(0.95, 0.7, 0.2)
db.strokeWidth(2)
db.rect(status_x, status_y, status_w, status_h)
db.strokeWidth(0)

# Text
db.font("Helvetica-Bold")
db.fontSize(scale.caption * 1.2)
db.fill(*colors["text"])
db.text("PRELIMINARY", (status_x + 12, status_y + status_h - 20))

db.font("Helvetica")
db.fontSize(scale.caption)
db.fill(0.4, 0.4, 0.4)
db.text("v0.1.0", (status_x + 12, status_y + status_h - 40))
```

## Visual Scores (Dot System)

Rating visualization with filled/unfilled dots:

```python
def draw_score_dots(x, y, current, maximum, dot_size=8, dot_spacing=12):
    """Draw score indicators as dots"""
    for i in range(maximum):
        if i < current:
            db.fill(*colors["accent"])  # Filled
        else:
            db.fill(0.85, 0.85, 0.85)   # Unfilled
        db.oval(x + (i * dot_spacing), y, dot_size, dot_size)

# Use it
dimensions = [
    ("Crisis Safety", 2, 3),
    ("Regulatory Fitness", 1, 3),
    ("Trauma-Informed Flow", 3, 3),
]

y = grid[(0, 5)][1]
for name, score, max_score in dimensions:
    db.font("Helvetica")
    db.fontSize(scale.body)
    db.fill(*colors["text"])
    db.text(name, (MARGIN, y))

    draw_score_dots(MARGIN + 200, y + 2, score, max_score)
    y -= 20
```

## Timeline Arrow

Showing progression:

```python
# Horizontal timeline
timeline_y = grid[(0, 12)][1]
arrow_start = MARGIN
arrow_end = WIDTH - MARGIN - 100

# Line
db.stroke(0.5, 0.5, 0.5)
db.strokeWidth(2)
db.line((arrow_start, timeline_y), (arrow_end, timeline_y))

# Arrow head
db.line((arrow_end, timeline_y), (arrow_end - 10, timeline_y - 5))
db.line((arrow_end, timeline_y), (arrow_end - 10, timeline_y + 5))
db.strokeWidth(0)

# Label
db.font("Helvetica-Light")
db.fontSize(scale.caption)
db.fill(0.5, 0.5, 0.5)
db.text("temporal progression →", (arrow_end - 140, timeline_y + 8))
```

## Grid Visualization (Debug)

Show grid structure during development:

```python
# At the end of your script (before saveImage)

# Visualize grid
grid.draw(show_index=True)

# This shows:
# - Grid lines in magenta
# - Column/row indices
# - Helps verify layout calculations
```

**Remove before final output!**

## Different Page Sizes

### A4

```python
WIDTH, HEIGHT, MARGIN = setup_poster_page("a4", margin_ratio=1/10)
# 595 × 842 pt
```

### Tabloid (11×17)

```python
WIDTH, HEIGHT, MARGIN = setup_poster_page("tabloid", margin_ratio=1/10)
# 792 × 1224 pt
```

### Square

```python
WIDTH, HEIGHT, MARGIN = setup_poster_page("square", margin_ratio=1/10)
# 792 × 792 pt
```

### Landscape

```python
WIDTH, HEIGHT, MARGIN = setup_poster_page("letter",
                                           margin_ratio=1/10,
                                           orientation="landscape")
# 792 × 612 pt (flipped)
```

## Custom Colors

```python
# Define custom palette
custom_colors = {
    "background": (0.96, 0.96, 0.94),  # Warm white
    "text": (0.15, 0.1, 0.05),          # Warm black
    "accent": (0.8, 0.3, 0.2)           # Terracotta
}

# Use it
db.fill(*custom_colors["background"])
db.rect(0, 0, WIDTH, HEIGHT)
```

## Adding Textures

```python
# Load texture from assets
texture_path = "../../assets/paper/01.jpg"

# Place image
db.image(
    texture_path,
    (0, 0),
    alpha=0.3  # 30% opacity
)

# Draw content on top
# ...
```

**Available textures**: See `../../assets/README.md`

## Complete Working Example

See `../../examples/longitudinalbench_poster_v7.py` (352 lines) for a production-ready poster with:
- Grid-based layout (12×16)
- Three-tier color-coded cards
- Two-column content
- Status badge
- Score visualization
- Timeline arrow
- Proper text wrapping
- All design principles applied

**Run it**:
```bash
uv run python examples/longitudinalbench_poster_v7.py
open output/longitudinalbench_poster_v7.pdf
```

## Tips

1. **Start with minimal example** - Get the basics working first
2. **Use grid visualization** - `grid.draw(show_index=True)` during development
3. **Test text wrapping early** - Ensure content fits before adding detail
4. **Reference working code** - Copy patterns from examples
5. **Iterate visually** - Save and view PDF frequently

## Common Modifications

### Larger Title
```python
# Before
db.fontSize(scale.title)  # 91pt

# After
db.fontSize(scale.title * 1.2)  # 109pt
```

### Tighter Grid
```python
# Before
grid = Grid.from_margins(..., column_gutter=10, row_gutter=10)

# After
grid = Grid.from_margins(..., column_gutter=5, row_gutter=5)
```

### More Columns
```python
# Before
grid = Grid.from_margins(..., column_subdivisions=12)

# After
grid = Grid.from_margins(..., column_subdivisions=16)
# Allows finer horizontal control
```

## Next Steps

1. Copy minimal example to start
2. Modify for your content
3. Reference these patterns as needed
4. See `reference.md` for API details
5. Check `../../docs/` for design theory
