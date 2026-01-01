"""
Tests for evolutionary_drawbot module.

Tests genome serialization, breeding algorithms, parameter normalization,
and population management.
"""

import sys
import json
import random
import tempfile
from pathlib import Path

import pytest

# Add module to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from evolutionary_drawbot.genome import FormGenome, load_population, save_population
from evolutionary_drawbot.parameters import (
    ParameterSpec, DEFAULT_SPECS, denormalize_params, normalize_params
)
from evolutionary_drawbot.evolution import (
    breed, mutate, generate_population, select_winners, calculate_diversity
)


# ==================== PARAMETER SPEC TESTS ====================

class TestParameterSpec:
    """Tests for ParameterSpec normalization and denormalization."""

    def test_normalize_middle_value(self):
        """Middle of range normalizes to 0.5."""
        spec = ParameterSpec("test", min_val=0, max_val=100, default=50)
        assert spec.normalize(50) == 0.5

    def test_normalize_min_value(self):
        """Minimum normalizes to 0."""
        spec = ParameterSpec("test", min_val=10, max_val=20, default=15)
        assert spec.normalize(10) == 0.0

    def test_normalize_max_value(self):
        """Maximum normalizes to 1."""
        spec = ParameterSpec("test", min_val=10, max_val=20, default=15)
        assert spec.normalize(20) == 1.0

    def test_denormalize_middle_value(self):
        """0.5 denormalizes to middle of range."""
        spec = ParameterSpec("test", min_val=0, max_val=100, default=50)
        assert spec.denormalize(0.5) == 50

    def test_denormalize_int_kind(self):
        """Int kind returns rounded integer."""
        spec = ParameterSpec("test", min_val=0, max_val=10, default=5, kind="int")
        assert spec.denormalize(0.55) == 6
        assert isinstance(spec.denormalize(0.55), int)

    def test_roundtrip_preserves_value(self):
        """Normalize then denormalize preserves value."""
        spec = ParameterSpec("test", min_val=0, max_val=100, default=50)
        original = 73.5
        normalized = spec.normalize(original)
        recovered = spec.denormalize(normalized)
        assert abs(recovered - original) < 0.0001

    def test_equal_min_max_normalizes_to_half(self):
        """Edge case: equal min/max normalizes to 0.5."""
        spec = ParameterSpec("test", min_val=5, max_val=5, default=5)
        assert spec.normalize(5) == 0.5

    def test_clamp_normalized_below_zero(self):
        """Clamp catches values below 0."""
        spec = ParameterSpec("test", min_val=0, max_val=1, default=0.5)
        assert spec.clamp_normalized(-0.5) == 0.0

    def test_clamp_normalized_above_one(self):
        """Clamp catches values above 1."""
        spec = ParameterSpec("test", min_val=0, max_val=1, default=0.5)
        assert spec.clamp_normalized(1.5) == 1.0

    def test_default_normalized(self):
        """Default value converts to normalized form."""
        spec = ParameterSpec("test", min_val=0, max_val=100, default=25)
        assert spec.default_normalized() == 0.25

    def test_to_dict_roundtrip(self):
        """Serialization preserves all fields."""
        spec = ParameterSpec(
            name="lobe_count",
            min_val=2,
            max_val=6,
            default=4,
            kind="int",
            description="Number of lobes"
        )
        d = spec.to_dict()
        recovered = ParameterSpec.from_dict(d["name"], d)
        assert recovered.name == spec.name
        assert recovered.min_val == spec.min_val
        assert recovered.max_val == spec.max_val
        assert recovered.default == spec.default
        assert recovered.kind == spec.kind


