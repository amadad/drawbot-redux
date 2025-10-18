"""
Color Theory in DrawBot
=======================
Design Principle: Color harmony, contrast, and emotional impact
Historical Context: Based on Johannes Itten, Josef Albers, and modern digital color theory
Key Concepts: Color wheels, harmonies, contrast types, color psychology
DrawBot Features Used: fill(), cmykFill(), colorSpace(), linearGradient(), blendMode()
Parameters to Experiment With: hue_shift, saturation, brightness, opacity
"""

import math
import colorsys

# Import DrawBot
try:
    import drawBot as db
except ImportError:
    # If running from within the library, add parent path
    import sys
    import os
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    sys.path.insert(0, project_root)
    import drawBot as db

# Constants
COLOR_WHEEL_SEGMENTS = 12
GOLDEN_ANGLE = 137.5  # Golden angle in degrees

def hsv_to_rgb(h, s, v):
    """Convert HSV to RGB color space"""
    return colorsys.hsv_to_rgb(h, s, v)

def rgb_to_hsv(r, g, b):
    """Convert RGB to HSV color space"""
    return colorsys.rgb_to_hsv(r, g, b)

def draw_color_wheel(x, y, radius):
    """Draw a color wheel showing hue relationships"""
    for i in range(360):
        angle = math.radians(i)
        # Draw thin wedge
        path = db.BezierPath()
        path.moveTo((x, y))
        
        x1 = x + radius * math.cos(angle)
        y1 = y + radius * math.sin(angle)
        x2 = x + radius * math.cos(angle + math.radians(1))
        y2 = y + radius * math.sin(angle + math.radians(1))
        
        path.lineTo((x1, y1))
        path.lineTo((x2, y2))
        path.closePath()
        
        # Set color
        hue = i / 360
        rgb = hsv_to_rgb(hue, 1, 1)
        db.fill(*rgb)
        db.drawPath(path)
    
    # Draw center white circle
    db.fill(1, 1, 1)
    db.oval(x - radius/3, y - radius/3, radius/3 * 2, radius/3 * 2)

def demonstrate_color_harmonies():
    """Show different color harmony systems"""
    page_width, page_height = 842, 595  # A4 Landscape
    margin = 50
    
    db.newPage(page_width, page_height)
    db.fill(0.1, 0.1, 0.1)  # Dark background
    db.rect(0, 0, page_width, page_height)
    
    # Title
    db.fill(1, 1, 1)
    db.font("Helvetica-Bold")
    db.fontSize(28)
    db.text("Color Harmonies", (margin, page_height - margin))
    
    # Draw color wheels with different harmonies
    wheel_size = 80
    y_pos = page_height - 200
    x_start = margin + wheel_size
    
    harmonies = [
        ("Complementary", [(0, 1, 1), (0.5, 1, 1)]),
        ("Triadic", [(0, 1, 1), (0.333, 1, 1), (0.667, 1, 1)]),
        ("Analogous", [(0, 1, 1), (0.083, 1, 1), (0.917, 1, 1)]),
        ("Split-Complementary", [(0, 1, 1), (0.417, 1, 1), (0.583, 1, 1)]),
        ("Tetradic", [(0, 1, 1), (0.25, 1, 1), (0.5, 1, 1), (0.75, 1, 1)])
    ]
    
    for i, (name, colors) in enumerate(harmonies):
        x = x_start + i * (wheel_size * 2.5)
        
        # Draw mini color wheel
        draw_color_wheel(x, y_pos, wheel_size)
        
        # Mark harmony points
        for h, s, v in colors:
            angle = h * 2 * math.pi
            px = x + wheel_size * 0.8 * math.cos(angle)
            py = y_pos + wheel_size * 0.8 * math.sin(angle)
            
            db.fill(0, 0, 0)
            db.oval(px - 5, py - 5, 10, 10)
            db.fill(1, 1, 1)
            db.oval(px - 3, py - 3, 6, 6)
        
        # Draw connecting lines
        db.stroke(1, 1, 1, 0.5)
        db.strokeWidth(2)
        for j in range(len(colors)):
            h1, _, _ = colors[j]
            h2, _, _ = colors[(j + 1) % len(colors)]
            
            angle1 = h1 * 2 * math.pi
            angle2 = h2 * 2 * math.pi
            
            x1 = x + wheel_size * 0.8 * math.cos(angle1)
            y1 = y_pos + wheel_size * 0.8 * math.sin(angle1)
            x2 = x + wheel_size * 0.8 * math.cos(angle2)
            y2 = y_pos + wheel_size * 0.8 * math.sin(angle2)
            
            db.line((x1, y1), (x2, y2))
        db.stroke(None)
        
        # Label
        db.fill(1, 1, 1)
        db.font("Helvetica")
        db.fontSize(12)
        db.text(name, (x - wheel_size, y_pos - wheel_size - 20), align="center")
        
        # Show color swatches
        swatch_y = y_pos - wheel_size - 60
        for j, (h, s, v) in enumerate(colors):
            rgb = hsv_to_rgb(h, s, v)
            db.fill(*rgb)
            db.rect(x - wheel_size + j * 25, swatch_y, 20, 20)

