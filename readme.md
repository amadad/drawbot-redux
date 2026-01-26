# DrawBot Redux

Design system for DrawBot with typography enforcement and CLI tooling.

## Install

```bash
uv pip install -e ".[cli,drawbot]"
```

## CLI

```bash
drawbot render script.py          # Render script
drawbot render script.py --open   # Render and open
drawbot preview script.py         # Quick render + open
drawbot watch script.py           # Hot reload
drawbot new poster --template grid  # Scaffold from template
drawbot from-spec poster.yaml     # Render from YAML
drawbot templates list            # List templates
```

## Usage

```python
import drawBot as db
from drawbot_grid import Grid
from drawbot_design_system import (
    POSTER_SCALE, setup_poster_page, draw_wrapped_text, get_output_path
)

WIDTH, HEIGHT, MARGIN = setup_poster_page("letter")
grid = Grid.from_margins((-MARGIN,)*4, column_subdivisions=12, row_subdivisions=8)

db.fill(0.1)
db.rect(*grid[(0, 6)], *grid*(12, 2))  # Header bar

db.saveImage(str(get_output_path("poster.pdf")))
```

## Structure

```
├── cli/           # CLI tool
├── lib/           # Design system
├── examples/      # Example scripts
├── docs/          # guide.md, api.md
└── tests/
```

## Docs

- [docs/guide.md](docs/guide.md) - Design system usage
- [docs/api.md](docs/api.md) - DrawBot API reference
