# Image Filters and Effects

Quick reference for working with images, textures, and visual effects in DrawBot.

## Basic Image Loading

```python
import drawBot as db

# Method 1: Direct path (simple)
db.image("../../assets/paper/01.jpg", (x, y))

# Method 2: ImageObject (for filters)
img = db.ImageObject("../../assets/paper/01.jpg")
img.gaussianBlur(5)
db.image(img, (x, y))

# Method 3: With size
db.image("path.jpg", (x, y), width=300, height=200)
```

## Common Filter Patterns

### Texture Overlay with Opacity

```python
# Semi-transparent texture overlay
img = db.ImageObject("../../assets/paper/01.jpg")
db.image(img, (0, 0), alpha=0.3)  # 30% opacity
```

### Blurred Background

```python
# Soft focus background
img = db.ImageObject("photo.jpg")
img.gaussianBlur(radius=20)  # Higher = more blur
db.image(img, (0, 0))
```

### Desaturated (Black & White)

```python
# Reduce saturation for B&W effect
img = db.ImageObject("photo.jpg")
img.colorControls(saturation=0, brightness=1, contrast=1)
db.image(img, (x, y))
```

### Sepia Tone

```python
# Vintage sepia effect
img = db.ImageObject("photo.jpg")
img.sepiaTone(intensity=1.0)  # 0.0-1.0
db.image(img, (x, y))
```

### Vignette (Darkened Edges)

```python
# Combine with blend mode for vignette
db.image("photo.jpg", (0, 0))
db.fill(0, 0, 0, 0.3)
db.blendMode("multiply")
db.oval(0, 0, WIDTH, HEIGHT)  # Dark overlay
db.blendMode("normal")
```

## Essential Filters

### Blur Filters

```python
img.gaussianBlur(radius)               # Standard blur (radius: 0-100)
img.boxBlur(radius)                    # Faster box blur
img.motionBlur(radius, angle)          # Directional blur (angle in degrees)
```

### Color Adjustments

```python
# All-in-one color control
img.colorControls(
    saturation=1.0,   # 0=grayscale, 1=normal, >1=vibrant
    brightness=1.0,   # <1=darker, 1=normal, >1=brighter
    contrast=1.0      # <1=flat, 1=normal, >1=punchy
)

# Individual adjustments
img.exposureAdjust(exposure=0.5)       # -10 to 10 (0=normal)
img.hueAdjust(angle=180)               # Shift hue (0-360 degrees)
img.vibrance(amount=0.5)               # Smart saturation (0-1)
img.sepiaTone(intensity=1.0)           # Sepia effect (0-1)
```

### Sharpening

```python
img.sharpenLuminance(sharpness=0.4)    # Sharpen (0-2, careful >1)
img.unsharpMask(radius=2.5, intensity=0.5)  # Advanced sharpen
```

### Creative Effects

```python
img.colorInvert()                      # Negative effect
img.colorPosterize(levels=6)           # Reduce colors (2-30)
img.edges(intensity=1.0)               # Edge detection
img.pixellate(scale=8)                 # Pixelate effect
img.crystallize(radius=20)             # Crystallize/mosaic
img.pointillize(radius=20, center=(x, y))  # Pointillism
```

## Blend Modes

DrawBot supports Photoshop-style blend modes:

```python
db.blendMode("normal")      # Default
db.blendMode("multiply")    # Darken
db.blendMode("screen")      # Lighten
db.blendMode("overlay")     # Contrast
db.blendMode("softLight")   # Subtle lighting
db.blendMode("hardLight")   # Strong lighting
db.blendMode("colorDodge")  # Brighten highlights
db.blendMode("colorBurn")   # Darken shadows
```

Common uses:
- `multiply` - Darken textures, shadows
- `screen` - Lighten, glow effects
- `overlay` - Add texture with contrast
- `softLight` - Subtle texture overlay

## Texture Application Patterns

### Full-Page Texture

```python
# Paper texture over entire page
db.fill(*colors["background"])
db.rect(0, 0, WIDTH, HEIGHT)

# Overlay texture
db.blendMode("multiply")
db.image("../../assets/paper/01.jpg", (0, 0), alpha=0.2)
db.blendMode("normal")
```

