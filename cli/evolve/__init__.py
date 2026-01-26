"""
Evolutionary form generation CLI commands.

Commands:
    init        Initialize project with output directories
    gen0        Generate initial population (generation 0)
    render      Render candidates and create contact sheet
    select      Record selected winners
    breed       Breed next generation from winners
    status      Show current evolution status
"""

import json
from pathlib import Path
from typing import Optional

import typer
from rich.console import Console
from rich.table import Table

app = typer.Typer(
    name="evolve",
    help="Evolutionary form generation - breed visual shapes through selection",
    no_args_is_help=True,
)

console = Console()

# Project paths
REPO_ROOT = Path(__file__).resolve().parent.parent.parent
OUTPUT_DIR = REPO_ROOT / "output"
GENERATIONS_DIR = OUTPUT_DIR / "generations"
DEFAULT_CONFIG = Path(__file__).parent / "brand_dna.json"


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


def parse_generation(generation: str) -> int:
    """Parse generation argument to integer, handling both 'gen_000' and '0' formats."""
    try:
        if generation.startswith("gen_"):
            return int(generation.split("_")[1])
        return int(generation)
    except (ValueError, IndexError):
        console.print(f"[red]Error:[/red] Invalid generation format: {generation}")
        console.print("  Expected: gen_000 or 0")
        raise typer.Exit(1)