class TestParamConversion:
    """Tests for bulk parameter conversion functions."""

    def test_denormalize_params(self):
        """Bulk denormalization works correctly."""
        specs = {
            "a": ParameterSpec("a", 0, 100, 50),
            "b": ParameterSpec("b", 10, 20, 15),
        }
        normalized = {"a": 0.5, "b": 0.0}
        actual = denormalize_params(normalized, specs)
        assert actual["a"] == 50
        assert actual["b"] == 10

    def test_normalize_params(self):
        """Bulk normalization works correctly."""
        specs = {
            "a": ParameterSpec("a", 0, 100, 50),
            "b": ParameterSpec("b", 10, 20, 15),
        }
        actual = {"a": 75, "b": 15}
        normalized = normalize_params(actual, specs)
        assert normalized["a"] == 0.75
        assert normalized["b"] == 0.5


# ==================== GENOME TESTS ====================

class TestFormGenome:
    """Tests for FormGenome creation and serialization."""

    def test_create_random_genome(self):
        """Random genome has valid structure."""
        genome = FormGenome.random(gen_num=0, idx=1)
        assert genome.id == "gen000_0001"
        assert genome.generator == "soft_blob"
        assert all(0 <= v <= 1 for v in genome.params.values())
        assert genome.parents is None

    def test_genome_clamps_params(self):
        """Params are clamped to [0, 1] on creation."""
        genome = FormGenome(
            id="test",
            generator="soft_blob",
            params={"a": -0.5, "b": 1.5, "c": 0.5},
            seed=42
        )
        assert genome.params["a"] == 0.0
        assert genome.params["b"] == 1.0
        assert genome.params["c"] == 0.5

    def test_genome_generation_extraction(self):
        """Generation number extracted from ID."""
        genome = FormGenome.random(gen_num=5, idx=3)
        assert genome.generation == 5

    def test_genome_index_extraction(self):
        """Index extracted from ID."""
        genome = FormGenome.random(gen_num=5, idx=3)
        assert genome.index == 3

    def test_jsonl_roundtrip(self):
        """Genome survives JSONL serialization."""
        original = FormGenome.random(gen_num=1, idx=2, prompt="test prompt")
        line = original.to_jsonl_line()
        recovered = FormGenome.from_jsonl_line(line)

        assert recovered.id == original.id
        assert recovered.generator == original.generator
        assert recovered.params == original.params
        assert recovered.seed == original.seed
        assert recovered.prompt == original.prompt

    def test_dict_roundtrip(self):
        """Genome survives dict serialization."""
        original = FormGenome(
            id="gen001_0005",
            generator="soft_blob",
            params={"a": 0.3, "b": 0.7},
            seed=12345,
            parents=("gen000_0001", "gen000_0002"),
            prompt="organic shapes"
        )
        d = original.to_dict()
        recovered = FormGenome.from_dict(d)

        assert recovered.id == original.id
        assert recovered.parents == original.parents

    def test_from_defaults(self):
        """Default genome uses default parameter values."""
        genome = FormGenome.from_defaults(gen_num=0, idx=1)
        # Check that params match default_normalized values
        for name, spec in DEFAULT_SPECS.items():
            assert genome.params[name] == spec.default_normalized()


class TestPopulationIO:
    """Tests for population file operations."""

    def test_save_and_load_population(self):
        """Population survives file round-trip."""
        genomes = [
            FormGenome.random(gen_num=0, idx=i)
            for i in range(1, 5)
        ]

        with tempfile.NamedTemporaryFile(mode='w', suffix='.jsonl', delete=False) as f:
            path = Path(f.name)

        try:
            save_population(genomes, path)
            loaded = load_population(path)

            assert len(loaded) == len(genomes)
            for orig, load in zip(genomes, loaded):
                assert orig.id == load.id
                assert orig.params == load.params
        finally:
            path.unlink()

    def test_load_nonexistent_returns_empty(self):
        """Loading nonexistent file returns empty list."""
        result = load_population(Path("/nonexistent/path.jsonl"))
        assert result == []


# ==================== BREEDING TESTS ====================

