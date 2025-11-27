"""
DrawBot Design System - Enforces professional design principles.

This module provides:
1. Typography scales (poster, book, magazine, report)
2. Point-based text wrapping (real measurements, not character heuristics)
3. Layout validation (overlap detection, boundary checks)
4. Portable path handling

Based on principles from:
- Hochuli: Detail in Typography
- Bringhurst: Elements of Typographic Style
- Müller-Brockmann: Grid Systems

Usage:
    from drawbot_design_system import (
        POSTER_SCALE, setup_poster_page, draw_wrapped_text, get_output_path
    )
"""

from pathlib import Path
from typing import Tuple, List, Optional, Dict, Any
from dataclasses import dataclass

# Lazy import drawBot to allow core-only installs that don't use drawing functions
_db = None

def _get_db():
    """Lazy-load drawBot on first use, with clear error if not installed."""
    global _db
    if _db is None:
        try:
            import drawBot as db_module
            _db = db_module
        except ImportError:
            raise ImportError(
                "drawBot is required for drawing functions but is not installed.\n"
                "Install with: uv sync --extra drawbot\n"
                "Or: pip install drawBot"
            )
    return _db

# Create a proxy that lazy-loads on attribute access
class _DrawBotProxy:
    def __getattr__(self, name):
        return getattr(_get_db(), name)

db = _DrawBotProxy()

__all__ = [
    # Path management
    'REPO_ROOT', 'OUTPUT_DIR', 'get_output_path',
    # Typography scales
    'TypographyScale', 'POSTER_SCALE', 'MAGAZINE_SCALE', 'BOOK_SCALE', 'REPORT_SCALE',
    'create_typography_scale',
    # Scale ratios
    'MINOR_SECOND', 'MAJOR_SECOND', 'MINOR_THIRD', 'MAJOR_THIRD',
    'PERFECT_FOURTH', 'PERFECT_FIFTH', 'GOLDEN_RATIO',
    # Text functions
    'get_text_metrics', 'wrap_text_to_width', 'draw_wrapped_text',
    # Layout
    'validate_layout_fit', 'setup_poster_page',
    # Helpers
    'get_spacing_for_context', 'get_color_palette',
]

# ==================== PATH MANAGEMENT ====================

REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = REPO_ROOT / "output"

def _ensure_output_dir():
    """Create output directory on first use (not at import time)."""
    OUTPUT_DIR.mkdir(exist_ok=True)

