# Print Production Checklist

Reference guide for preparing DrawBot designs for professional print output.

## Quick Start: Print-Ready Setup

```python
from drawbot_design_system import (
    setup_print_page,
    validate_print_ready,
    PRINT_PRESETS
)
import drawBot as db

# Set up page with bleed
specs = setup_print_page("letter", include_bleed=True)

# Draw background to FULL canvas (extends into bleed)
db.fill(0.2, 0.4, 0.8)
db.rect(0, 0, specs['canvas_width'], specs['canvas_height'])

# Position content relative to trim edge + safe margin
content_x = specs['trim_x'] + specs['safe_margin']
content_y = specs['trim_y'] + specs['safe_margin']

# ... draw content ...

# Validate before export
is_valid, warnings = validate_print_ready()
for w in warnings:
    print(w)

db.saveImage("print_ready.pdf")
```

---

## Print Terminology

| Term | Definition | Typical Value |
|------|------------|---------------|
| **Trim Size** | Final cut size of printed piece | 8.5" x 11" (letter) |
| **Bleed** | Extra area beyond trim for edge-to-edge printing | 0.125" (9pt) |
| **Safe Margin** | Keep important content inside this boundary | 0.5" (36pt) from trim |
| **Crop Marks** | Lines showing where to cut | At trim corners |
| **Registration** | Alignment marks for multi-color printing | Usually automatic |

---

## Pre-Flight Checklist

### Page Setup

- [ ] **Correct trim size** - Matches intended final dimensions
- [ ] **Bleed included** - Canvas extends 0.125" (US) or 3mm (metric) beyond trim
- [ ] **Background extends to bleed** - No white edges after cutting
- [ ] **Safe margin respected** - Important content 0.5" inside trim

### Color

- [ ] **CMYK for print** - Use `cmykFill()` and `cmykStroke()`
- [ ] **No RGB-only colors** - Convert or specify in CMYK
- [ ] **Rich black for large areas** - Use (0.6, 0.4, 0.4, 1.0) not (0, 0, 0, 1.0)
- [ ] **Total ink coverage < 300%** - Sum of C+M+Y+K percentages

### Typography

- [ ] **Fonts embedded** - PDF includes font data
- [ ] **Minimum text size** - 6pt for body, 4pt absolute minimum
- [ ] **Black text on white** - Use 100% K only, not 4-color black
- [ ] **No hairline rules** - Minimum stroke width 0.25pt

### Images

- [ ] **Resolution 300 DPI** - At final printed size
- [ ] **CMYK color mode** - For photos and rasters
- [ ] **No upscaling** - Images at 100% or smaller

### File Format

- [ ] **PDF/X-1a or PDF/X-4** - Print-ready standards
- [ ] **Fonts embedded** - Or converted to outlines
- [ ] **No transparency issues** - Flattened if required
- [ ] **Correct page count** - Single page or proper imposition

---

## Bleed Specifications

### Standard Bleed Values

| Region | Bleed | In Points |
|--------|-------|-----------|
| US/Canada | 0.125 inches | 9pt |
| Europe (Metric) | 3mm | 8.5pt |
| Large Format | 0.25-0.5 inches | 18-36pt |

### Using `setup_print_page()`

```python
from drawbot_design_system import setup_print_page

# Letter with standard US bleed
specs = setup_print_page("letter", include_bleed=True)
# specs = {
#   'width': 612, 'height': 792,        # Trim size
#   'canvas_width': 630, 'canvas_height': 810,  # With bleed
#   'bleed': 9, 'safe_margin': 36,
#   'trim_x': 9, 'trim_y': 9            # Offset to trim
# }

# A4 with metric bleed
specs = setup_print_page("a4", include_bleed=True)

# Custom bleed
specs = setup_print_page("tabloid", include_bleed=True, custom_bleed=18)

# No bleed (screen/digital only)
specs = setup_print_page("letter", include_bleed=False)
```

---

## CMYK Color for Print

### Basic CMYK Usage

```python
import drawBot as db

# CMYK values are 0-1 range (representing 0-100%)
db.cmykFill(0, 1, 1, 0)       # Red (0% cyan, 100% magenta, 100% yellow, 0% black)
db.cmykFill(1, 0, 1, 0)       # Green
db.cmykFill(1, 1, 0, 0)       # Blue
db.cmykFill(0, 0, 0, 1)       # Black (100% K only)

# With opacity
db.cmykFill(0, 0.5, 1, 0, 0.8)  # Orange at 80% opacity

# Stroke
db.cmykStroke(0, 0, 0, 1)     # Black stroke
db.strokeWidth(1)
```

### Rich Black

For large black areas, use rich black to prevent washed-out appearance:

```python
# Rich black (recommended for large areas)
db.cmykFill(0.6, 0.4, 0.4, 1.0)  # 60C 40M 40Y 100K

# Pure black (for small text only)
db.cmykFill(0, 0, 0, 1.0)  # 0C 0M 0Y 100K

# Registration black (for crop marks only, not content!)
db.cmykFill(1, 1, 1, 1)  # 100C 100M 100Y 100K - NEVER use for content
```

### Ink Limits

Total ink (C + M + Y + K) should not exceed:
- **Coated paper**: 320-340%
- **Uncoated paper**: 280-300%
- **Newsprint**: 240-260%

