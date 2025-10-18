"""
Basic Shapes in DrawBot
=======================
Master the fundamental drawing primitives.

What you'll learn:
- Rectangle variations
- Circles and ellipses
- Lines and paths
- Polygons and stars
- Combining shapes
"""

import sys
import os

# Add the project root to Python path to find the local drawBot module
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import drawBot as db

# Create a larger canvas to showcase all shapes
db.newPage(800, 1000)

# Background
db.fill(0.98)  # Almost white
db.rect(0, 0, 800, 1000)

# Title
db.fill(0)
db.font("Helvetica-Bold")
db.fontSize(32)
db.text("Basic Shapes in DrawBot", (50, 930))

# Helper function to draw labels
def label(text, x, y):
    db.fill(0.3)
    db.font("Helvetica")
    db.fontSize(12)
    db.text(text, (x, y))

# SECTION 1: RECTANGLES
# ---------------------
y_offset = 850

# Basic rectangle
db.fill(0.8, 0.2, 0.2)  # Red
db.rect(50, y_offset - 100, 150, 80)
label("rect(x, y, width, height)", 50, y_offset - 120)

# Rounded rectangle (using BezierPath if roundedRect not available)
db.fill(0.2, 0.6, 0.8)  # Blue
# Create a rounded rectangle manually
path = db.BezierPath()
path.rect(250, y_offset - 100, 150, 80)
db.drawPath(path)
label("Rectangle (rounded corners N/A)", 250, y_offset - 120)

# Square (equal width and height)
db.fill(0.3, 0.7, 0.3)  # Green
db.rect(450, y_offset - 100, 80, 80)
label("Square: equal dimensions", 450, y_offset - 120)

# SECTION 2: CIRCLES AND ELLIPSES
# --------------------------------
y_offset = 650

# Perfect circle
db.fill(0.9, 0.6, 0.1)  # Orange
db.oval(50, y_offset - 100, 100, 100)
label("Perfect circle", 50, y_offset - 120)

# Ellipse (stretched circle)
db.fill(0.6, 0.2, 0.8)  # Purple
db.oval(200, y_offset - 100, 150, 80)
label("Ellipse: oval()", 200, y_offset - 120)

# Circle with stroke only
db.fill(None)  # No fill
db.stroke(0.2, 0.4, 0.8)  # Blue stroke
db.strokeWidth(4)
db.oval(400, y_offset - 100, 100, 100)
label("Stroke only", 400, y_offset - 120)
db.stroke(None)  # Reset stroke

# SECTION 3: LINES AND PATHS
# --------------------------
y_offset = 450

# Simple line
db.stroke(0)
db.strokeWidth(2)
db.line((50, y_offset), (150, y_offset - 50))
label("line() function", 50, y_offset - 70)

# Multiple connected lines
db.newPath()
db.moveTo((200, y_offset))
db.lineTo((250, y_offset - 80))
db.lineTo((300, y_offset - 60))
db.lineTo((350, y_offset - 90))
db.lineTo((400, y_offset - 20))
db.drawPath()
label("Connected lines", 200, y_offset - 100)

# Curved path (bezier)
db.newPath()
db.moveTo((450, y_offset))
db.curveTo((500, y_offset - 100), (600, y_offset - 100), (650, y_offset))
db.drawPath()
label("Bezier curve", 450, y_offset - 70)
db.stroke(None)

# SECTION 4: POLYGONS
# -------------------
y_offset = 300

# Triangle
db.fill(0.8, 0.8, 0.2)  # Yellow
db.polygon((100, y_offset - 80), (50, y_offset), (150, y_offset))
label("Triangle: polygon()", 50, y_offset - 100)

# Pentagon
db.fill(0.4, 0.7, 0.9)  # Light blue
db.polygon((250, y_offset - 80), (300, y_offset - 95), 
           (350, y_offset - 70), (340, y_offset - 20), 
           (260, y_offset - 20))
label("Pentagon", 250, y_offset - 115)

# Regular hexagon (using math)
import math
db.fill(0.9, 0.3, 0.5)  # Pink
center_x, center_y = 500, y_offset - 50
radius = 40
points = []
for i in range(6):
    angle = i * math.pi * 2 / 6
    x = center_x + radius * math.cos(angle)
    y = center_y + radius * math.sin(angle)
    points.append((x, y))
db.polygon(*points)
label("Regular hexagon", 450, y_offset - 100)

# SECTION 5: COMBINING SHAPES
# ---------------------------
y_offset = 150

# House (combining rectangles and triangles)
# Base
db.fill(0.7, 0.5, 0.3)  # Brown
db.rect(50, y_offset - 60, 100, 80)
# Roof
db.fill(0.8, 0.2, 0.2)  # Red
db.polygon((40, y_offset + 20), (100, y_offset + 60), (160, y_offset + 20))
# Door
db.fill(0.3, 0.2, 0.1)  # Dark brown
db.rect(85, y_offset - 60, 30, 50)
# Window
db.fill(0.5, 0.7, 0.9)  # Light blue
db.rect(60, y_offset - 20, 25, 25)
label("Combined shapes", 50, y_offset - 80)

# Abstract composition
# Background circle
db.fill(0.9, 0.9, 0.3, 0.5)  # Yellow, transparent
db.oval(250, y_offset - 50, 100, 100)
# Overlapping square
db.fill(0.3, 0.3, 0.9, 0.5)  # Blue, transparent
db.rect(275, y_offset - 25, 50, 50)
# Central circle
db.fill(0.9, 0.3, 0.3, 0.7)  # Red, semi-transparent
db.oval(285, y_offset - 15, 30, 30)
label("Layered composition", 250, y_offset - 80)

# Star (custom path)
db.fill(0.1, 0.1, 0.1)  # Almost black
center_x, center_y = 500, y_offset
outer_radius = 40
inner_radius = 20
points = 10  # 5-pointed star
db.newPath()
for i in range(points):
    angle = i * math.pi * 2 / points - math.pi / 2
    if i % 2 == 0:
        x = center_x + outer_radius * math.cos(angle)
        y = center_y + outer_radius * math.sin(angle)
    else:
        x = center_x + inner_radius * math.cos(angle)
        y = center_y + inner_radius * math.sin(angle)
    if i == 0:
        db.moveTo((x, y))
    else:
        db.lineTo((x, y))
db.closePath()
db.drawPath()
label("Star shape", 450, y_offset - 60)

# Save the output
output_path = "output/02_basic_shapes.pdf"
db.saveImage(output_path)
print(f"Saved to {output_path}")

# 🎯 EXERCISES:
# -------------
# 1. Create a smiley face using circles and curves
# 2. Draw a simple car using rectangles and circles
# 3. Make a pattern using one shape repeated with different colors
# 4. Create an abstract composition with overlapping transparent shapes
# 5. Draw a simple logo using geometric shapes

# 💡 SHAPE TIPS:
# --------------
# - rect() is the most basic shape - master it first
# - oval() with equal width/height makes a perfect circle
# - polygon() can create any shape with straight sides
# - Use newPath() for complex custom shapes
# - Combine simple shapes to create complex illustrations

# 🔍 WHAT'S NEXT:
# ---------------
# Continue to 03_color_theory.py to master color in DrawBot