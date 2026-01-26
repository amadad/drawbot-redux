# DrawBot Redux

Design system for DrawBot with CLI tooling.

## CLI

```bash
drawbot render script.py          # Render
drawbot preview script.py         # Render + open
drawbot watch script.py           # Hot reload
drawbot new poster --template grid  # Scaffold
drawbot from-spec poster.yaml     # YAML spec

# Evolutionary forms
drawbot evolve init               # Initialize
drawbot evolve gen0 -n 16         # Generate population
drawbot evolve select gen_000 -w 1,2,3  # Select winners
drawbot evolve breed gen_000      # Breed next gen
drawbot evolve status             # Show status
```

## Quick Reference

```python
import drawBot as db
from drawbot_grid import Grid
from drawbot_design_system import (
    POSTER_SCALE, setup_poster_page, draw_wrapped_text, get_output_path
)

# Setup
WIDTH, HEIGHT, MARGIN = setup_poster_page("letter")  # or a4, tabloid
grid = Grid.from_margins((-MARGIN,)*4, column_subdivisions=12, row_subdivisions=8)
scale = POSTER_SCALE  # or MAGAZINE_SCALE, BOOK_SCALE, REPORT_SCALE

# Draw with grid
x, y = grid[(0, 6)]       # Position at col 0, row 6
w, h = grid * (12, 2)     # Size: 12 cols, 2 rows
db.rect(x, y, w, h)

# Text
db.font("Helvetica Bold")
db.fontSize(scale.title)  # 91pt
draw_wrapped_text(text, x, y, w, h, "Helvetica", scale.body)

# Save
db.saveImage(str(get_output_path("poster.pdf")))
```

## Typography Scales

| Scale | Base | Ratio | Use |
|-------|------|-------|-----|
| POSTER_SCALE | 18pt | 1.5 | Posters |
| MAGAZINE_SCALE | 11pt | 1.25 | Magazines |
| BOOK_SCALE | 11pt | 1.2 | Books |
| REPORT_SCALE | 12pt | 1.25 | Reports |

## Common Mistakes

- DrawBot uses **bottom-left** origin (not top-left)
- Call `newPage()` before drawing
- Set fill/stroke **before** drawing, not after
- Use `draw_wrapped_text()` not `textwrap.wrap()`
- Use `get_output_path()` not hardcoded paths

## Structure

```
cli/
  main.py      # CLI entry point
  spec.py      # YAML spec renderer
  evolve/      # Evolutionary form generation
lib/           # Design system
examples/      # Examples
docs/          # guide.md, api.md
```
