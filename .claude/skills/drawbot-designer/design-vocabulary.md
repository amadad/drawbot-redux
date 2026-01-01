# Design Vocabulary

Translation layer from natural language intent to concrete design decisions.

**Use this file first** when interpreting user requests. Map their words to specific choices, then implement using the design system.

---

## Aesthetic Directions (Bold Choices)

Before mapping moods, consider committing to a distinct aesthetic tradition:

| Direction | Grid | Type | Color | Texture | Energy |
|-----------|------|------|-------|---------|--------|
| **Swiss Modernism** | Strict 12-col, asymmetric | Helvetica, Akzidenz | Limited, high contrast | Clean, none | Ordered precision |
| **Punk/Zine** | Broken, overlapping | Mixed sizes, ransom-note | Black + neon | Photocopy grain | Chaotic rebellion |
| **Japanese Minimalism** | Open, asymmetric | One weight, generous space | Muted, single accent | Paper texture | Quiet tension |
| **Constructivist** | Diagonal, dynamic | Bold sans, angled | Red, black, white | Rough | Revolutionary energy |
| **Psychedelic** | Warped, radial | Flowing, decorative | Vibrating complementaries | Dense patterns | Overwhelming |
| **Corporate Brutalist** | Simple, stark | Oversized, bold | Black + one color | None | Confrontational |
| **Art Deco** | Symmetric, ornate | Geometric display | Gold, black, cream | Metallic | Glamorous |
| **Bauhaus** | Geometric modules | Futura, geometric | Primary + black | None | Functional clarity |
| **Vernacular** | Irregular, hand-drawn | Sign-painter, imperfect | Local, saturated | Painted texture | Authentic warmth |
| **Tech Noir** | Dense, terminal | Monospace, technical | Dark + neon accent | Scanlines, noise | Dystopian edge |
| **Editorial** | Multi-column, varied | Serif body, sans display | Sophisticated, limited | Paper quality | Intellectual calm |
| **Organic/Natural** | Flowing, curved | Humanist, hand-drawn | Earth tones | Natural textures | Living movement |

**Usage**: Pick ONE direction. Let it guide every subsequent choice.

---

## Mood → Design Mapping

### "Modern" / "Contemporary"
```
Grid:        Asymmetric (8+4 or 9+3 split)
Typography:  Sans-serif, high size contrast (title 3x+ body)
Colors:      Limited (2-3 max), one bold accent
Whitespace:  Generous (1/8 margin ratio)
Alignment:   Left-aligned, ragged right
Elements:    Minimal, purposeful negative space
Avoid:       Decoration, gradients, centered text
```

### "Classic" / "Traditional" / "Elegant"
```
Grid:        Symmetric, centered content
Typography:  Serif or mixed (serif body, sans headers)
Colors:      Muted, analogous palette
Whitespace:  Balanced, formal margins (1/10)
Alignment:   Centered or justified
Elements:    Rules, subtle borders, refined details
Avoid:       Bold colors, asymmetry, tight spacing
```

### "Bold" / "Impactful" / "Striking"
```
Grid:        Simple (2-3 major zones)
Typography:  Extra large title (scale.title * 1.5+), minimal body
Colors:      High contrast, black + one accent
Whitespace:  Strategic, frames the message
Alignment:   Left or centered, never justified
Elements:    One dominant element, everything else supports
Avoid:       Multiple focal points, busy layouts
```

### "Minimal" / "Clean" / "Simple"
```
Grid:        Sparse (6 columns, 4 rows max)
Typography:  One typeface, two weights max
Colors:      Monochrome or single accent
Whitespace:  Dominant (50%+ of canvas)
Alignment:   Consistent throughout
Elements:    Essential only, no decoration
Avoid:       Gradients, shadows, multiple colors
```

### "Corporate" / "Professional" / "Business"
```
Grid:        Standard 12-column, symmetric
Typography:  Conservative scale, clear hierarchy
Colors:      Blues, grays + one brand accent
Whitespace:  Standard (1/10 margin)
Alignment:   Left-aligned, structured
Elements:    Logo placement, contact info, clear sections
Avoid:       Playful elements, unusual layouts
```

### "Playful" / "Fun" / "Creative"
```
Grid:        Broken or overlapping elements
Typography:  Mixed sizes, varied weights
Colors:      Vibrant, complementary or triadic
Whitespace:  Varied, creates rhythm
Alignment:   Mixed, intentionally dynamic
Elements:    Shapes, patterns, visual surprises
Avoid:       Rigid grids, monochrome, formality
```

### "Urgent" / "Important" / "Alert"
```
Grid:        Simple, direct
Typography:  Bold weights, large sizes
Colors:      Red/orange accents, high contrast
Whitespace:  Tight, creates tension
Alignment:   Left or centered
Elements:    Exclamation, badges, highlighted text
Avoid:       Subtlety, decorative elements
```