def get_output_path(filename: str) -> Path:
    """Get absolute path for output file (works on any machine)."""
    _ensure_output_dir()
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
        descender = db.fontDescender()  # Should be negative
        line_height = db.fontLineHeight()
        x_height = db.fontXHeight()
        cap_height = db.fontCapHeight()
    except Exception as e:
        # Fallback if metrics not available
        # Log warning so issues don't go unnoticed
        import warnings
        warnings.warn(f"Could not get font metrics for '{font}' at {size}pt: {e}")
        ascender = size * 0.8
        descender = -size * 0.2  # Descender should be negative (below baseline)
        line_height = size * 1.2
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

    Measures each word with DrawBot to ensure accurate line breaks.
    Handles variable-width fonts correctly (unlike character-count methods).

    Args:
        text: Text to wrap
        width_in_points: Maximum line width in points
        font: Font name
        size: Font size in points

    Returns:
        List of wrapped lines
    """
    db.font(font)
    db.fontSize(size)

    words = text.split()
    if not words:
        return []

    lines = []
    current_line_words = []
    current_line_width = 0.0
    space_width, _ = db.textSize(" ")

    for word in words:
        word_width, _ = db.textSize(word)

        # Calculate width if we add this word
        if current_line_words:
            test_width = current_line_width + space_width + word_width
        else:
            test_width = word_width

        if test_width <= width_in_points:
            # Word fits on current line
            current_line_words.append(word)
            current_line_width = test_width
        else:
            # Word doesn't fit - start new line
            if current_line_words:
                lines.append(" ".join(current_line_words))

            # Handle words wider than the box (long URLs, etc.)
            if word_width > width_in_points:
                # Break the word into multiple chunks
                chunks = _break_long_word(word, width_in_points, font, size)
                # Add all but the last chunk as separate lines
                for chunk in chunks[:-1]:
                    lines.append(chunk)
                # Start new line with final chunk (may continue with more words)
                if chunks:
                    last_chunk = chunks[-1]
                    last_width, _ = db.textSize(last_chunk)
                    current_line_words = [last_chunk]
                    current_line_width = last_width
                else:
                    current_line_words = []
                    current_line_width = 0.0
            else:
                current_line_words = [word]
                current_line_width = word_width

    # Don't forget the last line
    if current_line_words:
        lines.append(" ".join(current_line_words))

    return lines


def _break_long_word(word: str, max_width: float, font: str, size: float) -> List[str]:
    """
    Break a word that's too wide for the column into multiple chunks.

    Returns a list of chunks, each fitting within max_width (with hyphens added
    to all but the last chunk).
    """
    db.font(font)
    db.fontSize(size)

    hyphen_width, _ = db.textSize("-")
    available = max_width - hyphen_width

    chunks = []
    remaining = word

    while remaining:
        # Check if remainder fits without hyphen
        remaining_width, _ = db.textSize(remaining)
        if remaining_width <= max_width:
            chunks.append(remaining)
            break

        # Find how many characters fit with hyphen
        found_break = False
        for i in range(len(remaining), 0, -1):
            part_width, _ = db.textSize(remaining[:i])
            if part_width <= available:
                chunks.append(remaining[:i] + "-")
                remaining = remaining[i:]
                found_break = True
                break

        # Fallback: take at least one character to avoid infinite loop
        if not found_break:
            if remaining:
                chunks.append(remaining[0] + "-")
                remaining = remaining[1:]
            else:
                break

    return chunks if chunks else [""]

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

def validate_layout_fit(
    elements: List[Dict[str, Any]],
    page_height: float,
    page_width: Optional[float] = None
) -> Tuple[bool, Optional[str]]:
    """
    Validate that all elements fit on page without overlapping.

    Coordinate system: DrawBot uses bottom-left origin.
    - y is the TOP of the element
    - Element extends from y down to (y - height)

    Args:
        elements: List of dicts with:
            - 'y': float - Top Y coordinate
            - 'height': float - Element height
            - 'name': str - Element name for error messages
            - 'x': float (optional) - Left X coordinate
            - 'width': float (optional) - Element width
        page_height: Total page height
        page_width: Total page width (optional, for horizontal checks)

    Returns:
        (fits: bool, error_message: Optional[str])
    """
    if not elements:
        return True, None

    # Sort by y position (top to bottom, highest y first)
    sorted_elements = sorted(elements, key=lambda e: e['y'], reverse=True)

    for i, elem in enumerate(sorted_elements):
        elem_top = elem['y']
        elem_bottom = elem['y'] - elem['height']
        elem_name = elem.get('name', f'Element {i}')

        # Check if element extends above page
        if elem_top > page_height:
            overhang = elem_top - page_height
            return False, f"{elem_name} extends {overhang:.1f}pt above page top"

        # Check if element extends below page
        if elem_bottom < 0:
            return False, f"{elem_name} extends {abs(elem_bottom):.1f}pt below page bottom"

        # Check horizontal bounds if provided
        if page_width and 'x' in elem and 'width' in elem:
            if elem['x'] < 0:
                return False, f"{elem_name} extends {abs(elem['x']):.1f}pt past left edge"
            if elem['x'] + elem['width'] > page_width:
                overhang = (elem['x'] + elem['width']) - page_width
                return False, f"{elem_name} extends {overhang:.1f}pt past right edge"

        # Check for overlaps with elements below
        if i < len(sorted_elements) - 1:
            next_elem = sorted_elements[i + 1]
            next_top = next_elem['y']
            next_name = next_elem.get('name', f'Element {i+1}')

            # Overlap occurs if current bottom is below next top
            if elem_bottom < next_top:
                overlap = next_top - elem_bottom
                return False, f"{elem_name} overlaps {next_name} by {overlap:.1f}pt"

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
