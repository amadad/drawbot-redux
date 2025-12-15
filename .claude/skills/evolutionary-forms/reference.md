# API Reference

Complete reference for the evolutionary_drawbot package.

## Module: `parameters`

### ParameterSpec

```python
from evolutionary_drawbot.parameters import ParameterSpec, DEFAULT_SPECS

@dataclass
class ParameterSpec:
    name: str           # Parameter name
    min_val: float      # Minimum actual value
    max_val: float      # Maximum actual value
    default: float      # Default actual value
    kind: str           # "float" or "int"
    description: str    # Human-readable description

    def normalize(self, value: float) -> float
        """Map actual value to [0..1]"""

    def denormalize(self, norm: float) -> float
        """Map [0..1] to actual value"""

    def clamp_normalized(self, norm: float) -> float
        """Clamp to [0..1]"""

    def default_normalized(self) -> float
        """Get default in normalized form"""
```

### DEFAULT_SPECS

Pre-defined specs for soft_blob generator:

```python
DEFAULT_SPECS = {
    "lobe_count": ParameterSpec("lobe_count", 2, 6, 4, "int"),
    "lobe_depth": ParameterSpec("lobe_depth", 0.0, 1.0, 0.3),
    "envelope_factor": ParameterSpec("envelope_factor", 0.3, 0.9, 0.6),
    "roundness": ParameterSpec("roundness", 0.0, 1.0, 0.7),
    "wobble": ParameterSpec("wobble", 0.0, 0.2, 0.05),
    "tension": ParameterSpec("tension", 0.3, 0.9, 0.6),
    "aspect": ParameterSpec("aspect", 0.6, 1.4, 1.0),
    "rotation": ParameterSpec("rotation", 0, 360, 0),
}
```

### Functions

```python
def load_specs_from_config(config_path: Path) -> Dict[str, ParameterSpec]
    """Load specs from brand_dna.json, falling back to defaults"""

def denormalize_params(normalized: Dict[str, float], specs) -> Dict[str, float]
    """Convert all normalized params to actual values"""

def normalize_params(actual: Dict[str, float], specs) -> Dict[str, float]
    """Convert all actual params to normalized [0..1]"""
```

---

## Module: `genome`

### FormGenome

```python
from evolutionary_drawbot.genome import FormGenome

@dataclass
class FormGenome:
    id: str                              # "gen000_0001"
    generator: str                       # "soft_blob"
    params: Dict[str, float]             # Normalized [0..1] values
    seed: int                            # RNG seed for reproducibility
    parents: Optional[Tuple[str, str]]   # Parent IDs if bred
    prompt: Optional[str]                # Source prompt if any
    created_at: float                    # Unix timestamp

    @property
    def generation(self) -> int
        """Extract generation number from ID"""

    @property
    def index(self) -> int
        """Extract 1-based index within generation"""

    def to_dict(self) -> dict
    def to_jsonl_line(self) -> str

    @classmethod
    def from_dict(cls, d: dict) -> 'FormGenome'

    @classmethod
    def from_jsonl_line(cls, line: str) -> 'FormGenome'

    @classmethod
    def random(
        cls,
        gen_num: int,
        idx: int,
        specs: Optional[Dict[str, ParameterSpec]] = None,
        generator: str = "soft_blob",
        prompt: Optional[str] = None,
        constraints: Optional[Dict[str, Tuple[float, float]]] = None
    ) -> 'FormGenome'
        """Generate random genome with optional constraints"""

    @classmethod
    def from_defaults(cls, gen_num: int, idx: int, ...) -> 'FormGenome'
        """Create genome with all default values"""
```

### Persistence Functions

```python
def load_population(jsonl_path: Path) -> List[FormGenome]
    """Load population from JSONL file"""

def save_population(genomes: List[FormGenome], jsonl_path: Path) -> None
    """Save population to JSONL file"""
```

---

## Module: `evolution`

### Breeding

```python
from evolutionary_drawbot.evolution import breed, mutate, generate_population

def breed(
    parent_a: FormGenome,
    parent_b: FormGenome,
    gen_num: int,
    idx: int,
    crossover_method: str = "uniform"  # or "single_point"
) -> FormGenome
    """Create offspring via crossover"""

def mutate(
    genome: FormGenome,
    rate: float = 0.2,       # Probability per parameter
    strength: float = 0.15   # Max perturbation magnitude
) -> FormGenome
    """Apply random mutations (returns new genome)"""

def generate_population(
    size: int,
    gen_num: int,
    parents: Optional[List[FormGenome]] = None,
    specs: Optional[Dict[str, ParameterSpec]] = None,
    prompt_constraints: Optional[Dict[str, Tuple[float, float]]] = None,
    mutation_rate: float = 0.2,
    mutation_strength: float = 0.15,
    generator: str = "soft_blob"
) -> List[FormGenome]
    """Generate population (random if no parents, bred otherwise)"""
```

