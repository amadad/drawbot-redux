# Design Foundations

This directory contains the foundational design systems for the DrawBot Design Library.

## Typography Systems

The typography systems module provides comprehensive typographic tools and demonstrations based on classical design principles.

### Features

- **Modular Type Scales**: Generate harmonious type scales using golden ratio, musical scale, or classic ratios
- **Baseline Grid**: Create consistent vertical rhythm with baseline grids
- **Hierarchy Demonstrations**: Compare good vs bad typographic hierarchy
- **Advanced Features**: FormattedString examples with mixed styles, tracking, and baseline shifts
- **Type Specimens**: Visual type scale demonstrations

### Usage

#### Basic Import

```python
import sys
import os

# Add project root to Python path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_root)

import drawBot as db
from typography_systems import calculate_type_scale, GOLDEN_RATIO, BASELINE_UNIT
```

#### Generate Type Scale

```python
# Generate a 5-step scale starting at 12pt using golden ratio
sizes = calculate_type_scale(12, GOLDEN_RATIO, 5)
# Result: [12.0, 19.416, 31.416, 50.832, 82.248]
```

#### Run Demonstrations

```python
from typography_systems import demonstrate_hierarchy, demonstrate_advanced_features, create_type_specimen

# Run all demonstrations
demonstrate_hierarchy()
demonstrate_advanced_features()
create_type_specimen()

# Save output
db.saveImage("typography_output.pdf")
```

### Design Constants

- `GOLDEN_RATIO = 1.618` - Classical golden ratio for type scaling
- `MUSICAL_SCALE = 1.25` - Major third interval
- `CLASSIC_SCALE = 1.333` - Perfect fourth interval
- `BASELINE_UNIT = 8` - Baseline grid unit in points

### Color Palette

- `BLACK = (0, 0, 0)`
- `GRAY_DARK = (0.2, 0.2, 0.2)`
- `GRAY_MID = (0.5, 0.5, 0.5)`
- `GRAY_LIGHT = (0.8, 0.8, 0.8)`
- `RED_ACCENT = (0.9, 0.1, 0.1)`

## Running the Examples

### From Project Root

```bash
# Activate virtual environment
source .venv/bin/activate

# Run typography systems
python drawbot-design-library/foundations/run_typography.py

# Run simple example
python drawbot-design-library/examples/typography_example.py
```

### From Foundations Directory

```bash
cd drawbot-design-library/foundations
source ../../.venv/bin/activate
python run_typography.py
```

## Output Files

The demonstrations generate PDF files in the `output/` directory:

- `typography_systems_output.pdf` - Full typography systems demonstration
- `typography_example.pdf` - Simple typography example
- `test_typography_output.pdf` - Test output

## Design Principles

The typography systems are based on:

1. **Emil Ruder's Typographie** - Swiss design principles
2. **Jan Tschichold's Principles** - Classical typography rules
3. **Modular Scale Theory** - Mathematical relationships in type
4. **Baseline Grid Systems** - Consistent vertical rhythm

## Troubleshooting

### ModuleNotFoundError: No module named 'drawBot'

This error occurs when the local DrawBot module isn't in the Python path. The scripts in this directory handle this automatically by adding the project root to `sys.path`.

### OpenType Features

Some OpenType features may not be available in all DrawBot versions. The code includes fallbacks and comments for compatibility.

## Next Steps

- Explore the `color_theory.py` module for color systems
- Check `composition_rules.py` for layout principles
- Review `grid_systems.py` for grid-based layouts 