```python
def check_ink_limit(c, m, y, k, limit=300):
    """Check if CMYK values exceed ink limit."""
    total = (c + m + y + k) * 100
    if total > limit:
        print(f"Warning: Total ink {total:.0f}% exceeds {limit}% limit")
    return total <= limit

# Example
check_ink_limit(0.6, 0.4, 0.4, 1.0)  # 240% - OK
check_ink_limit(1.0, 1.0, 0.8, 0.5)  # 330% - May cause issues
```

---

## Image Resolution

### DPI Requirements

| Use Case | Minimum DPI | Recommended |
|----------|-------------|-------------|
| Photo printing | 300 DPI | 300-350 DPI |
| Line art | 600 DPI | 1200 DPI |
| Large format (posters) | 150-200 DPI | 200 DPI |
| Billboards | 50-100 DPI | Depends on viewing distance |

### Calculating Actual DPI

```python
def calculate_dpi(pixel_width, print_width_inches):
    """Calculate DPI for an image at given print size."""
    return pixel_width / print_width_inches

# Example: 3000px image printed at 10 inches
dpi = calculate_dpi(3000, 10)  # 300 DPI - good for print

# Example: 1000px image printed at 10 inches
dpi = calculate_dpi(1000, 10)  # 100 DPI - too low!
```

### Working with Images in DrawBot

```python
import drawBot as db

# Check image dimensions
img_width, img_height = db.imageSize("photo.jpg")

# Calculate required print size at 300 DPI
max_print_width = img_width / 300  # inches
max_print_height = img_height / 300  # inches

print(f"Image can print up to {max_print_width:.1f}\" x {max_print_height:.1f}\" at 300 DPI")
```

---

## Export Settings

### PDF for Print

```python
import drawBot as db

# Standard PDF (fonts embedded)
db.saveImage("output.pdf")

# PDF with specific settings (via Quartz)
# Note: For production, use professional preflight tools
```

### High-Resolution Raster

```python
# 300 DPI PNG (for proofing or digital print)
db.saveImage("output.png", imageResolution=300)

# 600 DPI TIFF (for high-quality print)
db.saveImage("output.tiff", imageResolution=600)
```

---

## Common Print Sizes

### US Standard Sizes

| Name | Dimensions (inches) | Points | Use Case |
|------|---------------------|--------|----------|
| Letter | 8.5 x 11 | 612 x 792 | Documents, flyers |
| Legal | 8.5 x 14 | 612 x 1008 | Legal documents |
| Tabloid | 11 x 17 | 792 x 1224 | Posters, spreads |
| Half Letter | 5.5 x 8.5 | 396 x 612 | Booklets |

### ISO Sizes (Metric)

| Name | Dimensions (mm) | Points | Use Case |
|------|-----------------|--------|----------|
| A4 | 210 x 297 | 595 x 842 | International standard |
| A3 | 297 x 420 | 842 x 1191 | Posters |
| A5 | 148 x 210 | 420 x 595 | Booklets |
| A2 | 420 x 594 | 1191 x 1684 | Large posters |

### Poster Sizes

| Name | Dimensions | Points |
|------|------------|--------|
| 18 x 24 | 18 x 24 inches | 1296 x 1728 |
| 24 x 36 | 24 x 36 inches | 1728 x 2592 |
| 27 x 40 | 27 x 40 inches | 1944 x 2880 |

---

## Troubleshooting

### White Edge After Cutting

**Cause**: Background doesn't extend to bleed
**Fix**: Use `setup_print_page(include_bleed=True)` and draw background to full canvas

### Washed-Out Black

**Cause**: Using 100% K only for large black areas
**Fix**: Use rich black: `cmykFill(0.6, 0.4, 0.4, 1.0)`

### Fuzzy Text

**Cause**: Text printed below minimum size or using 4-color black
**Fix**: Keep text 6pt+ and use 100% K only for black text

### Pixelated Images

**Cause**: Image resolution too low for print size
**Fix**: Use 300 DPI images or reduce print size

### Color Shift from Screen

**Cause**: RGB to CMYK conversion differences
**Fix**: Work in CMYK from start; proof on calibrated system

---

## Quick Reference: PRINT_PRESETS

```python
PRINT_PRESETS = {
    "letter": {
        "width": 612,       # 8.5 inches
        "height": 792,      # 11 inches
        "bleed": 9,         # 0.125 inches
        "safe_margin": 36,  # 0.5 inches
    },
    "tabloid": {
        "width": 792,       # 11 inches
        "height": 1224,     # 17 inches
        "bleed": 9,
        "safe_margin": 36,
    },
    "a4": {
        "width": 595,       # 210 mm
        "height": 842,      # 297 mm
        "bleed": 8.5,       # 3 mm
        "safe_margin": 28,  # 10 mm
    },
    "a3": {
        "width": 842,       # 297 mm
        "height": 1191,     # 420 mm
        "bleed": 8.5,
        "safe_margin": 28,
    },
    "poster_24x36": {
        "width": 1728,      # 24 inches
        "height": 2592,     # 36 inches
        "bleed": 18,        # 0.25 inches
        "safe_margin": 72,  # 1 inch
    },
}
```

---

## See Also

- [design-system-usage.md](design-system-usage.md) - Complete design system guide
- [drawbot-api-quick-reference.md](drawbot-api-quick-reference.md) - DrawBot API reference
- [typography-style-guide.md](typography-style-guide.md) - Typography for print