### Texture in Specific Area

```python
# Add texture to a specific box
db.fill(0.9, 0.9, 0.85)
db.rect(x, y, width, height)

# Clip texture to box
with db.savedState():
    db.translate(x, y)
    db.clipPath()
    db.rect(0, 0, width, height)
    db.image("../../assets/cardboard/01.jpg", (0, 0), alpha=0.3)
```

### Gradient Texture

```python
# Combine gradient with texture
from drawbot_design_system import get_color_palette
colors = get_color_palette("warm")

# Draw gradient
gradient = db.linearGradient(
    (0, HEIGHT),
    (0, 0),
    [colors["primary"], colors["secondary"]]
)
db.fill(gradient)
db.rect(0, 0, WIDTH, HEIGHT)

# Overlay texture
db.blendMode("overlay")
db.image("../../assets/gradient/001.jpg", (0, 0), alpha=0.4)
db.blendMode("normal")
```

## Available Textures

See `../../assets/README.md` for complete catalog.

Quick reference:
- **gradient/** (1,001) - Abstract gradients, blend modes
- **gold/** (202) - Luxury, metallic effects
- **paper/** (57) - Natural paper, documents
- **cardboard/** (101) - Rough, organic texture
- **marker/** (100) - Hand-drawn feel
- **bubble/** (201) - Playful, organic
- **ziplock/** (102) - Plastic, modern
- **rust/** (51) - Grunge, weathered

## Troubleshooting

| Problem | Cause | Fix |
|---------|-------|-----|
| Image not showing | Wrong path | Use Path or check `assets/` structure |
| Texture too strong | High alpha | Reduce `alpha=0.1` to `alpha=0.3` |
| Slow rendering | Many filters | Use simpler filters, cache ImageObject |
| Colors look wrong | Blend mode active | Reset with `db.blendMode("normal")` |

## Performance Tips

1. **Create ImageObject once** - Don't reload in loops
   ```python
   # ✅ Good
   img = db.ImageObject("texture.jpg")
   for i in range(10):
       db.image(img, (x, y))

   # ❌ Bad
   for i in range(10):
       db.image("texture.jpg", (x, y))  # Reloads 10 times
   ```

2. **Chain filters** - Apply multiple filters to same ImageObject
   ```python
   img = db.ImageObject("photo.jpg")
   img.gaussianBlur(5)
   img.colorControls(saturation=0.7, brightness=1.1, contrast=1.2)
   img.sepiaTone(0.3)
   db.image(img, (0, 0))
   ```

3. **Use appropriate blur radius** - Small values (1-5) for subtle, large (20+) for dramatic

## Example: Photo Poster with Effects

```python
from drawbot_skia import drawbot as db
from drawbot_design_system import setup_poster_page, get_output_path

WIDTH, HEIGHT, MARGIN = setup_poster_page("letter")

# Load and process photo
photo = db.ImageObject("../../assets/gradient/001.jpg")
photo.gaussianBlur(3)
photo.colorControls(saturation=1.3, brightness=1.1, contrast=1.1)
photo.vibrance(0.2)

# Draw
db.image(photo, (0, 0), width=WIDTH, height=HEIGHT)

# Add overlay texture
db.blendMode("multiply")
db.image("../../assets/paper/01.jpg", (0, 0), alpha=0.15)
db.blendMode("normal")

db.saveImage(str(get_output_path("photo_poster.pdf")))
```

## When to Use Filters

- **Blur** - Backgrounds, depth of field, soft focus
- **Saturation** - Control color intensity, B&W conversion
- **Sepia** - Vintage, nostalgic feel
- **Sharpen** - Enhance clarity (use sparingly)
- **Posterize** - Graphic, pop-art style
- **Blend modes** - Combine images, add textures

## Advanced: Custom Image Processing

For pixel-level manipulation, use Pillow (PIL) before DrawBot:

```python
from PIL import Image
from drawbot_skia import drawbot as db

# Process with Pillow
img = Image.open("photo.jpg")
img = img.filter(Image.BLUR)
img.save("/tmp/processed.jpg")

# Use in DrawBot
db.image("/tmp/processed.jpg", (0, 0))
```

See `../../docs/drawbot-image-filters-reference.md` for complete filter API.
