# Layout & Design Principles for DrawBot

**Macro-typography and compositional design guidelines for creating posters, layouts, and editorial designs.**

This guide complements `style.md` (microtypography) with layout-level principles. Use these rules when composing pages, establishing grids, creating hierarchy, and making spatial decisions.

---

## Page Proportions & Margins

### Classic Page Ratios

```python
# Common page proportions (width : height)
LETTER = (8.5, 11)          # 1 : 1.29 (US standard)
A4 = (210, 297)             # 1 : 1.414 (ISO standard, √2 ratio)
GOLDEN = (1, 1.618)         # 1 : 1.618 (golden ratio)
SQUARE = (1, 1)             # 1 : 1
TABLOID = (11, 17)          # 1 : 1.545

# For visual harmony, use these ratios
```

### Margin Systems

**Van de Graaf Canon** (Classical book margins):
- Divide page into 9ths both ways (3×3 grid)
- Text block: Inner 4 sections
- Margins: 2:3:4:6 ratio (inner:top:outer:bottom)
- Creates elegant, balanced proportions

```python
# Van de Graaf margins for letter-size page
width, height = 612, 792  # Points (8.5×11 inches)
unit = width / 9

inner_margin = unit * 2      # 136pt
top_margin = unit * 1.5      # 102pt
outer_margin = unit * 3      # 204pt
bottom_margin = unit * 4     # 272pt
```

**Golden Ratio Margins**:
```python
# Simple golden ratio margins
margin = min(width, height) / 1.618 / 4  # ~1/6 of short dimension
# Use same margin all around, or:
top_margin = margin
side_margin = margin * 1.618
bottom_margin = margin * 2  # Heavier bottom
```

**Modern Minimal**:
```python
# Equal margins (modernist)
margin = width / 12  # 8.33% margins

# Breathing room (generous)
margin = width / 8   # 12.5% margins
```

### Line Length (Measure)

**Optimal readability**:
- **45-75 characters per line** (CPL)
- **Ideal: 60-65 characters** (2.5 alphabets)
- Too short: choppy, frequent saccades
- Too long: hard to find next line

```python
# Calculate column width from character count
chars_per_line = 65
avg_char_width = db.textSize("m")[0]  # Use 'm' as average
column_width = chars_per_line * avg_char_width

# Or measure actual text
sample = "abcdefghijklmnopqrstuvwxyz"
alphabet_width = db.textSize(sample * 2.5)[0]
column_width = alphabet_width
```

**Multi-column layouts**:
- **Narrow columns (30-40 CPL)**: News, captions
- **Wide columns (70-80 CPL)**: Books, essays
- **Poster text (20-30 CPL)**: Large type, scannable

---

## Typography Scale & Hierarchy

### Modular Scale

Use consistent ratios between type sizes for visual harmony:

```python
# Common scales
MINOR_SECOND = 1.067     # Subtle
MAJOR_SECOND = 1.125     # Gentle
MINOR_THIRD = 1.2        # Balanced
MAJOR_THIRD = 1.25       # Strong
PERFECT_FOURTH = 1.333   # Clear
PERFECT_FIFTH = 1.5      # Bold
GOLDEN_RATIO = 1.618     # Dramatic

# Example hierarchy (base 16pt, ratio 1.5)
base = 16
small = base / 1.5      # 10.67pt - captions
body = base             # 16pt - body text
h3 = base * 1.5         # 24pt - subheadings
h2 = base * 1.5 ** 2    # 36pt - headings
h1 = base * 1.5 ** 3    # 54pt - titles
display = base * 1.5 ** 4  # 81pt - hero text
```

### Practical Type Sizes

```python
# Editorial/Book
caption = 9-10
footnote = 8-9
body = 10-12
subhead = 14-18
heading = 24-36
title = 48-72

# Poster/Display
body_text = 14-18       # Larger for distance reading
subhead = 24-36
heading = 48-72
hero = 96-144           # Eye-catching
```