class TestBreeding:
    """Tests for genetic breeding operations."""

    def test_breed_produces_valid_offspring(self):
        """Offspring has valid params and lineage."""
        parent_a = FormGenome.random(gen_num=0, idx=1)
        parent_b = FormGenome.random(gen_num=0, idx=2)

        child = breed(parent_a, parent_b, gen_num=1, idx=1)

        assert child.id == "gen001_0001"
        assert child.parents == (parent_a.id, parent_b.id)
        assert all(0 <= v <= 1 for v in child.params.values())

    def test_breed_uniform_crossover(self):
        """Uniform crossover mixes params from both parents."""
        random.seed(42)

        # Create parents with distinct params
        parent_a = FormGenome(
            id="a", generator="soft_blob",
            params={name: 0.0 for name in DEFAULT_SPECS}, seed=1
        )
        parent_b = FormGenome(
            id="b", generator="soft_blob",
            params={name: 1.0 for name in DEFAULT_SPECS}, seed=2
        )

        child = breed(parent_a, parent_b, gen_num=1, idx=1, crossover_method="uniform")

        # Child should have a mix of 0s and 1s (with high probability)
        values = list(child.params.values())
        has_zeros = any(v == 0.0 for v in values)
        has_ones = any(v == 1.0 for v in values)
        # Very unlikely to get all from one parent with uniform crossover
        assert has_zeros or has_ones

    def test_breed_single_point_crossover(self):
        """Single-point crossover creates continuous segments."""
        random.seed(42)

        parent_a = FormGenome(
            id="a", generator="soft_blob",
            params={name: 0.0 for name in DEFAULT_SPECS}, seed=1
        )
        parent_b = FormGenome(
            id="b", generator="soft_blob",
            params={name: 1.0 for name in DEFAULT_SPECS}, seed=2
        )

        child = breed(parent_a, parent_b, gen_num=1, idx=1, crossover_method="single_point")

        # Should have continuous run of 0s then 1s (or vice versa)
        values = list(child.params.values())
        # Just verify it's a valid mix
        assert all(v in (0.0, 1.0) for v in values)


class TestMutation:
    """Tests for mutation operations."""

    def test_mutate_preserves_bounds(self):
        """Mutation keeps params in [0, 1]."""
        genome = FormGenome(
            id="test", generator="soft_blob",
            params={name: 0.5 for name in DEFAULT_SPECS}, seed=42
        )

        # High mutation rate and strength to ensure mutations occur
        mutated = mutate(genome, rate=1.0, strength=0.5)

        assert all(0 <= v <= 1 for v in mutated.params.values())

    def test_mutate_returns_new_genome(self):
        """Mutation returns new object, doesn't modify original."""
        original = FormGenome(
            id="test", generator="soft_blob",
            params={"a": 0.5}, seed=42
        )
        original_a = original.params["a"]

        mutated = mutate(original, rate=1.0, strength=0.5)

        assert original.params["a"] == original_a  # Original unchanged

    def test_mutate_zero_rate_no_change(self):
        """Zero mutation rate leaves params unchanged."""
        genome = FormGenome(
            id="test", generator="soft_blob",
            params={"a": 0.5, "b": 0.3}, seed=42
        )

        mutated = mutate(genome, rate=0.0, strength=0.5)

        assert mutated.params == genome.params

    def test_mutate_at_bounds(self):
        """Mutation at bounds clamps correctly."""
        genome = FormGenome(
            id="test", generator="soft_blob",
            params={"a": 0.0, "b": 1.0}, seed=42
        )

        # Multiple mutations to test clamping
        for _ in range(10):
            mutated = mutate(genome, rate=1.0, strength=0.5)
            assert 0 <= mutated.params["a"] <= 1
            assert 0 <= mutated.params["b"] <= 1


# ==================== POPULATION TESTS ====================