def demonstrate_color_contrast():
    """Show different types of color contrast"""
    page_width, page_height = 595, 842
    margin = 50
    
    db.newPage(page_width, page_height)
    db.fill(0.95, 0.95, 0.95)
    db.rect(0, 0, page_width, page_height)
    
    # Title
    db.fill(0, 0, 0)
    db.font("Helvetica-Bold")
    db.fontSize(28)
    db.text("Color Contrast Types", (margin, page_height - margin))
    
    # Based on Johannes Itten's seven color contrasts
    y_pos = page_height - 120
    box_size = 80
    
    contrasts = [
        ("Hue Contrast", [
            (1, 0, 0),     # Red
            (0, 0, 1),     # Blue
            (1, 1, 0)      # Yellow
        ]),
        ("Light-Dark", [
            (0, 0, 0),     # Black
            (0.5, 0.5, 0.5), # Gray
            (1, 1, 1)      # White
        ]),
        ("Cold-Warm", [
            (0, 0.4, 0.8), # Cool blue
            (0.5, 0.5, 0.5), # Neutral
            (1, 0.3, 0)    # Warm orange
        ]),
        ("Complementary", [
            (1, 0, 0),     # Red
            (0, 1, 0)      # Green
        ]),
        ("Saturation", [
            (0.5, 0.5, 0.5), # Gray
            (0.5, 0.3, 0.3), # Desaturated red
            (1, 0, 0)      # Pure red
        ]),
        ("Quantity", [
            (1, 0.8, 0),   # Large yellow area
            (0.4, 0, 0.6)  # Small violet area
        ])
    ]
    
    for i, (name, colors) in enumerate(contrasts):
        if i % 2 == 0:
            x = margin
            if i > 0:
                y_pos -= 150
        else:
            x = page_width / 2
        
        # Label
        db.fill(0, 0, 0)
        db.font("Helvetica-Bold")
        db.fontSize(14)
        db.text(name, (x, y_pos))
        
        # Color samples
        if name == "Quantity":
            # Special case for quantity contrast
            db.fill(*colors[0])
            db.rect(x, y_pos - 80, 120, 60)
            db.fill(*colors[1])
            db.rect(x + 130, y_pos - 60, 30, 40)
        else:
            for j, color in enumerate(colors):
                db.fill(*color)
                db.rect(x + j * (box_size + 10), y_pos - 80, box_size, box_size)

