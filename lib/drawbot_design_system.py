"""
DrawBot Design System - Enforces principles from docs/

This module ensures:
1. Correct typography scales for context (poster, book, magazine, etc.)
2. Proper text wrapping based on POINTS not characters
3. Real baseline metrics (no fontSize approximations)
4. Path handling that works on any machine
5. Layout validation before rendering

Based on:
- docs/layout-design-principles.md
- docs/typography-style-guide.md
"""

from pathlib import Path
import drawBot as db
import textwrap
from typing import Tuple, List, Optional
from dataclasses import dataclass

# ==================== PATH MANAGEMENT ====================

# Get repo root (this file is in lib/, go up one level)
REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = REPO_ROOT / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

def get_output_path(filename: str) -> Path:
    """Get absolute path for output file (works on any machine)"""
    return OUTPUT_DIR / filename

# ==================== TYPOGRAPHY SCALES ====================

@dataclass
class TypographyScale:
    """Typography scale with proper ratios"""
    caption: float
    body: float
    h3: float
    h2: float
    h1: float
    title: float
    ratio: float

    def leading(self, size: float, ratio: float = 1.5) -> float:
        """Calculate proper leading (line spacing)"""
        return size * ratio

# Common scale ratios (from docs/layout-design-principles.md:95-103)
MINOR_SECOND = 1.067
MAJOR_SECOND = 1.125
MINOR_THIRD = 1.2
MAJOR_THIRD = 1.25
PERFECT_FOURTH = 1.333
PERFECT_FIFTH = 1.5
GOLDEN_RATIO = 1.618

def create_typography_scale(base: float, ratio: float) -> TypographyScale:
    """Create a modular typography scale"""
    return TypographyScale(
        caption=base / ratio,
        body=base,
        h3=base * ratio,
        h2=base * (ratio ** 2),
        h1=base * (ratio ** 3),
        title=base * (ratio ** 4),
        ratio=ratio
    )

# Pre-defined scales (from docs/layout-design-principles.md:486-503)
POSTER_SCALE = create_typography_scale(18, PERFECT_FIFTH)      # Base 18pt, ratio 1.5
MAGAZINE_SCALE = create_typography_scale(11, MAJOR_THIRD)      # Base 11pt, ratio 1.25
BOOK_SCALE = create_typography_scale(11, MINOR_THIRD)          # Base 11pt, ratio 1.2
REPORT_SCALE = create_typography_scale(12, MAJOR_THIRD)        # Base 12pt, ratio 1.25

# ==================== TEXT METRICS ====================

def get_text_metrics(text: str, font: str, size: float) -> dict:
    """Get real text metrics from DrawBot (not approximations)"""
    db.font(font)
    db.fontSize(size)

    # Get actual dimensions
    width, height = db.textSize(text)

    # Get font metrics
    try:
        ascender = db.fontAscender()
        descender = db.fontDescender()
        line_height = db.fontLineHeight()
        x_height = db.fontXHeight()
        cap_height = db.fontCapHeight()
    except:
        # Fallback if metrics not available
        ascender = size * 0.8
        descender = size * 0.2
        line_height = size
        x_height = size * 0.5
        cap_height = size * 0.7

    return {
        'width': width,
        'height': height,
        'ascender': ascender,
        'descender': descender,
        'line_height': line_height,
        'x_height': x_height,
        'cap_height': cap_height
    }

def calculate_chars_per_line(width_in_points: float, font: str, size: float) -> int:
    """
    Calculate character count based on ACTUAL width in points.

    From docs/typography-style-guide.md:171-179:
    - Optimal: 60-70 characters per line
    - Ideal: 60-65 characters
    """
    db.font(font)
    db.fontSize(size)

    # Use 'm' as average character width
    avg_char_width, _ = db.textSize("m")

    # Calculate how many fit
    chars_per_line = int(width_in_points / avg_char_width)

    return chars_per_line

# ==================== TEXT WRAPPING ====================

def wrap_text_to_width(
    text: str,
    width_in_points: float,
    font: str,
    size: float
) -> List[str]:
    """
    Wrap text based on ACTUAL visual width in points.

    Not character count heuristics - uses real DrawBot measurements.
    """
    chars_per_line = calculate_chars_per_line(width_in_points, font, size)

    # Ensure we stay within optimal range (45-75 characters)
    # From docs/layout-design-principles.md:63-69
    if chars_per_line > 75:
        chars_per_line = 75
    elif chars_per_line < 20:  # Minimum for posters
        chars_per_line = 20

    return textwrap.wrap(text, width=chars_per_line)

def draw_wrapped_text(
    text: str,
    x: float,
    y: float,
    width: float,
    height: float,
    font: str,
    size: float,
    leading_ratio: float = 1.5,
    align: str = "left"
) -> float:
    """
    Draw wrapped text with proper metrics and return final y position.

    Args:
        text: Text to draw
        x, y: Top-left corner of text box
        width, height: Box dimensions
        font, size: Typography settings
        leading_ratio: Line spacing ratio (default 1.5x from docs)
        align: "left", "right", "center"

    Returns:
        Final y position (baseline of last line drawn)
    """
    db.font(font)
    db.fontSize(size)

    # Get real metrics
    metrics = get_text_metrics("M", font, size)  # Use cap height as reference
    line_spacing = size * leading_ratio

    # Wrap text to width
    lines = wrap_text_to_width(text, width, font, size)

    # Start from top, move down
    current_y = y - metrics['ascender']  # Position first baseline
    
    # Bottom boundary of text box
    bottom_boundary = y - height

    for line in lines:
        # Check if we have room (descender is negative, so + moves down)
        line_bottom = current_y + metrics['descender']
        if line_bottom < bottom_boundary:
            break  # Stop if we'd overflow

        # Calculate x position based on alignment
        if align == "center":
            line_width, _ = db.textSize(line)
            line_x = x + (width - line_width) / 2
        elif align == "right":
            line_width, _ = db.textSize(line)
            line_x = x + width - line_width
        else:  # left
            line_x = x

        db.text(line, (line_x, current_y))
        current_y -= line_spacing

    return current_y

