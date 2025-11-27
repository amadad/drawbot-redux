# DrawBot Redux

Compositional design system for DrawBot with automatic enforcement of typography principles.

## Quick Reference

```python
# ✅ CORRECT import
import drawBot as db

# ✅ Design system import
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "lib"))

from drawbot_grid import Grid
from drawbot_design_system import (
    POSTER_SCALE, setup_poster_page, draw_wrapped_text, get_output_path
)
```

## Mandatory Workflow

### 1. Setup Page and Grid

```python
WIDTH, HEIGHT, MARGIN = setup_poster_page("letter")  # or "a4", "tabloid"

grid = Grid.from_margins(
    (-MARGIN, -MARGIN, -MARGIN, -MARGIN),
    column_subdivisions=12,
    row_subdivisions=8
)
```

### 2. Use Typography Scales

```python
scale = POSTER_SCALE  # or MAGAZINE_SCALE, BOOK_SCALE, REPORT_SCALE

db.font("Helvetica")
db.fontSize(scale.title)   # 91pt
db.fontSize(scale.body)    # 18pt
db.fontSize(scale.caption) # 12pt
```

### 3. Draw with Grid Coordinates

```python
# ✅ RIGHT - Semantic coordinates
header_box = (*grid[(0, 6)], *grid*(12, 2))
db.rect(*header_box)

# ❌ WRONG - Manual calculations
db.rect(MARGIN, HEIGHT - 200, WIDTH - 2*MARGIN, 100)
```

### 4. Use Proper Text Wrapping

```python
# ✅ RIGHT - Point-based wrapping (measures actual words)
draw_wrapped_text(text, x, y, width, height, font, size)

# ❌ WRONG - Character-count heuristics
import textwrap
textwrap.wrap(text, width=70)
```

### 5. Save with Portable Paths

```python
# ✅ RIGHT
db.saveImage(str(get_output_path("my_poster.pdf")))

# ❌ WRONG
db.saveImage("/Users/you/Projects/drawbot-redux/output/my_poster.pdf")
```

## Project Structure

```
drawbot-redux/
├── lib/                      # CORE: Design system (use this)
│   ├── drawbot_design_system.py
│   └── drawbot_grid.py
│
├── examples/                 # Production examples
│   ├── minimal_poster_example.py    # Start here
│   ├── longitudinalbench_poster_v7.py
│   ├── FIXED_tier_card_example.py
│   └── scty_poster.py
│
├── docs/                     # Documentation
│   ├── agent-learning-reference.md
│   ├── design-system-usage.md
│   ├── drawbot-api-quick-reference.md
│   └── typography-style-guide.md
│
└── output/                   # Generated files (gitignored)
```

## Typography Scales

| Context  | Scale          | Base | Ratio | Use For |
|----------|----------------|------|-------|---------|
| Poster   | POSTER_SCALE   | 18pt | 1.5   | Posters, displays |
| Magazine | MAGAZINE_SCALE | 11pt | 1.25  | Magazines |
| Book     | BOOK_SCALE     | 11pt | 1.2   | Books, long-form |
| Report   | REPORT_SCALE   | 12pt | 1.25  | Reports, docs |

## Common Mistakes

❌ **Top-left origin thinking** - DrawBot uses bottom-left
❌ **Drawing before newPage()** - Always call newPage first
❌ **Fill/stroke after drawing** - Set before, not after
❌ **Manual text wrapping** - Use draw_wrapped_text()
❌ **Hardcoded paths** - Use get_output_path()
❌ **Manual calculations** - Use grid coordinates

## Running Scripts

```bash
uv run python examples/minimal_poster_example.py
```

## Key Documentation

- `docs/agent-learning-reference.md` - Technical reference for code generation
- `docs/design-system-usage.md` - Complete usage guide
- `docs/drawbot-api-quick-reference.md` - API lookup
