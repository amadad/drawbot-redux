---
name: drawbot-designer
description: Create well-designed posters, layouts, and graphics using DrawBot with automatic enforcement of typography principles from Hochuli, Bringhurst, and Müller-Brockmann. Use when users request posters, layouts, graphics, editorial designs, or mention DrawBot, typography, grid systems, or programmatic design. Requires drawbot-skia package.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
---

# DrawBot Designer

Create professional posters, layouts, and graphics with automatic enforcement of design principles.

## Quick Start

1. **Read [examples.md](examples.md)** for working code you can copy
2. **Use [templates/](templates/)** to start a new project
3. **Check [reference.md](reference.md)** for API details
4. **See [filters.md](filters.md)** for image effects and textures

## When to Use This Skill

Activate when the user requests:
- Posters, layouts, graphics, or editorial designs
- Modifications to existing DrawBot code
- Typography or layout advice
- DrawBot script creation or debugging

## Core Principles

This skill automatically enforces:
- **Typography**: Hochuli's Detail in Typography (microtypography)
- **Layout**: Müller-Brockmann grid systems (macrotypography)
- **Hierarchy**: CRAP principles (Contrast, Repetition, Alignment, Proximity)

## Mandatory Workflow

**CRITICAL**: Always use the design system. Never write manual calculations.

### Step 1: Setup

```python
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "lib"))

from drawbot_skia import drawbot as db
from drawbot_grid import Grid
from drawbot_design_system import (
    POSTER_SCALE,        # or MAGAZINE_SCALE, BOOK_SCALE, REPORT_SCALE
    get_output_path,
    draw_wrapped_text,
    setup_poster_page
)
```

### Step 2: Create Page and Grid

```python
# Page setup (creates canvas automatically)
WIDTH, HEIGHT, MARGIN = setup_poster_page("letter", margin_ratio=1/10)

# Grid (automatically reads canvas size)
grid = Grid.from_margins(
    (-MARGIN, -MARGIN, -MARGIN, -MARGIN),
    column_subdivisions=12,
    row_subdivisions=16
)
```

### Step 3: Use Semantic Coordinates

```python
# ✅ CORRECT: Grid coordinates
header = (*grid[(0, 14)], *grid*(12, 2))  # Full width, top 2 rows

# ❌ WRONG: Manual calculations
header = (MARGIN, HEIGHT - 200, WIDTH - MARGIN*2, 150)
```

### Step 4: Wrap Text Properly

```python
# ✅ CORRECT: Point-based wrapping
draw_wrapped_text(text, x, y, width, height, font, size)

# ❌ WRONG: Character-count heuristics
wrapped = textwrap.wrap(text, width=70)
```

### Step 5: Save with Portable Paths

```python
# ✅ CORRECT: Works on any machine
db.saveImage(str(get_output_path("output.pdf")))

# ❌ WRONG: Hardcoded path
db.saveImage("/Users/you/...")
```

## Resources

### This Skill Directory

- **[examples.md](examples.md)** - Working code examples
- **[reference.md](reference.md)** - Complete API reference
- **[filters.md](filters.md)** - Image effects, textures, blend modes
- **[templates/](templates/)** - Starting templates:
  - `minimal_poster.py` - Simple poster
  - `two_column.py` - Magazine layout
  - `card_layout.py` - Color-coded cards

### Project Files

- **Complete examples**: `../../examples/`
  - `minimal_poster_example.py` - 80-line working poster
  - `longitudinalbench_poster_v7.py` - 352-line production poster
- **Documentation**: `../../docs/`
  - `DESIGN_SYSTEM_USAGE.md` - Complete usage guide
  - `layout-design-principles.md` - Grid theory, CRAP, decision matrices
  - `typography-style-guide.md` - Hochuli's spacing, line length, readability
- **Assets**: `../../assets/` - 1,807 textures

## Typography Scales

| Context  | Scale          | Base | Ratio | When to Use           |
|----------|----------------|------|-------|-----------------------|
| Poster   | POSTER_SCALE   | 18pt | 1.5   | Posters, displays     |
| Magazine | MAGAZINE_SCALE | 11pt | 1.25  | Magazines, newsletters|
| Book     | BOOK_SCALE     | 11pt | 1.2   | Books, long-form      |
| Report   | REPORT_SCALE   | 12pt | 1.25  | Reports, docs         |

Access sizes:
```python
scale = POSTER_SCALE
scale.caption   # 12pt
scale.body      # 18pt
scale.h3        # 27pt
scale.h2        # 40.5pt
scale.h1        # 60.75pt
scale.title     # 91.125pt
```

## Grid Patterns

