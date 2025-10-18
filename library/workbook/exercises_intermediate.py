"""
Intermediate DrawBot Exercises
==============================
More challenging exercises that combine multiple concepts.
Focus on design systems, complex layouts, and creative coding.

Prerequisites: Complete basic exercises first
"""

import sys
import os

# Add the project root to Python path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import drawBot as db
import random
import colorsys

# EXERCISE 1: Modular Type System
# Goal: Create a modular type scale using a ratio (e.g., 1.5)
# Display all sizes with sample text, maintaining baseline grid

def exercise_1():
    """Your code here"""
    db.newPage(800, 1000)
    base_size = 12
    ratio = 1.5
    # TODO: Create 6 levels of type hierarchy
    pass

# EXERCISE 2: Dynamic Logo System
# Goal: Create a logo that can adapt to different sizes/contexts
# Must work at 16x16, 64x64, and 200x200

def exercise_2():
    """Your code here"""
    # TODO: Create adaptive logo at 3 sizes
    pass

# EXERCISE 3: Data Visualization
# Goal: Create a bar chart from this data
# Data: [45, 78, 23, 89, 56, 91, 34, 67]
# Add labels, colors, and proper scaling

def exercise_3():
    """Your code here"""
    db.newPage(800, 600)
    data = [45, 78, 23, 89, 56, 91, 34, 67]
    # TODO: Create bar chart
    pass

# EXERCISE 4: Generative Pattern
# Goal: Create a pattern that uses randomness but feels cohesive
# Use seed for reproducibility

def exercise_4():
    """Your code here"""
    db.newPage(600, 600)
    random.seed(12345)
    # TODO: Create generative pattern
    pass

# EXERCISE 5: Magazine Layout
# Goal: Create a magazine spread with images and text
# Use placeholders for images, real text for typography

def exercise_5():
    """Your code here"""
    # Create two-page spread
    # TODO: Design magazine layout
    pass

# EXERCISE 6: Animation Sequence
# Goal: Create a smooth transition between two states
# Example: Morphing from square to circle over 10 frames

def exercise_6():
    """Your code here"""
    # TODO: Create morphing animation
    pass

# EXERCISE 7: Color Harmony System
# Goal: Generate a complete color palette from a base color
# Include: analogous, complementary, triadic schemes

def exercise_7():
    """Your code here"""
    db.newPage(800, 1000)
    base_hue = 0.6  # Blue
    # TODO: Generate color harmonies
    pass

# EXERCISE 8: Responsive Poster
# Goal: Design a poster that works at 3 different aspect ratios
# Maintain visual hierarchy and balance

def exercise_8():
    """Your code here"""
    # TODO: Create responsive poster design
    pass

# EXERCISE 9: Custom Typography
# Goal: Create decorative letters using geometric shapes
# Spell out "DESIGN" with custom letterforms

def exercise_9():
    """Your code here"""
    db.newPage(800, 400)
    # TODO: Create custom letterforms
    pass

# EXERCISE 10: Complex Grid System
# Goal: Design a dashboard layout using nested grids
# Include: header, sidebar, main content, widgets

def exercise_10():
    """Your code here"""
    db.newPage(1200, 800)
    # TODO: Create dashboard with nested grids
    pass

# ========== SOLUTIONS BELOW ==========
# =====================================