### Leading (Line Spacing)

**Formula**: `leading = font_size * ratio`

```python
# Line spacing ratios
TIGHT = 1.2             # Compact, dense
NORMAL = 1.4-1.5        # Standard book text
COMFORTABLE = 1.6-1.8   # Generous, easy reading
LOOSE = 2.0+            # Airy, display text

# Example
font_size = 12
leading = font_size * 1.5  # 18pt total (12pt + 6pt space)
db.lineHeight(leading)
```

**Rules**:
- Longer lines → more leading
- Lighter typefaces → more leading
- Darker typefaces → less leading
- Sans-serif → slightly more than serif

---

## Grid Systems

### Basic Grid Formula

```python
def create_grid(canvas_w, canvas_h, cols, rows, margin, gutter):
    """
    Calculate grid system

    Returns: dict with grid metrics
    """
    # Content area after margins
    content_w = canvas_w - (margin * 2)
    content_h = canvas_h - (margin * 2)

    # Column/row dimensions
    col_width = (content_w - (gutter * (cols - 1))) / cols
    row_height = (content_h - (gutter * (rows - 1))) / rows

    return {
        'content_box': (margin, margin, content_w, content_h),
        'col_width': col_width,
        'row_height': row_height,
        'gutter': gutter
    }

# Usage
grid = create_grid(612, 792, cols=6, rows=8, margin=72, gutter=20)
```

### Common Grid Patterns

**Single Column** (Books, essays):
```python
margin = 72
content_width = width - (margin * 2)
# One text column, generous margins
```

**Two Column** (Magazines, reports):
```python
cols = 2
gutter = 24
col_width = (content_width - gutter) / 2
```

**Three Column** (Newspapers, newsletters):
```python
cols = 3
gutter = 16
# Narrower columns, more gutter
```

**Multi-Column Flexible** (Editorial):
```python
# 6-column grid, use 2, 3, or 6 columns
base_cols = 6
# Text spans 4 cols, image spans 2 cols, etc.
```

### Baseline Grid

Align all text to common vertical rhythm:

```python
# Establish baseline
baseline_unit = 6  # pt
leading = baseline_unit * 3  # 18pt for 12pt type

# All elements align to multiples of baseline_unit
# Headings, images, spacing - all in multiples of 6pt
```

---

## Visual Hierarchy

### Contrast Principles (CRAP)

**C**ontrast - **R**epetition - **A**lignment - **P**roximity

**Contrast**: Make different elements VERY different
```python
# Weak contrast (confusing)
heading_size = 16
body_size = 14  # Too similar!

# Strong contrast (clear)
heading_size = 36
body_size = 12  # 3:1 ratio, obvious hierarchy
```

**Repetition**: Consistent styling creates unity
```python
# Use same heading style throughout
# Use same spacing patterns
# Repeat colors, weights, alignments
```

**Alignment**: Everything aligns to something
```python
# Avoid:
random_x_positions = [10, 23, 45, 67]  # Messy

# Use:
left_edge = margin
all_text_starts_at = left_edge  # Clean
```

**Proximity**: Group related items, separate unrelated
```python
# Related elements: tight spacing
caption_to_image = 8

# Unrelated elements: generous spacing
paragraph_spacing = 24
```

### Scale for Hierarchy

```python
# Z-index of importance
1. Hero text (largest, boldest, positioned first)
2. Primary heading (large, weighted)
3. Secondary heading (medium)
4. Body text (readable size)
5. Captions / metadata (smallest)
```

**Example hierarchy**:
```python
db.fontSize(96); db.font("Helvetica-Bold")
db.text("HERO", (margin, page_height - 200))

db.fontSize(36); db.font("Helvetica-Bold")
db.text("Heading", (margin, page_height - 300))

db.fontSize(16); db.font("Helvetica")
db.textBox(body_text, (margin, margin, col_width, 400))

db.fontSize(10); db.font("Helvetica-Oblique")
db.text("Caption", (margin, margin - 20))
```

