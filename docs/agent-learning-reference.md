# DrawBot Learning Reference - For Coding Agents

## Purpose
This is a **flattened reference** for AI coding agents. Human-readable learning path exists in `docs/learning/`, but this is the technical quick reference for agents generating DrawBot code.

## Critical Rules - Always Follow

### 1. Coordinate System (MOST IMPORTANT)
```python
# WRONG - CSS/screen thinking (top-left origin)
rect(0, 0, 100, 100)  # You expect top-left, but it's bottom-left!

# RIGHT - DrawBot uses bottom-left origin
# Origin (0,0) is BOTTOM-LEFT corner
# X increases rightward →
# Y increases upward ↑
rect(0, height() - 100, 100, 100)  # Now at top-left

# Moving "down" means DECREASING Y
y = 300  # Start high
y = y - 50  # Now at 250 (lower on page)
```

### 2. Always Define Canvas First
```python
# MUST do this before any drawing
newPage(width, height)  # Then draw

# NOT this
rect(100, 100, 200, 200)  # Error or unexpected default canvas
```

### 3. Set Fill/Stroke Before Drawing
```python
# RIGHT order
fill(0.5)
stroke(0)
strokeWidth(2)
rect(100, 100, 200, 200)  # Uses above settings

# NOT this
rect(100, 100, 200, 200)
fill(0.5)  # Too late, already drawn
```

### 4. Mandatory Import Pattern
```python
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "lib"))

# Now can import design system
from drawbot_grid import Grid
from drawbot_design_system import POSTER_SCALE, get_output_path
```

### 5. Use Design System Functions
```python
# DON'T manually calculate everything
# DO use system helpers:

# Setup
setup_poster_page()  # Auto-handles canvas

# Grid
grid = Grid.from_margins(
    (-MARGIN, -MARGIN, -MARGIN, -MARGIN),
    column_subdivisions=12,
    row_subdivisions=8
)

# Typography
draw_wrapped_text(text, box, POSTER_SCALE['body'])

# Output
saveImage(get_output_path('filename.pdf'))
```

## Drawing Primitives

```python
# Rectangle: x, y = bottom-left corner
rect(x, y, width, height)

# Oval: x, y = bottom-left of bounding box
oval(x, y, width, height)

# Line: two points
line((x1, y1), (x2, y2))

# Polygon: multiple points, optional close
polygon((x1, y1), (x2, y2), (x3, y3), close=True)

# Text: x, y = baseline left
text("string", (x, y))
```

## Color System

```python
# Grayscale (0=black, 1=white)
fill(0.5)

# RGB (0-1 range)
fill(1, 0, 0)  # Red

# RGBA (with alpha)
fill(1, 0, 0, 0.5)  # Semi-transparent red

# CMYK
cmykFill(0, 1, 1, 0)  # Red in CMYK

# Hex (use helper)
def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16)/255 for i in (0, 2, 4))

fill(*hex_to_rgb('#FF6633'))
```

## Grid System (Critical for Layout)

```python
from drawbot_grid import Grid

# Create grid
grid = Grid.from_margins(
    (-20, -20, -20, -20),  # margins (left, bottom, right, top)
    column_subdivisions=12,
    row_subdivisions=8,
    column_gutter=10,
    row_gutter=10
)

# Use grid coordinates (semantic, no math!)
x, y = grid[(0, 6)]  # Column 0, Row 6 (bottom-left of cell)
w, h = grid * (3, 2)  # Width of 3 cols, height of 2 rows

# Draw box in grid
rect(x, y, w, h)

# Span multiple cells
header_box = (*grid[(0, 6)], *grid * (12, 2))  # Full width, 2 rows
rect(*header_box)

# Debug: visualize grid
grid.draw(show_index=True)
```

## Typography System

```python
from drawbot_design_system import POSTER_SCALE, draw_wrapped_text

# Don't manually wrap text, use helper
box = (x, y, width, height)
draw_wrapped_text(
    text="Long text that needs wrapping",
    box=box,
    type_style=POSTER_SCALE['body']
)

# Available scales
POSTER_SCALE = {
    'display': {...},
    'title': {...},
    'heading': {...},
    'subheading': {...},
    'body': {...},
    'caption': {...}
}

# Manual text properties
font('Helvetica')
fontSize(24)
lineHeight(30)
```

## Common Patterns

### Centered Element
```python
newPage(400, 400)
radius = 50
# Center circle
oval(
    width()/2 - radius,
    height()/2 - radius,
    radius * 2,
    radius * 2
)
```

### Pattern Generation
```python
# Grid of squares
cols = rows = 10
cell_size = width() / cols

for row in range(rows):
    for col in range(cols):
        x = col * cell_size
        y = row * cell_size

        # Alternate colors
        if (row + col) % 2 == 0:
            fill(0)
        else:
            fill(1)

        rect(x, y, cell_size, cell_size)
```

### Working with Margins
```python
MARGIN = 40
content_width = width() - (MARGIN * 2)
content_height = height() - (MARGIN * 2)

# Draw in safe area
rect(MARGIN, MARGIN, content_width, content_height)
```

## File I/O

```python
from pathlib import Path

# Output directory
output_dir = Path(__file__).parent / 'output'
output_dir.mkdir(exist_ok=True)

# Save with path helper
from drawbot_design_system import get_output_path
saveImage(get_output_path('my_poster.pdf'))

# Or manual
saveImage(str(output_dir / 'output.pdf'))

# Multiple formats
saveImage('output.pdf')  # Vector
saveImage('output.png', resolution=300)  # Raster
saveImage('output.svg')  # Vector, single page
```

## Multi-Page Documents

