# PotPress

**Area:** Water Security · **Status:** Concept · **Prototype budget:** about $600 USD · **Difficulty:** 3 of 5

Hydraulic press with printable mold geometry for silver-treated ceramic pot filters, plus a QC flow-rate test jig.

## Problem

Ceramic pot filters work well, but local producers have no low-cost way to form them consistently.

## Concept

Hydraulic press with printable mold geometry for silver-treated ceramic pot filters, plus a QC flow-rate test jig.

Full design precis: [docs/02-concept.md](docs/02-concept.md)

## Key components

- 20 t bottle jack
- Welded press frame
- Aluminum or cast mold halves
- Flow-test rig

The working bill of materials is in [bom/bom.csv](bom/bom.csv).

## Safety

> Hydraulic presses store significant energy. Guard pinch points and never exceed the jack rating.

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