def color_psychology_examples():
    """Demonstrate emotional associations of colors"""
    page_width, page_height = 842, 595
    margin = 50
    
    db.newPage(page_width, page_height)
    db.fill(0.98, 0.98, 0.98)
    db.rect(0, 0, page_width, page_height)
    
    # Title
    db.fill(0, 0, 0)
    db.font("Helvetica-Bold")
    db.fontSize(28)
    db.text("Color Psychology & Emotion", (margin, page_height - margin))
    
    # Color associations
    associations = [
        ("Energy & Passion", [(0.9, 0.1, 0.1), (1, 0.4, 0), (1, 0.8, 0)]),
        ("Trust & Stability", [(0, 0.3, 0.6), (0, 0.5, 0.8), (0.1, 0.2, 0.4)]),
        ("Growth & Nature", [(0.1, 0.6, 0.2), (0.3, 0.7, 0.3), (0.5, 0.8, 0.3)]),
        ("Luxury & Mystery", [(0.4, 0, 0.6), (0.6, 0, 0.8), (0.2, 0, 0.3)]),
        ("Optimism & Creativity", [(1, 0.8, 0), (1, 0.6, 0), (1, 0.9, 0.3)])
    ]
    
    y_pos = page_height - 120
    
    for mood, colors in associations:
        # Mood label
        db.fill(0, 0, 0)
        db.font("Helvetica-Bold")
        db.fontSize(16)
        db.text(mood, (margin, y_pos))
        
        # Color gradient bar
        x = margin
        y = y_pos - 40
        bar_width = 600
        bar_height = 30
        
        # Create gradient
        gradient_colors = []
        gradient_positions = []
        for i, color in enumerate(colors):
            gradient_colors.append(color)
            gradient_positions.append(i / (len(colors) - 1))
        
        db.linearGradient(
            (x, y), (x + bar_width, y),
            gradient_colors,
            gradient_positions
        )
        db.rect(x, y, bar_width, bar_height)
        
        y_pos -= 80

def demonstrate_color_accessibility():
    """Show color accessibility considerations"""
    page_width, page_height = 595, 842
    margin = 50
    
    db.newPage(page_width, page_height)
    db.fill(1, 1, 1)
    db.rect(0, 0, page_width, page_height)
    
    # Title
    db.fill(0, 0, 0)
    db.font("Helvetica-Bold")
    db.fontSize(28)
    db.text("Color Accessibility", (margin, page_height - margin))
    
    # Contrast ratios
    y_pos = page_height - 120
    
    db.font("Helvetica-Bold")
    db.fontSize(16)
    db.text("WCAG Contrast Ratios", (margin, y_pos))
    
    y_pos -= 40
    
    # Good examples
    db.fill(0, 0.6, 0)
    db.font("Helvetica")
    db.fontSize(14)
    db.text("✓ Good Contrast", (margin, y_pos))
    
    y_pos -= 30
    examples = [
        ((0, 0, 0), (1, 1, 1), "Black on White (21:1)"),
        ((0, 0, 0.6), (1, 1, 1), "Dark Blue on White (8.6:1)"),
        ((1, 1, 1), (0.2, 0.2, 0.2), "White on Dark Gray (13.1:1)")
    ]
    
    for fg, bg, label in examples:
        db.fill(*bg)
        db.rect(margin, y_pos - 25, 200, 30)
        db.fill(*fg)
        db.text("Sample Text", (margin + 10, y_pos - 20))
        db.fill(0, 0, 0)
        db.text(label, (margin + 220, y_pos - 15))
        y_pos -= 40
    
    # Bad examples
    y_pos -= 20
    db.fill(0.8, 0, 0)
    db.fontSize(14)
    db.text("✗ Poor Contrast", (margin, y_pos))
    
    y_pos -= 30
    bad_examples = [
        ((0.7, 0.7, 0), (1, 1, 1), "Light Yellow on White (1.5:1)"),
        ((0.5, 0.5, 0.5), (0.6, 0.6, 0.6), "Gray on Gray (1.3:1)"),
        ((0, 0.8, 0), (0, 1, 0), "Green on Green (1.25:1)")
    ]
    
    for fg, bg, label in bad_examples:
        db.fill(*bg)
        db.rect(margin, y_pos - 25, 200, 30)
        db.fill(*fg)
        db.text("Sample Text", (margin + 10, y_pos - 20))
        db.fill(0, 0, 0)
        db.text(label, (margin + 220, y_pos - 15))
        y_pos -= 40
    
    # Color blindness simulation
    y_pos -= 40
    db.font("Helvetica-Bold")
    db.fontSize(16)
    db.text("Color Blindness Considerations", (margin, y_pos))
    
    y_pos -= 40
    db.font("Helvetica")
    db.fontSize(12)
    
    # Don't rely on color alone
    db.fill(0, 0, 0)
    db.text("Don't rely on color alone:", (margin, y_pos))
    
    y_pos -= 30
    # Bad: color only
    db.fill(1, 0, 0)
    db.oval(margin, y_pos - 15, 20, 20)
    db.fill(0, 1, 0)
    db.oval(margin + 30, y_pos - 15, 20, 20)
    db.fill(0, 0, 0)
    db.text("Bad: Red = Stop, Green = Go", (margin + 70, y_pos - 10))
    
    y_pos -= 30
    # Good: color + symbol
    db.fill(1, 0, 0)
    db.rect(margin, y_pos - 15, 20, 20)
    db.fill(1, 1, 1)
    db.font("Helvetica-Bold")
    db.fontSize(16)
    db.text("✕", (margin + 3, y_pos - 12))
    
    db.fill(0, 0.7, 0)
    db.oval(margin + 30, y_pos - 15, 20, 20)
    db.fill(1, 1, 1)
    db.text("✓", (margin + 33, y_pos - 12))
    
    db.fill(0, 0, 0)
    db.font("Helvetica")
    db.fontSize(12)
    db.text("Good: Color + Symbol", (margin + 70, y_pos - 10))

