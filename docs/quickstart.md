# DrawBot Redux - Quick Start

## What This Is

A design system that **automatically enforces** typography principles from Hochuli, Bringhurst, and Müller-Brockmann. No more broken layouts, text overflow, or wrong typography scales.

## Installation

```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone and setup
git clone https://github.com/amadad/drawbot-redux.git
cd drawbot-redux
uv sync

# For GIF support
brew install gifsicle
```

## 30-Second Example

```bash
# Run the minimal example
uv run python examples/minimal_poster_example.py

# View output
open output/minimal_poster.pdf
```

**That's it!** You have a professionally-designed poster following all the principles from the documentation.

## Project Structure

```
drawbot-redux/
├── lib/                         # Core design system
│   ├── drawbot_grid.py          # Grid system (auto-reads canvas)
│   └── drawbot_design_system.py # Typography, wrapping, validation
├── examples/                    # Example scripts
│   ├── minimal_poster_example.py       # Quick start (80 lines)
│   ├── longitudinalbench_poster_v7.py  # Complete example (352 lines)
│   └── [40+ official DrawBot examples]
├── docs/                        # Documentation
│   ├── design-system-usage.md   # Complete usage guide
│   ├── layout-design-principles.md  # Müller-Brockmann grid theory
│   └── typography-style-guide.md    # Hochuli microtypography
├── assets/                      # 1,807 textures in 8 categories
├── output/                      # Generated files (gitignored)
└── mcp/                         # MCP server for Claude Desktop
```

## Writing Your First Poster

Create `my_poster.py` in `examples/`:

```python
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "lib"))

import drawBot as db
from drawbot_grid import Grid
from drawbot_design_system import (
    POSTER_SCALE,
    get_output_path,
    get_color_palette,
    setup_poster_page
)

# Setup (one line creates canvas)
WIDTH, HEIGHT, MARGIN = setup_poster_page("letter")

# Grid (automatically reads canvas size)
grid = Grid.from_margins(
    (-MARGIN, -MARGIN, -MARGIN, -MARGIN),
    column_subdivisions=12,
    row_subdivisions=8
)

# Typography (pre-defined scale from docs)
scale = POSTER_SCALE

# Colors (70-20-10 rule)
colors = get_color_palette("professional")

# Background
db.fill(*colors["background"])
db.rect(0, 0, WIDTH, HEIGHT)

# Title
db.font("Helvetica-Bold")
db.fontSize(scale.title)
db.fill(*colors["text"])
db.text("My Poster", (MARGIN, grid[(0, 7)][1]))

# Save (portable path)
db.saveImage(str(get_output_path("my_poster.pdf")))
print("✓ Saved to output/my_poster.pdf")
```

Run it:
```bash
uv run python examples/my_poster.py
open output/my_poster.pdf
```

## What You Get Automatically

✅ **Grid System** - Semantic coordinates, no manual math
✅ **Typography Scales** - Poster: 18pt base, Magazine: 11pt, Book: 11pt
✅ **Text Wrapping** - Point-based (not character count)
✅ **Real Metrics** - Actual ascender/descender (not fontSize approximations)
✅ **Portable Paths** - Works on any machine
✅ **Layout Validation** - Checks fit before drawing
✅ **Color Palettes** - 70-20-10 rule enforced

## Examples

### Minimal (80 lines)
```bash
uv run python examples/minimal_poster_example.py
```

Basic poster showing the essentials.

### Complete (352 lines)
```bash
uv run python examples/longitudinalbench_poster_v7.py
```

Full-featured poster with:
- Grid-based layout (12×16)
- Three-tier architecture visualization
- Color-coded cards
- Two-column content
- Proper text wrapping
- Layout validation

## Documentation

- **`docs/design-system-usage.md`** - Complete usage guide
- **`docs/layout-design-principles.md`** - Grid systems, CRAP, hierarchy
- **`docs/typography-style-guide.md`** - Hochuli's Detail in Typography
- **`docs/drawbot-api-quick-reference.md`** - Core API (95% of needs)
- **`docs/agent-learning-reference.md`** - For AI code generation
- **`docs/learning-structure.md`** - For AI learning/teaching

## For AI Coding Agents

**Code Generation**: `docs/agent-learning-reference.md`
**Learning Framework**: `docs/learning-structure.md`

## Next Steps

1. **Read**: `docs/design-system-usage.md`
2. **Study**: `examples/minimal_poster_example.py`
3. **Create**: Your own poster
4. **Learn**: `docs/layout-design-principles.md`

## Support

- Documentation: `docs/`
- Examples: `examples/`
- Issues: https://github.com/amadad/drawbot-redux/issues
- Original DrawBot: http://www.drawbot.com

---

**The gap between documentation and code is closed. Your designs will automatically follow Hochuli, Bringhurst, and Müller-Brockmann. 🎉**