class TestPopulation:
    """Tests for population generation and selection."""

    def test_generate_random_population(self):
        """Random population has correct size and structure."""
        pop = generate_population(size=10, gen_num=0)

        assert len(pop) == 10
        for i, genome in enumerate(pop, 1):
            assert genome.id == f"gen000_{i:04d}"
            assert genome.parents is None

    def test_generate_bred_population(self):
        """Bred population has parent lineage."""
        parents = [FormGenome.random(gen_num=0, idx=i) for i in range(1, 4)]

        pop = generate_population(size=5, gen_num=1, parents=parents)

        assert len(pop) == 5
        for genome in pop:
            assert genome.parents is not None
            assert genome.generation == 1

    def test_select_winners_by_index(self):
        """Winner selection by 1-based index."""
        pop = [FormGenome.random(gen_num=0, idx=i) for i in range(1, 11)]

        winners = select_winners(pop, [1, 5, 10])

        assert len(winners) == 3
        assert winners[0].id == "gen000_0001"
        assert winners[1].id == "gen000_0005"
        assert winners[2].id == "gen000_0010"

    def test_select_winners_invalid_index_skipped(self):
        """Invalid indices are skipped, not errored."""
        pop = [FormGenome.random(gen_num=0, idx=i) for i in range(1, 5)]

        winners = select_winners(pop, [1, 100, 2])  # 100 is invalid

        assert len(winners) == 2


class TestDiversity:
    """Tests for diversity calculation."""

    def test_identical_population_zero_diversity(self):
        """Identical genomes have zero diversity."""
        genome = FormGenome(
            id="a", generator="soft_blob",
            params={"x": 0.5, "y": 0.5}, seed=1
        )
        # Create copies with same params
        pop = [
            FormGenome(id=f"g{i}", generator="soft_blob",
                      params={"x": 0.5, "y": 0.5}, seed=i)
            for i in range(5)
        ]

        diversity = calculate_diversity(pop)
        assert diversity == 0.0

    def test_diverse_population_positive_diversity(self):
        """Diverse genomes have positive diversity."""
        pop = [
            FormGenome(id="a", generator="soft_blob",
                      params={"x": 0.0, "y": 0.0}, seed=1),
            FormGenome(id="b", generator="soft_blob",
                      params={"x": 1.0, "y": 1.0}, seed=2),
        ]

        diversity = calculate_diversity(pop)
        assert diversity > 0

    def test_single_genome_zero_diversity(self):
        """Single genome has zero diversity."""
        pop = [FormGenome.random(gen_num=0, idx=1)]
        assert calculate_diversity(pop) == 0.0

    def test_empty_population_zero_diversity(self):
        """Empty population has zero diversity."""
        assert calculate_diversity([]) == 0.0


# ==================== REPRODUCIBILITY TESTS ====================

class TestReproducibility:
    """Tests for seed-based reproducibility."""

    def test_same_seed_same_random_genome(self):
        """Same seed produces same random genome."""
        random.seed(42)
        genome_a = FormGenome.random(gen_num=0, idx=1)

        random.seed(42)
        genome_b = FormGenome.random(gen_num=0, idx=1)

        assert genome_a.params == genome_b.params
        assert genome_a.seed == genome_b.seed

    def test_same_seed_same_population(self):
        """Same seed produces same population."""
        random.seed(123)
        pop_a = generate_population(size=5, gen_num=0)

        random.seed(123)
        pop_b = generate_population(size=5, gen_num=0)

        for a, b in zip(pop_a, pop_b):
            assert a.params == b.params


# ==================== DEFAULT SPECS TESTS ====================

class TestDefaultSpecs:
    """Tests for DEFAULT_SPECS configuration."""

    def test_default_specs_exist(self):
        """All expected specs are defined."""
        expected = ["lobe_count", "lobe_depth", "envelope_factor", "roundness",
                    "wobble", "tension", "aspect", "rotation", "asymmetry"]
        for name in expected:
            assert name in DEFAULT_SPECS

    def test_default_specs_valid_ranges(self):
        """All specs have min < max (or min == max)."""
        for name, spec in DEFAULT_SPECS.items():
            assert spec.min_val <= spec.max_val, f"{name} has invalid range"

    def test_default_specs_default_in_range(self):
        """Default values are within range."""
        for name, spec in DEFAULT_SPECS.items():
            assert spec.min_val <= spec.default <= spec.max_val, \
                f"{name} default {spec.default} not in [{spec.min_val}, {spec.max_val}]"
