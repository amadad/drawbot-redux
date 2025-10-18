"""
Composition Rules in DrawBot
============================
Design Principle: Visual hierarchy, balance, rhythm, and emphasis
Historical Context: Based on principles from Bauhaus, Swiss Design, and Gestalt psychology
Key Concepts: Rule of thirds, golden ratio, symmetry, tension, white space
DrawBot Features Used: Mathematical positioning, transforms, visual guides
Parameters to Experiment With: ratios, angles, spacing, alignment
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

# Constants
GOLDEN_RATIO = 1.618
RULE_OF_THIRDS = 1/3
FIBONACCI = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def draw_composition_guides(width, height, guide_type="all"):
    """Draw various composition guides"""
    db.stroke(0.8, 0.2, 0.2, 0.3)
    db.strokeWidth(1)
    
    if guide_type in ["all", "thirds"]:
        # Rule of thirds
        db.stroke(0.8, 0.2, 0.2, 0.3)
        # Vertical lines
        db.line((width * RULE_OF_THIRDS, 0), (width * RULE_OF_THIRDS, height))
        db.line((width * 2 * RULE_OF_THIRDS, 0), (width * 2 * RULE_OF_THIRDS, height))
        # Horizontal lines
        db.line((0, height * RULE_OF_THIRDS), (width, height * RULE_OF_THIRDS))
        db.line((0, height * 2 * RULE_OF_THIRDS), (width, height * 2 * RULE_OF_THIRDS))
    
    if guide_type in ["all", "golden"]:
        # Golden ratio
        db.stroke(0.8, 0.6, 0, 0.3)
        golden_v = width / GOLDEN_RATIO
        golden_h = height / GOLDEN_RATIO
        db.line((golden_v, 0), (golden_v, height))
        db.line((width - golden_v, 0), (width - golden_v, height))
        db.line((0, golden_h), (width, golden_h))
        db.line((0, height - golden_h), (width, height - golden_h))
    
    if guide_type in ["all", "diagonal"]:
        # Diagonal guides
        db.stroke(0.2, 0.2, 0.8, 0.3)
        db.line((0, 0), (width, height))
        db.line((width, 0), (0, height))
    
    db.stroke(None)

def demonstrate_balance_types():
    """Show different types of visual balance"""
    page_width, page_height = 842, 595  # A4 Landscape
    margin = 40
    
    db.newPage(page_width, page_height)
    db.fill(0.98, 0.98, 0.98)
    db.rect(0, 0, page_width, page_height)
    
    # Title
    db.fill(0, 0, 0)
    db.font("Helvetica-Bold")
    db.fontSize(28)
    db.text("Types of Visual Balance", (margin, page_height - margin))
    
    # Setup for examples
    example_width = 180
    example_height = 180
    y_pos = page_height - 120
    
    # 1. Symmetrical Balance
    x_pos = margin
    db.fill(0, 0, 0)
    db.font("Helvetica-Bold")
    db.fontSize(14)
    db.text("Symmetrical", (x_pos, y_pos - example_height - 30))
    
    # Draw frame
    db.stroke(0.8, 0.8, 0.8)
    db.strokeWidth(1)
    db.fill(None)
    db.rect(x_pos, y_pos - example_height, example_width, example_height)
    
    # Symmetrical elements
    db.fill(0.2, 0.2, 0.2)
    db.rect(x_pos + 20, y_pos - 60, 60, 40)
    db.rect(x_pos + example_width - 80, y_pos - 60, 60, 40)
    db.rect(x_pos + 20, y_pos - 120, 60, 40)
    db.rect(x_pos + example_width - 80, y_pos - 120, 60, 40)
    
    # Center line
    db.stroke(0.8, 0.2, 0.2, 0.5)
    db.line((x_pos + example_width/2, y_pos - example_height), 
            (x_pos + example_width/2, y_pos))
    
    # 2. Asymmetrical Balance
    x_pos += example_width + 40
    db.stroke(None)
    db.fill(0, 0, 0)
    db.font("Helvetica-Bold")
    db.fontSize(14)
    db.text("Asymmetrical", (x_pos, y_pos - example_height - 30))
    
    # Draw frame
    db.stroke(0.8, 0.8, 0.8)
    db.fill(None)
    db.rect(x_pos, y_pos - example_height, example_width, example_height)
    
    # Asymmetrical but balanced elements
    db.fill(0.2, 0.2, 0.2)
    db.rect(x_pos + 20, y_pos - 100, 80, 80)  # Large element
    db.fill(0.5, 0.5, 0.5)
    db.rect(x_pos + 120, y_pos - 50, 30, 30)  # Small element far from center
    db.rect(x_pos + 110, y_pos - 140, 40, 20)  # Medium element
    db.fill(0.8, 0.8, 0.8)
    db.rect(x_pos + 130, y_pos - 100, 20, 40)  # Small light element
    
    # 3. Radial Balance
    x_pos += example_width + 40
    db.stroke(None)
    db.fill(0, 0, 0)
    db.font("Helvetica-Bold")
    db.fontSize(14)
    db.text("Radial", (x_pos, y_pos - example_height - 30))
    
    # Draw frame
    db.stroke(0.8, 0.8, 0.8)
    db.fill(None)
    db.rect(x_pos, y_pos - example_height, example_width, example_height)
    
    # Radial elements
    center_x = x_pos + example_width/2
    center_y = y_pos - example_height/2
    
    for i in range(8):
        angle = (i / 8) * math.pi * 2
        x = center_x + math.cos(angle) * 60
        y = center_y + math.sin(angle) * 60
        
        db.save()
        db.translate(x, y)
        db.rotate(math.degrees(angle))
        db.fill(0.2 + i * 0.08, 0.2 + i * 0.08, 0.2 + i * 0.08)
        db.rect(-15, -5, 30, 10)
        db.restore()
    
    # Center
    db.fill(0, 0, 0)
    db.oval(center_x - 10, center_y - 10, 20, 20)
    
    # 4. Crystallographic (All-over)
    x_pos += example_width + 40
    db.stroke(None)
    db.fill(0, 0, 0)
    db.font("Helvetica-Bold")
    db.fontSize(14)
    db.text("Crystallographic", (x_pos, y_pos - example_height - 30))
    
    # Draw frame
    db.stroke(0.8, 0.8, 0.8)
    db.fill(None)
    db.rect(x_pos, y_pos - example_height, example_width, example_height)
    
    # Pattern elements
    for row in range(6):
        for col in range(6):
            x = x_pos + 10 + col * 28
            y = y_pos - example_height + 10 + row * 28
            db.fill(0.3, 0.3, 0.3)
            db.oval(x, y, 20, 20)

def demonstrate_visual_hierarchy():
    """Show how to create clear visual hierarchy"""
    page_width, page_height = 595, 842
    margin = 50
    
    db.newPage(page_width, page_height)
    db.fill(1, 1, 1)
    db.rect(0, 0, page_width, page_height)
    
    # Title
    db.fill(0, 0, 0)
    db.font("Helvetica-Bold")
    db.fontSize(28)
    db.text("Visual Hierarchy Principles", (margin, page_height - margin))
    
    # Good example
    y_pos = page_height - 120
    column_width = (page_width - margin * 3) / 2
    
    db.fill(0, 0.6, 0)
    db.font("Helvetica")
    db.fontSize(14)
    db.text("GOOD: Clear Hierarchy", (margin, y_pos))
    
    y_pos -= 30
    # Primary element - largest, boldest
    db.fill(0, 0, 0)
    db.font("Helvetica-Bold")
    db.fontSize(36)
    db.text("Primary", (margin, y_pos))
    
    # Secondary element - medium size, less bold
    y_pos -= 50
    db.fill(0.3, 0.3, 0.3)
    db.font("Helvetica")
    db.fontSize(24)
    db.text("Secondary Element", (margin, y_pos))
    
    # Tertiary elements - smaller, lighter
    y_pos -= 40
    db.fill(0.5, 0.5, 0.5)
    db.fontSize(14)
    db.text("Supporting information that provides", (margin, y_pos))
    y_pos -= 18
    db.text("context and detail to the main elements.", (margin, y_pos))
    
    # Bad example
    y_pos = page_height - 120
    x_pos = margin * 2 + column_width
    
    db.fill(0.8, 0, 0)
    db.font("Helvetica")
    db.fontSize(14)
    db.text("BAD: Unclear Hierarchy", (x_pos, y_pos))
    
    y_pos -= 30
    # All elements similar size and weight
    db.fill(0, 0, 0)
    db.font("Helvetica")
    db.fontSize(18)
    db.text("Primary", (x_pos, y_pos))
    
    y_pos -= 30
    db.fontSize(18)
    db.text("Secondary Element", (x_pos, y_pos))
    
    y_pos -= 30
    db.fontSize(16)
    db.text("Supporting information that provides", (x_pos, y_pos))
    y_pos -= 20
    db.text("context and detail to the main elements.", (x_pos, y_pos))

def demonstrate_focal_points():
    """Show techniques for creating focal points"""
    page_width, page_height = 842, 595
    margin = 40
    
    db.newPage(page_width, page_height)
    db.fill(0.95, 0.95, 0.95)
    db.rect(0, 0, page_width, page_height)
    
    # Title
    db.fill(0, 0, 0)
    db.font("Helvetica-Bold")
    db.fontSize(28)
    db.text("Creating Focal Points", (margin, page_height - margin))
    
    # Examples grid
    example_size = 160
    techniques = [
        ("Contrast", lambda x, y: draw_contrast_focal(x, y, example_size)),
        ("Isolation", lambda x, y: draw_isolation_focal(x, y, example_size)),
        ("Convergence", lambda x, y: draw_convergence_focal(x, y, example_size)),
        ("Color", lambda x, y: draw_color_focal(x, y, example_size))
    ]
    
    y_pos = page_height - 120
    
    for i, (name, draw_func) in enumerate(techniques):
        x = margin + (i % 2) * (example_size + 60)
        y = y_pos - (i // 2) * (example_size + 80)
        
        # Label
        db.fill(0, 0, 0)
        db.font("Helvetica-Bold")
        db.fontSize(14)
        db.text(name, (x, y + 20))
        
        # Example
        draw_func(x, y - example_size)

def draw_contrast_focal(x, y, size):
    """Focal point through contrast"""
    # Light elements
    db.fill(0.8, 0.8, 0.8)
    for i in range(5):
        for j in range(5):
            if i == 2 and j == 2:
                continue
            db.rect(x + i * 32, y + j * 32, 25, 25)
    
    # Focal point - high contrast
    db.fill(0, 0, 0)
    db.rect(x + 2 * 32 - 5, y + 2 * 32 - 5, 35, 35)

def draw_isolation_focal(x, y, size):
    """Focal point through isolation"""
    # Grouped elements
    db.fill(0.5, 0.5, 0.5)
    for i in range(4):
        for j in range(4):
            db.rect(x + i * 20, y + j * 20, 15, 15)
    
    # Isolated focal point
    db.fill(0, 0, 0)
    db.oval(x + 110, y + 110, 30, 30)

def draw_convergence_focal(x, y, size):
    """Focal point through convergence"""
    # Converging lines
    center_x = x + size / 2
    center_y = y + size / 2
    
    db.stroke(0.6, 0.6, 0.6)
    db.strokeWidth(1)
    for angle in range(0, 360, 30):
        rad = math.radians(angle)
        x1 = center_x + math.cos(rad) * size / 2
        y1 = center_y + math.sin(rad) * size / 2
        db.line((x1, y1), (center_x, center_y))
    
    # Focal point
    db.stroke(None)
    db.fill(0, 0, 0)
    db.oval(center_x - 15, center_y - 15, 30, 30)

def draw_color_focal(x, y, size):
    """Focal point through color"""
    # Neutral elements
    db.fill(0.7, 0.7, 0.7)
    for i in range(5):
        for j in range(5):
            if i == 1 and j == 3:
                continue
            db.rect(x + i * 32, y + j * 32, 25, 25)
    
    # Colored focal point
    db.fill(0.9, 0.1, 0.1)
    db.rect(x + 1 * 32, y + 3 * 32, 25, 25)

def demonstrate_white_space():
    """Show the power of white space in composition"""
    page_width, page_height = 595, 842
    margin = 50
    
    db.newPage(page_width, page_height)
    db.fill(1, 1, 1)
    db.rect(0, 0, page_width, page_height)
    
    # Title
    db.fill(0, 0, 0)
    db.font("Helvetica-Bold")
    db.fontSize(28)
    db.text("The Power of White Space", (margin, page_height - margin))
    
    # Cramped example
    y_pos = page_height - 150
    db.fill(0.8, 0, 0)
    db.font("Helvetica")
    db.fontSize(14)
    db.text("Without White Space", (margin, y_pos))
    
    # Draw cramped layout
    y_pos -= 30
    db.stroke(0.8, 0.8, 0.8)
    db.strokeWidth(1)
    db.fill(None)
    db.rect(margin, y_pos - 200, 220, 200)
    
    # Cramped elements
    db.fill(0.3, 0.3, 0.3)
    for i in range(4):
        for j in range(4):
            db.rect(margin + 5 + i * 52, y_pos - 195 + j * 48, 50, 45)
    
    # Spacious example
    x_pos = margin + 300
    y_pos = page_height - 150
    db.fill(0, 0.6, 0)
    db.font("Helvetica")
    db.fontSize(14)
    db.text("With White Space", (x_pos, y_pos))
    
    # Draw spacious layout
    y_pos -= 30
    db.stroke(0.8, 0.8, 0.8)
    db.fill(None)
    db.rect(x_pos, y_pos - 200, 220, 200)
    
    # Spacious elements
    db.fill(0.3, 0.3, 0.3)
    positions = [(20, 20), (140, 40), (60, 100), (120, 140)]
    for px, py in positions:
        db.rect(x_pos + px, y_pos - 180 + py, 40, 30)
    
    # White space principles
    y_pos -= 250
    db.stroke(None)
    db.fill(0, 0, 0)
    db.font("Helvetica-Bold")
    db.fontSize(16)
    db.text("White Space Principles:", (margin, y_pos))
    
    principles = [
        "• Creates breathing room and reduces visual stress",
        "• Emphasizes important elements through isolation",
        "• Improves readability and comprehension",
        "• Conveys elegance and sophistication",
        "• Groups related elements and separates unrelated ones"
    ]
    
    db.font("Helvetica")
    db.fontSize(12)
    y_pos -= 25
    for principle in principles:
        db.text(principle, (margin, y_pos))
        y_pos -= 20

def demonstrate_movement_and_rhythm():
    """Show how to create visual movement and rhythm"""
    page_width, page_height = 842, 595
    margin = 40
    
    db.newPage(page_width, page_height)
    db.fill(0.98, 0.98, 0.98)
    db.rect(0, 0, page_width, page_height)
    
    # Title
    db.fill(0, 0, 0)
    db.font("Helvetica-Bold")
    db.fontSize(28)
    db.text("Movement & Rhythm", (margin, page_height - margin))
    
    # Regular rhythm
    y_pos = page_height - 120
    db.font("Helvetica-Bold")
    db.fontSize(14)
    db.text("Regular Rhythm", (margin, y_pos))
    
    y_pos -= 40
    db.fill(0.3, 0.3, 0.3)
    for i in range(8):
        db.rect(margin + i * 40, y_pos, 30, 40)
    
    # Progressive rhythm
    y_pos -= 100
    db.fill(0, 0, 0)
    db.text("Progressive Rhythm", (margin, y_pos))
    
    y_pos -= 40
    db.fill(0.3, 0.3, 0.3)
    x = margin
    for i in range(8):
        size = 20 + i * 5
        db.rect(x, y_pos, size, size)
        x += size + 10
    
    # Flowing rhythm
    y_pos -= 100
    db.fill(0, 0, 0)
    db.text("Flowing Rhythm", (margin, y_pos))
    
    y_pos -= 40
    db.stroke(0.3, 0.3, 0.3)
    db.strokeWidth(3)
    db.fill(None)
    path = db.BezierPath()
    path.moveTo((margin, y_pos + 20))
    for i in range(1, 8):
        x = margin + i * 80
        y = y_pos + 20 + math.sin(i * 0.8) * 30
        path.curveTo(
            (x - 40, y - 20),
            (x - 40, y + 20),
            (x, y)
        )
    db.drawPath(path)
    
    # Alternating rhythm
    y_pos -= 100
    db.stroke(None)
    db.fill(0, 0, 0)
    db.text("Alternating Rhythm", (margin, y_pos))
    
    y_pos -= 40
    for i in range(8):
        if i % 2 == 0:
            db.fill(0.3, 0.3, 0.3)
            db.rect(margin + i * 40, y_pos, 30, 50)
        else:
            db.fill(0.7, 0.7, 0.7)
            db.oval(margin + i * 40 + 5, y_pos + 10, 20, 20)

# Main execution
if __name__ == "__main__":
    demonstrate_balance_types()
    demonstrate_visual_hierarchy()
    demonstrate_focal_points()
    demonstrate_white_space()
    demonstrate_movement_and_rhythm()
    
    db.saveImage("composition_rules.pdf")
    print("Composition rules guide created successfully!")