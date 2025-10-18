"""
Color Theory in DrawBot
=======================
Understanding color models and how to use them effectively.

What you'll learn:
- RGB color model
- HSB (HSV) color model
- Color with transparency (alpha)
- Gradients
- Color harmonies
"""

import sys
import os

# Add the project root to Python path to find the local drawBot module
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import drawBot as db
import colorsys  # For HSB/HSV color conversion

# Create multiple pages to explore different color concepts
# PAGE 1: RGB Color Model
db.newPage(800, 1000)

# Background
db.fill(0.95)
db.rect(0, 0, 800, 1000)

# Title
db.fill(0)
db.font("Helvetica-Bold")
db.fontSize(32)
db.text("RGB Color Model", (50, 930))

# RGB explanation
db.font("Helvetica")
db.fontSize(14)
db.text("RGB: Red, Green, Blue - Values from 0 to 1", (50, 890))

# RGB Primary Colors
y_pos = 800
size = 120

# Red
db.fill(1, 0, 0)  # Pure red
db.rect(50, y_pos, size, size)
db.fill(0)
db.fontSize(12)
db.text("R: 1, G: 0, B: 0", (50, y_pos - 20))

# Green
db.fill(0, 1, 0)  # Pure green
db.rect(200, y_pos, size, size)
db.fill(0)
db.text("R: 0, G: 1, B: 0", (200, y_pos - 20))

# Blue
db.fill(0, 0, 1)  # Pure blue
db.rect(350, y_pos, size, size)
db.fill(0)
db.text("R: 0, G: 0, B: 1", (350, y_pos - 20))

# RGB Color Mixing
y_pos = 600
db.fontSize(16)
db.text("Color Mixing in RGB", (50, y_pos + 150))

# Red + Green = Yellow
db.fill(1, 1, 0)
db.rect(50, y_pos, size, size)
db.fill(0)
db.fontSize(12)
db.text("R: 1, G: 1, B: 0 = Yellow", (50, y_pos - 20))

# Red + Blue = Magenta
db.fill(1, 0, 1)
db.rect(200, y_pos, size, size)
db.fill(0)
db.text("R: 1, G: 0, B: 1 = Magenta", (200, y_pos - 20))

# Green + Blue = Cyan
db.fill(0, 1, 1)
db.rect(350, y_pos, size, size)
db.fill(0)
db.text("R: 0, G: 1, B: 1 = Cyan", (350, y_pos - 20))

# All colors = White
db.fill(1, 1, 1)
db.stroke(0.8)
db.rect(500, y_pos, size, size)
db.stroke(None)
db.fill(0)
db.text("R: 1, G: 1, B: 1 = White", (500, y_pos - 20))

# RGB Gradient Example
y_pos = 400
db.fontSize(16)
db.text("RGB Gradients", (50, y_pos + 80))

# Red to Blue gradient
steps = 50
for i in range(steps):
    r = 1 - (i / steps)  # Red decreases
    b = i / steps        # Blue increases
    db.fill(r, 0, b)
    db.rect(50 + i * 12, y_pos, 12, 60)

db.fill(0)
db.fontSize(12)
db.text("Red to Blue gradient", (50, y_pos - 20))

# Grayscale
y_pos = 250
db.fontSize(16)
db.text("Grayscale: Equal RGB Values", (50, y_pos + 80))

for i in range(11):
    gray = i / 10
    db.fill(gray, gray, gray)
    db.rect(50 + i * 60, y_pos, 50, 50)
    # Label
    db.fill(0.5)
    db.fontSize(10)
    db.text(f"{gray:.1f}", (55 + i * 60, y_pos - 15))

# Color swatches with common colors
y_pos = 100
db.fill(0)
db.fontSize(16)
db.text("Common RGB Colors", (50, y_pos + 80))

colors = [
    ((0.2, 0.2, 0.2), "Dark Gray"),
    ((0.94, 0.52, 0.13), "Orange"),
    ((0.55, 0.27, 0.07), "Brown"),
    ((0.5, 0, 0.5), "Purple"),
    ((1, 0.75, 0.8), "Pink"),
    ((0, 0.5, 0), "Dark Green")
]