def create_color_palette_generator():
    """Generate harmonious color palettes"""
    page_width, page_height = 595, 842
    margin = 50
    
    db.newPage(page_width, page_height)
    db.fill(0.95, 0.95, 0.95)
    db.rect(0, 0, page_width, page_height)
    
    # Title
    db.fill(0, 0, 0)
    db.font("Helvetica-Bold")
    db.fontSize(28)
    db.text("Generated Color Palettes", (margin, page_height - margin))
    
    # Base color
    base_hue = 210 / 360  # Blue base
    
    # Generate different palette variations
    y_pos = page_height - 120
    
    palette_types = [
        ("Monochromatic", lambda h: [
            (h, 0.2, 0.9),
            (h, 0.4, 0.8),
            (h, 0.6, 0.7),
            (h, 0.8, 0.6),
            (h, 1.0, 0.5)
        ]),
        ("Analogous", lambda h: [
            (h - 0.083, 0.7, 0.8),
            (h - 0.042, 0.8, 0.7),
            (h, 0.9, 0.6),
            (h + 0.042, 0.8, 0.7),
            (h + 0.083, 0.7, 0.8)
        ]),
        ("Triadic", lambda h: [
            (h, 0.9, 0.7),
            (h, 0.5, 0.5),
            (h + 0.333, 0.9, 0.7),
            (h + 0.333, 0.5, 0.5),
            (h + 0.667, 0.9, 0.7)
        ]),
        ("Split-Complementary", lambda h: [
            (h, 0.9, 0.7),
            (h, 0.6, 0.5),
            (h + 0.417, 0.8, 0.6),
            (h + 0.583, 0.8, 0.6),
            (0, 0, 0.9)  # Neutral
        ])
    ]
    
    for name, palette_func in palette_types:
        # Label
        db.fill(0, 0, 0)
        db.font("Helvetica-Bold")
        db.fontSize(14)
        db.text(name, (margin, y_pos))
        
        # Generate and display palette
        colors = palette_func(base_hue)
        
        for i, (h, s, v) in enumerate(colors):
            h = h % 1  # Wrap hue values
            rgb = hsv_to_rgb(h, s, v)
            db.fill(*rgb)
            
            x = margin + i * 95
            y = y_pos - 60
            
            # Color swatch
            db.rect(x, y, 80, 40)
            
            # Color values
            db.fill(0, 0, 0)
            db.font("Helvetica")
            db.fontSize(9)
            db.text(f"HSV: {int(h*360)}°", (x, y - 15))
            db.text(f"RGB: {int(rgb[0]*255)},{int(rgb[1]*255)},{int(rgb[2]*255)}", 
                   (x, y - 25))
        
        y_pos -= 120

# Main execution
if __name__ == "__main__":
    demonstrate_color_harmonies()
    demonstrate_color_contrast()
    color_psychology_examples()
    demonstrate_color_accessibility()
    create_color_palette_generator()
    
    db.saveImage("color_theory.pdf")
    print("Color theory guide created successfully!")