# DrawBot Redux

Compositional design system for DrawBot with automatic enforcement of typography principles.

## Quick Start

```bash
# Install
uv sync --extra drawbot

# Run example
uv run python examples/minimal_poster_example.py

# View output
open output/minimal_poster.pdf
```

## What This Does

Enforces professional design principles automatically:

- **Grid-based layouts** - Semantic coordinates, no pixel math
- **Typography scales** - Poster, magazine, book, report contexts
- **Point-based text wrapping** - Measures words, no overflow
- **Layout validation** - Catches overlaps before rendering

Based on Hochuli, Bringhurst, and Müller-Brockmann.

## Project Structure

```
drawbot-redux/
├── lib/                      # CORE: Design system
│   ├── drawbot_design_system.py   # Typography, wrapping, validation
│   └── drawbot_grid.py            # Grid system
│
├── examples/                 # Production examples
│   ├── minimal_poster_example.py  # Start here
│   ├── longitudinalbench_poster_v7.py
│   ├── FIXED_tier_card_example.py
│   └── scty_poster.py
│
├── docs/                     # Documentation
│   ├── quickstart.md
│   ├── design-system-usage.md
│   ├── agent-learning-reference.md
│   ├── drawbot-api-quick-reference.md
│   ├── drawbot-image-filters-reference.md
│   ├── typography-style-guide.md
│   └── layout-design-principles.md
│
├── evolutionary_drawbot/     # Parametric form evolution system
└── output/                   # Generated files (gitignored)
```

## Usage

### Basic Pattern

```python
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "lib"))

import drawBot as db
from drawbot_grid import Grid
from drawbot_design_system import (
    POSTER_SCALE, setup_poster_page, draw_wrapped_text, get_output_path
)

# Setup
WIDTH, HEIGHT, MARGIN = setup_poster_page("letter")
grid = Grid.from_margins((-MARGIN, -MARGIN, -MARGIN, -MARGIN),
                         column_subdivisions=12, row_subdivisions=8)

# Draw with grid
header = (*grid[(0, 6)], *grid*(12, 2))  # Full width, top 2 rows
db.rect(*header)

# Save
db.saveImage(str(get_output_path("poster.pdf")))
```

### Typography Scales

```python
from drawbot_design_system import POSTER_SCALE, MAGAZINE_SCALE, BOOK_SCALE

scale = POSTER_SCALE  # 18pt base, 1.5 ratio
db.fontSize(scale.title)    # 91pt
db.fontSize(scale.body)     # 18pt
db.fontSize(scale.caption)  # 12pt
```

### Text Wrapping

```python
from drawbot_design_system import draw_wrapped_text

# Point-based wrapping (measures actual words)
draw_wrapped_text(
    text="Your text here...",
    x=100, y=500,
    width=400, height=300,
    font="Helvetica", size=18
)
```

## Installation Options

```bash
# Core only
uv sync

# With DrawBot (macOS)
uv sync --extra drawbot

# With MCP server
uv sync --extra mcp

# With font editing tools
uv sync --extra fonts

# Development
uv sync --extra dev
```

## Documentation

| Doc | Purpose |
|-----|---------|
| [quickstart.md](docs/quickstart.md) | 5-minute start |
| [design-system-usage.md](docs/design-system-usage.md) | Complete guide |
| [drawbot-api-quick-reference.md](docs/drawbot-api-quick-reference.md) | DrawBot API reference |
| [drawbot-image-filters-reference.md](docs/drawbot-image-filters-reference.md) | Image filters reference |
| [typography-style-guide.md](docs/typography-style-guide.md) | Typography principles |
| [agent-learning-reference.md](docs/agent-learning-reference.md) | For AI agents |

## Credits

- [DrawBot](https://github.com/typemytype/drawbot) - Just van Rossum, Erik van Blokland, Frederik Berlaen
- Typography: Hochuli, Bringhurst, Müller-Brockmann
