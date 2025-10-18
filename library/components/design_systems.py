"""
Design Systems Components
=========================
Reusable functions and systems for consistent design
These components can be imported and used across projects
"""

import math
import random

# Import DrawBot
try:
    import drawBot as db
except ImportError:
    import sys
    import os
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    sys.path.insert(0, project_root)
    import drawBot as db

# Mathematical Constants
GOLDEN_RATIO = 1.618
SQRT_2 = 1.414
PI = math.pi

# Standard Scales
MUSICAL_SCALES = {
    "minor_second": 1.067,
    "major_second": 1.125,
    "minor_third": 1.2,
    "major_third": 1.25,
    "perfect_fourth": 1.333,
    "augmented_fourth": 1.414,
    "perfect_fifth": 1.5,
    "golden_ratio": 1.618
}

def modular_scale(base_size, ratio, steps=5, round_to=None):
    """
    Generate a modular scale for consistent sizing
    
    Args:
        base_size: Starting size
        ratio: Scale ratio (use MUSICAL_SCALES constants)
        steps: Number of steps up and down from base
        round_to: Round to nearest value (useful for baseline grids)
    
    Returns:
        List of sizes
    """
    scale = []
    
    # Generate sizes below base
    for i in range(steps, 0, -1):
        size = base_size / (ratio ** i)
        if round_to:
            size = round(size / round_to) * round_to
        scale.append(size)
    
    # Add base size
    scale.append(base_size)
    
    # Generate sizes above base
    for i in range(1, steps + 1):
        size = base_size * (ratio ** i)
        if round_to:
            size = round(size / round_to) * round_to
        scale.append(size)
    
    return scale

def baseline_grid(width, height, unit=8, color=(0.9, 0.9, 0.9), show_major=True):
    """
    Draw a baseline grid for vertical rhythm
    
    Args:
        width, height: Canvas dimensions
        unit: Base unit for grid
        color: Grid line color
        show_major: Show stronger lines every 4 units
    """
    db.stroke(*color)
    db.strokeWidth(0.5)
    
    # Draw baseline grid
    for y in range(0, int(height), unit):
        db.line((0, y), (width, y))
    
    # Draw major lines
    if show_major:
        db.stroke(*color[:-1], color[-1] * 2)  # Darker
        db.strokeWidth(1)
        for y in range(0, int(height), unit * 4):
            db.line((0, y), (width, y))
    
    db.stroke(None)

def column_grid(width, height, columns, gutter, margin=None):
    """
    Calculate column grid measurements
    
    Args:
        width, height: Canvas dimensions
        columns: Number of columns
        gutter: Space between columns
        margin: Page margins (auto-calculated if None)
    
    Returns:
        Dict with grid measurements
    """
    if margin is None:
        margin = width * 0.067  # Classic proportion
    
    content_width = width - (2 * margin)
    column_width = (content_width - (columns - 1) * gutter) / columns
    
    return {
        "margin": margin,
        "content_width": content_width,
        "column_width": column_width,
        "gutter": gutter,
        "columns": columns,
        "height": height
    }

def draw_column_guides(grid_info, color=(0.8, 0.2, 0.2, 0.3)):
    """Draw column guides from grid_info dict"""
    db.stroke(*color)
    db.strokeWidth(1)
    
    margin = grid_info["margin"]
    column_width = grid_info["column_width"]
    gutter = grid_info["gutter"]
    columns = grid_info["columns"]
    height = grid_info["height"]
    
    # Draw columns
    for i in range(columns):
        x = margin + i * (column_width + gutter)
        db.fill(*color[:3], color[3] * 0.5)
        db.rect(x, 0, column_width, height)
    
    db.stroke(None)
    db.fill(None)

