"""
Pattern Generation Cookbook
===========================
Recipes for creating repeating patterns and textures.

Patterns covered:
- Grid patterns
- Dot patterns
- Line patterns
- Geometric patterns
- Random/organic patterns
- Islamic patterns
"""

import sys
import os

# Add the project root to Python path to find the local drawBot module
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import drawBot as db

import math
import random

# Pattern 1: Basic Grid Pattern
db.newPage(800, 800)
db.fill(0.95)
db.rect(0, 0, 800, 800)

db.fill(0)
db.font("Helvetica-Bold")
db.fontSize(24)
db.text("Grid Patterns", (50, 750))

# Simple grid
def draw_grid_pattern(x, y, width, height, cols, rows):
    """Draw a basic grid pattern"""
    cell_w = width / cols
    cell_h = height / rows
    
    db.stroke(0.3)
    db.strokeWidth(1)
    
    for i in range(cols + 1):
        x_pos = x + i * cell_w
        db.line((x_pos, y), (x_pos, y + height))
    
    for j in range(rows + 1):
        y_pos = y + j * cell_h
        db.line((x, y_pos), (x + width, y_pos))
    
    db.stroke(None)

draw_grid_pattern(50, 450, 300, 250, 10, 8)

# Modular grid with shapes
def draw_modular_grid(x, y, size, modules):
    """Draw a grid with alternating shapes"""
    module_size = size / modules
    
    for i in range(modules):
        for j in range(modules):
            x_pos = x + i * module_size
            y_pos = y + j * module_size
            
            # Alternate between shapes
            if (i + j) % 2 == 0:
                db.fill(0.8, 0.2, 0.2)
                db.rect(x_pos + 5, y_pos + 5, module_size - 10, module_size - 10)
            else:
                db.fill(0.2, 0.2, 0.8)
                db.oval(x_pos + 5, y_pos + 5, module_size - 10, module_size - 10)

draw_modular_grid(400, 450, 300, 8)

# Pattern 2: Dot Patterns
y_offset = 350

db.fontSize(18)
db.fill(0)
db.text("Dot Patterns", (50, y_offset))

# Regular dot grid
def draw_dot_pattern(x, y, width, height, spacing):
    """Draw a regular dot pattern"""
    cols = int(width / spacing)
    rows = int(height / spacing)
    
    db.fill(0)
    for i in range(cols):
        for j in range(rows):
            x_pos = x + i * spacing + spacing / 2
            y_pos = y + j * spacing + spacing / 2
            db.oval(x_pos - 2, y_pos - 2, 4, 4)

draw_dot_pattern(50, 150, 150, 150, 15)

# Halftone pattern
def draw_halftone(x, y, width, height, max_size=10):
    """Draw a halftone gradient pattern"""
    spacing = max_size + 2
    cols = int(width / spacing)
    rows = int(height / spacing)
    
    for i in range(cols):
        for j in range(rows):
            x_pos = x + i * spacing + spacing / 2
            y_pos = y + j * spacing + spacing / 2
            
            # Calculate distance from center for gradient
            center_x = x + width / 2
            center_y = y + height / 2
            distance = math.sqrt((x_pos - center_x)**2 + (y_pos - center_y)**2)
            max_distance = math.sqrt((width/2)**2 + (height/2)**2)
            
            # Size based on distance
            size = max_size * (1 - distance / max_distance)
            if size > 0:
                db.fill(0)
                db.oval(x_pos - size/2, y_pos - size/2, size, size)

draw_halftone(250, 150, 150, 150)

# Random dots
def draw_random_dots(x, y, width, height, count):
    """Draw randomly placed dots"""
    random.seed(42)  # For consistency
    
    for _ in range(count):
        x_pos = x + random.random() * width
        y_pos = y + random.random() * height
        size = random.uniform(2, 8)
        opacity = random.uniform(0.3, 1)
        
        db.fill(0, opacity)
        db.oval(x_pos - size/2, y_pos - size/2, size, size)

draw_random_dots(450, 150, 150, 150, 200)

# Pattern 3: Line Patterns
db.newPage(800, 800)
db.fill(0.95)
db.rect(0, 0, 800, 800)

db.fill(0)
db.font("Helvetica-Bold")
db.fontSize(24)
db.text("Line Patterns", (50, 750))

# Parallel lines
def draw_parallel_lines(x, y, width, height, spacing, angle=0):
    """Draw parallel lines at an angle"""
    db.save()
    db.translate(x + width/2, y + height/2)
    db.rotate(angle)
    
    db.stroke(0)
    db.strokeWidth(1)
    
    # Calculate number of lines needed
    diagonal = math.sqrt(width**2 + height**2)
    lines = int(diagonal / spacing) + 1
    
    for i in range(lines):
        line_pos = -diagonal/2 + i * spacing
        db.line((-diagonal/2, line_pos), (diagonal/2, line_pos))
    
    db.stroke(None)
    db.restore()

# Different angles
draw_parallel_lines(50, 500, 150, 150, 10, 0)
draw_parallel_lines(250, 500, 150, 150, 10, 45)
draw_parallel_lines(450, 500, 150, 150, 10, -45)

# Cross-hatch pattern
def draw_crosshatch(x, y, width, height, spacing):
    """Draw a crosshatch pattern"""
    # First set of lines
    draw_parallel_lines(x, y, width, height, spacing, 45)
    # Second set perpendicular
    draw_parallel_lines(x, y, width, height, spacing, -45)

