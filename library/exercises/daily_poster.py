"""
Daily Poster Exercise
=====================
Practice exercise: Create a poster every day with constraints
This helps develop quick decision-making and creative problem-solving
"""

import random
from datetime import datetime
import sys
import os
import math

# Import DrawBot
try:
    import drawBot as db
except ImportError:
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    sys.path.insert(0, project_root)
    import drawBot as db

# Add parent directory to path to import design_systems
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.design_systems import *

# Daily constraints generator
def get_daily_constraints():
    """Generate random constraints for today's poster"""
    # Use date as seed for consistent daily challenge
    today = datetime.now().strftime("%Y%m%d")
    random.seed(int(today))
    
    # Constraint options
    colors = [
        ["black", "white"],
        ["black", "white", "red"],
        ["blue", "yellow"],
        ["complementary"],
        ["monochromatic"],
        ["analogous"]
    ]
    
    themes = [
        "rhythm",
        "contrast",
        "balance",
        "movement",
        "hierarchy",
        "space",
        "tension",
        "harmony",
        "chaos",
        "order"
    ]
    
    shapes = [
        ["circles only"],
        ["rectangles only"],
        ["triangles only"],
        ["mixed geometric"],
        ["organic curves"],
        ["lines only"]
    ]
    
    typography = [
        "sans-serif only",
        "all lowercase",
        "ALL CAPS",
        "single word",
        "number focus",
        "no text"
    ]
    
    return {
        "date": today,
        "color_scheme": random.choice(colors),
        "theme": random.choice(themes),
        "shapes": random.choice(shapes),
        "typography": random.choice(typography),
        "grid": random.choice([3, 4, 6, 8, 12])
    }

def create_daily_poster(constraints=None):
    """Create a poster based on daily constraints"""
    if constraints is None:
        constraints = get_daily_constraints()
    
    # Setup
    width, height = 420, 594  # A2
    margin = 40
    
    db.newPage(width, height)
    
    # Background
    db.fill(1, 1, 1)
    db.rect(0, 0, width, height)
    
    # Set up grid
    grid = column_grid(width, height, constraints["grid"], 20, margin)
    
    # Interpret color scheme
    if constraints["color_scheme"] == ["black", "white"]:
        colors = [(0, 0, 0), (1, 1, 1)]
    elif constraints["color_scheme"] == ["black", "white", "red"]:
        colors = [(0, 0, 0), (1, 1, 1), (0.9, 0.1, 0.1)]
    elif constraints["color_scheme"] == ["blue", "yellow"]:
        colors = [(0.1, 0.3, 0.8), (1, 0.8, 0)]
    elif constraints["color_scheme"] == ["complementary"]:
        base = (random.random(), random.random(), random.random())
        colors = color_palette_generator(base, "complementary", 3)
    elif constraints["color_scheme"] == ["monochromatic"]:
        base = (random.random(), random.random(), random.random())
        colors = color_palette_generator(base, "monochromatic", 4)
    else:  # analogous
        base = (random.random(), random.random(), random.random())
        colors = color_palette_generator(base, "analogous", 4)
    
    # Create composition based on theme
    if constraints["theme"] == "rhythm":
        create_rhythm_composition(width, height, margin, colors, constraints)
    elif constraints["theme"] == "contrast":
        create_contrast_composition(width, height, margin, colors, constraints)
    elif constraints["theme"] == "balance":
        create_balance_composition(width, height, margin, colors, constraints)
    elif constraints["theme"] == "movement":
        create_movement_composition(width, height, margin, colors, constraints)
    else:
        create_random_composition(width, height, margin, colors, constraints)
    
    # Add constraint info
    db.fill(0.7, 0.7, 0.7)
    db.font("Helvetica")
    db.fontSize(8)
    info = f"Date: {constraints['date']} | Theme: {constraints['theme']} | Grid: {constraints['grid']} | {constraints['typography']}"
    db.text(info, (margin, 10))

def create_rhythm_composition(width, height, margin, colors, constraints):
    """Create a composition focusing on rhythm"""
    # Repeating elements with variation
    element_size = 40
    
    for i in range(5):
        for j in range(8):
            x = margin + i * (width - 2 * margin) / 4
            y = margin + j * (height - 2 * margin) / 7
            
            # Size variation creates rhythm
            size = element_size * (1 + math.sin(i * 0.5 + j * 0.3) * 0.5)
            
            db.fill(*random.choice(colors))
            
            if "circles" in constraints["shapes"][0]:
                db.oval(x - size/2, y - size/2, size, size)
            elif "rectangles" in constraints["shapes"][0]:
                db.rect(x - size/2, y - size/2, size, size * 0.8)
            elif "triangles" in constraints["shapes"][0]:
                draw_triangle(x, y, size)