def fibonacci_sequence(n):
    """Generate Fibonacci sequence up to n terms"""
    fib = [1, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib

def golden_rectangle(x, y, width, depth=5):
    """
    Draw a golden rectangle with subdivisions
    
    Args:
        x, y: Starting position
        width: Initial width
        depth: Number of subdivisions
    """
    if depth <= 0:
        return
    
    height = width / GOLDEN_RATIO
    
    # Draw rectangle
    db.stroke(0, 0, 0, 0.5)
    db.strokeWidth(1)
    db.fill(None)
    db.rect(x, y, width, height)
    
    # Draw arc for golden spiral
    db.stroke(0.8, 0.6, 0, 0.5)
    db.strokeWidth(2)
    
    # Quarter circle
    path = db.BezierPath()
    path.arc((x, y), width, 0, 90, clockwise=False)
    db.drawPath(path)
    
    # Subdivide
    if width > height:
        golden_rectangle(x + height, y, width - height, depth - 1)
    else:
        golden_rectangle(x, y + width, height - width, depth - 1)
    
    db.stroke(None)

def color_palette_generator(base_color, mode="analogous", variations=5):
    """
    Generate color palettes from a base color
    
    Args:
        base_color: (r, g, b) tuple
        mode: "analogous", "complementary", "triadic", "monochromatic"
        variations: Number of color variations
    
    Returns:
        List of color tuples
    """
    import colorsys
    
    # Convert to HSV
    h, s, v = colorsys.rgb_to_hsv(*base_color)
    colors = []
    
    if mode == "analogous":
        # Colors next to each other on wheel
        step = 30 / 360  # 30 degrees
        for i in range(variations):
            offset = (i - variations // 2) * step
            new_h = (h + offset) % 1
            colors.append(colorsys.hsv_to_rgb(new_h, s, v))
    
    elif mode == "complementary":
        # Opposite colors
        colors.append(base_color)
        comp_h = (h + 0.5) % 1
        colors.append(colorsys.hsv_to_rgb(comp_h, s, v))
        # Add variations
        for i in range(variations - 2):
            var_s = s * (0.5 + i * 0.5 / (variations - 2))
            var_v = v * (0.7 + i * 0.3 / (variations - 2))
            colors.append(colorsys.hsv_to_rgb(h, var_s, var_v))
    
    elif mode == "triadic":
        # Three colors equally spaced
        for i in range(3):
            new_h = (h + i * 0.333) % 1
            colors.append(colorsys.hsv_to_rgb(new_h, s, v))
        # Add tints/shades
        for i in range(variations - 3):
            idx = i % 3
            base_h, base_s, base_v = colorsys.rgb_to_hsv(*colors[idx])
            colors.append(colorsys.hsv_to_rgb(base_h, base_s * 0.5, base_v))
    
    elif mode == "monochromatic":
        # Same hue, different saturation/value
        for i in range(variations):
            factor = i / (variations - 1)
            new_s = s * (0.3 + 0.7 * factor)
            new_v = v * (0.5 + 0.5 * factor)
            colors.append(colorsys.hsv_to_rgb(h, new_s, new_v))
    
    return colors

def type_hierarchy(base_size=16, scale_name="major_third", levels=5):
    """
    Generate a typographic hierarchy
    
    Args:
        base_size: Body text size
        scale_name: Name from MUSICAL_SCALES
        levels: Number of hierarchy levels
    
    Returns:
        Dict with size recommendations
    """
    scale = modular_scale(base_size, MUSICAL_SCALES[scale_name], levels//2)
    
    # Find appropriate sizes
    sizes = sorted(scale, reverse=True)
    
    return {
        "display": sizes[0] if len(sizes) > 0 else base_size * 4,
        "h1": sizes[1] if len(sizes) > 1 else base_size * 3,
        "h2": sizes[2] if len(sizes) > 2 else base_size * 2.5,
        "h3": sizes[3] if len(sizes) > 3 else base_size * 2,
        "h4": sizes[4] if len(sizes) > 4 else base_size * 1.5,
        "body": base_size,
        "caption": sizes[-1] if sizes[-1] < base_size else base_size * 0.875
    }

def responsive_breakpoints():
    """Common responsive breakpoints"""
    return {
        "mobile": 320,
        "mobile_landscape": 480,
        "tablet": 768,
        "desktop": 1024,
        "desktop_large": 1440,
        "desktop_xlarge": 1920
    }

def draw_guides(width, height, guide_type="all"):
    """
    Draw composition guides
    
    Args:
        width, height: Canvas dimensions
        guide_type: "thirds", "golden", "center", "diagonal", "all"
    """
    guides = {
        "thirds": (0.8, 0.2, 0.2, 0.3),  # Red
        "golden": (0.8, 0.6, 0, 0.3),    # Orange
        "center": (0.2, 0.2, 0.8, 0.3),  # Blue
        "diagonal": (0.2, 0.8, 0.2, 0.3) # Green
    }
    
    if guide_type == "all" or guide_type == "thirds":
        db.stroke(*guides["thirds"])
        db.strokeWidth(1)
        # Rule of thirds
        for i in [1/3, 2/3]:
            db.line((width * i, 0), (width * i, height))
            db.line((0, height * i), (width, height * i))
    
    if guide_type == "all" or guide_type == "golden":
        db.stroke(*guides["golden"])
        db.strokeWidth(1)
        # Golden ratio
        golden_x = width / GOLDEN_RATIO
        golden_y = height / GOLDEN_RATIO
        db.line((golden_x, 0), (golden_x, height))
        db.line((width - golden_x, 0), (width - golden_x, height))
        db.line((0, golden_y), (width, golden_y))
        db.line((0, height - golden_y), (width, height - golden_y))
    
    if guide_type == "all" or guide_type == "center":
        db.stroke(*guides["center"])
        db.strokeWidth(1)
        # Center lines
        db.line((width/2, 0), (width/2, height))
        db.line((0, height/2), (width, height/2))
    
    if guide_type == "all" or guide_type == "diagonal":
        db.stroke(*guides["diagonal"])
        db.strokeWidth(1)
        # Diagonals
        db.line((0, 0), (width, height))
        db.line((width, 0), (0, height))
    
    db.stroke(None)

def random_seed_design(seed):
    """Set random seed for reproducible randomness"""
    random.seed(seed)
    
def map_range(value, in_min, in_max, out_min, out_max):
    """Map a value from one range to another"""
    return out_min + (value - in_min) * (out_max - out_min) / (in_max - in_min)

def constrain(value, min_val, max_val):
    """Constrain a value between min and max"""
    return max(min_val, min(value, max_val))

# Test the system
if __name__ == "__main__":
    # Test modular scale
    width, height = 595, 842
    
    db.newPage(width, height)
    db.fill(1, 1, 1)
    db.rect(0, 0, width, height)
    
    # Draw baseline grid
    baseline_grid(width, height, 8)
    
    # Test type hierarchy
    hierarchy = type_hierarchy(12, "perfect_fourth")
    
    y_pos = height - 50
    for name, size in hierarchy.items():
        db.fill(0, 0, 0)
        db.font("Helvetica")
        db.fontSize(size)
        db.text(f"{name}: {int(size)}pt", (50, y_pos))
        y_pos -= size + 10
    
    # Test color palette
    db.newPage(width, height)
    db.fill(1, 1, 1)
    db.rect(0, 0, width, height)
    
    base_color = (0.2, 0.4, 0.8)
    modes = ["analogous", "complementary", "triadic", "monochromatic"]
    
    y_pos = height - 50
    for mode in modes:
        colors = color_palette_generator(base_color, mode, 5)
        
        db.fill(0, 0, 0)
        db.font("Helvetica")
        db.fontSize(14)
        db.text(mode.title(), (50, y_pos))
        
        x_pos = 50
        for color in colors:
            db.fill(*color)
            db.rect(x_pos, y_pos - 40, 40, 30)
            x_pos += 50
        
        y_pos -= 80
    
    db.saveImage("design_systems_test.pdf")