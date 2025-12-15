"""
Evolutionary DrawBot Form Generation System

A parametric form generation and breeding system for creating organic visual forms.

Usage:
    from evolutionary_drawbot import FormGenome, ParameterSpec, generate_soft_blob

CLI:
    uv run python -m evolutionary_drawbot gen0 --population 16
    uv run python -m evolutionary_drawbot render gen_000
    uv run python -m evolutionary_drawbot select gen_000 --winners 3,7,12
    uv run python -m evolutionary_drawbot breed gen_000
"""

from .parameters import ParameterSpec, DEFAULT_SPECS, load_specs_from_config
from .genome import FormGenome

__all__ = [
    'ParameterSpec',
    'DEFAULT_SPECS',
    'load_specs_from_config',
    'FormGenome',
]

__version__ = '0.1.0'
