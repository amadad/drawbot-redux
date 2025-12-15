"""
Command-line interface for evolutionary form generation.

Commands:
    init        Initialize project with brand_dna.json
    gen0        Generate initial population (generation 0)
    render      Render candidates and create contact sheet
    select      Record selected winners
    breed       Breed next generation from winners
    status      Show current evolution status
"""

import argparse
import json
import sys
from pathlib import Path
from typing import List, Optional

# Project paths
REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = REPO_ROOT / "output"
GENERATIONS_DIR = OUTPUT_DIR / "generations"
CONFIG_DIR = REPO_ROOT / "config"
DEFAULT_CONFIG = CONFIG_DIR / "brand_dna.json"


def get_generation_dir(gen_num: int) -> Path:
    """Get directory for a specific generation."""
    return GENERATIONS_DIR / f"gen_{gen_num:03d}"


def get_latest_generation() -> int:
    """Find the highest generation number that exists."""
    if not GENERATIONS_DIR.exists():
        return -1

    gen_nums = []
    for d in GENERATIONS_DIR.iterdir():
        if d.is_dir() and d.name.startswith("gen_"):
            try:
                gen_nums.append(int(d.name.split("_")[1]))
            except (ValueError, IndexError):
                pass

    return max(gen_nums) if gen_nums else -1


def load_config() -> dict:
    """Load brand_dna.json configuration."""
    if DEFAULT_CONFIG.exists():
        with open(DEFAULT_CONFIG, 'r') as f:
            return json.load(f)
    return {}


def cmd_init(args):
    """Initialize project directories and config."""
    print("Initializing evolutionary DrawBot project...")

    # Create directories
    GENERATIONS_DIR.mkdir(parents=True, exist_ok=True)
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)

    print(f"  Created: {GENERATIONS_DIR}")
    print(f"  Created: {CONFIG_DIR}")

    # Check for config
    if DEFAULT_CONFIG.exists():
        print(f"  Config exists: {DEFAULT_CONFIG}")
    else:
        print(f"  Warning: No config at {DEFAULT_CONFIG}")
        print("  Create config/brand_dna.json to customize parameters")

    print("\nReady! Next steps:")
    print("  1. Run: uv run python -m evolutionary_drawbot gen0 --population 16")
    print("  2. View contact sheet and select winners")
    print("  3. Run: uv run python -m evolutionary_drawbot select gen_000 --winners 3,7,12")
    print("  4. Run: uv run python -m evolutionary_drawbot breed gen_000")


def cmd_gen0(args):
    """Generate initial population (generation 0)."""
    from .parameters import load_specs_from_config
    from .genome import FormGenome, save_population
    from .translator import translate_prompt, explain_constraints
    from .evolution import generate_population
    from .render import render_population
    from .contact_sheet import generate_contact_sheet

    config = load_config()
    specs = load_specs_from_config(DEFAULT_CONFIG)
    style = config.get("style", {})

    gen_num = 0
    gen_dir = get_generation_dir(gen_num)
    candidates_dir = gen_dir / "candidates"
    candidates_dir.mkdir(parents=True, exist_ok=True)

    # Process prompt constraints if provided
    constraints = None
    if args.prompt:
        constraints = translate_prompt(args.prompt)
        print(f"Prompt: '{args.prompt}'")
        print(explain_constraints(constraints))
        print()

    # Generate population
    print(f"Generating {args.population} candidates with '{args.generator}' generator...")
    population = generate_population(
        size=args.population,
        gen_num=gen_num,
        specs=specs,
        prompt_constraints=constraints,
        generator=args.generator,
    )

    # Save population
    pop_file = gen_dir / "population.jsonl"
    save_population(population, pop_file)
    print(f"  Saved population: {pop_file}")

    # Render candidates
    print("Rendering candidates...")
    render_population(
        population,
        candidates_dir,
        canvas_size=(200, 200),
        format="svg",
        style=style,
        specs=specs,
    )
    print(f"  Rendered {len(population)} SVGs to: {candidates_dir}")

    # Generate contact sheet
    contact_sheet = gen_dir / "contact_sheet.pdf"
    generate_contact_sheet(
        population,
        contact_sheet,
        cols=4,
        rows=4,
        style=style,
        specs=specs,
    )
    print(f"  Contact sheet: {contact_sheet}")

    print(f"\nGeneration {gen_num} complete!")
    print(f"  View: {contact_sheet}")
    print(f"  Then run: uv run python -m evolutionary_drawbot select gen_{gen_num:03d} --winners 1,2,3")


