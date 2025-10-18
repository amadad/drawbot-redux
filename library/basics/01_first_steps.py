"""
First Steps with DrawBot
========================
Welcome to DrawBot! This is your first program.

What you'll learn:
- How to create a canvas
- How to draw basic shapes
- How to add color
- How to save your work

DrawBot coordinates:
- (0, 0) is the bottom-left corner
- x increases to the right
- y increases upward
"""

# Import DrawBot - this gives us access to all drawing functions
import sys
import os

# Add the project root to Python path to find the local drawBot module
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import drawBot as db

# LESSON 1: Create your first canvas
# ----------------------------------
# newPage() creates a new drawing surface
# Default size is 1000 x 1000 pixels
db.newPage(600, 600)

# LESSON 2: Set a background color
# --------------------------------
# Colors in DrawBot use values from 0 to 1
# fill() sets the color for shapes
db.fill(0.95)  # Light gray (95% white)
db.rect(0, 0, 600, 600)  # Draw a rectangle that covers the whole canvas

# LESSON 3: Draw your first shape
# -------------------------------
# Let's draw a red circle in the center
db.fill(1, 0, 0)  # Red (R=1, G=0, B=0)
# oval(x, y, width, height)
db.oval(200, 200, 200, 200)  # Circle at (200, 200) with 200px diameter

# LESSON 4: Add more shapes
# -------------------------
# Blue square
db.fill(0, 0, 1)  # Blue
db.rect(100, 400, 100, 100)  # Square at (100, 400)

# Green triangle using a path
db.fill(0, 0.8, 0)  # Green
db.newPath()  # Start a new path
db.moveTo((400, 400))  # Move to first point
db.lineTo((500, 400))  # Draw line to second point
db.lineTo((450, 500))  # Draw line to third point
db.closePath()  # Close the path
db.drawPath()  # Fill the path

# LESSON 5: Add some text
# -----------------------
db.fill(0)  # Black
db.font("Helvetica-Bold")  # Set the font
db.fontSize(24)  # Set the size
db.text("Hello DrawBot!", (200, 50))  # Draw text at position

# LESSON 6: Draw with transparency
# --------------------------------
# You can add a fourth value for alpha (transparency)
db.fill(1, 1, 0, 0.5)  # Yellow with 50% opacity
db.oval(250, 250, 150, 150)  # Overlapping circle

# LESSON 7: Using stroke (outline)
# --------------------------------
db.fill(None)  # No fill
db.stroke(0)  # Black stroke
db.strokeWidth(3)  # 3 pixel wide stroke
db.rect(50, 50, 500, 500)  # Border around everything

# LESSON 8: Save your creation
# ----------------------------
# Save as PDF (vector format - can scale without losing quality)
output_path = "output/01_first_steps.pdf"
db.saveImage(output_path)
print(f"Saved to {output_path}")

# You can also save as PNG, JPG, etc.
# db.saveImage("output/01_first_steps.png")

# 🎯 EXERCISES:
# -------------
# 1. Change the background color to your favorite color
# 2. Add another shape (try a polygon or star)
# 3. Change the text to your name
# 4. Experiment with different transparency values
# 5. Try different stroke widths and colors

# 💡 TIPS:
# --------
# - Colors use values from 0 to 1, not 0 to 255
# - The coordinate system starts at bottom-left (like math, not like web)
# - You can layer shapes - later shapes appear on top
# - Save often and experiment freely!

# 🔍 WHAT'S NEXT:
# ---------------
# Continue to 02_basic_shapes.py to learn more shape primitives