def solution_1():
    """Modular Type System Solution"""
    db.newPage(800, 1000)
    base_size = 12
    ratio = 1.5
    baseline = 8
    margin = 60
    y_pos = 900
    
    # Background
    db.fill(0.98)
    db.rect(0, 0, 800, 1000)
    
    # Draw baseline grid
    db.stroke(0.9)
    db.strokeWidth(0.5)
    for y in range(0, 1000, baseline):
        db.line((0, y), (800, y))
    db.stroke(None)
    
    # Title
    db.font("Helvetica-Bold")
    db.fontSize(24)
    db.fill(0)
    db.text("Modular Type Scale (1:1.5)", (margin, y_pos))
    
    # Type scale
    scales = ["Caption", "Body", "Subhead", "Title 3", "Title 2", "Title 1"]
    
    for i, label in enumerate(scales):
        size = round(base_size * (ratio ** i))
        y_pos -= baseline * max(3, int(size / baseline) + 1)
        
        # Snap to baseline
        y_pos = (y_pos // baseline) * baseline
        
        db.fontSize(size)
        db.font("Helvetica")
        
        # Label
        db.fill(0.5)
        db.fontSize(10)
        db.text(f"{label} ({size}pt)", (margin, y_pos + size + 4))
        
        # Sample text
        db.fill(0)
        db.fontSize(size)
        db.text("The quick brown fox jumps over the lazy dog", (margin, y_pos))

def solution_2():
    """Dynamic Logo System Solution"""
    sizes = [(16, 16), (64, 64), (200, 200)]
    
    for i, (w, h) in enumerate(sizes):
        db.newPage(300, 300)
        db.fill(0.95)
        db.rect(0, 0, 300, 300)
        
        # Center logo
        x = (300 - w) / 2
        y = (300 - h) / 2
        
        # Logo adapts based on size
        if w <= 16:
            # Minimal version - just a mark
            db.fill(0.2, 0.4, 0.8)
            db.rect(x, y, w, h)
        elif w <= 64:
            # Simplified version
            db.fill(0.2, 0.4, 0.8)
            db.rect(x, y, w/2, h)
            db.fill(0.8, 0.2, 0.4)
            db.rect(x + w/2, y, w/2, h/2)
        else:
            # Full version with details
            # Main shape
            db.fill(0.2, 0.4, 0.8)
            db.rect(x, y, w/2, h)
            
            # Secondary elements
            db.fill(0.8, 0.2, 0.4)
            db.rect(x + w/2, y + h/2, w/2, h/2)
            
            db.fill(0.3, 0.8, 0.3)
            db.oval(x + w/2, y, w/4, h/4)
            
            # Typography (only at large size)
            db.fill(1)
            db.font("Helvetica-Bold")
            db.fontSize(24)
            db.text("LOGO", (x + 20, y + 20))

def solution_3():
    """Data Visualization Solution"""
    db.newPage(800, 600)
    data = [45, 78, 23, 89, 56, 91, 34, 67]
    labels = ["A", "B", "C", "D", "E", "F", "G", "H"]
    
    # Background
    db.fill(0.98)
    db.rect(0, 0, 800, 600)
    
    # Chart settings
    margin = 60
    chart_width = 800 - 2 * margin
    chart_height = 400
    max_value = max(data)
    bar_width = chart_width / len(data) * 0.8
    gap = chart_width / len(data) * 0.2
    
    # Title
    db.font("Helvetica-Bold")
    db.fontSize(24)
    db.fill(0)
    db.text("Data Visualization", (margin, 550))
    
    # Draw axes
    db.stroke(0.3)
    db.strokeWidth(2)
    db.line((margin, 100), (margin, 500))
    db.line((margin, 100), (800 - margin, 100))
    
    # Draw bars
    for i, value in enumerate(data):
        x = margin + i * (bar_width + gap) + gap/2
        height = (value / max_value) * chart_height
        
        # Color based on value
        hue = 0.6 - (value / max_value) * 0.4
        r, g, b = colorsys.hsv_to_rgb(hue, 0.7, 0.9)
        db.fill(r, g, b)
        db.stroke(None)
        
        db.rect(x, 100, bar_width, height)
        
        # Value label
        db.fill(0)
        db.font("Helvetica")
        db.fontSize(12)
        db.text(str(value), (x + bar_width/2 - 10, 100 + height + 10))
        
        # Category label
        db.text(labels[i], (x + bar_width/2 - 5, 80))

def solution_4():
    """Generative Pattern Solution"""
    db.newPage(600, 600)
    random.seed(12345)
    
    # Background
    db.fill(0.1)
    db.rect(0, 0, 600, 600)
    
    # Grid for structure
    grid_size = 30
    
    for x in range(0, 600, grid_size):
        for y in range(0, 600, grid_size):
            # Random decision for each cell
            choice = random.random()
            
            with db.savedState():
                db.translate(x + grid_size/2, y + grid_size/2)
                
                if choice < 0.3:
                    # Circle
                    db.fill(0.9, 0.2, 0.3, 0.8)
                    size = random.uniform(10, 25)
                    db.oval(-size/2, -size/2, size, size)
                
                elif choice < 0.6:
                    # Rotated square
                    db.fill(0.2, 0.9, 0.4, 0.8)
                    db.rotate(random.uniform(0, 45))
                    size = random.uniform(15, 20)
                    db.rect(-size/2, -size/2, size, size)
                
                elif choice < 0.8:
                    # Line
                    db.stroke(0.9, 0.9, 0.2, 0.8)
                    db.strokeWidth(2)
                    db.rotate(random.choice([0, 45, 90, 135]))
                    db.line((-grid_size/2, 0), (grid_size/2, 0))
                    db.stroke(None)

def solution_5():
    """Magazine Layout Solution"""
    # Left page
    db.newPage(600, 800)
    
    # Background
    db.fill(1)
    db.rect(0, 0, 600, 800)
    
    # Large image placeholder
    db.fill(0.85)
    db.rect(0, 400, 600, 400)
    db.fill(0.5)
    db.font("Helvetica")
    db.fontSize(24)
    db.text("IMAGE", (250, 580))
    
    # Article title
    db.fill(0)
    db.font("Helvetica-Bold")
    db.fontSize(72)
    db.text("DESIGN", (60, 250))
    db.fontSize(64)
    db.text("THINKING", (60, 180))
    
    # Subtitle
    db.font("Helvetica")
    db.fontSize(18)
    db.fill(0.3)
    db.text("How creativity shapes our future", (60, 140))
    
    # Right page
    db.newPage(600, 800)
    
    # Background
    db.fill(1)
    db.rect(0, 0, 600, 800)
    
    # Three column layout
    columns = 3
    col_width = 160
    gutter = 20
    margin = 40
    
    # Drop cap
    db.font("Helvetica-Bold")
    db.fontSize(96)
    db.fill(0.9, 0.1, 0.1)
    db.text("W", (margin, 650))
    
    # Body text
    db.font("Helvetica")
    db.fontSize(11)
    db.fill(0)
    
    body_text = """hen we talk about design thinking, we're discussing more than just a methodology. It's a mindset that transforms how we approach problems and create solutions. This human-centered approach has revolutionized industries from technology to healthcare.

The process begins with empathy - understanding the people we're designing for. Through observation and conversation, we uncover needs that users themselves might not articulate. This deep understanding forms the foundation of innovative solutions.

Ideation follows, where quantity trumps quality. The goal is to generate numerous ideas without judgment, creating a rich pool of possibilities. From wild concepts to practical solutions, every idea has value in expanding our thinking."""
    
    # First column (with drop cap indent)
    db.textBox(body_text[:200], (margin + 60, 550, col_width - 60, 200))
    
    # Remaining columns
    db.textBox(body_text[200:400], (margin + col_width + gutter, 550, col_width, 200))
    db.textBox(body_text[400:], (margin + 2*(col_width + gutter), 550, col_width, 200))
    
    # Pull quote
    db.font("Helvetica-Bold")
    db.fontSize(24)
    db.fill(0.9, 0.1, 0.1)
    quote = "\"Design is not just what it looks like. Design is how it works.\""
    db.textBox(quote, (margin, 320, 520, 100))
    
    # Small images
    for i in range(3):
        x = margin + i * (col_width + gutter)
        db.fill(0.9)
        db.rect(x, 100, col_width, 120)

def solution_6():
    """Animation Sequence Solution"""
    frames = 10
    
    for frame in range(frames):
        db.newPage(400, 400)
        
        # Background
        db.fill(0.1)
        db.rect(0, 0, 400, 400)
        
        # Calculate morphing progress
        progress = frame / (frames - 1)
        
        # Center position
        cx, cy = 200, 200
        size = 150
        
        # Morph from square to circle
        # Use corner radius to create smooth transition
        corner_radius = size/2 * progress
        
        db.fill(0.2, 0.6, 1)
        
        # Draw morphing shape
        path = db.BezierPath()
        path.roundedRect(cx - size/2, cy - size/2, size, size, corner_radius)
        db.drawPath(path)
        
        # Rotating elements
        for i in range(8):
            angle = i * 45 + frame * 5
            with db.savedState():
                db.translate(cx, cy)
                db.rotate(angle)
                db.translate(100, 0)
                
                # Small circles that fade
                db.fill(1, 1, 1, 1 - progress * 0.5)
                db.oval(-5, -5, 10, 10)

def solution_7():
    """Color Harmony System Solution"""
    db.newPage(800, 1000)
    base_hue = 0.6  # Blue
    margin = 50
    
    # Background
    db.fill(0.98)
    db.rect(0, 0, 800, 1000)
    
    # Title
    db.font("Helvetica-Bold")
    db.fontSize(32)
    db.fill(0)
    db.text("Color Harmony System", (margin, 950))
    
    # Base color
    db.fontSize(18)
    db.text("Base Color", (margin, 850))
    r, g, b = colorsys.hsv_to_rgb(base_hue, 0.8, 0.9)
    db.fill(r, g, b)
    db.rect(margin, 800, 100, 40)
    
    # Analogous colors
    y_pos = 720
    db.fill(0)
    db.text("Analogous", (margin, y_pos + 40))
    for i in range(5):
        hue = (base_hue + (i - 2) * 0.083) % 1
        r, g, b = colorsys.hsv_to_rgb(hue, 0.8, 0.9)
        db.fill(r, g, b)
        db.rect(margin + i * 120, y_pos, 100, 40)
    
    # Complementary
    y_pos = 600
    db.fill(0)
    db.text("Complementary", (margin, y_pos + 40))
    comp_hue = (base_hue + 0.5) % 1
    
    r1, g1, b1 = colorsys.hsv_to_rgb(base_hue, 0.8, 0.9)
    r2, g2, b2 = colorsys.hsv_to_rgb(comp_hue, 0.8, 0.9)
    
    db.fill(r1, g1, b1)
    db.rect(margin, y_pos, 100, 40)
    db.fill(r2, g2, b2)
    db.rect(margin + 120, y_pos, 100, 40)
    
    # Triadic
    y_pos = 480
    db.fill(0)
    db.text("Triadic", (margin, y_pos + 40))
    for i in range(3):
        hue = (base_hue + i * 0.333) % 1
        r, g, b = colorsys.hsv_to_rgb(hue, 0.8, 0.9)
        db.fill(r, g, b)
        db.rect(margin + i * 120, y_pos, 100, 40)
    
    # Split complementary
    y_pos = 360
    db.fill(0)
    db.text("Split Complementary", (margin, y_pos + 40))
    split1 = (base_hue + 0.416) % 1
    split2 = (base_hue + 0.583) % 1
    
    for i, hue in enumerate([base_hue, split1, split2]):
        r, g, b = colorsys.hsv_to_rgb(hue, 0.8, 0.9)
        db.fill(r, g, b)
        db.rect(margin + i * 120, y_pos, 100, 40)
    
    # Tetradic (square)
    y_pos = 240
    db.fill(0)
    db.text("Tetradic", (margin, y_pos + 40))
    for i in range(4):
        hue = (base_hue + i * 0.25) % 1
        r, g, b = colorsys.hsv_to_rgb(hue, 0.8, 0.9)
        db.fill(r, g, b)
        db.rect(margin + i * 120, y_pos, 100, 40)

def solution_8():
    """Responsive Poster Solution"""
    # Three aspect ratios
    formats = [
        ("Mobile", 400, 700),
        ("Square", 600, 600),
        ("Wide", 800, 400)
    ]
    
    for name, width, height in formats:
        db.newPage(width, height)
        
        # Adaptive layout based on aspect ratio
        if height > width:  # Portrait
            # Vertical composition
            db.fill(0.1, 0.2, 0.8)
            db.rect(0, 0, width, height)
            
            # Title at top
            db.fill(1)
            db.font("Helvetica-Bold")
            db.fontSize(width / 10)
            db.text("ADAPT", (width * 0.1, height * 0.8))
            
            # Central element
            db.fill(0.9, 0.2, 0.3)
            size = width * 0.6
            db.oval((width - size)/2, height * 0.3, size, size)
            
        elif height == width:  # Square
            # Centered composition
            db.fill(0.8, 0.8, 0.2)
            db.rect(0, 0, width, height)
            
            # Diagonal text
            with db.savedState():
                db.translate(width/2, height/2)
                db.rotate(45)
                db.fill(0.1)
                db.font("Helvetica-Bold")
                db.fontSize(width / 8)
                db.text("ADAPT", (-width/4, 0))
            
            # Corner elements
            db.fill(0.1, 0.1, 0.1)
            for x, y in [(0, 0), (width-100, 0), (0, height-100), (width-100, height-100)]:
                db.rect(x, y, 100, 100)
                
        else:  # Landscape
            # Horizontal composition
            db.fill(0.2, 0.8, 0.4)
            db.rect(0, 0, width, height)
            
            # Text on left
            db.fill(0)
            db.font("Helvetica-Bold")
            db.fontSize(height / 4)
            db.text("ADAPT", (width * 0.05, height * 0.4))
            
            # Elements on right
            for i in range(3):
                db.fill(0.1, 0.1, 0.1, 0.3 + i * 0.2)
                size = height * 0.6
                x = width * 0.5 + i * size * 0.4
                y = (height - size) / 2
                db.oval(x, y, size, size)

def solution_9():
    """Custom Typography Solution"""
    db.newPage(800, 400)
    
    # Background
    db.fill(0.1)
    db.rect(0, 0, 800, 400)
    
    letters = "DESIGN"
    start_x = 50
    letter_width = 120
    
    for i, letter in enumerate(letters):
        x = start_x + i * letter_width
        y = 100
        
        with db.savedState():
            db.translate(x, y)
            
            if letter == "D":
                # D from circle and rectangle
                db.fill(0.9, 0.2, 0.2)
                db.rect(0, 0, 30, 100)
                db.oval(15, 0, 85, 100)
                db.fill(0.1)
                db.oval(30, 20, 45, 60)
                
            elif letter == "E":
                # E from rectangles
                db.fill(0.2, 0.9, 0.2)
                db.rect(0, 0, 30, 100)
                db.rect(0, 70, 80, 30)
                db.rect(0, 35, 60, 30)
                db.rect(0, 0, 80, 30)
                
            elif letter == "S":
                # S from circles
                db.fill(0.2, 0.2, 0.9)
                db.oval(0, 50, 50, 50)
                db.oval(30, 0, 50, 50)
                db.fill(0.1)
                db.rect(35, 55, 20, 20)
                db.rect(10, 25, 20, 20)
                
            elif letter == "I":
                # I from rectangles
                db.fill(0.9, 0.9, 0.2)
                db.rect(25, 0, 30, 100)
                db.rect(0, 70, 80, 30)
                db.rect(0, 0, 80, 30)
                
            elif letter == "G":
                # G from circle with cutout
                db.fill(0.9, 0.2, 0.9)
                db.oval(0, 0, 100, 100)
                db.fill(0.1)
                db.oval(20, 20, 60, 60)
                db.rect(50, 40, 50, 30)
                db.fill(0.9, 0.2, 0.9)
                db.rect(60, 0, 40, 40)
                
            elif letter == "N":
                # N from diagonal
                db.fill(0.2, 0.9, 0.9)
                db.rect(0, 0, 25, 100)
                db.rect(75, 0, 25, 100)
                # Diagonal
                with db.savedState():
                    db.translate(12, 0)
                    db.rotate(35)
                    db.rect(0, 0, 25, 120)

def solution_10():
    """Complex Grid System Solution"""
    db.newPage(1200, 800)
    
    # Background
    db.fill(0.95)
    db.rect(0, 0, 1200, 800)
    
    # Main grid: 12 columns
    margin = 20
    gutter = 20
    columns = 12
    
    content_width = 1200 - 2 * margin
    col_width = (content_width - (columns - 1) * gutter) / columns
    
    # Header
    header_height = 80
    db.fill(0.2, 0.3, 0.8)
    db.rect(margin, 800 - margin - header_height, content_width, header_height)
    
    # Logo
    db.fill(1)
    db.font("Helvetica-Bold")
    db.fontSize(24)
    db.text("DASHBOARD", (margin + 20, 800 - margin - 50))
    
    # Sidebar (3 columns)
    sidebar_width = col_width * 3 + gutter * 2
    sidebar_top = 800 - margin - header_height - gutter
    
    db.fill(0.25)
    db.rect(margin, margin, sidebar_width, sidebar_top - margin)
    
    # Sidebar items
    db.fill(0.35)
    for i in range(5):
        y = sidebar_top - 60 - i * 70
        db.rect(margin + 20, y, sidebar_width - 40, 50)
    
    # Main content area (9 columns)
    main_x = margin + sidebar_width + gutter
    main_width = col_width * 9 + gutter * 8
    
    # Sub-grid for widgets (3x2)
    widget_cols = 3
    widget_rows = 2
    widget_gutter = 20
    
    widget_width = (main_width - (widget_cols - 1) * widget_gutter) / widget_cols
    widget_height = (sidebar_top - margin - widget_gutter) / widget_rows
    
    # Draw widgets
    colors = [
        (0.9, 0.3, 0.3),
        (0.3, 0.9, 0.3),
        (0.3, 0.3, 0.9),
        (0.9, 0.9, 0.3),
        (0.9, 0.3, 0.9),
        (0.3, 0.9, 0.9)
    ]
    
    for row in range(widget_rows):
        for col in range(widget_cols):
            i = row * widget_cols + col
            x = main_x + col * (widget_width + widget_gutter)
            y = margin + row * (widget_height + widget_gutter)
            
            # Widget background
            db.fill(1)
            db.stroke(0.8)
            db.strokeWidth(1)
            db.rect(x, y, widget_width, widget_height)
            db.stroke(None)
            
            # Widget content
            if i < len(colors):
                db.fill(*colors[i], 0.2)
                db.rect(x + 20, y + 20, widget_width - 40, widget_height - 80)
                
                # Widget title
                db.fill(0.2)
                db.font("Helvetica-Bold")
                db.fontSize(16)
                db.text(f"Widget {i+1}", (x + 20, y + widget_height - 40))

# Uncomment to run specific solutions
# solution_1()
# solution_2()
# etc...

# Save output
db.saveImage("workbook_intermediate.pdf")
print("Intermediate exercises created!")