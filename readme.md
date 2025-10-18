# DrawBot Redux

Compositional design system combining DrawBot's programmatic graphics with automatic enforcement of typography principles from Hochuli, Bringhurst, and Müller-Brockmann.

**Features:**
- 🎨 Grid-based layouts with semantic coordinates
- 📐 Pre-defined typography scales (poster, magazine, book, report)
- 📝 Point-based text wrapping (no overflow)
- 🔧 Real font metrics (no approximations)
- 🤖 Agent skills for Claude Code
- 1,807 texture assets in 8 categories

## Quick Start

### Installation

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

### Create Your First Poster

```bash
# Run the minimal example
uv run python examples/minimal_poster_example.py

# View output
open output/minimal_poster.pdf
```

**That's it!** You have a professionally-designed poster following all principles.

## Project Structure

```
drawbot-redux/
├── lib/                  # Core design system
│   ├── drawbot_grid.py   # Grid system (auto-reads canvas)
│   └── drawbot_design_system.py  # Typography, wrapping, validation
│
├── examples/             # Working examples
│   ├── minimal_poster_example.py       # Quick start
│   └── longitudinalbench_poster_v7.py  # Complete example
│
├── docs/                 # Documentation
│   ├── quickstart.md     # Fast start guide
│   ├── agent-learning-reference.md     # For AI coding agents
│   ├── learning-structure.md           # Pedagogical framework
│   ├── design-system-usage.md          # Design system guide
│   ├── drawbot-api-quick-reference.md  # Core API
│   └── layout-design-principles.md     # Composition theory
│
├── assets/               # 1,807 textures (gitignored)
├── library/              # Tutorials, cookbook, foundations
├── scripts/              # Utility scripts
├── mcp/                  # MCP server
├── archive/              # Historical work
│   ├── summaries/        # Project evolution docs
│   ├── experiments/      # Old experimental code
│   └── old/              # Legacy archive
│
├── CLAUDE.md             # Agent instructions
└── pyproject.toml        # Python project config
```

## What You Get

✅ **Automatic enforcement** of design principles
✅ **Grid-based layouts** with semantic coordinates
✅ **Proper typography scales** for different contexts
✅ **Point-based text wrapping** (no overflow)
✅ **Real font metrics** (no approximations)
✅ **Portable paths** (works on any machine)
✅ **Layout validation** (prevents overlaps)

## Using with Claude Code

The project includes an agent skill that automatically helps Claude Code:
1. Use the design system correctly
2. Follow typography principles
3. Apply grid-based layouts
4. Create professional designs

Just ask Claude: **"Create a poster"** and it uses the system automatically.

## Documentation

- **[Quick Start](docs/quickstart.md)** - Get drawing in 5 minutes
- **[Design System Guide](docs/design-system-usage.md)** - Complete usage
- **[Learning Structure](docs/learning-structure.md)** - Pedagogical framework
- **[API Reference](docs/drawbot-api-quick-reference.md)** - Core API
- **[Agent Reference](docs/agent-learning-reference.md)** - For AI coding

## Examples

### Minimal Poster (80 lines)
```bash
uv run python examples/minimal_poster_example.py
```

### Complete Poster (352 lines)
```bash
uv run python examples/longitudinalbench_poster_v7.py
```

## What Makes This Different

**Before**: Manual calculations, text overflow, wrong typography scales
**After**: Automatic enforcement of professional design principles

The gap between documentation and code is closed. 🎉

## Assets

1,807 textures in 8 categories (stored separately, not in repo):
- gradient (1,001) - Color gradients, transitions
- gold (202) - Metallic gold, foils
- bubble (201) - Bubble wrap, spheres
- cardboard (101) - Cardboard, corrugated
- ziplock (102) - Plastic bags, transparency
- marker (100) - Hand-drawn textures
- paper (57) - Paper grain, subtle backgrounds
- rust (51) - Weathered metal

See `assets/README.md` for complete catalog.

## Credits

Built on:
- **[DrawBot](https://github.com/typemytype/drawbot)** by Just van Rossum, Erik van Blokland, Frederik Berlaen
- **Typography principles** from Jost Hochuli, Robert Bringhurst, Josef Müller-Brockmann
- **Python for Designers** pedagogical approach

## License

See [license.txt](license.txt)

---

**DrawBot Redux: Professional design automation with enforced principles** 🎨🤖