def cmd_render(args):
    """Render candidates and create contact sheet for a generation."""
    from .parameters import load_specs_from_config
    from .genome import load_population
    from .render import render_population
    from .contact_sheet import generate_contact_sheet

    config = load_config()
    specs = load_specs_from_config(DEFAULT_CONFIG)
    style = config.get("style", {})

    # Parse generation from argument
    gen_name = args.generation
    if gen_name.startswith("gen_"):
        gen_num = int(gen_name.split("_")[1])
    else:
        gen_num = int(gen_name)

    gen_dir = get_generation_dir(gen_num)
    if not gen_dir.exists():
        print(f"Error: Generation directory not found: {gen_dir}")
        sys.exit(1)

    pop_file = gen_dir / "population.jsonl"
    if not pop_file.exists():
        print(f"Error: Population file not found: {pop_file}")
        sys.exit(1)

    population = load_population(pop_file)
    print(f"Loaded {len(population)} genomes from {pop_file}")

    candidates_dir = gen_dir / "candidates"
    candidates_dir.mkdir(parents=True, exist_ok=True)

    # Render candidates
    print("Rendering candidates...")
    render_population(
        population,
        candidates_dir,
        canvas_size=(200, 200),
        format="svg",
        style=style,
        specs=specs,
    )
    print(f"  Rendered {len(population)} SVGs to: {candidates_dir}")

    # Generate contact sheet
    contact_sheet = gen_dir / "contact_sheet.pdf"
    generate_contact_sheet(
        population,
        contact_sheet,
        cols=4,
        rows=4,
        style=style,
        specs=specs,
    )
    print(f"  Contact sheet: {contact_sheet}")


def cmd_select(args):
    """Record selected winners for a generation."""
    from .genome import load_population

    # Parse generation
    gen_name = args.generation
    if gen_name.startswith("gen_"):
        gen_num = int(gen_name.split("_")[1])
    else:
        gen_num = int(gen_name)

    gen_dir = get_generation_dir(gen_num)
    pop_file = gen_dir / "population.jsonl"

    if not pop_file.exists():
        print(f"Error: Population file not found: {pop_file}")
        sys.exit(1)

    population = load_population(pop_file)

    # Parse winner indices
    winner_indices = [int(x.strip()) for x in args.winners.split(",")]

    # Validate indices
    valid_winners = []
    for idx in winner_indices:
        if 1 <= idx <= len(population):
            valid_winners.append(idx)
        else:
            print(f"Warning: Invalid index {idx} (population size: {len(population)})")

    if not valid_winners:
        print("Error: No valid winners selected")
        sys.exit(1)

    # Save winners
    winners_file = gen_dir / "winners.json"
    with open(winners_file, 'w') as f:
        json.dump({
            "generation": gen_num,
            "population_size": len(population),
            "winner_indices": valid_winners,
            "winner_ids": [population[i-1].id for i in valid_winners],
        }, f, indent=2)

    print(f"Recorded {len(valid_winners)} winners: {valid_winners}")
    print(f"  Saved to: {winners_file}")
    print(f"\nNext: uv run python -m evolutionary_drawbot breed gen_{gen_num:03d}")


def cmd_breed(args):
    """Breed next generation from selected winners."""
    from .parameters import load_specs_from_config
    from .genome import load_population, save_population
    from .evolution import generate_population, select_winners
    from .render import render_population
    from .contact_sheet import generate_contact_sheet

    config = load_config()
    specs = load_specs_from_config(DEFAULT_CONFIG)
    style = config.get("style", {})
    evo_config = config.get("evolution", {})

    # Parse source generation
    gen_name = args.generation
    if gen_name.startswith("gen_"):
        src_gen = int(gen_name.split("_")[1])
    else:
        src_gen = int(gen_name)

    src_dir = get_generation_dir(src_gen)
    winners_file = src_dir / "winners.json"
    pop_file = src_dir / "population.jsonl"

    if not winners_file.exists():
        print(f"Error: No winners recorded for generation {src_gen}")
        print(f"  Run: uv run python -m evolutionary_drawbot select gen_{src_gen:03d} --winners ...")
        sys.exit(1)

    if not pop_file.exists():
        print(f"Error: Population file not found: {pop_file}")
        sys.exit(1)

    # Load winners
    with open(winners_file, 'r') as f:
        winners_data = json.load(f)
    winner_indices = winners_data["winner_indices"]

    population = load_population(pop_file)
    parents = select_winners(population, winner_indices)

    print(f"Breeding from {len(parents)} parents: {winner_indices}")

    # Create new generation
    new_gen = src_gen + 1
    new_dir = get_generation_dir(new_gen)
    candidates_dir = new_dir / "candidates"
    candidates_dir.mkdir(parents=True, exist_ok=True)

    pop_size = args.population or evo_config.get("default_population_size", 16)
    mutation_rate = evo_config.get("mutation_rate", 0.2)
    mutation_strength = evo_config.get("mutation_strength", 0.15)

    print(f"Generating {pop_size} offspring...")
    new_population = generate_population(
        size=pop_size,
        gen_num=new_gen,
        parents=parents,
        specs=specs,
        mutation_rate=mutation_rate,
        mutation_strength=mutation_strength,
    )

    # Save population
    new_pop_file = new_dir / "population.jsonl"
    save_population(new_population, new_pop_file)
    print(f"  Saved population: {new_pop_file}")

    # Render candidates
    print("Rendering candidates...")
    render_population(
        new_population,
        candidates_dir,
        canvas_size=(200, 200),
        format="svg",
        style=style,
        specs=specs,
    )
    print(f"  Rendered {len(new_population)} SVGs to: {candidates_dir}")

    # Generate contact sheet
    contact_sheet = new_dir / "contact_sheet.pdf"
    generate_contact_sheet(
        new_population,
        contact_sheet,
        cols=4,
        rows=4,
        style=style,
        specs=specs,
    )
    print(f"  Contact sheet: {contact_sheet}")

    print(f"\nGeneration {new_gen} complete!")
    print(f"  View: {contact_sheet}")
    print(f"  Then run: uv run python -m evolutionary_drawbot select gen_{new_gen:03d} --winners 1,2,3")


