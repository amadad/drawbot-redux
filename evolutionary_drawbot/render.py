"""
Render genomes to visual output files.

Each genome is rendered to an SVG/PDF file along with a metadata JSON file
that captures all parameters, seed, lineage, and generation info.
"""

import json
import time
from pathlib import Path
from typing import Tuple, Dict, Any, Optional, List

from .genome import FormGenome
from .parameters import DEFAULT_SPECS, ParameterSpec, load_specs_from_config
from .form_generators import GENERATORS


# Lazy DrawBot import
_db = None


def _get_db():
    """Lazy-load drawBot on first use."""
    global _db
    if _db is None:
        try:
            import drawBot as db_module
            _db = db_module
        except ImportError:
            raise ImportError(
                "drawBot is required for rendering but is not installed.\n"
                "Install with: uv sync --extra drawbot"
            )
    return _db


def _render_dot_field(db, form_data: Dict[str, Any], style: Dict[str, Any]):
    """Render a dot field."""
    fill_color = style.get("fill_color", [0.2, 0.25, 0.35])
    dots = form_data.get('dots', [])

    db.fill(*fill_color)
    db.stroke(None)

    for x, y, radius in dots:
        db.oval(x - radius/2, y - radius/2, radius, radius)


def _render_accent_nodes(db, form_data: Dict[str, Any], style: Dict[str, Any]):
    """Render accent nodes."""
    fill_color = style.get("fill_color", [0.2, 0.25, 0.35])
    nodes = form_data.get('nodes', [])

    db.fill(*fill_color)
    db.stroke(None)

    for x, y, radius in nodes:
        db.oval(x - radius/2, y - radius/2, radius, radius)


def _render_layered_form(db, form_data: Dict[str, Any], style: Dict[str, Any]):
    """Render a layered compound form with multiple layers."""
    # Get colors from style, with defaults
    primary_color = style.get("fill_color", [0.8, 0.2, 0.6])  # Pink default
    shadow_color = style.get("shadow_color", [0.85, 0.85, 0.88])

    for layer in form_data.get('layers', []):
        layer_name = layer.get('name', '')

        if layer_name == 'shadow':
            # Draw shadow fill
            path = layer.get('path')
            if path:
                fill_color = layer.get('fill_color', shadow_color)
                db.fill(*fill_color)
                db.stroke(None)
                db.drawPath(path)

        elif layer_name == 'outline':
            # Draw stroke outline (no fill)
            path = layer.get('path')
            if path:
                stroke_weight = layer.get('stroke_weight', 1.5)
                db.fill(None)
                db.stroke(*primary_color)
                db.strokeWidth(stroke_weight)
                db.drawPath(path)

        elif layer_name == 'dots':
            # Draw interior dot grid
            dots = layer.get('dots', [])
            db.fill(*primary_color)
            db.stroke(None)
            for x, y, radius in dots:
                db.oval(x - radius/2, y - radius/2, radius, radius)

        elif layer_name == 'accents':
            # Draw accent dots
            dots = layer.get('dots', [])
            db.fill(*primary_color)
            db.stroke(None)
            for x, y, radius in dots:
                db.oval(x - radius/2, y - radius/2, radius, radius)


def render_genome(
    genome: FormGenome,
    output_dir: Path,
    canvas_size: Tuple[float, float] = (200, 200),
    format: str = "svg",
    style: Optional[Dict[str, Any]] = None,
    specs: Optional[Dict[str, ParameterSpec]] = None
) -> Tuple[Path, Path]:
    """
    Render a genome to an image file and metadata JSON.

    Args:
        genome: The FormGenome to render
        output_dir: Directory to save output files
        canvas_size: (width, height) of canvas in points
        format: Output format ("svg", "pdf", "png")
        style: Optional style dict with fill_color, stroke_color, stroke_width
        specs: Parameter specifications for denormalization

    Returns:
        Tuple of (image_path, metadata_path)
    """
    db = _get_db()

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Default style
    style = style or {
        "fill_color": [0.2, 0.25, 0.35],
        "stroke_color": [0.1, 0.12, 0.18],
        "stroke_width": 1.5,
        "background": [1.0, 1.0, 1.0],
    }

    specs = specs or DEFAULT_SPECS

    # Get the generator function
    generator_func = GENERATORS.get(genome.generator)
    if not generator_func:
        raise ValueError(f"Unknown generator: {genome.generator}")

    # Set up canvas
    width, height = canvas_size
    db.newDrawing()
    db.newPage(width, height)

    # Background
    bg = style.get("background", [1.0, 1.0, 1.0])
    db.fill(*bg)
    db.rect(0, 0, width, height)

    # Generate and draw the form
    center = (width / 2, height / 2)
    size = min(width, height) * 0.8

    result = generator_func(genome, center, size, specs)

    # Check result type and render accordingly
    if isinstance(result, dict):
        result_type = result.get('type', '')
        if result_type == 'layered':
            _render_layered_form(db, result, style)
        elif result_type == 'dot_field':
            _render_dot_field(db, result, style)
        elif result_type == 'accent_nodes':
            _render_accent_nodes(db, result, style)
        else:
            # Unknown dict type, try to render as simple form
            pass
    else:
        # Simple path rendering (BezierPath)
        path = result
        fill = style.get("fill_color", [0.2, 0.25, 0.35])
        stroke = style.get("stroke_color")
        stroke_width = style.get("stroke_width", 0)

        # For shape_outline, we want stroke only
        if genome.generator == "shape_outline":
            db.fill(None)
            db.stroke(*fill)  # Use fill color as stroke
            db.strokeWidth(stroke_width if stroke_width > 0 else 1.5)
        else:
            db.fill(*fill)
            if stroke and stroke_width > 0:
                db.stroke(*stroke)
                db.strokeWidth(stroke_width)
            else:
                db.stroke(None)
        db.drawPath(path)

    # Determine output paths
    file_base = f"{genome.index:04d}"
    image_path = output_dir / f"{file_base}.{format}"
    meta_path = output_dir / f"{file_base}_meta.json"

    # Save image
    db.saveImage(str(image_path))
    db.endDrawing()

    # Save metadata
    metadata = {
        "genome": genome.to_dict(),
        "render_info": {
            "canvas_size": list(canvas_size),
            "format": format,
            "style": style,
            "rendered_at": time.time(),
        },
        "generator_info": {
            "name": genome.generator,
            "version": "1.0.0",
        }
    }

    with open(meta_path, 'w') as f:
        json.dump(metadata, f, indent=2)

    return image_path, meta_path


def render_population(
    genomes: List[FormGenome],
    output_dir: Path,
    canvas_size: Tuple[float, float] = (200, 200),
    format: str = "svg",
    style: Optional[Dict[str, Any]] = None,
    specs: Optional[Dict[str, ParameterSpec]] = None
) -> List[Tuple[Path, Path]]:
    """
    Render all genomes in a population.

    Args:
        genomes: List of FormGenome to render
        output_dir: Directory to save output files
        canvas_size: (width, height) of canvas
        format: Output format
        style: Style dict
        specs: Parameter specifications

    Returns:
        List of (image_path, metadata_path) tuples
    """
    results = []

    for genome in genomes:
        image_path, meta_path = render_genome(
            genome, output_dir, canvas_size, format, style, specs
        )
        results.append((image_path, meta_path))

    return results