```python
# Each newPage() creates new page in PDF
for i in range(5):
    newPage(400, 400)
    text(f"Page {i+1}", (20, 20))

saveImage('multi-page.pdf')  # All pages in one PDF
```

## Transformations

```python
# Translate (move origin)
translate(100, 100)
rect(0, 0, 50, 50)  # Actually at (100, 100)

# Rotate (degrees, around current origin)
rotate(45)

# Scale
scale(2)  # 2x larger

# Use savedState() to isolate transforms
with savedState():
    translate(200, 200)
    rotate(45)
    rect(0, 0, 100, 100)
# Transform cleared, back to original state
```

## Paths (Advanced)

```python
# Begin path
path = BezierPath()
path.moveTo((100, 100))
path.lineTo((200, 200))
path.curveTo((300, 200), (300, 300), (200, 300))
path.closePath()

# Draw path
fill(0.5)
stroke(0)
strokeWidth(2)
drawPath(path)
```

## Common Mistakes to Avoid

```python
# ❌ WRONG: Top-left thinking
rect(0, 0, 100, 100)  # Expects top-left, gets bottom-left

# ✅ RIGHT: Bottom-left origin
rect(0, height() - 100, 100, 100)

# ❌ WRONG: No canvas defined
rect(100, 100, 200, 200)  # Unpredictable default

# ✅ RIGHT: Always define canvas first
newPage(400, 400)
rect(100, 100, 200, 200)

# ❌ WRONG: Drawing before fill
rect(100, 100, 200, 200)
fill(0.5)  # Too late

# ✅ RIGHT: Fill before draw
fill(0.5)
rect(100, 100, 200, 200)

# ❌ WRONG: Not using design system
# Manual text wrapping, grid math, etc.

# ✅ RIGHT: Use system
from drawbot_design_system import draw_wrapped_text, setup_poster_page
from drawbot_grid import Grid
```

## Quick Checks

Before generating DrawBot code, verify:

1. ✅ `newPage()` called first?
2. ✅ Bottom-left origin mental model?
3. ✅ Fill/stroke set before drawing?
4. ✅ Using grid system for layout?
5. ✅ Using design system for typography?
6. ✅ Proper import path for lib/?
7. ✅ Output path uses get_output_path()?

## Decision Tree

```
Need to draw something?
├─ Basic shape? → Use rect/oval/line/polygon
├─ Text? → Use draw_wrapped_text() from design system
├─ Pattern? → Use for loops + grid system
├─ Layout? → Use Grid.from_margins()
└─ Complex? → Build with BezierPath

Need positioning?
├─ Absolute? → Use coordinates directly
├─ Centered? → Use width()/2, height()/2
├─ Grid-based? → Use grid[(col, row)]
└─ Relative? → Use margins + calculations

Need typography?
├─ Basic? → font(), fontSize(), text()
├─ Wrapped? → draw_wrapped_text()
├─ Scales? → POSTER_SCALE['body'], etc.
└─ Custom? → Define own type_style dict
```

## Performance Notes

- Multiple pages = multiple newPage() calls
- savedState() for isolated transforms
- Grid calculations are pre-computed (efficient)
- Text wrapping helper handles line breaks

## Debugging

```python
# Visual coordinate check
def debug_point(x, y, label=""):
    fill(1, 0, 0)
    oval(x-5, y-5, 10, 10)
    fill(0)
    text(label, (x+10, y+10))

# Grid visualization
grid.draw(show_index=True)  # Shows structure

# Print values
print(f"Canvas: {width()}×{height()}")
print(f"Grid cell: {grid[(0,0)]}")
```

## Example: Complete Poster Template

```python
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "lib"))

from drawbot_grid import Grid
from drawbot_design_system import (
    POSTER_SCALE,
    get_output_path,
    setup_poster_page,
    draw_wrapped_text
)

# Constants
MARGIN = 40

# Setup
setup_poster_page()  # Creates 18×24 inch canvas

# Grid
grid = Grid.from_margins(
    (-MARGIN, -MARGIN, -MARGIN, -MARGIN),
    column_subdivisions=12,
    row_subdivisions=16
)

# Header
header_box = (*grid[(0, 14)], *grid * (12, 2))
fill(0.2)
rect(*header_box)

fill(1)
draw_wrapped_text(
    "Poster Title",
    header_box,
    POSTER_SCALE['title']
)

# Body
body_box = (*grid[(1, 1)], *grid * (10, 12))
fill(0)
draw_wrapped_text(
    "Body text here...",
    body_box,
    POSTER_SCALE['body']
)

# Save
saveImage(get_output_path('poster.pdf'))
```

## Integration Points

- **Full learning path**: `docs/learning/LEARNING_PATH.md`
- **Design system usage**: `docs/DESIGN_SYSTEM_USAGE.md`
- **API reference**: `docs/drawbot-api-quick-reference.md`
- **Coordinate rules**: `docs/COORDINATE_SYSTEM_RULES.md`
- **Examples**: `examples/longitudinalbench_poster_v7.py`

## Agent Workflow

When generating DrawBot code:

1. **Check intent**: What does user want to draw?
2. **Verify knowledge**: Do I know bottom-left origin rule?
3. **Choose approach**: Basic shapes or grid system?
4. **Import correctly**: Add lib path, import system
5. **Structure**: newPage → grid → fill → draw → save
6. **Test mentally**: Walk through coordinates bottom-up
7. **Add comments**: Explain coordinate choices
8. **Output**: Generate working code

## Version
- DrawBot: drawbot (cross-platform)
- Design System: drawbot-redux (this repo)
- Grid System: lib/drawbot_grid.py
- Last Updated: 2025-10-18

---

**For human learning**: See `docs/learning/START_HERE.md`
**For agent reference**: Use this document