def cmd_status(args):
    """Show current evolution status."""
    from .genome import load_population
    from .evolution import calculate_diversity

    print("Evolutionary DrawBot Status")
    print("=" * 40)

    if not GENERATIONS_DIR.exists():
        print("\nNo generations found. Run 'init' then 'gen0' to start.")
        return

    latest = get_latest_generation()
    if latest < 0:
        print("\nNo generations found. Run 'gen0' to create initial population.")
        return

    print(f"\nGenerations: 0 to {latest}")

    for gen_num in range(latest + 1):
        gen_dir = get_generation_dir(gen_num)
        pop_file = gen_dir / "population.jsonl"
        winners_file = gen_dir / "winners.json"
        contact_sheet = gen_dir / "contact_sheet.pdf"

        status_parts = []

        if pop_file.exists():
            population = load_population(pop_file)
            status_parts.append(f"{len(population)} candidates")

            diversity = calculate_diversity(population)
            status_parts.append(f"diversity={diversity:.3f}")
        else:
            status_parts.append("no population")

        if winners_file.exists():
            with open(winners_file, 'r') as f:
                w = json.load(f)
            status_parts.append(f"winners={w['winner_indices']}")
        elif gen_num < latest:
            status_parts.append("winners=?")

        if contact_sheet.exists():
            status_parts.append("PDF ready")

        print(f"\n  gen_{gen_num:03d}: {', '.join(status_parts)}")

    print(f"\nNext steps:")
    gen_dir = get_generation_dir(latest)
    if not (gen_dir / "winners.json").exists():
        print(f"  1. View: {gen_dir / 'contact_sheet.pdf'}")
        print(f"  2. Run: uv run python -m evolutionary_drawbot select gen_{latest:03d} --winners 1,2,3")
    else:
        print(f"  Run: uv run python -m evolutionary_drawbot breed gen_{latest:03d}")


def main():
    """Main entry point for CLI."""
    parser = argparse.ArgumentParser(
        description="Evolutionary DrawBot Form Generation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  uv run python -m evolutionary_drawbot init
  uv run python -m evolutionary_drawbot gen0 --population 16
  uv run python -m evolutionary_drawbot gen0 --population 16 --prompt "soft protective curves"
  uv run python -m evolutionary_drawbot select gen_000 --winners 3,7,12
  uv run python -m evolutionary_drawbot breed gen_000
  uv run python -m evolutionary_drawbot status
"""
    )

    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # init
    p_init = subparsers.add_parser("init", help="Initialize project")
    p_init.set_defaults(func=cmd_init)

    # gen0
    p_gen0 = subparsers.add_parser("gen0", help="Generate initial population")
    p_gen0.add_argument("--population", "-n", type=int, default=16,
                        help="Population size (default: 16)")
    p_gen0.add_argument("--prompt", "-p", type=str,
                        help="Natural language description for initial constraints")
    p_gen0.add_argument("--generator", "-g", type=str, default="soft_blob",
                        choices=["soft_blob", "layered_form", "shape_outline", "dot_field", "accent_nodes"],
                        help="Generator type (default: soft_blob)")
    p_gen0.set_defaults(func=cmd_gen0)

    # render
    p_render = subparsers.add_parser("render", help="Render candidates and contact sheet")
    p_render.add_argument("generation", help="Generation to render (e.g., gen_000 or 0)")
    p_render.set_defaults(func=cmd_render)

    # select
    p_select = subparsers.add_parser("select", help="Record selected winners")
    p_select.add_argument("generation", help="Generation to select from")
    p_select.add_argument("--winners", "-w", required=True,
                          help="Comma-separated list of winner indices (1-based)")
    p_select.set_defaults(func=cmd_select)

    # breed
    p_breed = subparsers.add_parser("breed", help="Breed next generation")
    p_breed.add_argument("generation", help="Source generation to breed from")
    p_breed.add_argument("--population", "-n", type=int,
                         help="Population size (default from config)")
    p_breed.set_defaults(func=cmd_breed)

    # status
    p_status = subparsers.add_parser("status", help="Show evolution status")
    p_status.set_defaults(func=cmd_status)

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        sys.exit(1)

    args.func(args)


if __name__ == "__main__":
    main()
