# Examples

Production-ready examples using the DrawBot design system.

## Quick Start

```bash
uv run python examples/minimal_poster_example.py
```

## Production Examples

| File | Description | Complexity |
|------|-------------|------------|
| `minimal_poster_example.py` | **Start here** - Basic poster with grid & typography | Simple |
| `longitudinalbench_poster_v7.py` | Professional research poster with full design system | Advanced |
| `FIXED_tier_card_example.py` | Color-coded card layout | Medium |
| `scty_poster.py` | Tech studio poster design | Medium |

## API Demos

The `api-demos/` directory contains basic DrawBot API demonstrations:
- Shapes: rect, oval, line, polygon, star
- Colors: fill, gradients (linear, radial, CMYK)
- Text: basic text, textBox, font attributes
- Paths: bezier paths, boolean operations
- State: savedState, transforms

These demonstrate raw DrawBot - **not** the design system.

## Running Examples

All examples output to the `output/` directory:

```bash
# Run any example
uv run python examples/minimal_poster_example.py

# Output appears at:
# output/minimal_poster.pdf
```

## Template Structure

Every design system example follows this pattern:

```python
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "lib"))

import drawBot as db
from drawbot_grid import Grid
from drawbot_design_system import (
    POSTER_SCALE, setup_poster_page, draw_wrapped_text, get_output_path
)

# 1. Setup page
WIDTH, HEIGHT, MARGIN = setup_poster_page("letter")

# 2. Create grid
grid = Grid.from_margins(
    (-MARGIN, -MARGIN, -MARGIN, -MARGIN),
    column_subdivisions=12,
    row_subdivisions=8
)

# 3. Draw with grid coordinates
header_box = (*grid[(0, 6)], *grid*(12, 2))
db.rect(*header_box)

# 4. Save
db.saveImage(str(get_output_path("output.pdf")))
```
