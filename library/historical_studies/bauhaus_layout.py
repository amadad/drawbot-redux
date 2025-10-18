"""
Bauhaus Layout Study
====================
Design Principle: Form follows function, geometric abstraction, primary colors
Historical Context: 1919-1933 Germany, Walter Gropius, László Moholy-Nagy, Herbert Bayer
Key Concepts: Geometric shapes, asymmetry, photomontage, experimental typography
DrawBot Features Used: Basic shapes, rotations, primary colors, custom type arrangements
Study Reference: Bauhaus exhibition posters and publication designs
"""

import math

# Import DrawBot
try:
    import drawBot as db
except ImportError:
    import sys
    import os
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    sys.path.insert(0, project_root)
    import drawBot as db

# Bauhaus Color Palette
BAUHAUS_RED = (0.87, 0.13, 0.13)
BAUHAUS_BLUE = (0.13, 0.33, 0.61)
BAUHAUS_YELLOW = (0.98, 0.76, 0.09)
BLACK = (0, 0, 0)
WHITE = (1, 1, 1)
GRAY = (0.7, 0.7, 0.7)

def draw_bauhaus_circle(x, y, radius, segments=3):
    """Draw a Bauhaus-style segmented circle"""
    colors = [BAUHAUS_RED, BAUHAUS_BLUE, BAUHAUS_YELLOW]
    
    for i in range(segments):
        start_angle = (i / segments) * 360
        end_angle = ((i + 1) / segments) * 360
        
        db.fill(*colors[i % len(colors)])
        
        path = db.BezierPath()
        path.moveTo((x, y))
        
        # Draw arc
        for angle in range(int(start_angle), int(end_angle) + 1):
            rad = math.radians(angle)
            px = x + radius * math.cos(rad)
            py = y + radius * math.sin(rad)
            if angle == int(start_angle):
                path.lineTo((px, py))
            else:
                path.lineTo((px, py))
        
        path.closePath()
        db.drawPath(path)

def recreate_bauhaus_poster():
    """Recreate a classic Bauhaus exhibition poster style"""
    width, height = 420, 594  # A2
    
    db.newPage(width, height)
    
    # Background
    db.fill(0.95, 0.95, 0.95)
    db.rect(0, 0, width, height)
    
    # Geometric composition
    # Large circle
    draw_bauhaus_circle(width * 0.7, height * 0.7, 120)
    
    # Overlapping rectangle
    db.fill(*BAUHAUS_RED)
    db.save()
    db.translate(width * 0.3, height * 0.5)
    db.rotate(25)
    db.rect(-80, -60, 160, 120)
    db.restore()
    
    # Triangle
    db.fill(*BAUHAUS_BLUE)
    triangle = db.BezierPath()
    triangle.moveTo((width * 0.2, height * 0.3))
    triangle.lineTo((width * 0.4, height * 0.3))
    triangle.lineTo((width * 0.3, height * 0.5))
    triangle.closePath()
    db.drawPath(triangle)
    
    # Typography - experimental layout
    db.fill(*BLACK)
    
    # "BAUHAUS" vertically
    db.save()
    db.translate(60, height - 100)
    db.rotate(-90)
    db.font("Helvetica-Bold")  # Would use custom Bauhaus font if available
    db.fontSize(72)
    db.text("BAUHAUS", (0, 0))
    db.restore()
    
    # "AUSSTELLUNG" diagonally
    db.save()
    db.translate(width * 0.5, height * 0.3)
    db.rotate(45)
    db.fontSize(24)
    db.text("AUSSTELLUNG", (0, 0))
    db.restore()
    
    # Date in corner
    db.font("Helvetica")
    db.fontSize(14)
    db.text("1923", (width - 80, 40))
    
    # Grid lines as design element
    db.stroke(*GRAY, 0.5)
    db.strokeWidth(1)
    for i in range(0, width, 40):
        db.line((i, 0), (i + 200, height))
    db.stroke(None)

def create_herbert_bayer_style():
    """Create a poster in Herbert Bayer's universal typography style"""
    width, height = 420, 594
    
    db.newPage(width, height)
    
    # White background
    db.fill(*WHITE)
    db.rect(0, 0, width, height)
    
    # Geometric elements
    # Red circle
    db.fill(*BAUHAUS_RED)
    db.oval(width - 150, height - 200, 120, 120)
    
    # Blue square
    db.fill(*BAUHAUS_BLUE)
    db.rect(50, height - 300, 100, 100)
    
    # Yellow triangle
    db.fill(*BAUHAUS_YELLOW)
    triangle = db.BezierPath()
    triangle.moveTo((width/2 - 60, 100))
    triangle.lineTo((width/2 + 60, 100))
    triangle.lineTo((width/2, 220))
    triangle.closePath()
    db.drawPath(triangle)
    
    # Typography - all lowercase (Bayer's universal alphabet concept)
    db.fill(*BLACK)
    db.font("Helvetica-Bold")
    
    # Main text
    db.fontSize(64)
    db.text("universal", (50, height/2))
    
    db.fontSize(48)
    db.text("type", (50, height/2 - 70))
    
    # Diagonal text
    db.save()
    db.translate(width - 100, height/2 - 100)
    db.rotate(-45)
    db.fontSize(24)
    db.text("herbert bayer", (0, 0))
    db.restore()
    
    # Connecting lines
    db.stroke(*BLACK)
    db.strokeWidth(2)
    db.line((50, height/2 + 20), (width - 150, height - 200))
    db.line((150, height - 250), (width/2, 160))
    db.stroke(None)