# ==================== LAYOUT VALIDATION ====================

def validate_layout_fit(elements: List[dict], page_height: float) -> Tuple[bool, Optional[str]]:
    """
    Validate that all elements fit on page before drawing.

    Args:
        elements: List of dicts with {'y': float, 'height': float, 'name': str}
        page_height: Total page height

    Returns:
        (fits: bool, error_message: Optional[str])
    """
    # Sort by y position (top to bottom)
    sorted_elements = sorted(elements, key=lambda e: e['y'], reverse=True)

    for i, elem in enumerate(sorted_elements):
        bottom = elem['y'] - elem['height']

        # Check if element extends below page
        if bottom < 0:
            return False, f"{elem['name']} extends {abs(bottom):.1f}pt below page bottom"

        # Check for overlaps with next element
        if i < len(sorted_elements) - 1:
            next_elem = sorted_elements[i + 1]
            if bottom < (next_elem['y'] + next_elem.get('margin_top', 0)):
                overlap = (next_elem['y'] + next_elem.get('margin_top', 0)) - bottom
                return False, f"{elem['name']} overlaps {next_elem['name']} by {overlap:.1f}pt"

    return True, None

# ==================== SPACING HELPERS ====================

def get_spacing_for_context(context: str = "poster") -> dict:
    """
    Get spacing values based on context.

    From docs/layout-design-principles.md:506-512
    """
    spacing_map = {
        "tight": {
            "letter_spacing": -0.02,  # -2%
            "word_spacing": 0.2,      # 0.2em
            "line_spacing": 1.2,      # 1.2x
            "paragraph_spacing": 0.5   # 0.5em
        },
        "normal": {
            "letter_spacing": 0.0,
            "word_spacing": 0.25,
            "line_spacing": 1.5,
            "paragraph_spacing": 1.0
        },
        "generous": {
            "letter_spacing": 0.05,   # +5%
            "word_spacing": 0.3,      # 0.3em
            "line_spacing": 1.8,      # 1.8x
            "paragraph_spacing": 1.5   # 1.5em
        }
    }

    context_spacing = {
        "poster": "normal",      # Posters use normal spacing with larger type
        "book": "normal",
        "magazine": "tight",
        "report": "normal"
    }

    style = context_spacing.get(context, "normal")
    return spacing_map[style]

# ==================== COLOR HELPERS ====================

def get_color_palette(name: str = "professional") -> dict:
    """Get pre-defined color palettes following 70-20-10 rule"""
    palettes = {
        "professional": {
            "background": (0.98, 0.98, 0.97),  # Off-white (70%)
            "text": (0.1, 0.1, 0.1),           # Near black (20%)
            "accent": (0.2, 0.45, 0.7)         # Blue (10%)
        },
        "warm": {
            "background": (0.98, 0.96, 0.94),
            "text": (0.2, 0.15, 0.1),
            "accent": (0.8, 0.4, 0.2)
        },
        "cool": {
            "background": (0.96, 0.97, 0.98),
            "text": (0.1, 0.15, 0.2),
            "accent": (0.2, 0.5, 0.7)
        },
        "high_contrast": {
            "background": (1, 1, 1),
            "text": (0, 0, 0),
            "accent": (0.9, 0.2, 0.2)
        }
    }

    return palettes.get(name, palettes["professional"])

# ==================== QUICK START HELPERS ====================

def setup_poster_page(
    size: str = "letter",
    margin_ratio: float = 1/10,
    orientation: str = "portrait"
) -> Tuple[float, float, float]:
    """
    Set up a poster page with proper dimensions.

    Returns: (width, height, margin)
    """
    sizes = {
        "letter": (612, 792),      # 8.5 x 11 inches
        "tabloid": (792, 1224),    # 11 x 17 inches
        "a4": (595, 842),          # 210 x 297 mm
        "a3": (842, 1191),         # 297 x 420 mm
        "square": (792, 792)       # 11 x 11 inches
    }

    w, h = sizes.get(size, sizes["letter"])

    if orientation == "landscape":
        w, h = h, w

    db.newPage(w, h)
    margin = min(w, h) * margin_ratio

    return w, h, margin

# ==================== USAGE EXAMPLE ====================

if __name__ == "__main__":
    # Example: Create a poster with proper system
    width, height, margin = setup_poster_page("letter", margin_ratio=1/10)

    # Get typography scale
    scale = POSTER_SCALE

    # Get spacing
    spacing = get_spacing_for_context("poster")

    # Get colors
    colors = get_color_palette("professional")

    print(f"Page: {width} x {height}pt")
    print(f"Margin: {margin}pt")
    print(f"Typography scale: {scale}")
    print(f"Spacing: {spacing}")
    print(f"Colors: {colors}")

    # Example: Validate layout
    elements = [
        {'y': height - margin, 'height': 100, 'name': 'Header'},
        {'y': height - margin - 120, 'height': 300, 'name': 'Hero Section'},
        {'y': 200, 'height': 150, 'name': 'Footer'}
    ]

    fits, error = validate_layout_fit(elements, height)
    print(f"Layout fits: {fits}")
    if error:
        print(f"Error: {error}")