for i, (color, name) in enumerate(colors):
    db.fill(*color)
    x = 50 + (i % 3) * 200
    y = y_pos - (i // 3) * 60
    db.rect(x, y, 50, 50)
    db.fill(0)
    db.fontSize(10)
    db.text(name, (x + 60, y + 20))
    db.text(f"RGB: {color}", (x + 60, y + 5))

# PAGE 2: HSB Color Model
db.newPage(800, 1000)

# Background
db.fill(0.95)
db.rect(0, 0, 800, 1000)

# Title
db.fill(0)
db.font("Helvetica-Bold")
db.fontSize(32)
db.text("HSB Color Model", (50, 930))

# HSB explanation
db.font("Helvetica")
db.fontSize(14)
db.text("HSB: Hue, Saturation, Brightness - More intuitive for designers", (50, 890))

# Hue wheel
y_pos = 750
db.fontSize(16)
db.text("Hue: The Color (0-360°)", (50, y_pos + 80))

# Draw hue spectrum
hue_steps = 36
for i in range(hue_steps):
    hue = i / hue_steps  # 0 to 1
    # Convert HSB to RGB for drawing
    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
    db.fill(r, g, b)
    angle_start = i * 10
    angle_end = (i + 1) * 10
    db.newPath()
    db.moveTo((400, y_pos))
    db.arc((400, y_pos), 80, angle_start, angle_end, clockwise=False)
    db.closePath()
    db.drawPath()

# Saturation examples
y_pos = 550
db.fill(0)
db.fontSize(16)
db.text("Saturation: Color Intensity (0-100%)", (50, y_pos + 80))

# Show saturation variations
for i in range(11):
    saturation = i / 10
    r, g, b = colorsys.hsv_to_rgb(0.5, saturation, 1)
    db.fill(r, g, b)  # Blue hue
    db.rect(50 + i * 60, y_pos, 50, 50)
    db.fill(0)
    db.fontSize(10)
    db.text(f"{int(saturation * 100)}%", (52 + i * 60, y_pos - 15))

# Brightness examples
y_pos = 400
db.fill(0)
db.fontSize(16)
db.text("Brightness: Light Amount (0-100%)", (50, y_pos + 80))

# Show brightness variations
for i in range(11):
    brightness = i / 10
    r, g, b = colorsys.hsv_to_rgb(0.5, 1, brightness)
    db.fill(r, g, b)  # Blue hue, full saturation
    db.rect(50 + i * 60, y_pos, 50, 50)
    db.fill(0.5)
    db.fontSize(10)
    db.text(f"{int(brightness * 100)}%", (52 + i * 60, y_pos - 15))

# Color harmonies using HSB
y_pos = 250
db.fill(0)
db.fontSize(16)
db.text("Color Harmonies using HSB", (50, y_pos + 80))

base_hue = 0.15  # Orange

# Complementary (opposite on wheel)
r, g, b = colorsys.hsv_to_rgb(base_hue, 1, 1)
db.fill(r, g, b)
db.rect(50, y_pos, 60, 60)
r, g, b = colorsys.hsv_to_rgb((base_hue + 0.5) % 1, 1, 1)
db.fill(r, g, b)
db.rect(120, y_pos, 60, 60)
db.fill(0)
db.fontSize(12)
db.text("Complementary", (50, y_pos - 20))

# Analogous (adjacent colors)
x_offset = 250
r, g, b = colorsys.hsv_to_rgb((base_hue - 0.08) % 1, 1, 1)
db.fill(r, g, b)
db.rect(x_offset, y_pos, 60, 60)
r, g, b = colorsys.hsv_to_rgb(base_hue, 1, 1)
db.fill(r, g, b)
db.rect(x_offset + 70, y_pos, 60, 60)
r, g, b = colorsys.hsv_to_rgb((base_hue + 0.08) % 1, 1, 1)
db.fill(r, g, b)
db.rect(x_offset + 140, y_pos, 60, 60)
db.fill(0)
db.text("Analogous", (x_offset, y_pos - 20))

# Triadic (three equidistant)
x_offset = 500
r, g, b = colorsys.hsv_to_rgb(base_hue, 1, 1)
db.fill(r, g, b)
db.rect(x_offset, y_pos, 60, 60)
r, g, b = colorsys.hsv_to_rgb((base_hue + 0.333) % 1, 1, 1)
db.fill(r, g, b)
db.rect(x_offset + 70, y_pos, 60, 60)
r, g, b = colorsys.hsv_to_rgb((base_hue + 0.666) % 1, 1, 1)
db.fill(r, g, b)
db.rect(x_offset + 140, y_pos, 60, 60)
db.fill(0)
db.text("Triadic", (x_offset, y_pos - 20))

# PAGE 3: Transparency and Gradients
db.newPage(800, 1000)

# Background
db.fill(0.95)
db.rect(0, 0, 800, 1000)

# Title
db.fill(0)
db.font("Helvetica-Bold")
db.fontSize(32)
db.text("Transparency & Gradients", (50, 930))

# Alpha channel demonstration
y_pos = 800
db.fontSize(16)
db.text("Alpha Channel (Transparency)", (50, y_pos + 80))

# Draw overlapping circles with different alpha values
for i in range(5):
    alpha = 0.2 + i * 0.2
    db.fill(1, 0, 0, alpha)  # Red with varying alpha
    db.oval(50 + i * 80, y_pos, 120, 120)
    db.fill(0)
    db.fontSize(10)
    db.text(f"Alpha: {alpha:.1f}", (70 + i * 80, y_pos - 20))

# Color blending with transparency
y_pos = 600
db.fontSize(16)
db.text("Color Blending with Transparency", (50, y_pos + 120))

# Base shapes
db.fill(1, 0, 0, 0.5)  # Red 50%
db.rect(50, y_pos, 100, 100)

db.fill(0, 0, 1, 0.5)  # Blue 50%
db.rect(100, y_pos, 100, 100)

db.fill(0, 1, 0, 0.5)  # Green 50%
db.oval(100, y_pos - 50, 100, 100)

# Linear gradient simulation
y_pos = 400
db.fontSize(16)
db.text("Gradient Simulation", (50, y_pos + 80))

# Smooth gradient using many rectangles
gradient_steps = 100
for i in range(gradient_steps):
    t = i / gradient_steps
    # Interpolate between two colors
    r = 1 * (1 - t) + 0 * t  # From red to cyan
    g = 0 * (1 - t) + 1 * t
    b = 0 * (1 - t) + 1 * t
    db.fill(r, g, b)
    db.rect(50 + i * 6, y_pos, 6, 60)

db.fill(0)
db.fontSize(12)
db.text("Red to Cyan gradient", (50, y_pos - 20))

# Radial gradient effect
y_pos = 200
db.fontSize(16)
db.text("Radial Gradient Effect", (50, y_pos + 120))

# Draw concentric circles
center_x, center_y = 150, y_pos + 50
for i in range(20):
    t = i / 20
    db.fill(1, 0.5 * t, 0, 1 - t * 0.7)  # Orange fading out
    radius = 80 - i * 4
    db.oval(center_x - radius, center_y - radius, radius * 2, radius * 2)

# Save the complete color theory guide
output_path = "output/03_color_theory.pdf"
db.saveImage(output_path)
print(f"Saved to {output_path}")

# 🎯 EXERCISES:
# -------------
# 1. Create a sunset using RGB gradients
# 2. Design a color palette using HSB harmonies
# 3. Make overlapping shapes with different transparencies
# 4. Create a rainbow using the HSB hue wheel
# 5. Design a logo using only 3 colors and their variations

# 💡 COLOR TIPS:
# --------------
# - RGB is good for screen work, HSB is more intuitive for choosing colors
# - Use transparency to create depth and interesting overlaps
# - Color harmonies (complementary, analogous, etc.) create pleasing combinations
# - Gradients can be simulated with many small steps
# - Less is often more - limit your color palette

# 🔍 WHAT'S NEXT:
# ---------------
# Continue to 04_typography_basics.py to learn about working with text