def load_config() -> dict:
    """Load brand_dna.json configuration."""
    if DEFAULT_CONFIG.exists():
        try:
            with open(DEFAULT_CONFIG, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            console.print(f"[yellow]Warning:[/yellow] Invalid JSON in {DEFAULT_CONFIG.name}: {e}")
    return {}


@app.command()
def init():
    """Initialize project directories."""
    console.print("[blue]Initializing evolutionary DrawBot project...[/blue]")

    GENERATIONS_DIR.mkdir(parents=True, exist_ok=True)
    console.print(f"  Created: {GENERATIONS_DIR}")

    if DEFAULT_CONFIG.exists():
        console.print(f"  Config: {DEFAULT_CONFIG}")
    else:
        console.print(f"  [yellow]Warning:[/yellow] No config at {DEFAULT_CONFIG}")

    console.print("\n[green]Ready![/green] Next steps:")
    console.print("  1. drawbot evolve gen0 --population 16")
    console.print("  2. View contact sheet and select winners")
    console.print("  3. drawbot evolve select gen_000 --winners 3,7,12")
    console.print("  4. drawbot evolve breed gen_000")


@app.command()
def gen0(
    population: int = typer.Option(16, "--population", "-n", help="Population size"),
    prompt: Optional[str] = typer.Option(None, "--prompt", "-p", help="Natural language description"),
    generator: str = typer.Option(
        "soft_blob", "--generator", "-g",
        help="Generator type: soft_blob, layered_form, shape_outline, dot_field, accent_nodes"
    ),
):
    """Generate initial population (generation 0)."""
    from .parameters import load_specs_from_config
    from .genome import save_population
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
    if prompt:
        constraints = translate_prompt(prompt)
        console.print(f"[blue]Prompt:[/blue] '{prompt}'")
        console.print(explain_constraints(constraints))
        console.print()

    # Generate population
    console.print(f"[blue]Generating {population} candidates with '{generator}' generator...[/blue]")
    pop = generate_population(
        size=population,
        gen_num=gen_num,
        specs=specs,
        prompt_constraints=constraints,
        generator=generator,
    )

    # Save population
    pop_file = gen_dir / "population.jsonl"
    save_population(pop, pop_file)
    console.print(f"  Saved population: {pop_file}")

    # Render candidates
    console.print("[blue]Rendering candidates...[/blue]")
    render_population(
        pop,
        candidates_dir,
        canvas_size=(200, 200),
        format="svg",
        style=style,
        specs=specs,
    )
    console.print(f"  Rendered {len(pop)} SVGs to: {candidates_dir}")

    # Generate contact sheet
    contact_sheet = gen_dir / "contact_sheet.pdf"
    generate_contact_sheet(pop, contact_sheet, cols=4, rows=4, style=style, specs=specs)
    console.print(f"  Contact sheet: {contact_sheet}")

    console.print(f"\n[green]Generation {gen_num} complete![/green]")
    console.print(f"  View: {contact_sheet}")
    console.print(f"  Then: drawbot evolve select gen_{gen_num:03d} --winners 1,2,3")


@app.command("render")
def render_cmd(
    generation: str = typer.Argument(..., help="Generation to render (e.g., gen_000 or 0)"),
):
    """Render candidates and create contact sheet for a generation."""
    from .parameters import load_specs_from_config
    from .genome import load_population
    from .render import render_population
    from .contact_sheet import generate_contact_sheet

    config = load_config()
    specs = load_specs_from_config(DEFAULT_CONFIG)
    style = config.get("style", {})

    gen_num = parse_generation(generation)
    gen_dir = get_generation_dir(gen_num)

    if not gen_dir.exists():
        console.print(f"[red]Error:[/red] Generation directory not found: {gen_dir}")
        raise typer.Exit(1)

    pop_file = gen_dir / "population.jsonl"
    if not pop_file.exists():
        console.print(f"[red]Error:[/red] Population file not found: {pop_file}")
        raise typer.Exit(1)

    pop = load_population(pop_file)
    console.print(f"[blue]Loaded {len(pop)} genomes from {pop_file}[/blue]")

    candidates_dir = gen_dir / "candidates"
    candidates_dir.mkdir(parents=True, exist_ok=True)

    console.print("[blue]Rendering candidates...[/blue]")
    render_population(pop, candidates_dir, canvas_size=(200, 200), format="svg", style=style, specs=specs)
    console.print(f"  Rendered {len(pop)} SVGs to: {candidates_dir}")

    contact_sheet = gen_dir / "contact_sheet.pdf"
    generate_contact_sheet(pop, contact_sheet, cols=4, rows=4, style=style, specs=specs)
    console.print(f"  Contact sheet: {contact_sheet}")


@app.command()
def select(
    generation: str = typer.Argument(..., help="Generation to select from"),
    winners: str = typer.Option(..., "--winners", "-w", help="Comma-separated winner indices (1-based)"),
):
    """Record selected winners for a generation."""
    from .genome import load_population

    gen_num = parse_generation(generation)
    gen_dir = get_generation_dir(gen_num)
    pop_file = gen_dir / "population.jsonl"

    if not pop_file.exists():
        console.print(f"[red]Error:[/red] Population file not found: {pop_file}")
        raise typer.Exit(1)

    pop = load_population(pop_file)

    # Parse winner indices
    try:
        winner_indices = [int(x.strip()) for x in winners.split(",") if x.strip()]
    except ValueError:
        console.print("[red]Error:[/red] Winners must be comma-separated numbers (e.g., 1,2,3)")
        raise typer.Exit(1)

    if not winner_indices:
        console.print("[red]Error:[/red] No winner indices provided")
        raise typer.Exit(1)

    # Validate indices
    valid_winners = []
    for idx in winner_indices:
        if 1 <= idx <= len(pop):
            valid_winners.append(idx)
        else:
            console.print(f"[yellow]Warning:[/yellow] Invalid index {idx} (population size: {len(pop)})")

    if not valid_winners:
        console.print("[red]Error:[/red] No valid winners selected")
        raise typer.Exit(1)

    # Save winners
    winners_file = gen_dir / "winners.json"
    with open(winners_file, 'w') as f:
        json.dump({
            "generation": gen_num,
            "population_size": len(pop),
            "winner_indices": valid_winners,
            "winner_ids": [pop[i-1].id for i in valid_winners],
        }, f, indent=2)

    console.print(f"[green]Recorded {len(valid_winners)} winners:[/green] {valid_winners}")
    console.print(f"  Saved to: {winners_file}")
    console.print(f"\nNext: drawbot evolve breed gen_{gen_num:03d}")


@app.command()
def breed(
    generation: str = typer.Argument(..., help="Source generation to breed from"),
    population: Optional[int] = typer.Option(None, "--population", "-n", help="Population size"),
):
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

    src_gen = parse_generation(generation)
    src_dir = get_generation_dir(src_gen)
    winners_file = src_dir / "winners.json"
    pop_file = src_dir / "population.jsonl"

    if not winners_file.exists():
        console.print(f"[red]Error:[/red] No winners recorded for generation {src_gen}")
        console.print(f"  Run: drawbot evolve select gen_{src_gen:03d} --winners ...")
        raise typer.Exit(1)

    if not pop_file.exists():
        console.print(f"[red]Error:[/red] Population file not found: {pop_file}")
        raise typer.Exit(1)

    # Load winners
    with open(winners_file, 'r') as f:
        winners_data = json.load(f)
    winner_indices = winners_data["winner_indices"]

    pop = load_population(pop_file)
    parents = select_winners(pop, winner_indices)

    console.print(f"[blue]Breeding from {len(parents)} parents:[/blue] {winner_indices}")

    # Create new generation
    new_gen = src_gen + 1
    new_dir = get_generation_dir(new_gen)
    candidates_dir = new_dir / "candidates"
    candidates_dir.mkdir(parents=True, exist_ok=True)

    pop_size = population or evo_config.get("default_population_size", 16)
    mutation_rate = evo_config.get("mutation_rate", 0.2)
    mutation_strength = evo_config.get("mutation_strength", 0.15)

    console.print(f"[blue]Generating {pop_size} offspring...[/blue]")
    new_pop = generate_population(
        size=pop_size,
        gen_num=new_gen,
        parents=parents,
        specs=specs,
        mutation_rate=mutation_rate,
        mutation_strength=mutation_strength,
    )

    # Save population
    new_pop_file = new_dir / "population.jsonl"
    save_population(new_pop, new_pop_file)
    console.print(f"  Saved population: {new_pop_file}")

    # Render candidates
    console.print("[blue]Rendering candidates...[/blue]")
    render_population(new_pop, candidates_dir, canvas_size=(200, 200), format="svg", style=style, specs=specs)
    console.print(f"  Rendered {len(new_pop)} SVGs to: {candidates_dir}")

    # Generate contact sheet
    contact_sheet = new_dir / "contact_sheet.pdf"
    generate_contact_sheet(new_pop, contact_sheet, cols=4, rows=4, style=style, specs=specs)
    console.print(f"  Contact sheet: {contact_sheet}")

    console.print(f"\n[green]Generation {new_gen} complete![/green]")
    console.print(f"  View: {contact_sheet}")
    console.print(f"  Then: drawbot evolve select gen_{new_gen:03d} --winners 1,2,3")


@app.command()
def status():
    """Show current evolution status."""
    from .genome import load_population
    from .evolution import calculate_diversity

    console.print("[bold]Evolutionary DrawBot Status[/bold]")
    console.print("=" * 40)

    if not GENERATIONS_DIR.exists():
        console.print("\nNo generations found. Run 'drawbot evolve init' then 'drawbot evolve gen0' to start.")
        return

    latest = get_latest_generation()
    if latest < 0:
        console.print("\nNo generations found. Run 'drawbot evolve gen0' to create initial population.")
        return

    console.print(f"\n[blue]Generations:[/blue] 0 to {latest}")

    table = Table()
    table.add_column("Gen", style="cyan")
    table.add_column("Candidates")
    table.add_column("Diversity")
    table.add_column("Winners")
    table.add_column("Status")

    for gen_num in range(latest + 1):
        gen_dir = get_generation_dir(gen_num)
        pop_file = gen_dir / "population.jsonl"
        winners_file = gen_dir / "winners.json"
        contact_sheet = gen_dir / "contact_sheet.pdf"

        row = [f"gen_{gen_num:03d}"]

        if pop_file.exists():
            pop = load_population(pop_file)
            row.append(str(len(pop)))
            diversity = calculate_diversity(pop)
            row.append(f"{diversity:.3f}")
        else:
            row.extend(["?", "?"])

        if winners_file.exists():
            with open(winners_file, 'r') as f:
                w = json.load(f)
            row.append(str(w['winner_indices']))
        elif gen_num < latest:
            row.append("[yellow]?[/yellow]")
        else:
            row.append("-")

        if contact_sheet.exists():
            row.append("[green]PDF ready[/green]")
        else:
            row.append("[yellow]no PDF[/yellow]")

        table.add_row(*row)

    console.print(table)

    gen_dir = get_generation_dir(latest)
    console.print("\n[bold]Next steps:[/bold]")
    if not (gen_dir / "winners.json").exists():
        console.print(f"  1. View: {gen_dir / 'contact_sheet.pdf'}")
        console.print(f"  2. drawbot evolve select gen_{latest:03d} --winners 1,2,3")
    else:
        console.print(f"  drawbot evolve breed gen_{latest:03d}")
