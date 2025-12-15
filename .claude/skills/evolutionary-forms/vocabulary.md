# Form Vocabulary

Mapping from natural language descriptions to form parameters.

## How Translation Works

The translator tokenizes prompts and matches keywords to parameter constraints. Multiple keywords combine (intersect) their constraints.

```
"soft protective 4 lobes"
   ↓
   soft → roundness: [0.7, 1.0], tension: [0.5, 0.8], wobble: [0.02, 0.1]
   protective → envelope_factor: [0.65, 0.9], lobe_depth: [0.2, 0.5]
   4 lobes → lobe_count: [0.4, 0.6]  (normalized: 4 is middle of 2-6 range)
   ↓
Combined constraints for random generation
```

## Keyword Reference

### Softness Spectrum

| Word | roundness | tension | wobble | lobe_depth |
|------|-----------|---------|--------|------------|
| **soft** | 0.7-1.0 | 0.5-0.8 | 0.02-0.1 | — |
| **gentle** | 0.6-0.9 | 0.4-0.7 | — | 0.1-0.4 |
| **hard** | 0.0-0.3 | 0.6-0.9 | — | — |
| **angular** | 0.0-0.2 | 0.7-0.9 | — | — |
| **sharp** | 0.0-0.15 | — | — | 0.5-0.8 |

### Protection Spectrum

| Word | envelope_factor | lobe_depth | roundness | aspect |
|------|-----------------|------------|-----------|--------|
| **protective** | 0.65-0.9 | 0.2-0.5 | — | — |
| **safe** | 0.6-0.85 | — | 0.5-0.8 | — |
| **embracing** | 0.7-0.9 | — | — | 0.4-0.7 (tall) |
| **nurturing** | 0.6-0.85 | — | 0.6-0.9 | — |
| **sheltering** | 0.7-0.9 | — | — | — |

### Organic Spectrum

| Word | wobble | roundness | tension |
|------|--------|-----------|---------|
| **organic** | 0.1-0.2 | 0.4-0.7 | 0.3-0.6 |
| **natural** | 0.08-0.15 | 0.5-0.8 | — |
| **flowing** | — | 0.6-0.9 | 0.3-0.5 |
| **fluid** | — | 0.7-0.95 | 0.25-0.45 |

### Strength Spectrum

| Word | lobe_depth | envelope_factor | lobe_count | aspect |
|------|------------|-----------------|------------|--------|
| **bold** | 0.4-0.7 | 0.5-0.75 | — | — |
| **strong** | 0.35-0.6 | — | — | 0.5-0.65 (tall) |
| **powerful** | 0.5-0.8 | — | 0.6-1.0 (many) | — |

### Delicacy Spectrum

| Word | wobble | lobe_depth | roundness |
|------|--------|------------|-----------|
| **delicate** | 0.0-0.05 | 0.1-0.3 | 0.7-0.95 |
| **subtle** | 0.0-0.08 | 0.05-0.25 | — |
| **light** | — | 0.1-0.3 | — |

### Complexity

| Word | lobe_count | lobe_depth | wobble |
|------|------------|------------|--------|
| **complex** | 0.7-1.0 (5-6) | 0.3-0.6 | — |
| **simple** | 0.0-0.3 (2-3) | 0.1-0.35 | — |
| **intricate** | 0.8-1.0 (5-6) | — | 0.05-0.12 |

### Shape Descriptors

| Word | roundness | lobe_depth | tension |
|------|-----------|------------|---------|
| **round** | 0.8-1.0 | 0.0-0.2 | — |
| **curved** | 0.6-0.9 | — | 0.4-0.7 |
| **wavy** | — | 0.3-0.5 | 0.35-0.55 |
| **scalloped** | 0.5-0.8 | 0.4-0.7 | — |

### Proportions

| Word | aspect (normalized) | Actual ratio |
|------|---------------------|--------------|
| **tall** | 0.25-0.45 | 0.7-0.85 |
| **wide** | 0.7-1.0 | 1.15-1.4 |
| **compact** | 0.45-0.55 | 0.95-1.05 |

### Structure Words

| Word | lobe_count | lobe_depth | roundness |
|------|------------|------------|-----------|
| **petals** | 0.4-0.8 | — | — |
| **lobes** | 0.4-0.8 | — | — |
| **flower** | 0.6-1.0 | — | 0.5-0.8 |
| **clover** | 0.2-0.4 | 0.3-0.5 | — |

### Explicit Lobe Counts

| Word | lobe_count (normalized) | Actual count |
|------|-------------------------|--------------|
| two / 2 | ~0.0 | 2 |
| three / 3 | ~0.25 | 3 |
| four / 4 | ~0.5 | 4 |
| five / 5 | ~0.75 | 5 |
| six / 6 | ~1.0 | 6 |

Usage: "three lobes", "4 petals", "five-fold"

## Combination Examples

### "soft protective 4 lobes"
```
roundness: max(0.7, —) = 0.7 to min(1.0, —) = 1.0
tension: 0.5-0.8
wobble: 0.02-0.1
envelope_factor: 0.65-0.9
lobe_depth: 0.2-0.5
lobe_count: ~0.5 (4 lobes)
```
Result: Smooth, slightly wobbly, protective forms with 4 distinct lobes.

### "bold organic flowing"
```
lobe_depth: max(0.4, —) = 0.4 to min(0.7, —) = 0.7
envelope_factor: 0.5-0.75
wobble: 0.1-0.2
roundness: max(0.4, 0.6) = 0.6 to min(0.7, 0.9) = 0.7
tension: max(0.3, 0.3) = 0.3 to min(0.6, 0.5) = 0.5
```
Result: Bold presence with organic irregularity and flowing curves.

### "delicate intricate flower"
```
wobble: max(0.0, 0.05) = 0.05 to min(0.05, 0.12) = 0.05
lobe_depth: 0.1-0.3
roundness: max(0.7, 0.5) = 0.7 to min(0.95, 0.8) = 0.8
lobe_count: max(0.8, 0.6) = 0.8 to min(1.0, 1.0) = 1.0
```
Result: Very clean 5-6 lobe flower forms with subtle depth.

## Visual Parameter Guide

### lobe_count (2-6)
```
2 lobes      3 lobes      4 lobes      5 lobes      6 lobes
   ()          ❀            ✤            ✿            ❁
  shell      trefoil     quatrefoil    cinquefoil   hexafoil
```

### lobe_depth (0-1)
```
0.0          0.3          0.6          1.0
 ○            ◉            ✳            ✴
circle    shallow      medium       deep
```

### envelope_factor (0.3-0.9)
```
0.3          0.6          0.9
 ○            ◐            ◑
symmetric   slight     protective
            bulge        embrace
```

### roundness (0-1)
```
0.0          0.5          1.0
 ⬡            ◇            ○
angular    mixed       smooth
```

### wobble (0-0.2)
```
0.0          0.1          0.2
clean      natural     handmade
precise    organic     irregular
```

### tension (0.3-0.9)
```
0.3          0.6          0.9
loose      balanced    tight
flowing    moderate    controlled
```

## Creating New Keywords

To add custom keywords, edit `evolutionary_drawbot/translator.py`:

```python
KEYWORD_MAP["mystical"] = {
    "wobble": (0.1, 0.18),
    "lobe_count": (0.6, 1.0),
    "roundness": (0.5, 0.75),
    "envelope_factor": (0.55, 0.75),
}
```

Then use: `--prompt "mystical flowing"`
