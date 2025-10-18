# DrawBot Redux - Claude Code Integration

## Overview

DrawBot Redux is now fully integrated with Claude Code, providing an **agentic design system** that automatically enforces typography and layout principles from Hochuli, Bringhurst, and Müller-Brockmann.

## What We Built

### 1. **Anthropic Skill** (`.claude-plugin/`)

A complete skill that teaches Claude Code how to:
- Create well-designed posters, layouts, and graphics
- Use the DrawBot design system correctly
- Follow established design principles automatically
- Never violate typography or layout rules

### 2. **Design System** (`lib/`)

**Enforces principles automatically:**
- ✅ Grid-based layouts (semantic coordinates)
- ✅ Proper typography scales (context-aware)
- ✅ Point-based text wrapping (no overflow)
- ✅ Real font metrics (no approximations)
- ✅ Portable paths (works anywhere)
- ✅ Layout validation (prevents overlaps)

### 3. **Working Examples** (`examples/`)

Two production-ready templates:
- `minimal_poster_example.py` - Quick start (80 lines)
- `longitudinalbench_poster_v7.py` - Complete example (352 lines)

## Using with Claude Code

### Quick Start

```bash
# In your project directory
cd /path/to/drawbot-redux

# Start Claude Code
claude

# Ask Claude to create a poster
"Create a poster for a machine learning conference"
```

Claude Code will automatically:
1. Use the design system (`lib/drawbot_design_system.py`)
2. Apply grid-based layout
3. Use proper typography scales
4. Wrap text correctly
5. Save with portable paths

### Install the Skill

#### Option 1: As a Plugin Marketplace (Recommended)

If this repo is public on GitHub:

```bash
claude
> /plugin marketplace add <your-github-username>/drawbot-redux
```

Then just mention the skill:
```
"Use the drawbot-designer skill to create a poster"
```

#### Option 2: Manual Installation

```bash
# Copy skill to Claude Code plugins directory
mkdir -p ~/.config/claude-code/plugins/drawbot-redux
cp -r .claude-plugin/* ~/.config/claude-code/plugins/drawbot-redux/
```

Restart Claude Code and the skill will be available.

## Workflows

### 1. Create a New Poster

```bash
claude
> Create a poster for an AI safety benchmark with a three-tier architecture
```

Claude Code will:
- ✅ Use the design system automatically
- ✅ Create grid-based layout
- ✅ Apply proper typography
- ✅ Save to `output/`

### 2. Fix a Broken Layout

```bash
claude
> This poster has text overflow. Fix it using the design system.
```

Claude Code will:
- ✅ Replace manual calculations with grid coordinates
- ✅ Use `draw_wrapped_text()` for proper wrapping
- ✅ Apply real font metrics

### 3. Migrate Old Scripts

```bash
claude
> Migrate examples/longitudinalbench_poster_v2.py to use the design system
```

Claude Code will:
- ✅ Add proper imports from `lib/`
- ✅ Replace hardcoded values with system helpers
- ✅ Use grid coordinates instead of manual math

### 4. Debug Typography Issues

```bash
claude
> The line spacing looks wrong. Use real font metrics.
```

Claude Code will:
- ✅ Replace fontSize approximations with `get_text_metrics()`
- ✅ Use actual ascender/descender values
- ✅ Apply proper leading ratios

## Claude Code Features Used

### 1. **File Editing** ✓
Claude Code directly edits files using the design system:
```python
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "lib"))

from drawbot_design_system import POSTER_SCALE, get_output_path
```

### 2. **Command Execution** ✓
Claude Code runs and tests the code:
```bash
uv run python examples/my_poster.py
```

### 3. **MCP Integration** ✓
The design system is available via MCP:
- Read documentation from `docs/`
- Access examples from `examples/`
- Use assets from `assets/`

### 4. **Codebase Awareness** ✓
Claude Code understands:
- Project structure (`lib/`, `examples/`, `docs/`)
- Design principles (from documentation)
- Working patterns (from examples)

## What Makes This Special

### Traditional Approach (Before)
```
User: "Create a poster"
Claude: [writes manual calculations, hardcoded values, breaks design rules]
Result: ❌ Text overflow, wrong typography, broken layout
```