db.fontSize(18)
db.fill(0)
db.text("Crosshatch", (50, 450))
draw_crosshatch(50, 250, 150, 150, 15)

# Wave pattern
def draw_wave_pattern(x, y, width, height, waves, amplitude):
    """Draw wavy lines"""
    db.stroke(0)
    db.strokeWidth(2)
    
    for i in range(waves):
        y_pos = y + (i + 0.5) * height / waves
        
        db.newPath()
        db.moveTo((x, y_pos))
        
        steps = 50
        for j in range(steps + 1):
            x_pos = x + j * width / steps
            wave_y = y_pos + amplitude * math.sin(j * math.pi * 4 / steps)
            db.lineTo((x_pos, wave_y))
        
        db.drawPath()
    
    db.stroke(None)

db.text("Waves", (250, 450))
draw_wave_pattern(250, 250, 150, 150, 8, 10)

# Pattern 4: Geometric Patterns
db.fontSize(18)
db.text("Geometric", (450, 450))

def draw_triangle_pattern(x, y, size, rows):
    """Draw a triangular tessellation"""
    tri_height = size * math.sqrt(3) / 2
    
    for row in range(rows):
        for col in range(rows):
            x_pos = x + col * size + (row % 2) * size / 2
            y_pos = y + row * tri_height
            
            # Upward triangle
            if (row + col) % 2 == 0:
                db.fill(0.2, 0.6, 0.9)
            else:
                db.fill(0.9, 0.4, 0.2)
            
            db.polygon(
                (x_pos, y_pos),
                (x_pos + size, y_pos),
                (x_pos + size/2, y_pos + tri_height)
            )

draw_triangle_pattern(450, 250, 30, 5)

# Pattern 5: Islamic Pattern
db.newPage(800, 800)
db.fill(0.95)
db.rect(0, 0, 800, 800)

db.fill(0)
db.font("Helvetica-Bold")
db.fontSize(24)
db.text("Islamic Geometric Pattern", (50, 750))

def draw_islamic_star(cx, cy, outer_radius, inner_radius, points):
    """Draw an Islamic star pattern"""
    angle_step = 2 * math.pi / points
    
    db.newPath()
    for i in range(points * 2):
        angle = i * angle_step / 2
        if i % 2 == 0:
            r = outer_radius
        else:
            r = inner_radius
        
        x = cx + r * math.cos(angle - math.pi/2)
        y = cy + r * math.sin(angle - math.pi/2)
        
        if i == 0:
            db.moveTo((x, y))
        else:
            db.lineTo((x, y))
    
    db.closePath()
    db.drawPath()

# Create a grid of stars
tile_size = 120
for row in range(5):
    for col in range(5):
        cx = 100 + col * tile_size
        cy = 600 - row * tile_size
        
        # Alternating colors
        if (row + col) % 2 == 0:
            db.fill(0.2, 0.4, 0.6)
        else:
            db.fill(0.8, 0.6, 0.2)
        
        draw_islamic_star(cx, cy, 50, 20, 8)

# Pattern 6: Organic/Random Pattern
db.newPage(800, 800)
db.fill(0.95)
db.rect(0, 0, 800, 800)

db.fill(0)
db.font("Helvetica-Bold")
db.fontSize(24)
db.text("Organic Patterns", (50, 750))

# Voronoi-inspired pattern
def draw_organic_cells(x, y, width, height, num_points):
    """Draw an organic cell pattern"""
    random.seed(123)
    
    # Generate random points
    points = []
    for _ in range(num_points):
        px = x + random.random() * width
        py = y + random.random() * height
        points.append((px, py))
    
    # Draw cells (simplified - just circles for now)
    for px, py in points:
        # Random size and color
        size = random.uniform(30, 80)
        gray = random.uniform(0.3, 0.8)
        
        db.fill(gray, gray, gray, 0.5)
        db.oval(px - size/2, py - size/2, size, size)

draw_organic_cells(50, 400, 700, 300, 30)

# Perlin noise-like pattern (simplified)
db.fontSize(18)
db.text("Noise Pattern", (50, 350))

def draw_noise_pattern(x, y, width, height, scale):
    """Draw a noise-like pattern using sine waves"""
    step = 5
    
    for i in range(0, int(width), step):
        for j in range(0, int(height), step):
            # Create pseudo-random values using sine
            value = (math.sin(i * 0.05) * math.sin(j * 0.05) + 1) / 2
            
            db.fill(value)
            db.rect(x + i, y + j, step, step)

draw_noise_pattern(50, 50, 200, 200, 20)

# Save the pattern cookbook
output_path = "output/pattern_generation.pdf"
db.saveImage(output_path)
print(f"Saved to {output_path}")

# 🎯 PATTERN EXERCISES:
# --------------------
# 1. Create a tartan/plaid pattern using overlapping colored lines
# 2. Design a hexagonal honeycomb pattern
# 3. Make a pattern that transitions from ordered to chaotic
# 4. Create a pattern inspired by nature (leaves, scales, etc.)
# 5. Design a pattern that could be used for fabric printing

# 💡 PATTERN TIPS:
# ----------------
# - Use loops for repetition - let the computer do the work
# - Modulo (%) operator is great for alternating elements
# - Random with a seed gives you controlled randomness
# - Mathematical functions (sin, cos) create smooth variations
# - Combine simple patterns to create complex ones

# 🔍 EXPLORE MORE:
# ----------------
# - Look into L-systems for plant-like patterns
# - Study tessellations and Penrose tilings
# - Experiment with recursive patterns
# - Try combining multiple pattern types