def demonstrate_bauhaus_principles():
    """Show key Bauhaus design principles"""
    width, height = 595, 842  # A4
    
    db.newPage(width, height)
    db.fill(*WHITE)
    db.rect(0, 0, width, height)
    
    margin = 50
    
    # Title
    db.fill(*BLACK)
    db.font("Helvetica-Bold")
    db.fontSize(32)
    db.text("Bauhaus Design Principles", (margin, height - margin))
    
    # 1. Primary shapes and colors
    y_section = height - 150
    db.fontSize(18)
    db.text("1. Primary Forms & Colors", (margin, y_section))
    
    y_example = y_section - 80
    
    # Circle
    db.fill(*BAUHAUS_RED)
    db.oval(margin, y_example, 60, 60)
    
    # Square
    db.fill(*BAUHAUS_BLUE)
    db.rect(margin + 80, y_example, 60, 60)
    
    # Triangle
    db.fill(*BAUHAUS_YELLOW)
    triangle = db.BezierPath()
    triangle.moveTo((margin + 160, y_example))
    triangle.lineTo((margin + 220, y_example))
    triangle.lineTo((margin + 190, y_example + 60))
    triangle.closePath()
    db.drawPath(triangle)
    
    # 2. Geometric construction
    y_section -= 180
    db.fill(*BLACK)
    db.fontSize(18)
    db.text("2. Geometric Construction", (margin, y_section))
    
    y_example = y_section - 80
    
    # Show construction lines
    db.stroke(*GRAY)
    db.strokeWidth(0.5)
    # Grid
    for i in range(5):
        x = margin + i * 30
        db.line((x, y_example), (x, y_example + 90))
    for i in range(4):
        y = y_example + i * 30
        db.line((margin, y), (margin + 120, y))
    
    # Constructed form
    db.stroke(None)
    db.fill(*BLACK, 0.8)
    db.rect(margin + 15, y_example + 15, 30, 60)
    db.rect(margin + 60, y_example + 30, 45, 30)
    
    # 3. Asymmetric balance
    y_section -= 180
    db.fontSize(18)
    db.text("3. Dynamic Asymmetry", (margin, y_section))
    
    y_example = y_section - 80
    
    # Asymmetric composition
    db.fill(*BAUHAUS_RED)
    db.rect(margin, y_example + 50, 80, 30)
    
    db.fill(*BAUHAUS_BLUE)
    db.rect(margin + 100, y_example, 30, 80)
    
    db.fill(*BAUHAUS_YELLOW)
    db.oval(margin + 140, y_example + 60, 20, 20)
    
    # Right column examples
    x_section = width / 2 + 20
    
    # 4. Typography experiments
    y_section = height - 330
    db.fill(*BLACK)
    db.fontSize(18)
    db.text("4. Experimental Typography", (x_section, y_section))
    
    y_example = y_section - 40
    
    # Rotated text
    db.save()
    db.translate(x_section + 50, y_example)
    db.rotate(90)
    db.fontSize(24)
    db.text("VERTICAL", (0, 0))
    db.restore()
    
    # Diagonal text
    db.save()
    db.translate(x_section + 100, y_example - 20)
    db.rotate(-30)
    db.fontSize(20)
    db.text("diagonal", (0, 0))
    db.restore()
    
    # 5. Function and form
    y_section -= 180
    db.fontSize(18)
    db.text("5. Form Follows Function", (x_section, y_section))
    
    y_example = y_section - 60
    
    # Functional layout example
    db.stroke(*BLACK)
    db.strokeWidth(1)
    db.fill(None)
    
    # Container
    db.rect(x_section, y_example, 180, 80)
    
    # Functional divisions
    db.line((x_section + 60, y_example), (x_section + 60, y_example + 80))
    db.line((x_section + 120, y_example), (x_section + 120, y_example + 80))
    
    # Labels
    db.stroke(None)
    db.fill(*BLACK)
    db.fontSize(10)
    db.text("INHALT", (x_section + 5, y_example + 35))
    db.text("FORM", (x_section + 65, y_example + 35))
    db.text("FARBE", (x_section + 125, y_example + 35))

