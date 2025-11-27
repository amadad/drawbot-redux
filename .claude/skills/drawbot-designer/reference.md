# DrawBot Designer - API Reference

Quick reference for the DrawBot Redux design system. For complete documentation, see `../../docs/`.

## Design System API

### Setup

```python
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "lib"))

import drawBot as db
from drawbot_grid import Grid
from drawbot_design_system import (
    POSTER_SCALE, MAGAZINE_SCALE, BOOK_SCALE, REPORT_SCALE,
    get_output_path,
    get_color_palette,
    draw_wrapped_text,
    setup_poster_page
)
```

### Typography Scales

| Scale          | Base | Ratio | Use Case                |
|----------------|------|-------|-------------------------|
| POSTER_SCALE   | 18pt | 1.5   | Posters, displays       |
| MAGAZINE_SCALE | 11pt | 1.25  | Magazines, newsletters  |
| BOOK_SCALE     | 11pt | 1.2   | Books, long-form text   |
| REPORT_SCALE   | 12pt | 1.25  | Reports, documentation  |

**Access sizes**:
```python
scale = POSTER_SCALE
scale.caption   # 12pt
scale.body      # 18pt
scale.h3        # 27pt
scale.h2        # 40.5pt
scale.h1        # 60.75pt
scale.title     # 91.125pt
scale.ratio     # 1.5
```

### Page Setup

```python
# Quick setup (creates canvas and returns dimensions)
WIDTH, HEIGHT, MARGIN = setup_poster_page(
    size="letter",          # "letter", "tabloid", "a4", "a3", "square"
    margin_ratio=1/10,      # Margin as fraction of page
    orientation="portrait"  # or "landscape"
)
```

### Grid System

```python
# Create grid (AFTER creating page)
grid = Grid.from_margins(
    (-MARGIN, -MARGIN, -MARGIN, -MARGIN),
    column_subdivisions=12,
    row_subdivisions=16,
    column_gutter=10,
    row_gutter=10
)

# Get coordinates: grid[(column, row)]
x, y = grid[(0, 15)]        # Column 0, Row 15 (top-left)

# Get dimensions: grid * (cols, rows)
w, h = grid * (12, 2)       # 12 columns wide, 2 rows tall

# Unpack for drawing
header = (*grid[(0, 14)], *grid*(12, 2))  # Full width, top 2 rows
db.rect(*header)

# Debug (shows grid lines and indices)
grid.draw(show_index=True)
```

**Grid coordinates**:
- Origin: Bottom-left (DrawBot convention)
- Row 0: Bottom of page
- Row N: Top of page (where N = row_subdivisions - 1)
- Column 0: Left edge
- Column M: Right edge (where M = column_subdivisions - 1)

### Text Wrapping

```python
# Point-based text wrapping (NOT character count)
final_y = draw_wrapped_text(
    text="Your long text here...",
    x=100,              # Top-left corner
    y=500,
    width=400,          # Box width in points
    height=200,         # Box height in points
    font="Helvetica",
    size=18,
    leading_ratio=1.5,  # Line spacing (1.5x recommended)
    align="left"        # "left", "right", "center"
)
# Returns: Final y position (for stacking content)
```

### Color Palettes

```python
colors = get_color_palette("professional")
# Returns:
# {
#   'background': (0.98, 0.98, 0.97),  # 70%
#   'text': (0.1, 0.1, 0.1),           # 20%
#   'accent': (0.2, 0.45, 0.7)         # 10%
# }

# Available palettes:
# - "professional" (default)
# - "warm"
# - "cool"
# - "high_contrast"

# Use:
db.fill(*colors["background"])
db.rect(0, 0, WIDTH, HEIGHT)
```

### Portable Paths

```python
# Always use get_output_path() (works on any machine)
output = get_output_path("my_poster.pdf")
db.saveImage(str(output))

# NOT this (hardcoded path):
# db.saveImage("/Users/you/...")
```

### Text Metrics

```python
from drawbot_design_system import get_text_metrics

# Get real font metrics (not approximations)
metrics = get_text_metrics("Sample", "Helvetica", 18)
# Returns:
# {
#   'width': 62.4,
#   'height': 18.0,
#   'ascender': 14.4,
#   'descender': -3.6,
#   'line_height': 18.0,
#   'x_height': 9.0,
#   'cap_height': 13.0
# }

# Use for proper spacing:
y -= metrics['line_height']  # NOT fontSize!
```

## Core DrawBot API

### Drawing Basics

