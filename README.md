# PotPress

![TRL 2](https://img.shields.io/badge/TRL-2%20of%209-0F766E) ![Hardware: CERN-OHL-S-2.0](https://img.shields.io/badge/hardware-CERN--OHL--S--2.0-111827) ![Software: MIT](https://img.shields.io/badge/software-MIT-111827)

**Area:** Water Security · **TRL:** 2 of 9 (concept formulated) · **Prototype budget:** about $600 USD · **Difficulty:** 3 of 5

Hydraulic press with printable mold geometry for silver-treated ceramic pot filters, plus a QC flow-rate test jig.

![PotPress concept](media/hero.png)

[Interactive 3D model](media/viewer.html) · [Concept blueprint (PDF)](media/concept-blueprint.pdf) · [Review note](docs/REVIEW.md)

## Problem

Ceramic pot filters work well, but local producers have no low-cost way to form them consistently. Imported presses cost about $3,000 to $3,500, locally built ones are one-off designs, and filter quality depends on an even wall and a consistent flow-rate check. Design with, not for: requirements must come from co-design sessions and trials with a working filter factory through a local partner.

## Concept

A 20 t bottle jack on the base lifts a guided platen carrying a cast aluminum female mold against a fixed male mold, forming one filter (about 280 mm across and 10 L working volume) per stroke. The male mold is pinned to the top crossbeam for pressing and raised by a hand crank for loading, and the female mold slides out on a carriage for demolding. One parametric filter geometry drives the molds, their 3D-printed casting patterns and a printed T-gauge for the four-station, one-hour flow-rate test rack. First-order estimates: a cycle of about 5 min, 50 or more pots per shift, and about $716 in parts, over the $600 target (see the [review note](docs/REVIEW.md)).

Full design precis: [docs/02-concept.md](docs/02-concept.md)

## Key components

- Welded steel channel frame: base, uprights and top crossbeam
- 20 t bottle jack, guided moving platen and return springs
- Cast aluminum female and male molds, cast from 3D-printed patterns
- Mold carriage with slide rails, and male mold slide with hand crank and load pins
- Four-station QC flow-test rack with printed T-gauges and collection buckets

The working bill of materials is in [bom/bom.csv](bom/bom.csv).

## Safety

> **Safety:** Hydraulic presses store significant energy. Guard pinch points, press only with the gate closed and both load pins home, and never exceed the jack rating. Molds are heavy; clay dust contains silica; silver compounds are corrosive. Passing the flow test does not prove a filter removes pathogens. See the safety section of the [design precis](docs/02-concept.md).

## Repository layout

| Folder | Contents |
| --- | --- |
| `docs/` | Problem, concept, requirements, calculations and design decisions |
| `cad/src/` | build123d Python source, the source of truth for all geometry |
| `cad/step/`, `cad/stl/` | Exported models for FreeCAD, other CAD tools and printing |
| `cad/drawings/` | 2D sketches and dimensioned drawings |
| `bom/` | Bill of materials |
| `electronics/` | KiCad schematics and PCB layouts |
| `firmware/` | Microcontroller code |
| `media/` | Renders, perspectives and photos |
| `build-log/` | Dated prototyping notes |

## Documentation

Controlled documents follow the portfolio [documentation standard](.kit/STANDARDS.md). Each carries a document ID (PPR-PRC-001 for the precis), a version and a revision history. Branded PDFs are built with `python .kit/render.py` and attached to GitHub Releases when a document is tagged, for example `PPR-PRC-001/v1.0`.

## Licenses

- **Hardware** (CAD, drawings, BOM, electronics): [CERN-OHL-S v2](LICENSE)
- **Software** (firmware, scripts, notebooks): [MIT](LICENSE-SOFTWARE)

Part of the open hardware portfolio at [amishchadha.com](https://amishchadha.com).