---

## Whitespace (Negative Space)

**Most important design element**: What you DON'T fill.

### Breathing Room

```python
# Minimum clearance around elements
tight_space = 0.5 * font_size      # 8pt for 16pt text
comfortable_space = 1 * font_size  # 16pt for 16pt text
generous_space = 2 * font_size     # 32pt for 16pt text
```

### Macro Whitespace

```python
# Page-level breathing room
header_space = height / 6      # Top 1/6th empty
footer_space = height / 8      # Bottom 1/8th for page numbers

# Section separation
section_gap = font_size * 3    # 48pt for 16pt text
```

### Active Whitespace vs. Passive

- **Active**: Intentional, creates focus (large margins around key element)
- **Passive**: Leftover gaps (avoid random scattered spaces)

---

## Color & Tone

### Typographic Color

"Color" = overall grayness/darkness of text block

```python
# Factors affecting typographic color:
# - Letterforms (thick vs. thin)
# - Letterspacing
# - Line spacing
# - Ink density

# Aim for: Even, consistent gray tone across page
```

### Actual Color Usage

**70-20-10 Rule**:
- 70% dominant color (usually white/background)
- 20% secondary color (text/main content)
- 10% accent color (highlights, calls-to-action)

```python
# Example poster palette
background = (1, 1, 1)        # 70% white
text_color = (0.1, 0.1, 0.1)  # 20% dark gray
accent = (0.9, 0.2, 0.2)      # 10% red
```

### Contrast for Readability

**Minimum contrast**: 4.5:1 (WCAG AA standard)
**Optimal contrast**: 7:1 or higher

```python
# Safe high-contrast pairs
black_on_white = ((0, 0, 0), (1, 1, 1))      # 21:1
dark_on_light = ((0.2, 0.2, 0.2), (0.95, 0.95, 0.95))  # ~13:1

# Avoid
gray_on_gray = ((0.5, 0.5, 0.5), (0.6, 0.6, 0.6))  # Too low!
```

---

## Alignment Systems

### Primary Alignments

**Left-aligned** (Flush left, ragged right):
- Most readable for Western languages
- Natural, comfortable
- Use for body text

**Right-aligned** (Flush right, ragged left):
- Uncomfortable for long text
- Use for captions, labels, special effects

**Centered**:
- Formal, symmetrical
- Good for titles, invitations
- Avoid for body text

**Justified**:
- Formal, traditional
- Can create word spacing issues
- Requires hyphenation

### Edge Alignment

```python
# Align to page edges
left_edge = margin
right_edge = width - margin
top_edge = height - margin
bottom_edge = margin

# Align to grid
col_1_left = margin
col_2_left = margin + col_width + gutter
```

### Optical Alignment

```python
# Text with punctuation needs adjustment
# Hang punctuation outside text block for visual alignment
# DrawBot: use tracking and negative positioning

# Example: Pull quotes
quote_indent = -10  # Hang opening quote
```

---

## Compositional Patterns

### Rule of Thirds

Divide canvas into 3×3 grid:
- Place key elements on intersection points
- Creates dynamic, balanced composition

```python
third_w = width / 3
third_h = height / 3

# Power points (visually strong positions)
points = [
    (third_w, third_h * 2),      # Top-left intersection
    (third_w * 2, third_h * 2),  # Top-right intersection
    (third_w, third_h),          # Bottom-left intersection
    (third_w * 2, third_h),      # Bottom-right intersection
]
```

### Z-Pattern & F-Pattern

**Z-pattern** (Posters, ads):
- Eye moves: Top-left → Top-right → Bottom-left → Bottom-right
- Place hero at top-left, CTA at bottom-right

**F-pattern** (Text-heavy, editorial):
- Eye moves: Top → Down left edge → Horizontal scans
- Headlines on left, body text flows right

### Symmetry vs. Asymmetry

