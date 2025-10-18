# DrawBot Redux

Compositional design system combining DrawBot's programmatic graphics with automatic enforcement of typography principles from Hochuli, Bringhurst, and Müller-Brockmann.

**IMPORTANT:** This project uses official DrawBot (macOS, full API) with a complete design system that automatically enforces professional design principles.

---

## Quick Reference

**Start Here**: [`docs/README.md`](docs/README.md)
**AI Agents**: [`docs/agent-learning-reference.md`](docs/agent-learning-reference.md)
**Quick Start**: [`docs/quickstart.md`](docs/quickstart.md)
**Examples**: [`examples/minimal_poster_example.py`](examples/minimal_poster_example.py)

---

## CRITICAL - DrawBot Import

```python
# ✅ CORRECT import for this project
import drawBot as db

# ✅ Full API available:
# - db.FormattedString()  # Rich text formatting
# - db.textBox()          # Automatic text wrapping
# - db.installedFonts()   # List system fonts
# - db.ImageObject()      # 200+ image filters
```

**This project uses official DrawBot 3.132** (NOT drawbot-skia)
- macOS only
- Complete API
- Superior typography

---

## MANDATORY Workflow

### 1. Import Design System

```python
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "lib"))

import drawBot as db
from drawbot_grid import Grid
from drawbot_design_system import (
    POSTER_SCALE,
    get_output_path,
    setup_poster_page,
    draw_wrapped_text
)
```

### 2. Setup Canvas with Grid

```python
# Auto-creates proper canvas
WIDTH, HEIGHT, MARGIN = setup_poster_page("letter")  # or "a4", "tabloid"

# Grid with semantic coordinates
grid = Grid.from_margins(
    (-MARGIN, -MARGIN, -MARGIN, -MARGIN),
    column_subdivisions=12,
    row_subdivisions=8
)
```

### 3. Use Typography Scales

```python
# Pre-defined scales (DON'T manually set sizes)
scale = POSTER_SCALE  # or MAGAZINE_SCALE, BOOK_SCALE, REPORT_SCALE

db.font("Helvetica")
db.fontSize(scale.title)   # 91pt (golden ratio from 18pt base)
db.fontSize(scale.body)    # 18pt (base)
db.fontSize(scale.caption) # 8pt
```

### 4. Draw with Grid Coordinates

```python
# ✅ RIGHT - Semantic coordinates
header_box = (*grid[(0, 14)], *grid * (12, 2))  # Cols 0-11, Rows 14-15
db.rect(*header_box)

# ❌ WRONG - Manual calculations
db.rect(MARGIN, HEIGHT - 200, WIDTH - 2*MARGIN, 100)
```

### 5. Use Proper Text Wrapping

```python
# ✅ RIGHT - Point-based wrapping
body_box = (*grid[(1, 1)], *grid * (10, 12))
draw_wrapped_text(
    "Your text here...",
    body_box,
    POSTER_SCALE['body']
)

# ❌ WRONG - Manual textwrap by characters
import textwrap
wrapped = textwrap.wrap(text, width=70)  # Characters, not points!
```

### 6. Save with Portable Paths

```python
# ✅ RIGHT - Portable
db.saveImage(str(get_output_path("my_poster.pdf")))

# ❌ WRONG - Hardcoded path
db.saveImage("/Users/you/Projects/drawbot-redux/output/my_poster.pdf")
```

---

## Project Structure

```
drawbot-redux/
├── lib/                  # Core design system ⭐
│   ├── drawbot_grid.py
│   └── drawbot_design_system.py
│
├── examples/             # Working examples ⭐
│   ├── minimal_poster_example.py       # Quick start (80 lines)
│   └── longitudinalbench_poster_v7.py  # Complete (352 lines)
│
├── docs/                 # Documentation ⭐
│   ├── README.md                       # Start here
│   ├── quickstart.md                   # 5-minute start
│   ├── agent-learning-reference.md     # AI agents (technical)
│   ├── learning-structure.md           # Pedagogical framework
│   ├── design-system-usage.md          # Complete guide
│   ├── drawbot-api-quick-reference.md  # API (95% of needs)
│   ├── layout-design-principles.md     # Composition theory
│   ├── typography-style-guide.md       # Typography details
│   └── archive/                        # Deep theory
│
├── assets/               # 1,807 textures (gitignored)
├── library/              # Tutorials, cookbook, foundations
├── scripts/              # Utilities
├── mcp/                  # MCP server
├── archive/              # Historical work
└── output/               # Generated files (gitignored)
```

---

## Running Scripts

```bash
# ✅ CORRECT
uv run python script.py

# ❌ WRONG
python script.py                  # Missing venv
python -m drawBot script.py       # Different tool
```

---

## Grid System (Critical for Layout)

**USE GRIDS** - Prevents overlaps and ensures proper fit:

