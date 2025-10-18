"""
Typography Basics in DrawBot
============================
Learn how to work with text and fonts.

What you'll learn:
- Setting fonts and sizes
- Text positioning and alignment
- Font attributes (weight, style)
- FormattedString for mixed styles
- Basic text layouts
"""

import sys
import os

# Add the project root to Python path to find the local drawBot module
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import drawBot as db

# PAGE 1: Font Basics
db.newPage(800, 1000)

# Background
db.fill(0.98)
db.rect(0, 0, 800, 1000)

# Title
db.fill(0)
db.font("Helvetica-Bold")
db.fontSize(36)
db.text("Typography Basics", (50, 930))

# System fonts demonstration
y_pos = 850
db.fontSize(16)
db.text("Common System Fonts", (50, y_pos))

# Different font examples
fonts_to_show = [
    ("Helvetica", "The quick brown fox jumps over the lazy dog"),
    ("Times-Roman", "The quick brown fox jumps over the lazy dog"),
    ("Courier", "The quick brown fox jumps over the lazy dog"),
    ("Georgia", "The quick brown fox jumps over the lazy dog"),
    ("Futura-Medium", "The quick brown fox jumps over the lazy dog")
]

y_pos = 800
for font_name, sample_text in fonts_to_show:
    try:
        db.font(font_name)
        db.fontSize(18)
        db.text(sample_text, (50, y_pos))
        # Label
        db.font("Helvetica")
        db.fontSize(12)
        db.fill(0.5)
        db.text(font_name, (600, y_pos))
        db.fill(0)
    except:
        # If font not available, skip
        pass
    y_pos -= 40

# Font sizes
y_pos = 550
db.font("Helvetica")
db.fontSize(16)
db.text("Font Sizes", (50, y_pos + 40))

sizes = [12, 18, 24, 36, 48]
y_pos = 520
for size in sizes:
    db.fontSize(size)
    db.text(f"{size}pt", (50, y_pos))
    y_pos -= size + 10

# Font weights (if available)
y_pos = 300
db.fontSize(16)
db.text("Font Weights", (50, y_pos + 40))

weights = [
    ("Helvetica-Light", "Light"),
    ("Helvetica", "Regular"),
    ("Helvetica-Bold", "Bold")
]

y_pos = 280
for font_variant, label in weights:
    try:
        db.font(font_variant)
        db.fontSize(24)
        db.text(label, (50, y_pos))
    except:
        pass
    y_pos -= 40

# Text alignment
y_pos = 150
db.font("Helvetica")
db.fontSize(16)
db.text("Text Alignment", (50, y_pos + 40))

# Visual alignment guides
db.stroke(0.8)
db.strokeWidth(1)
db.line((400, 0), (400, 200))  # Center line
db.stroke(None)

# Left aligned (default)
db.fontSize(14)
db.text("Left aligned", (50, y_pos))

# Center aligned using textBox
db.textBox("Center aligned", (0, y_pos - 30, 800, 20), align="center")

# Right aligned using textBox
db.textBox("Right aligned", (0, y_pos - 60, 750, 20), align="right")

# PAGE 2: Advanced Typography
db.newPage(800, 1000)

# Background
db.fill(0.98)
db.rect(0, 0, 800, 1000)

# Title
db.fill(0)
db.font("Helvetica-Bold")
db.fontSize(36)
db.text("Advanced Typography", (50, 930))

# FormattedString for mixed styles
y_pos = 850
db.font("Helvetica")
db.fontSize(16)
db.text("FormattedString: Mixed Styles", (50, y_pos))

# Create a formatted string
txt = db.FormattedString()

# Add different styled parts
txt.append("This is ", font="Helvetica", fontSize=18, fill=(0, 0, 0))
txt.append("bold", font="Helvetica-Bold", fontSize=18, fill=(1, 0, 0))
txt.append(" and ", font="Helvetica", fontSize=18, fill=(0, 0, 0))
txt.append("italic", font="Helvetica-Oblique", fontSize=18, fill=(0, 0, 1))
txt.append(" text with ", font="Helvetica", fontSize=18, fill=(0, 0, 0))
txt.append("different", font="Helvetica", fontSize=24, fill=(0, 0.6, 0))
txt.append(" sizes!", font="Helvetica", fontSize=14, fill=(0, 0, 0))

db.text(txt, (50, y_pos - 50))

# Line height and tracking
y_pos = 700
db.fontSize(16)
db.text("Line Height & Tracking", (50, y_pos + 40))

# Normal spacing
sample = "Typography\nis the art\nof arranging\ntype"
db.font("Helvetica")
db.fontSize(24)
db.text(sample, (50, y_pos - 50))

# Increased line height
txt = db.FormattedString()
txt.append(sample, font="Helvetica", fontSize=24, lineHeight=36)
db.text(txt, (250, y_pos - 50))

# Tracking (letter spacing)
txt = db.FormattedString()
txt.append("TRACKING", font="Helvetica-Bold", fontSize=24, tracking=10)
db.text(txt, (450, y_pos))

txt = db.FormattedString()
txt.append("TRACKING", font="Helvetica-Bold", fontSize=24, tracking=-2)
db.text(txt, (450, y_pos - 40))

