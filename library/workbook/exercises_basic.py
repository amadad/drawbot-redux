"""
Basic DrawBot Exercises
=======================
A collection of exercises to practice fundamental DrawBot concepts.
Complete each exercise and check your work against the solutions.

Exercise Format:
- Each exercise has a clear goal
- Hints are provided
- Solutions are at the bottom (no peeking!)
"""

import sys
import os

# Add the project root to Python path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import drawBot as db

# EXERCISE 1: Centered Circle
# Goal: Draw a red circle in the exact center of a 500x500 canvas
# Hint: Remember that oval() uses x, y, width, height

def exercise_1():
    """Your code here"""
    db.newPage(500, 500)
    # TODO: Draw a red circle (diameter 200) centered on the page
    pass

# EXERCISE 2: Color Gradient
# Goal: Create 10 squares in a row, each progressively darker
# Hint: Use a loop and calculate gray value based on loop index

def exercise_2():
    """Your code here"""
    db.newPage(600, 200)
    # TODO: Draw 10 squares (50x50) with gradient from white to black
    pass

# EXERCISE 3: Concentric Circles
# Goal: Draw 5 concentric circles with alternating colors (red/blue)
# Hint: Start with the largest circle and work inward

def exercise_3():
    """Your code here"""
    db.newPage(400, 400)
    # TODO: Draw 5 concentric circles, alternating red and blue
    pass

# EXERCISE 4: Typography Hierarchy
# Goal: Create a text hierarchy with 3 levels (Title, Subtitle, Body)
# Requirements: Different sizes, weights, and proper spacing

def exercise_4():
    """Your code here"""
    db.newPage(600, 800)
    # TODO: Create typography hierarchy
    # Title: 36pt, Bold
    # Subtitle: 24pt, Regular
    # Body: 14pt, Regular
    pass

# EXERCISE 5: Grid of Shapes
# Goal: Create a 4x4 grid of shapes with pattern
# Make every other shape a different color

def exercise_5():
    """Your code here"""
    db.newPage(400, 400)
    # TODO: Create 4x4 grid with alternating colored shapes
    pass

# EXERCISE 6: Basic Animation
# Goal: Create 5 frames showing a ball moving across the screen
# Hint: Use a loop to create pages with ball at different positions

def exercise_6():
    """Your code here"""
    # TODO: Create 5 frames of animation
    pass

# EXERCISE 7: Color Wheel
# Goal: Create a simple color wheel using HSB color space
# Hint: Use a loop to rotate hue values

def exercise_7():
    """Your code here"""
    db.newPage(500, 500)
    # TODO: Draw color wheel segments
    pass

# EXERCISE 8: Text on Path
# Goal: Draw text following a circular path
# Hint: Use rotate() and translate() transforms

def exercise_8():
    """Your code here"""
    db.newPage(500, 500)
    # TODO: Draw text in a circle
    pass

# EXERCISE 9: Pattern Design
# Goal: Create a repeating geometric pattern
# Use at least 3 different shapes

def exercise_9():
    """Your code here"""
    db.newPage(600, 600)
    # TODO: Create repeating pattern
    pass

# EXERCISE 10: Composition
# Goal: Create a balanced composition using the rule of thirds
# Include at least one large element and several small ones

def exercise_10():
    """Your code here"""
    db.newPage(600, 800)
    # TODO: Create balanced composition
    pass

# ========== SOLUTIONS BELOW - NO PEEKING! ==========
# ===================================================

def solution_1():
    """Centered Circle Solution"""
    db.newPage(500, 500)
    db.fill(1, 0, 0)  # Red
    # Center at 250, 250 with diameter 200
    db.oval(150, 150, 200, 200)

def solution_2():
    """Color Gradient Solution"""
    db.newPage(600, 200)
    for i in range(10):
        gray = 1 - (i / 9)  # From 1 (white) to 0 (black)
        db.fill(gray)
        db.rect(i * 60, 75, 50, 50)

def solution_3():
    """Concentric Circles Solution"""
    db.newPage(400, 400)
    center_x, center_y = 200, 200
    for i in range(5):
        radius = 180 - (i * 35)
        if i % 2 == 0:
            db.fill(1, 0, 0)  # Red
        else:
            db.fill(0, 0, 1)  # Blue
        db.oval(center_x - radius, center_y - radius, radius * 2, radius * 2)