```python
from drawbot_grid import Grid

# Define grid FIRST
grid = Grid.from_margins(
    (-MARGIN, -MARGIN, -MARGIN, -MARGIN),
    column_subdivisions=12,
    row_subdivisions=8,
    column_gutter=10,
    row_gutter=10
)

# Use semantic coordinates
header_box = (*grid[(0, 6)], *grid*(12, 2))   # Cols 0-11, Rows 6-7

# Debug: visualize grid
grid.draw(show_index=True)
```

**Benefits:**
- ✅ No manual math
- ✅ No overlaps (gutters enforced)
- ✅ Guaranteed fit
- ✅ Visual debugging

---

## Typography Scales

**DON'T manually set font sizes - Use scales:**

```python
from drawbot_design_system import POSTER_SCALE, MAGAZINE_SCALE, BOOK_SCALE

# Poster (18pt base, 1.5 ratio)
POSTER_SCALE = {
    'display': 205.4pt,
    'title': 91.125pt,
    'heading': 40.5pt,
    'subheading': 27pt,
    'body': 18pt,
    'caption': 8pt
}

# Magazine (11pt base, 1.25 ratio)
MAGAZINE_SCALE = {...}

# Book (11pt base, 1.2 ratio)
BOOK_SCALE = {...}
```

---

## Common Mistakes to Avoid

❌ **Top-left origin thinking** (DrawBot uses bottom-left)
❌ **Drawing before newPage()**
❌ **Fill/stroke after drawing** (set before)
❌ **Manual text wrapping with character counts**
❌ **fontSize approximations** (use real metrics)
❌ **Hardcoded paths** (use get_output_path())
❌ **Manual calculations** (use grid coordinates)
❌ **Wrong typography scales** (use pre-defined scales)

✅ **See `docs/agent-learning-reference.md` for complete rules**

---

## Documentation Hierarchy

### For AI Agents
1. **`docs/agent-learning-reference.md`** - Technical reference (code generation)
2. **`docs/learning-structure.md`** - Pedagogical framework (teaching)

### For Humans
1. **`docs/quickstart.md`** - Get started (5 min)
2. **`docs/design-system-usage.md`** - Complete guide
3. **`docs/README.md`** - Navigation hub

### For Reference
- **`docs/drawbot-api-quick-reference.md`** - API lookup
- **`docs/layout-design-principles.md`** - Composition theory
- **`docs/typography-style-guide.md`** - Typography details
- **`docs/drawbot-image-filters-reference.md`** - Image filters

---

## Code Style

**DrawBot Functions:**
- ALWAYS prefix with `db.` (e.g., `db.newPage()`, `db.rect()`, `db.fill()`)

**Design Approach:**
- Layer-based: background → content → foreground
- Define variables at top: margins, gutters, colors, sizes
- Comment design rationale, not obvious code

**Python:**
- Python 3.14+
- Use `uv` for dependencies (not pip)
- Output to `output/` directory

---

## Asset Library

**1,807 textures** in 8 categories (gitignored, stored separately):
- gradient (1,001) - Color gradients, transitions
- gold (202) - Metallic foils
- bubble (201) - Bubble wrap, spheres
- cardboard (101) - Corrugated, rustic
- ziplock (102) - Plastic, transparency
- marker (100) - Hand-drawn
- paper (57) - Subtle backgrounds
- rust (51) - Weathered metal

**See `assets/README.md` for complete catalog**

---

## Quick Decision Trees

**Need to draw?**
- Basic shape → Use rect/oval/line/polygon
- Text → Use draw_wrapped_text() from design system
- Pattern → Use loops + grid system
- Layout → Use Grid.from_margins()
- Complex → Build with BezierPath

**Need positioning?**
- Grid-based → Use grid[(col, row)]
- Centered → Use width()/2, height()/2
- Absolute → Use coordinates directly
- Relative → Use margins + calculations

**Need typography?**
- Scale → POSTER_SCALE, MAGAZINE_SCALE, BOOK_SCALE
- Wrapped text → draw_wrapped_text()
- Basic → font(), fontSize(), text()
- Rich text → FormattedString()

---

## External Resources

- **Official DrawBot**: http://www.drawbot.com
- **Repository**: https://github.com/typemytype/drawbot
- **Forum**: http://forum.drawbot.com
- **Python for Designers**: https://pythonfordesigners.com

---

## Environment & Security

- All code runs locally (no external servers)
- MCP server available for Claude Desktop integration
- Sandboxed execution via Dagger containers
- File system restricted to `output/` directory

---

**TL;DR:**
1. Use official DrawBot (import drawBot as db)
2. Use design system (lib/drawbot_design_system.py)
3. Use grid coordinates (not manual math)
4. Use pre-defined scales (not random sizes)
5. See docs/agent-learning-reference.md for details

**Clean, focused, professional.** 🎨
