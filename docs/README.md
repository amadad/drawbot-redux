# DrawBot Redux Documentation

Focused, essential documentation for compositional design with DrawBot.

---

## For AI Coding Agents

**Code Generation**: [`agent-learning-reference.md`](./agent-learning-reference.md)
- Critical rules (coordinate system, canvas-first, fill-before-draw)
- Drawing primitives and patterns
- Complete working templates
- Common mistakes to avoid
- Decision trees

**Pedagogical Framework**: [`learning-structure.md`](./learning-structure.md)
- 5-pillar approach (Foundation → Progression → Patterns → Design → Philosophy)
- 8-section progressive path with dependencies
- Mental models and assessment checkpoints
- Multiple learning paths (beginner, jump start, philosophy first, design-driven)

---

## For Humans

### Quick Start
**[`quickstart.md`](./quickstart.md)** - Get drawing in 5 minutes

### Design System
**[`design-system-usage.md`](./design-system-usage.md)** - Complete guide to the design system
- Grid-based layouts
- Typography scales
- Text wrapping
- Path handling
- Validation

### API References
**[`drawbot-api-quick-reference.md`](./drawbot-api-quick-reference.md)** - Core DrawBot API (95% of needs)
- Shapes, paths, text, colors
- Typography (variable fonts, OpenType)
- CMYK for print
- Boolean operations
- PDF features
- Animation

**[`drawbot-image-filters-reference.md`](./drawbot-image-filters-reference.md)** - 200+ image filters
- Blur, color, stylize effects
- Distortions and transformations
- Blend modes and compositing
- Generators and patterns

### Design Theory
**[`layout-design-principles.md`](./layout-design-principles.md)** - Composition & macro-typography
- Page proportions (Van de Graaf, Golden Ratio)
- Typography scales and hierarchy
- Grid systems
- Visual hierarchy (CRAP principles)
- Whitespace and color
- Quick decision matrices

**[`typography-style-guide.md`](./typography-style-guide.md)** - Microtypography
- Letter and word spacing
- Line length and readability
- Reading mechanics
- Emphasis systems
- Based on Hochuli's "Detail in Typography"

### Deep Theory (Rarely Needed)
**[`archive/`](./archive/)** - Full typography references
- Complete Hochuli transcription
- Original PDFs with illustrations

---

## Quick Lookup

| Need | Reference |
|------|-----------|
| **AI code generation** | agent-learning-reference.md |
| **Learning framework** | learning-structure.md |
| **Get started fast** | quickstart.md |
| **Design system** | design-system-usage.md |
| **DrawBot API** | drawbot-api-quick-reference.md |
| **Image effects** | drawbot-image-filters-reference.md |
| **Layout/grids/margins** | layout-design-principles.md |
| **Typography details** | typography-style-guide.md |
| **Code examples** | ../examples/ |
| **Textures** | ../assets/README.md |

---

## File Structure

```
docs/
├── README.md                           # This file
├── quickstart.md                       # Fast start guide
├── agent-learning-reference.md         # For AI coding agents (technical)
├── learning-structure.md               # For AI teaching/learning (pedagogical)
├── design-system-usage.md              # Design system guide
├── drawbot-api-quick-reference.md      # Core API
├── drawbot-image-filters-reference.md  # Image filters
├── layout-design-principles.md         # Composition theory
├── typography-style-guide.md           # Typography theory
└── archive/                            # Deep references
    ├── README.md
    ├── type.md                         # Full Hochuli
    └── Hochuli-DetailnTypography.pdf   # Original PDF
```

**Total**: 9 essential files + archive

---

## External Resources

- **Official DrawBot**: http://www.drawbot.com
- **Repository**: https://github.com/typemytype/drawbot
- **Forum**: http://forum.drawbot.com
- **Python for Designers**: https://pythonfordesigners.com

---

**Clean, focused, essential.**
