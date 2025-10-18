# DrawBot Redux - Agent Skills Setup

## ✅ Yes, Agent Skills Will Help Significantly!

Based on the Anthropic Skills framework you shared, **Agent Skills are the perfect solution** for DrawBot Redux. Here's how:

## What We've Built

### 1. Project Skill (`.claude/skills/drawbot-designer/`)

**Location**: `.claude/skills/drawbot-designer/SKILL.md`

This is a **project skill** that will be:
- ✅ Shared with your team via git
- ✅ Automatically available to anyone who clones the repo
- ✅ Model-invoked (Claude decides when to use it)
- ✅ Integrated with the design system

### 2. Key Features

**`allowed-tools` Configuration**:
```yaml
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
```

This restricts the skill to safe, design-focused operations without needing permission for each tool use.

**Specific Description**:
```yaml
description: Create well-designed posters, layouts, and graphics using DrawBot with automatic enforcement of typography principles from Hochuli, Bringhurst, and Müller-Brockmann. Use when users request posters, layouts, graphics, editorial designs, or mention DrawBot, typography, grid systems, or programmatic design. Requires drawbot-skia package.
```

This triggers the skill when users mention:
- "poster", "layout", "graphics", "editorial design"
- "DrawBot", "typography", "grid system"
- "programmatic design"

## How to Use

### For Team Members

1. **Clone the repo**:
   ```bash
   git clone <repo-url>
   cd drawbot-redux
   ```

2. **Start Claude Code**:
   ```bash
   claude
   ```

3. **Ask for design**:
   ```
   Create a poster for an AI safety benchmark
   ```

Claude will **automatically** use the `drawbot-designer` skill because:
- The request mentions "poster" (matches description)
- The skill is in `.claude/skills/` (project skill)
- Claude decides it's relevant and activates it

### For Personal Use

If you want this skill available across ALL your projects:

```bash
# Copy to personal skills directory
mkdir -p ~/.claude/skills/
cp -r .claude/skills/drawbot-designer ~/.claude/skills/

# Now available in any project
cd ~/other-project
claude
> Create a poster
# drawbot-designer skill is available!
```

## What the Skill Does

When activated, the skill:

1. **Reads documentation**: `docs/DESIGN_SYSTEM_USAGE.md`
2. **Uses the design system**: `lib/drawbot_design_system.py`
3. **Follows examples**: `examples/minimal_poster_example.py`
4. **Enforces principles**:
   - Grid-based layouts (no manual calculations)
   - Proper typography scales (context-aware)
   - Point-based text wrapping (no overflow)
   - Real font metrics (no approximations)

## Supporting Files Structure

```
.claude/skills/drawbot-designer/
├── SKILL.md              ← Main skill definition
└── (optional: add more)
    ├── REFERENCE.md      ← Could add API reference
    ├── EXAMPLES.md       ← Could add more examples
    └── PATTERNS.md       ← Could add design patterns
```

Currently we have all this in `docs/`, which the skill references.

## Testing the Skill

### 1. Verify it's loaded

```bash
claude
```

Then ask:
```
What skills are available?
```

You should see `drawbot-designer` in the list.

### 2. Test activation

Ask questions that should trigger it:
```
Create a poster for a machine learning conference
```

```
I need a layout for an editorial design
```

```
Help me with DrawBot typography
```