### "Calm" / "Peaceful" / "Serene"
```
Grid:        Open, balanced
Typography:  Light weights, generous leading (1.8x)
Colors:      Cool palette (blues, greens), low saturation
Whitespace:  Abundant, breathing room
Alignment:   Centered or left with wide margins
Elements:    Soft shapes, no hard edges
Avoid:       Bold colors, tight spacing, heavy weights
```

### "Technical" / "Data" / "Scientific"
```
Grid:        Dense, multi-column (12-16 columns)
Typography:  Monospace for data, sans for labels
Colors:      Functional (blue=info, green=good, red=alert)
Whitespace:  Efficient but not cramped
Alignment:   Left-aligned, tabular
Elements:    Charts, tables, code blocks, annotations
Avoid:       Decorative elements, script fonts
```

### "Editorial" / "Magazine"
```
Grid:        Multi-column (2-3), varied heights
Typography:  Drop caps, pull quotes, varied hierarchy
Colors:      Sophisticated, limited palette
Whitespace:  Column gutters, section breaks
Alignment:   Justified body, left headlines
Elements:    Large images, callouts, sidebars
Avoid:       Uniform blocks, single column
```

---

## Content Type → Layout Pattern

### Announcement / Event
```
Structure:   Hero title → Date/Time → Details → CTA
Grid:        12×8, top-heavy (title uses 40% of space)
Emphasis:    WHAT (largest), WHEN (prominent), WHERE (clear)
```

### Data / Results / Report
```
Structure:   Title → Key Finding → Supporting Data → Context
Grid:        12×16, dense
Emphasis:    Numbers large, labels small, hierarchy by importance
```

### Narrative / Story
```
Structure:   Hook → Body → Conclusion
Grid:        6×8 or 8×8, generous margins
Emphasis:    Opening line, pull quotes, clear sections
```

### Comparison / Versus
```
Structure:   Split layout (left vs right or top vs bottom)
Grid:        6+6 columns or 12×8 with horizontal split
Emphasis:    Equal weight to both sides, clear differentiation
```

### Process / Timeline
```
Structure:   Sequential zones (top→bottom or left→right)
Grid:        12×(steps×2), consistent step sizing
Emphasis:    Step numbers/titles, connecting elements
```

### List / Collection
```
Structure:   Repeated card pattern
Grid:        3×N or 4×N cards
Emphasis:    Consistent card styling, clear item boundaries
```

---

## Adjective → Specific Value

### Size Adjectives
| Word | Title Scale | Body Scale | Margin Ratio |
|------|-------------|------------|--------------|
| "huge" / "massive" | ×2.0 | ×1.2 | 1/12 |
| "large" / "big" | ×1.5 | ×1.1 | 1/10 |
| "normal" / "standard" | ×1.0 | ×1.0 | 1/10 |
| "small" / "compact" | ×0.8 | ×0.9 | 1/8 |
| "tiny" / "minimal" | ×0.6 | ×0.8 | 1/6 |

### Spacing Adjectives
| Word | Leading | Margin Ratio | Gutter |
|------|---------|--------------|--------|
| "tight" / "dense" | 1.2 | 1/12 | 5pt |
| "normal" | 1.5 | 1/10 | 10pt |
| "loose" / "airy" | 1.8 | 1/8 | 15pt |
| "spacious" | 2.0 | 1/6 | 20pt |

### Weight Adjectives
| Word | Font Weight | Stroke Width |
|------|-------------|--------------|
| "light" / "thin" | Light, Ultralight | 0.5pt |
| "regular" / "normal" | Regular, Roman | 1pt |
| "medium" | Medium | 1.5pt |
| "bold" / "heavy" | Bold, Black | 2-3pt |

### Color Intensity
| Word | Saturation | Approach |
|------|------------|----------|
| "muted" / "subtle" | 20-40% | Grays with tint |
| "soft" | 40-60% | Pastels |
| "normal" | 60-80% | Standard palette |
| "vibrant" / "bold" | 80-100% | Pure colors |

---

## Color Associations

### By Meaning
| Intent | Primary | Secondary | Accent |
|--------|---------|-----------|--------|
| Trust / Reliable | Blue | Gray | White |
| Growth / Health | Green | White | Dark gray |
| Energy / Action | Orange/Red | White | Black |
| Luxury / Premium | Black | Gold | White |
| Innovation / Tech | Blue | Purple | Cyan |
| Natural / Organic | Green | Brown | Cream |
| Friendly / Warm | Orange | Yellow | Brown |
| Serious / Formal | Navy | Gray | Burgundy |