### With DrawBot Redux Design System (Now)
```
User: "Create a poster"
Claude Code: [uses skill, applies design system automatically]
Result: ✅ Professional layout, correct typography, follows principles
```

**The design system makes it impossible to violate principles.**

## Example Session

```bash
$ claude

You: Create a poster for LongitudinalBench, an AI safety benchmark

Claude Code: I'll create a professional poster using the DrawBot design system.

[Uses drawbot-designer skill]
[Consults docs/DESIGN_SYSTEM_USAGE.md]
[References examples/minimal_poster_example.py]
[Creates poster with proper grid, typography, and layout]

✓ Created examples/longitudinalbench_poster.py
✓ Saved to output/longitudinalbench_poster.pdf

The poster uses:
- Grid-based layout (12×16)
- POSTER_SCALE typography (18pt base, 1.5 ratio)
- Point-based text wrapping
- Real font metrics
- Portable paths

You: The title should be larger

Claude Code: I'll increase the title size using the typography scale.

[Edits file to use scale.title instead of scale.h1]
[Re-runs script]

✓ Updated examples/longitudinalbench_poster.py
✓ Title now uses scale.title (91.125pt)

You: Perfect! Now create a minimal version

Claude Code: I'll create a simplified poster following the same patterns.

[Creates new file based on minimal_poster_example.py template]
[Uses same design system]

✓ Created examples/longitudinalbench_minimal.py
✓ Saved to output/longitudinalbench_minimal.pdf
```

## Advanced Usage

### With MCP Servers

The design system works with MCP servers for enhanced capabilities:

```bash
# Connect to Figma MCP server
claude --mcp figma

You: Pull the brand colors from our Figma design system and create a poster

Claude Code: [Uses Figma MCP to fetch colors]
             [Applies to get_color_palette()]
             [Creates poster with brand colors]
```

### In CI/CD

```bash
# Automated poster generation in CI
claude -p "Generate release poster with version number from package.json"

# Auto-fix typography issues
claude -p "Fix any typography issues in examples/*.py using the design system"
```

### Composable Commands

```bash
# Monitor logs and create reports
tail -f app.log | claude -p "If errors spike, create a status poster and save to output/"

# Batch process
find examples -name "*.py" | xargs -I {} claude -p "Ensure {} uses the design system"
```

## Key Files for Claude Code

When Claude Code is working with this project, it references:

1. **`CLAUDE.md`** - Primary instructions for agents
2. **`.claude-plugin/drawbot-designer/SKILL.md`** - Skill definition
3. **`docs/DESIGN_SYSTEM_USAGE.md`** - Complete usage guide
4. **`examples/minimal_poster_example.py`** - Quick start template
5. **`lib/drawbot_design_system.py`** - Core system

## Security & Privacy

✅ **Secure**: All code runs locally in your environment
✅ **Private**: No data sent to external servers
✅ **Sandboxed**: DrawBot executes in isolated containers (via Dagger)
✅ **Auditable**: All changes are visible in git history

## Enterprise Features

### Self-Hosting
Use Claude API, AWS Bedrock, or GCP Vertex AI:

```bash
# Configure for Bedrock
export ANTHROPIC_BEDROCK_REGION=us-west-2
claude --api bedrock
```

### Team Skills
Share the skill across your team:

```bash
# In team repo
git clone https://github.com/your-org/drawbot-redux.git
cd drawbot-redux
claude

# Skill is automatically available to all team members
```

### CI Integration

```yaml
# .github/workflows/posters.yml
name: Generate Release Posters

on:
  release:
    types: [created]

jobs:
  posters:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: anthropics/claude-code-action@v1
        with:
          prompt: |
            Create a release poster for ${{ github.event.release.tag_name }}
            using the drawbot-designer skill
```

## Next Steps

1. **Try it**: `claude` → "Create a poster"
2. **Read**: `docs/DESIGN_SYSTEM_USAGE.md`
3. **Customize**: Modify `.claude-plugin/drawbot-designer/SKILL.md`
4. **Share**: Add to your team's plugin marketplace

## Resources

- **Claude Code Docs**: https://docs.claude.com/claude-code
- **Skills Spec**: https://github.com/anthropics/skills
- **This Project**: `docs/`, `examples/`, `lib/`

---

**DrawBot Redux + Claude Code = Professional design automation with enforced principles** 🎨🤖