```python
# Canvas
db.newPage(width, height)
db.size(width, height)      # Alternative

# Shapes
db.rect(x, y, width, height)
db.oval(x, y, width, height)
db.line((x1, y1), (x2, y2))

# Fill and Stroke
db.fill(r, g, b)           # RGB 0-1
db.fill(r, g, b, a)        # RGBA
db.stroke(r, g, b)
db.strokeWidth(width)
db.fill(None)              # No fill
db.stroke(None)            # No stroke

# Text
db.font("Helvetica")
db.fontSize(18)
db.text("Hello", (x, y))   # y is baseline position

# Save
db.saveImage("path/to/file.pdf")  # PDF, PNG, SVG
```

### Coordinate System

**CRITICAL**: DrawBot uses **bottom-left origin**

```
(0, HEIGHT) ← Top-left      (WIDTH, HEIGHT) ← Top-right
     ↓                              ↓


     ↑                              ↑
(0, 0) ← Bottom-left        (WIDTH, 0) ← Bottom-right
```

- Y increases going UP
- Text baseline is AT y position (text extends upward)
- Use grid system to avoid confusion!

## Decision Matrix

### Choose Typography Scale

| Content       | Scale          | Reasoning                    |
|---------------|----------------|------------------------------|
| Poster        | POSTER_SCALE   | Large type (18pt base)       |
| Magazine      | MAGAZINE_SCALE | Medium type (11pt base)      |
| Book          | BOOK_SCALE     | Small type, tight spacing    |
| Report        | REPORT_SCALE   | Medium type, clear hierarchy |

### Choose Grid

| Layout Type   | Columns | Rows | Gutter | Use Case              |
|---------------|---------|------|--------|-----------------------|
| Poster        | 12      | 16   | 10pt   | Flexible, multi-area  |
| Two-column    | 12      | 8    | 20pt   | Magazine style        |
| Single-column | 6       | 8    | 10pt   | Simple, book-like     |

### Choose Line Length

| Context   | Characters/Line | Reasoning                     |
|-----------|-----------------|-------------------------------|
| Poster    | 20-30 CPL       | Large type, scannable         |
| Magazine  | 45-50 CPL       | Narrow columns                |
| Book      | 60-65 CPL       | Optimal readability           |
| Report    | 50-60 CPL       | Balance clarity & efficiency  |

## Common Patterns

### Two-Column Layout

```python
left_col = (*grid[(0, 1)], *grid*(5, 14))   # Cols 0-4, Rows 1-14
right_col = (*grid[(7, 1)], *grid*(5, 14))  # Cols 7-11, Rows 1-14
# Columns 5-6 = gutter (automatic)
```

### Stacked Sections

```python
header = (*grid[(0, 14)], *grid*(12, 2))    # Rows 14-15
content = (*grid[(0, 1)], *grid*(12, 13))   # Rows 1-13
footer = (*grid[(0, 0)], *grid*(12, 1))     # Row 0
```

### Centered Text

```python
text = "Title"
text_width, _ = db.textSize(text)
center_x = (WIDTH - text_width) / 2
db.text(text, (center_x, y))
```

## Troubleshooting

### Text Overflows Box

**Cause**: Using character-count wrapping
**Fix**: Use `draw_wrapped_text()` with point-based width

### Grid Doesn't Match Page

**Cause**: Grid created before `newPage()`
**Fix**: Always create page FIRST, then grid

### Wrong Typography Sizes

**Cause**: Using wrong scale for context
**Fix**: Use POSTER_SCALE for posters, not BOOK_SCALE

### Paths Don't Work on Other Machines

**Cause**: Hardcoded absolute paths
**Fix**: Use `get_output_path(filename)`

## Quick Checklist

Before finalizing code:

- [ ] Imports from `lib/` directory
- [ ] Used `setup_poster_page()` or `newPage()` BEFORE grid
- [ ] Grid created with `Grid.from_margins()`
- [ ] Used pre-defined scale (POSTER_SCALE, etc.)
- [ ] All layout uses grid coordinates
- [ ] All text uses `draw_wrapped_text()`
- [ ] Paths use `get_output_path()`
- [ ] No fontSize approximations

## Assets

**Textures**: `../../assets/` contains 1,807 textures:
- gradient (1,001)
- gold (202)
- bubble (201)
- cardboard (101)
- ziplock (102)
- marker (100)
- paper (57)
- rust (51)

See `../../assets/README.md` for catalog.

## Further Reading

- Complete guide: `../../docs/DESIGN_SYSTEM_USAGE.md`
- Layout theory: `../../docs/layout-design-principles.md`
- Typography: `../../docs/typography-style-guide.md`
- DrawBot API: `../../docs/drawbot-api-quick-reference.md`