**Symmetrical**:
- Formal, stable, traditional
- Good for: Invitations, certificates, classical layouts

**Asymmetrical**:
- Dynamic, modern, engaging
- Good for: Posters, magazines, contemporary design

```python
# Symmetrical layout
center_x = width / 2
db.text("Title", (center_x - title_width/2, y))

# Asymmetrical layout
db.text("Title", (margin, y))  # Flush left, dynamic
```

---

## Quick Decision Matrix

### Choose Layout Type

| Content Type | Grid | Margins | Line Length |
|--------------|------|---------|-------------|
| **Book/Essay** | Single column | Van de Graaf | 60-65 CPL |
| **Magazine** | 2-3 columns | Generous (1/8) | 45-50 CPL |
| **Newspaper** | 3-6 columns | Tight (1/12) | 35-40 CPL |
| **Poster** | Flexible grid | 1/6 - 1/4 | 20-30 CPL |
| **Report** | 2 columns | Moderate (1/10) | 50-60 CPL |

### Choose Type Scale

| Purpose | Base Size | Scale Ratio | Leading |
|---------|-----------|-------------|---------|
| **Book text** | 10-12pt | 1.2-1.25 | 1.4x |
| **Magazine** | 10-11pt | 1.25-1.333 | 1.5x |
| **Poster** | 16-24pt | 1.5-1.618 | 1.3x |
| **Web/Screen** | 16-18pt | 1.25-1.5 | 1.5x |
| **Report** | 11-12pt | 1.2-1.333 | 1.4x |

### Choose Spacing

| Element | Tight | Normal | Generous |
|---------|-------|--------|----------|
| **Letter spacing** | -2% | 0% | +5% |
| **Word spacing** | 0.2em | 0.25em | 0.3em |
| **Line spacing** | 1.2x | 1.5x | 1.8x |
| **Paragraph spacing** | 0.5em | 1em | 1.5em |

---

## Practical Layout Workflow

1. **Define canvas and margins**
   ```python
   width, height = 612, 792
   margin = width / 10
   ```

2. **Establish grid system**
   ```python
   grid = create_grid(width, height, cols=6, rows=8, margin=margin, gutter=20)
   ```

3. **Set type scale**
   ```python
   base_size = 12
   ratio = 1.5
   sizes = {
       'body': base_size,
       'h3': base_size * ratio,
       'h2': base_size * ratio**2,
       'h1': base_size * ratio**3,
   }
   ```

4. **Define color palette**
   ```python
   colors = {
       'bg': (1, 1, 1),
       'text': (0.1, 0.1, 0.1),
       'accent': (0.8, 0.2, 0.2),
   }
   ```

5. **Place content with hierarchy**
   - Start with largest element (hero)
   - Add secondary elements
   - Fill with body content
   - Add details and refinements

6. **Check spacing and alignment**
   - All elements align to grid
   - Consistent spacing patterns
   - Adequate breathing room

---

## Common Layout Mistakes to Avoid

❌ **Too many fonts** - Use 1-2 font families max
❌ **Weak contrast** - Make hierarchy obvious
❌ **Cramped spacing** - Give elements room to breathe
❌ **Random alignment** - Align everything to grid
❌ **Inconsistent spacing** - Use modular scale
❌ **Too-long lines** - Keep under 75 characters
❌ **Orphans/widows** - Avoid single words on lines
❌ **Centered body text** - Use flush left for readability
❌ **No whitespace** - Empty space is valuable
❌ **Ignoring hierarchy** - Make importance clear

---

## Further Reading

- **typography-style-guide.md** - Microtypography (letter/word/line spacing)
- **archive/type.md** - Hochuli's Detail in Typography (full text)
- **drawbot-api-quick-reference.md** - DrawBot functions
- Jan Tschichold: *The Form of the Book*
- Josef Müller-Brockmann: *Grid Systems in Graphic Design*
- Robert Bringhurst: *The Elements of Typographic Style*