### By Industry
| Industry | Safe Palette |
|----------|--------------|
| Finance | Navy, gray, green |
| Healthcare | Blue, white, green |
| Tech | Blue, purple, black |
| Food | Red, orange, yellow, green |
| Fashion | Black, white, one accent |
| Education | Blue, green, orange |
| Government | Navy, red, white |

---

## Refinement Vocabulary

When user asks to adjust:

### "More contrast"
- Increase title/body size ratio
- Darken darks, lighten lights
- Reduce middle grays

### "Less busy" / "Simplify"
- Remove decorative elements
- Reduce color count
- Increase whitespace
- Combine similar sections

### "More breathing room" / "Open up"
- Increase margins (next ratio up)
- Increase leading (add 0.3)
- Increase gutters (+5pt)

### "Tighter" / "More compact"
- Decrease margins
- Decrease leading (subtract 0.2)
- Reduce gutters

### "More hierarchy" / "Clearer structure"
- Increase size differences between levels
- Add section dividers (rules, space)
- Differentiate with color or weight

### "More unified" / "Cohesive"
- Reduce typeface count to 1-2
- Limit color palette
- Standardize spacing units

### "Pop more" / "Stand out"
- Increase accent color saturation
- Add contrast to key elements
- Increase size of focal point

### "Softer" / "Gentler"
- Reduce contrast
- Use lighter weights
- Add more whitespace
- Mute colors

---

## Quick Decision Trees

### User says a mood word:
1. Look up mood in "Mood → Design Mapping"
2. Apply those settings as defaults
3. Proceed with implementation

### User describes content:
1. Identify content type in "Content Type → Layout Pattern"
2. Apply that structure
3. Layer mood settings on top

### User gives adjustment:
1. Find adjustment in "Refinement Vocabulary"
2. Apply specific changes
3. Show result

### User gives no direction:
Default to:
- Grid: 12×8
- Scale: POSTER_SCALE
- Palette: "professional"
- Margin: 1/10
- Leading: 1.5

---

## Example Translations

**User:** "Create a bold modern poster for a tech conference"
```
Modern → Asymmetric grid, sans-serif, limited colors, generous whitespace
Bold → Large title (×1.5), high contrast, one dominant element
Tech → Blue/purple palette

Result:
- Grid: 9+3 columns, 12 rows
- Title: scale.title × 1.5, Helvetica Bold
- Colors: Dark blue bg, white text, cyan accent
- Margin: 1/8 ratio
- One large title, minimal supporting text
```

**User:** "Make an elegant invitation"
```
Elegant → Symmetric, serif, muted colors, balanced whitespace
Invitation → Announcement pattern (WHAT → WHEN → WHERE)

Result:
- Grid: 12×8, centered content
- Title: scale.h1, Georgia or similar serif
- Colors: Cream bg, dark gray text, gold accent
- Margin: 1/10 ratio
- Centered alignment, refined typography
```

**User:** "I need something urgent about a deadline"
```
Urgent → Simple grid, bold weights, red accent, tight spacing

Result:
- Grid: 12×4, simple zones
- Title: scale.title × 1.2, Helvetica Bold
- Colors: White bg, black text, red accent on deadline
- Margin: 1/10
- Prominent date/deadline, minimal other content
```

---

## Anti-Patterns (What to Avoid)

### Signs of "Template Design"
These indicate lack of intentionality:

| Pattern | Problem | Fix |
|---------|---------|-----|
| Everything centered | Static, lifeless | Introduce asymmetry |
| Equal margins all around | No hierarchy | Vary margins intentionally |
| Blue/purple gradient | AI cliché | Any other palette |
| Helvetica + Open Sans | Overused pairing | Bolder font choices |
| Perfect geometric shapes | Clip-art feel | Organic or custom forms |
| Text all same size | No hierarchy | Use the scale properly |
| Evenly distributed colors | No focal point | 70-20-10 rule |

### The "Could Be Anyone's" Test
If your design could work for any company/event/purpose, it lacks identity.
Ask: "What about this is specific to THIS context?"

### Font Defaults to Avoid
❌ Inter, Roboto, Open Sans, Montserrat, Poppins (overused in AI output)
❌ Arial, Calibri (default system fonts)
❌ Papyrus, Comic Sans (obviously)

### Color Defaults to Avoid
❌ `#6B5BFF` → `#F5F5FF` (purple gradient on white)
❌ `#667EEA` → `#764BA2` (blue-purple gradient)
❌ `#4A90A4` (generic "tech blue")

---

## Remember

1. **Aesthetic direction first** - Commit to a bold tradition
2. **Mood second** - Refine within that direction
3. **Content structure third** - Layout follows information hierarchy
4. **Refinement last** - Adjust based on feedback
5. **Check for anti-patterns** - Avoid the "AI look"

The design system handles the "how" (grids, scales, wrapping). This vocabulary handles the "what" (which settings express the intent).

**The goal isn't just correctness—it's memorability.**