def create_moholy_nagy_composition():
    """Create a composition inspired by László Moholy-Nagy"""
    width, height = 500, 500  # Square format
    
    db.newPage(width, height)
    
    # Black background
    db.fill(*BLACK)
    db.rect(0, 0, width, height)
    
    # Photogram-inspired elements
    # Transparent overlapping circles
    for i in range(5):
        x = 100 + i * 60
        y = height/2 + math.sin(i) * 100
        size = 80 + i * 20
        
        db.fill(1, 1, 1, 0.2)
        db.oval(x - size/2, y - size/2, size, size)
    
    # Geometric grid overlay
    db.stroke(1, 1, 1, 0.3)
    db.strokeWidth(1)
    
    # Diagonal lines
    for i in range(-5, 15):
        x1 = i * 50
        db.line((x1, 0), (x1 + height, height))
    
    # Constructivist elements
    db.stroke(None)
    
    # Red diagonal bar
    db.fill(*BAUHAUS_RED, 0.8)
    db.save()
    db.translate(width * 0.3, height * 0.7)
    db.rotate(-45)
    db.rect(-150, -20, 300, 40)
    db.restore()
    
    # Blue triangle
    db.fill(*BAUHAUS_BLUE, 0.7)
    triangle = db.BezierPath()
    triangle.moveTo((width * 0.7, height * 0.2))
    triangle.lineTo((width * 0.9, height * 0.4))
    triangle.lineTo((width * 0.7, height * 0.4))
    triangle.closePath()
    db.drawPath(triangle)
    
    # Typography
    db.fill(*WHITE)
    db.font("Helvetica-Bold")
    db.fontSize(48)
    
    # Experimental positioning
    db.save()
    db.translate(width * 0.2, height * 0.3)
    db.rotate(90)
    db.text("LICHT", (0, 0))
    db.restore()
    
    db.save()
    db.translate(width * 0.8, height * 0.8)
    db.rotate(-90)
    db.text("RAUM", (0, 0))
    db.restore()

def create_bauhaus_color_study():
    """Create a color theory study in Bauhaus style"""
    width, height = 595, 842
    
    db.newPage(width, height)
    db.fill(0.9, 0.9, 0.9)
    db.rect(0, 0, width, height)
    
    margin = 50
    
    # Title
    db.fill(*BLACK)
    db.font("Helvetica-Bold")
    db.fontSize(32)
    db.text("Bauhaus Color Theory", (margin, height - margin))
    
    # Johannes Itten color wheel recreation
    center_x = width / 2
    center_y = height / 2 + 100
    
    # Primary colors - center triangle
    radius = 80
    for i in range(3):
        angle = i * 120 - 90  # Start from top
        rad = math.radians(angle)
        x = center_x + radius * math.cos(rad)
        y = center_y + radius * math.sin(rad)
        
        if i == 0:
            color = BAUHAUS_YELLOW
        elif i == 1:
            color = BAUHAUS_RED
        else:
            color = BAUHAUS_BLUE
        
        # Draw triangle section
        path = db.BezierPath()
        path.moveTo((center_x, center_y))
        path.lineTo((x, y))
        
        next_angle = (i + 1) * 120 - 90
        next_rad = math.radians(next_angle)
        next_x = center_x + radius * math.cos(next_rad)
        next_y = center_y + radius * math.sin(next_rad)
        path.lineTo((next_x, next_y))
        path.closePath()
        
        db.fill(*color)
        db.drawPath(path)
    
    # Secondary colors - outer triangles
    outer_radius = 150
    
    # Color mixing demonstrations
    y_pos = height - 300
    
    # Show color mixing
    db.fontSize(16)
    db.fill(*BLACK)
    db.text("Primary Color Mixing:", (margin, y_pos))
    
    y_pos -= 40
    
    # Red + Yellow = Orange
    db.fill(*BAUHAUS_RED)
    db.oval(margin, y_pos, 30, 30)
    db.fill(*BLACK)
    db.text("+", (margin + 40, y_pos + 5))
    db.fill(*BAUHAUS_YELLOW)
    db.oval(margin + 60, y_pos, 30, 30)
    db.fill(*BLACK)
    db.text("=", (margin + 100, y_pos + 5))
    db.fill(1, 0.5, 0)  # Orange
    db.oval(margin + 120, y_pos, 30, 30)
    
    # Continue with other mixtures...

# Main execution
if __name__ == "__main__":
    recreate_bauhaus_poster()
    create_herbert_bayer_style()
    demonstrate_bauhaus_principles()
    create_moholy_nagy_composition()
    create_bauhaus_color_study()
    
    db.saveImage("bauhaus_layout.pdf")
    print("Bauhaus layout study created successfully!")