# Text on a path
y_pos = 450
db.fontSize(16)
db.text("Text on a Path", (50, y_pos + 80))

# Draw a circle path
center_x, center_y = 200, y_pos
radius = 80
db.newPath()
db.oval(center_x - radius, center_y - radius, radius * 2, radius * 2)
path = db.BezierPath()
path.oval(center_x - radius, center_y - radius, radius * 2, radius * 2)

# Draw the path (visual guide)
db.stroke(0.8)
db.strokeWidth(1)
db.drawPath()
db.stroke(None)

# Note: DrawBot doesn't directly support text on path, 
# but we can demonstrate the concept
db.fill(0)
db.fontSize(12)
db.text("(Text on path requires", (center_x - 60, center_y))
db.text("custom implementation)", (center_x - 60, center_y - 15))

# Text effects
y_pos = 250
db.fontSize(16)
db.text("Text Effects", (50, y_pos + 80))

# Shadow effect
db.fill(0.7)  # Gray shadow
db.text("Shadow Effect", (52, y_pos - 2))
db.fill(0)  # Black text
db.text("Shadow Effect", (50, y_pos))

# Outline effect
x_offset = 250
db.fontSize(24)
db.fill(None)
db.stroke(0)
db.strokeWidth(2)
db.text("Outline", (x_offset, y_pos))
db.stroke(None)

# Gradient fill (simulated)
x_offset = 400
letters = "GRADIENT"
for i, letter in enumerate(letters):
    t = i / len(letters)
    db.fill(1 - t, 0, t)  # Red to blue
    db.text(letter, (x_offset + i * 20, y_pos))

# PAGE 3: Typography Layout
db.newPage(800, 1000)

# Background
db.fill(0.98)
db.rect(0, 0, 800, 1000)

# Title
db.fill(0)
db.font("Helvetica-Bold")
db.fontSize(36)
db.text("Typography Layout", (50, 930))

# Text box with overflow
y_pos = 850
db.font("Helvetica")
db.fontSize(16)
db.text("Text Boxes", (50, y_pos))

# Long text for demonstration
long_text = """Design is not just what it looks like and feels like. Design is how it works. Good design is obvious. Great design is transparent. The details are not the details. They make the design."""

# Single column
db.fontSize(12)
box_height = 100
db.textBox(long_text, (50, y_pos - 150, 200, box_height))

# Visual box indicator
db.fill(None)
db.stroke(0.8)
db.rect(50, y_pos - 150, 200, box_height)
db.stroke(None)

# Two column layout
db.fill(0)
col_width = 180
col_gap = 20
db.textBox(long_text[:100], (300, y_pos - 150, col_width, box_height))
db.textBox(long_text[100:], (300 + col_width + col_gap, y_pos - 150, col_width, box_height))

# Justified text
y_pos = 650
db.fontSize(16)
db.text("Text Alignment Options", (50, y_pos))

alignment_text = "Justified text creates even edges on both sides by adjusting the spacing between words. This creates a clean, formal appearance."

# Different alignments
alignments = [
    ("left", 50),
    ("center", 300),
    ("right", 550),
]

y_pos = 600
for align, x in alignments:
    db.fontSize(10)
    db.fill(0.5)
    db.text(align.upper(), (x, y_pos))
    db.fill(0)
    db.fontSize(11)
    db.textBox(alignment_text, (x, y_pos - 80, 200, 70), align=align)
    
    # Box outline
    db.fill(None)
    db.stroke(0.9)
    db.rect(x, y_pos - 80, 200, 70)
    db.stroke(None)

# Typography hierarchy example
y_pos = 400
db.fill(0)
db.fontSize(16)
db.text("Typography Hierarchy", (50, y_pos + 40))

# Headline
db.font("Helvetica-Bold")
db.fontSize(32)
db.text("Main Headline", (50, y_pos))

# Subheadline
db.font("Helvetica")
db.fontSize(18)
db.fill(0.3)
db.text("Supporting subheadline goes here", (50, y_pos - 35))

# Body text
db.fontSize(12)
db.fill(0)
body = "Body text contains the main content. It should be readable and comfortable at smaller sizes. Good typography creates visual hierarchy and guides the reader through the content."
db.textBox(body, (50, y_pos - 120, 400, 80))

# Caption
db.fontSize(10)
db.fill(0.5)
db.text("Caption: Additional information in smaller type", (50, y_pos - 140))

# Save the typography guide
output_path = "output/04_typography_basics.pdf"
db.saveImage(output_path)
print(f"Saved to {output_path}")

# 🎯 EXERCISES:
# -------------
# 1. Create a poster using only typography (no shapes)
# 2. Design a business card with proper hierarchy
# 3. Make a quote poster with mixed font styles
# 4. Create a type specimen showing all weights of a font
# 5. Design a newsletter header with proper alignment

# 💡 TYPOGRAPHY TIPS:
# ------------------
# - Limit yourself to 2-3 fonts maximum
# - Use size and weight to create hierarchy
# - Pay attention to line height for readability
# - FormattedString gives you precise control
# - Consider the relationship between elements

# 🔍 WHAT'S NEXT:
# ---------------
# Explore the cookbook/ directory for practical recipes
# Or continue to foundations/ for deeper design principles