Claude should automatically use the skill (you'll see it in the response).

### 3. Debug if needed

```bash
claude --debug
```

This shows skill loading and activation decisions.

## Advantages Over MCP

| Feature | MCP Server | Agent Skill |
|---------|-----------|-------------|
| **Discovery** | Manual connection | Automatic (model-invoked) |
| **Sharing** | Separate installation | Git (automatic for team) |
| **Activation** | Explicit tool calls | Claude decides when relevant |
| **Permissions** | Per-tool prompts | `allowed-tools` (pre-approved) |
| **Maintenance** | Separate codebase | Alongside project code |

**Conclusion**: Agent Skills are better for this use case!

## Why This Works So Well

### 1. **Automatic Discovery**
Claude sees "poster" or "typography" and thinks:
> "The drawbot-designer skill is relevant here"

No need to tell Claude to use it explicitly.

### 2. **Progressive Disclosure**
The skill references:
```markdown
For complete usage, see docs/DESIGN_SYSTEM_USAGE.md
For examples, see examples/minimal_poster_example.py
```

Claude only loads these files when needed (saves context).

### 3. **Tool Permissions**
```yaml
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
```

Claude can use these tools without asking for permission each time, making the workflow smooth.

### 4. **Team Sharing**
```bash
git add .claude/skills/
git commit -m "Add drawbot-designer skill"
git push

# Team members:
git pull  # Skill is now available!
claude    # Starts using it automatically
```

## Real-World Usage

### Example 1: New Team Member

```bash
# New team member joins
git clone <repo>
cd drawbot-redux
claude

> Create a poster for our product launch

Claude: [Automatically uses drawbot-designer skill]
[Reads docs/DESIGN_SYSTEM_USAGE.md]
[Uses lib/drawbot_design_system.py]
[Creates professional poster following all principles]

✓ Created examples/product_launch_poster.py
✓ Saved to output/product_launch_poster.pdf
```

**No training needed!** The skill ensures correct usage automatically.

### Example 2: Consistent Quality

```bash
# Different team members, same quality
Team Member A: Create a poster for AI safety
Team Member B: Make a layout for our newsletter
Team Member C: Design graphics for the presentation

# All use the same skill → same quality
# All follow the same design principles
# All use the design system correctly
```

### Example 3: Iterative Design

```bash
claude

> Create a poster for LongitudinalBench

Claude: [Creates initial poster using skill]

> Make the title larger

Claude: [Uses skill knowledge to adjust with scale.title]

> Add a grid visualization

Claude: [Uses skill to add grid.draw(show_index=True)]
```

The skill maintains context throughout the conversation.

## File Organization

**Current structure**:
```
drawbot-redux/
├── .claude/
│   └── skills/
│       └── drawbot-designer/
│           └── SKILL.md          ← Agent Skill (✓ DONE)
├── lib/
│   ├── drawbot_grid.py           ← Core system
│   └── drawbot_design_system.py
├── docs/
│   ├── DESIGN_SYSTEM_USAGE.md    ← Referenced by skill
│   └── ...
└── examples/
    ├── minimal_poster_example.py  ← Referenced by skill
    └── ...
```

**Optional enhancements**:
```
.claude/skills/drawbot-designer/
├── SKILL.md                 ← Main (✓ done)
├── QUICK_REFERENCE.md       ← Quick API lookup
├── PATTERNS.md              ← Common design patterns
└── TROUBLESHOOTING.md       ← Common issues
```

## Next Steps

### 1. Test It

```bash
cd /path/to/drawbot-redux
claude

> Create a poster for an AI conference
```

Verify Claude uses the skill automatically.

### 2. Share with Team

```bash
git add .claude/
git commit -m "Add drawbot-designer Agent Skill"
git push
```

Team members will automatically get the skill.

### 3. Iterate

Based on usage, you can:
- Add more examples to SKILL.md
- Create additional reference files
- Refine the description for better triggering

### 4. Optional: Create Additional Skills

You could create specialized skills:

**`.claude/skills/drawbot-debug/`**:
```yaml
---
name: drawbot-debug
description: Debug DrawBot layout issues, fix text overflow, and validate designs. Use when debugging DrawBot code or fixing layout problems.
allowed-tools: Read, Grep, Bash
---
```

**`.claude/skills/drawbot-assets/`**:
```yaml
---
name: drawbot-assets
description: Find and apply textures from the 1,807 texture library. Use when adding textures, backgrounds, or visual effects to DrawBot designs.
allowed-tools: Read, Glob
---
```

## Summary

✅ **Agent Skills are perfect for DrawBot Redux**

**Benefits**:
1. Automatic activation (Claude decides when to use)
2. Team sharing via git (no separate installation)
3. Tool permissions pre-approved (`allowed-tools`)
4. Progressive disclosure (loads docs as needed)
5. Consistent quality (everyone uses the same system)

**Current Status**:
- ✅ Skill created: `.claude/skills/drawbot-designer/SKILL.md`
- ✅ Follows Anthropic best practices
- ✅ Ready for team use
- ✅ Integrates with design system

**Test it now**:
```bash
claude
> Create a poster
```

The skill will guide Claude to use the design system correctly! 🎉

---

**This is exactly what the Agent Skills framework was designed for.**