### Selection

```python
def select_winners(
    population: List[FormGenome],
    winner_indices: List[int]  # 1-based
) -> List[FormGenome]
    """Select genomes by index"""

def calculate_diversity(population: List[FormGenome]) -> float
    """Calculate genetic diversity (average pairwise distance)"""
```

---

## Module: `translator`

### Translation

```python
from evolutionary_drawbot.translator import translate_prompt

def translate_prompt(prompt: str) -> Dict[str, Tuple[float, float]]
    """Convert natural language to parameter constraints

    Returns: {param_name: (min_normalized, max_normalized)}
    """

# Example:
constraints = translate_prompt("soft protective 4 lobes")
# {'roundness': (0.7, 1.0), 'tension': (0.5, 0.8), ...}
```

### Utilities

```python
def get_available_keywords() -> List[str]
    """Return all recognized keywords"""

def get_keyword_categories() -> Dict[str, List[str]]
    """Return keywords organized by category"""

def explain_constraints(constraints: Dict[str, Tuple[float, float]]) -> str
    """Generate human-readable constraint explanation"""
```

---

## Module: `form_generators`

### soft_blob

```python
from evolutionary_drawbot.form_generators import generate_soft_blob, GENERATORS

def generate_soft_blob(
    genome: FormGenome,
    center: Tuple[float, float],
    size: float,
    specs: Optional[Dict[str, ParameterSpec]] = None
) -> BezierPath
    """Generate organic bezier form from genome"""

# Generator registry
GENERATORS = {
    "soft_blob": generate_soft_blob,
}
```

---

## Module: `render`

### Rendering

```python
from evolutionary_drawbot.render import render_genome, render_population

def render_genome(
    genome: FormGenome,
    output_dir: Path,
    canvas_size: Tuple[float, float] = (200, 200),
    format: str = "svg",  # "svg", "pdf", "png"
    style: Optional[Dict[str, Any]] = None,
    specs: Optional[Dict[str, ParameterSpec]] = None
) -> Tuple[Path, Path]
    """Render genome to image + metadata JSON

    Returns: (image_path, metadata_path)
    """

def render_population(
    genomes: List[FormGenome],
    output_dir: Path,
    ...
) -> List[Tuple[Path, Path]]
    """Render all genomes in population"""
```

### Style Dictionary

```python
style = {
    "fill_color": [0.2, 0.25, 0.35],    # RGB 0-1
    "stroke_color": [0.1, 0.12, 0.18],
    "stroke_width": 1.5,
    "background": [1.0, 1.0, 1.0],
}
```

---

## Module: `contact_sheet`

```python
from evolutionary_drawbot.contact_sheet import generate_contact_sheet

def generate_contact_sheet(
    genomes: List[FormGenome],
    output_path: Path,
    cols: int = 4,
    rows: int = 4,
    page_size: Tuple[float, float] = (612, 792),  # Letter
    margin: float = 40,
    style: Optional[Dict[str, Any]] = None,
    specs: Optional[Dict[str, ParameterSpec]] = None,
    title: Optional[str] = None
) -> Path
    """Generate multi-page PDF contact sheet"""

def generate_selection_summary(
    genomes: List[FormGenome],
    winner_indices: List[int],
    output_path: Path,
    ...
) -> Path
    """Generate summary PDF of selected winners only"""
```

---

## Configuration: `brand_dna.json`

```json
{
  "parameter_specs": {
    "lobe_count": {"min": 2, "max": 6, "default": 4, "kind": "int"},
    "lobe_depth": {"min": 0.0, "max": 1.0, "default": 0.3},
    ...
  },
  "style": {
    "fill_color": [0.2, 0.25, 0.35],
    "stroke_color": [0.1, 0.12, 0.18],
    "stroke_width": 1.5,
    "background": [1.0, 1.0, 1.0]
  },
  "evolution": {
    "default_population_size": 16,
    "mutation_rate": 0.2,
    "mutation_strength": 0.15
  },
  "generators": ["soft_blob"],
  "version": "1.0.0"
}
```

---

## File Formats

### population.jsonl

One genome per line:
```json
{"id": "gen000_0001", "generator": "soft_blob", "params": {"lobe_count": 0.5, ...}, "seed": 12345, "parents": null, "prompt": "soft protective", "created_at": 1702627200.0}
```

### winners.json

```json
{
  "generation": 0,
  "population_size": 16,
  "winner_indices": [1, 5, 9, 13],
  "winner_ids": ["gen000_0001", "gen000_0005", ...]
}
```

### *_meta.json

```json
{
  "genome": { ... full genome dict ... },
  "render_info": {
    "canvas_size": [200, 200],
    "format": "svg",
    "style": { ... },
    "rendered_at": 1702627200.0
  },
  "generator_info": {
    "name": "soft_blob",
    "version": "1.0.0"
  }
}
```