def solution_4():
    """Typography Hierarchy Solution"""
    db.newPage(600, 800)
    margin = 50
    y_pos = 750
    
    # Title
    db.font("Helvetica-Bold")
    db.fontSize(36)
    db.text("Design Systems", (margin, y_pos))
    
    # Subtitle
    y_pos -= 50
    db.font("Helvetica")
    db.fontSize(24)
    db.text("Building Consistent Visual Language", (margin, y_pos))
    
    # Body
    y_pos -= 60
    db.fontSize(14)
    body_text = """A design system is a collection of reusable components,
guided by clear standards, that can be assembled together
to build any number of applications. It ensures consistency
and scalability across all products."""
    db.textBox(body_text, (margin, y_pos - 100, 500, 100))

def solution_5():
    """Grid of Shapes Solution"""
    db.newPage(400, 400)
    size = 80
    padding = 20
    
    for row in range(4):
        for col in range(4):
            x = padding + col * (size + padding)
            y = padding + row * (size + padding)
            
            # Checkerboard pattern
            if (row + col) % 2 == 0:
                db.fill(0.2, 0.4, 0.8)
            else:
                db.fill(0.8, 0.2, 0.4)
            
            db.rect(x, y, size, size)

def solution_6():
    """Basic Animation Solution"""
    ball_size = 50
    for frame in range(5):
        db.newPage(500, 200)
        db.fill(0.95)
        db.rect(0, 0, 500, 200)
        
        # Calculate ball position
        x = 50 + (frame * 100)
        y = 75
        
        # Draw ball
        db.fill(1, 0, 0)
        db.oval(x, y, ball_size, ball_size)

def solution_7():
    """Color Wheel Solution"""
    import colorsys
    
    db.newPage(500, 500)
    center_x, center_y = 250, 250
    segments = 12
    
    for i in range(segments):
        angle = i * (360 / segments)
        hue = i / segments
        
        # Convert HSB to RGB
        r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
        db.fill(r, g, b)
        
        # Draw wedge using path
        with db.savedState():
            db.translate(center_x, center_y)
            db.rotate(angle)
            
            path = db.BezierPath()
            path.moveTo((0, 0))
            path.lineTo((200, 0))
            path.arc((0, 0), radius=200, startAngle=0, endAngle=360/segments, clockwise=False)
            path.closePath()
            db.drawPath(path)

def solution_8():
    """Text on Path Solution"""
    db.newPage(500, 500)
    center_x, center_y = 250, 250
    radius = 150
    text = "CIRCULAR TEXT EXAMPLE • "
    
    db.font("Helvetica-Bold")
    db.fontSize(16)
    
    # Calculate angle per character
    angle_per_char = 360 / len(text)
    
    for i, char in enumerate(text):
        with db.savedState():
            db.translate(center_x, center_y)
            db.rotate(i * angle_per_char)
            db.translate(radius, 0)
            db.rotate(90)  # Orient text outward
            db.text(char, (0, 0), align="center")

def solution_9():
    """Pattern Design Solution"""
    db.newPage(600, 600)
    
    # Create a module that repeats
    module_size = 60
    
    for row in range(10):
        for col in range(10):
            x = col * module_size
            y = row * module_size
            
            with db.savedState():
                db.translate(x + module_size/2, y + module_size/2)
                
                # Circle
                db.fill(0.2, 0.4, 0.8)
                db.oval(-20, -20, 40, 40)
                
                # Rotated squares
                db.fill(0.8, 0.2, 0.4)
                db.rotate(45)
                db.rect(-15, -15, 30, 30)
                
                # Small circles at corners
                db.fill(0.9, 0.9, 0)
                for angle in [0, 90, 180, 270]:
                    with db.savedState():
                        db.rotate(angle)
                        db.translate(25, 0)
                        db.oval(-5, -5, 10, 10)

def solution_10():
    """Composition Solution"""
    db.newPage(600, 800)
    
    # Rule of thirds grid (invisible)
    third_x = 600 / 3
    third_y = 800 / 3
    
    # Background
    db.fill(0.95)
    db.rect(0, 0, 600, 800)
    
    # Large element at intersection
    db.fill(0.2, 0.3, 0.8)
    db.oval(third_x - 80, third_y * 2 - 80, 160, 160)
    
    # Medium elements
    db.fill(0.8, 0.2, 0.3)
    db.rect(third_x * 2 - 40, third_y - 40, 80, 80)
    
    # Small elements for balance
    db.fill(0.3, 0.8, 0.3)
    for i in range(3):
        x = 50 + i * 80
        y = 50
        db.oval(x, y, 30, 30)
    
    # Line element
    db.stroke(0.2)
    db.strokeWidth(3)
    db.line((0, third_y), (600, third_y))
    db.stroke(None)

# To run solutions, uncomment and run:
# solution_1()
# solution_2()
# ... etc

# Save your work
db.saveImage("workbook_exercises.pdf")
print("Exercises created! Try solving them before looking at solutions.")