### Full Width Section
```python
header = (*grid[(0, 14)], *grid*(12, 2))  # All columns, 2 rows
```

### Two Columns
```python
left = (*grid[(0, 1)], *grid*(5, 13))    # Cols 0-4
right = (*grid[(7, 1)], *grid*(5, 13))   # Cols 7-11
# Columns 5-6 = automatic gutter
```

### Stacked Sections
```python
section1 = (*grid[(0, 10)], *grid*(12, 3))  # Rows 10-12
section2 = (*grid[(0, 6)], *grid*(12, 3))   # Rows 6-8
section3 = (*grid[(0, 2)], *grid*(12, 3))   # Rows 2-4
```

## Decision Matrix

| Content | Grid    | Typography     | Line Length |
|---------|---------|----------------|-------------|
| Poster  | 12×16   | POSTER_SCALE   | 20-30 CPL   |
| Magazine| 12×8    | MAGAZINE_SCALE | 45-50 CPL   |
| Book    | 6×8     | BOOK_SCALE     | 60-65 CPL   |
| Report  | 12×8    | REPORT_SCALE   | 50-60 CPL   |

## Verification Checklist

Before finalizing code, verify:

- [ ] Imports from `lib/` directory
- [ ] Used `setup_poster_page()` BEFORE grid
- [ ] Grid created with `Grid.from_margins()`
- [ ] Used pre-defined scale (POSTER_SCALE, etc.)
- [ ] All layout uses grid coordinates (not manual math)
- [ ] All text uses `draw_wrapped_text()` (not textwrap.wrap)
- [ ] Paths use `get_output_path()` (not hardcoded)
- [ ] No fontSize approximations

## Error Prevention

### Never Do This

❌ Hardcode page size in grid
❌ Use character counts for wrapping
❌ Approximate line height with fontSize
❌ Manual calculations instead of grid
❌ Truncate text with `[:N]`
❌ Hardcode absolute paths

### Always Do This

✅ Let grid read canvas size
✅ Use point-based wrapping
✅ Use real font metrics
✅ Use semantic grid coordinates
✅ Draw all text that fits
✅ Use portable path helpers

## Common Tasks

### Create a Poster

1. Copy `templates/minimal_poster.py` to `../../examples/` or your working directory
2. If copying to `examples/`, update the import path to use `.parent.parent` instead of `.parent.parent.parent.parent.parent`
3. Update title, subtitle, body text
4. Change filename in `get_output_path()`
5. Run: `uv run python your_file.py`

### Two-Column Layout

1. Copy `templates/two_column.py` to `../../examples/`
2. Update the import path if needed (see Create a Poster above)
3. Update column content
4. Adjust grid if needed (more/fewer rows)

### Color-Coded Cards

1. Copy `templates/card_layout.py` to `../../examples/`
2. Update the import path if needed (see Create a Poster above)
3. Modify card titles and descriptions
4. Change colors if desired

### Debug Layout Issues

1. Add `grid.draw(show_index=True)` before `saveImage()`
2. View PDF to see grid structure
3. Verify grid coordinates
4. Remove `grid.draw()` for final output

## Troubleshooting

| Problem | Cause | Fix |
|---------|-------|-----|
| Text overflows | Character-count wrapping | Use `draw_wrapped_text()` |
| Grid doesn't match | Created before `newPage()` | Create page FIRST |
| Wrong sizes | Wrong scale for context | Use POSTER_SCALE for posters |
| Paths don't work | Hardcoded paths | Use `get_output_path()` |

See [reference.md](reference.md) for detailed troubleshooting.

## Example Session

**User**: "Create a poster for an AI conference"

**Response**:
1. Copy `templates/minimal_poster.py`
2. Modify content:
   - Title: "AI Conference 2025"
   - Subtitle: "Advancing Machine Learning"
   - Body: Conference details
3. Save as `ai_conference.py`
4. Run: `uv run python examples/ai_conference.py`

Result: Professional poster following all design principles automatically.

## Progressive Disclosure

Start with templates, refer to examples and reference as needed:

1. **Start**: `templates/minimal_poster.py`
2. **Learn**: `examples.md` for patterns
3. **Reference**: `reference.md` for API details
4. **Effects**: `filters.md` for images/textures (when needed)
5. **Deep dive**: `../../docs/` for theory

Claude loads resources progressively as needed (saves context).

## Remember

The design system makes it **impossible to violate design principles**. Trust the system, use the helpers, and your designs will automatically follow Hochuli, Bringhurst, and Müller-Brockmann.

## Version History

- v1.0.0 (2025-10-18): Initial Agent Skill with curated content