def create_contrast_composition(width, height, margin, colors, constraints):
    """Create a composition focusing on contrast"""
    # Large vs small, dark vs light
    
    # Large dominant element
    db.fill(*colors[0])
    if "circles" in constraints["shapes"][0]:
        db.oval(margin, height/2 - 150, 300, 300)
    else:
        db.rect(margin, height/2 - 150, 300, 300)
    
    # Small contrasting elements
    for i in range(20):
        x = random.randint(int(margin + 320), int(width - margin - 20))
        y = random.randint(int(margin), int(height - margin - 20))
        
        db.fill(*colors[-1])
        if "circles" in constraints["shapes"][0]:
            db.oval(x, y, 20, 20)
        else:
            db.rect(x, y, 20, 20)

def create_balance_composition(width, height, margin, colors, constraints):
    """Create a composition focusing on balance"""
    # Asymmetric balance
    
    # Large element on one side
    db.fill(*colors[0], 0.8)
    large_size = 200
    db.rect(margin, height - margin - large_size - 100, large_size, large_size)
    
    # Multiple smaller elements to balance
    small_size = 50
    x_start = width - margin - small_size * 3
    
    for i in range(3):
        for j in range(4):
            db.fill(*colors[(i + j) % len(colors)], 0.8)
            x = x_start + i * (small_size + 10)
            y = margin + 50 + j * (small_size + 10)
            
            if "circles" in constraints["shapes"][0]:
                db.oval(x, y, small_size, small_size)
            else:
                db.rect(x, y, small_size, small_size)

def create_movement_composition(width, height, margin, colors, constraints):
    """Create a composition suggesting movement"""
    # Diagonal elements suggesting motion
    
    num_elements = 15
    for i in range(num_elements):
        progress = i / num_elements
        
        # Diagonal path
        x = margin + progress * (width - 2 * margin)
        y = height - margin - progress * (height - 2 * margin)
        
        # Size changes along path
        size = 20 + progress * 60
        
        # Rotation increases
        rotation = progress * 360
        
        db.save()
        db.translate(x, y)
        db.rotate(rotation)
        
        # Fade effect
        db.fill(*colors[i % len(colors)], 1 - progress * 0.7)
        
        if "rectangles" in constraints["shapes"][0]:
            db.rect(-size/2, -size/2, size, size * 0.3)
        else:
            db.oval(-size/2, -size/2, size, size)
        
        db.restore()

def create_random_composition(width, height, margin, colors, constraints):
    """Fallback random composition"""
    # Random placement following grid
    grid = column_grid(width, height, constraints["grid"], 20, margin)
    
    for i in range(random.randint(5, 15)):
        # Snap to grid
        col = random.randint(0, constraints["grid"] - 1)
        x = margin + col * (grid["column_width"] + 20)
        y = random.randint(int(margin), int(height - margin - 100))
        
        size = random.randint(30, 150)
        
        db.fill(*random.choice(colors), random.uniform(0.5, 1))
        
        if "circles" in constraints["shapes"][0]:
            db.oval(x, y, size, size)
        elif "rectangles" in constraints["shapes"][0]:
            db.rect(x, y, size, size * random.uniform(0.5, 2))
        else:
            draw_triangle(x + size/2, y + size/2, size)

def draw_triangle(x, y, size):
    """Helper to draw a triangle"""
    path = db.BezierPath()
    path.moveTo((x - size/2, y - size/2))
    path.lineTo((x + size/2, y - size/2))
    path.lineTo((x, y + size/2))
    path.closePath()
    db.drawPath(path)

def review_week_posters():
    """Create a review sheet of the week's posters"""
    # This would load and display thumbnails of the week's work
    pass

# Generate poster ideas
POSTER_PROMPTS = [
    "Design a poster for a jazz festival using only geometric shapes",
    "Create a typographic poster with a single word that expresses its meaning visually",
    "Design a poster about climate change using only two colors",
    "Make a poster celebrating mathematics using the golden ratio",
    "Create a poster about time using repetition and rhythm",
    "Design a movie poster using Swiss design principles",
    "Make a poster about music visualization using only lines",
    "Create a poster about architecture using modular grids",
    "Design a poster about nature using organic shapes",
    "Make a poster about technology using glitch aesthetics"
]

# Main execution
if __name__ == "__main__":
    # Get today's constraints
    constraints = get_daily_constraints()
    
    print(f"Today's Daily Poster Challenge ({constraints['date']}):")
    print(f"- Color Scheme: {constraints['color_scheme']}")
    print(f"- Theme: {constraints['theme']}")
    print(f"- Shapes: {constraints['shapes']}")
    print(f"- Typography: {constraints['typography']}")
    print(f"- Grid: {constraints['grid']} columns")
    print("\nRandom prompt idea:", random.choice(POSTER_PROMPTS))
    
    # Create the poster
    create_daily_poster(constraints)
    
    # Save with date
    filename = f"daily_poster_{constraints['date']}.pdf"
    db.saveImage(filename)
    print(f"\nPoster saved as: {filename}")