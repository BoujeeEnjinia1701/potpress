# PotPress

![TRL 3](https://img.shields.io/badge/TRL-3%20of%209-0F766E) ![Stage P3](https://img.shields.io/badge/stage-P3%20design%20outputs-0F766E) ![Hardware: CERN-OHL-S-2.0](https://img.shields.io/badge/hardware-CERN--OHL--S--2.0-111827) ![Software: MIT](https://img.shields.io/badge/software-MIT-111827) [![DOI](https://zenodo.org/badge/1386352245.svg)](https://zenodo.org/badge/latestdoi/1386352245) [![REUSE compliant](https://github.com/BoujeeEnjinia1701/potpress/actions/workflows/reuse.yml/badge.svg)](https://github.com/BoujeeEnjinia1701/potpress/actions/workflows/reuse.yml) [![Archived in Software Heritage](https://archive.softwareheritage.org/badge/origin/https://github.com/BoujeeEnjinia1701/potpress/)](https://archive.softwareheritage.org/browse/origin/?origin_url=https://github.com/BoujeeEnjinia1701/potpress)

**Area:** Water Security · **TRL:** 3 of 9 (proof of concept on paper) · **Value-engineering target:** $1,060 USD · **Difficulty:** 3 of 5

Hydraulic press with printable mold geometry for silver-treated ceramic pot filters, plus a QC flow-rate test jig.

![PotPress: hand-pumped hydraulic press for ceramic pot water filters, in a filter workshop](media/render-hero.png)

[Studio render](media/render-studio.png) · [Exploded render](media/render-exploded.png) · [Gate open render](media/render-gate-open.png) · [Lineup render](media/render-lineup.png) · [Interactive 3D model](media/viewer.html) · [Concept blueprint (PDF)](media/concept-blueprint.pdf) · [General arrangement PPR-DWG-001 (PDF)](cad/drawings/PPR-DWG-001.pdf) · [STEM check](docs/01b-stem-check.md) · [Concept options](docs/02a-concept-options.md) · [Requirements](docs/03-requirements.md) · [Traceability](docs/03b-traceability.md) · [Sizing note PPR-CAL-001](docs/04-calcs/01-sizing.md) · [Prototype build plan](docs/05-build-plan.md) · [Decisions](docs/06-design-decisions.md) · [Review note](docs/REVIEW.md)

## Concept rationale

The ceramic pot filter already works; what holds small factories back is the press that forms it. A hydraulic press built from standard steel channel, a car-shop bottle jack and molds cast by any aluminum foundry from 3D-printed patterns can be made and repaired in the regions where the filters are needed, instead of imported at several thousand dollars. Every dimension of the pot, the molds, the patterns and the flow gauge comes from one parametric file, so a factory that changes its filter size regenerates all of them together rather than redrawing by hand.

Keeping the design open matters because filter quality depends on details (an even wall, a consistent flow test) that each workshop now solves alone. An open, garage-buildable press lets factories, NGOs and university labs share improvements, compare results on the same geometry and build a second press when the first wears out.

## Burning platform

About 2.1 billion people still lacked safely managed drinking water in 2024, and 106 million drank untreated surface water ([WHO and UNICEF JMP, 2025](https://www.who.int/news/item/26-08-2025-1-in-4-people-globally-still-lack-access-to-safe-drinking-water---who--unicef)). WHO estimates that microbiologically contaminated drinking water causes about 505,000 diarrheal deaths each year, and that at least 1.7 billion people used a drinking water source contaminated with feces in 2022 ([WHO fact sheet, Drinking-water](https://www.who.int/news-room/fact-sheets/detail/drinking-water)).

Locally made ceramic pot filters are an established household option: filters based on the Potters for Peace technology are now made at over 50 independent factories in over 30 countries ([Potters for Peace](https://www.pottersforpeace.org/ceramic-water-filter-project)). Yet a filter press with its aluminum molds cost $3,000 to $3,500 to acquire, and a locally built Nigerian press still cost about $1,000 ([Erhuanga et al., IntechOpen, 2020](https://www.intechopen.com/chapters/71402)). The press is the gate on how many factories can start.

## Where it could be used

### By industry

| Industry | Use |
| --- | --- |
| Household water treatment enterprises | Form filters with an even wall at a small factory and check every one on the QC rack |
| Pottery and ceramics cooperatives | Add filter production to an existing kiln and clay supply with a press they can build and repair |
| Humanitarian and disaster response | Set up filter production near displaced or flood-hit communities without importing a press |
| Public health programs | Supply consistent filters to household water programs and record QC results the same way at every site |
| University and research labs | Study mix, pressing and firing variables on a repeatable press and shared geometry |
| Local fabrication shops and foundries | Build frames and cast molds from open drawings as a local service |

### By country or region

| Country or region | Why it matters there |
| --- | --- |
| Nicaragua | After Hurricane Mitch in October 1998, Potters for Peace set up its first filter production workshop here and distributed over 5,000 filters within six months ([Potters for Peace](https://www.pottersforpeace.org/ceramic-water-filter-project); [University of Pittsburgh](https://www.engineering.pitt.edu/subsites/projects/ceramic-filter/history/)) |
| Guatemala | The filter was designed here in 1981 by Dr. Fernando Mazariegos at the Central American Industrial Research Institute (ICAITI) ([Potters for Peace](https://www.pottersforpeace.org/ceramic-water-filter-project)) |
| Cambodia | One of the countries where Potters for Peace has trained filter producers ([Potters for Peace](https://www.pottersforpeace.org/ceramic-water-filter-project)); a shared press design would let new workshops match established ones |
| Nigeria | A locally built press cost about $1,000 against $3,000 to $3,500 for an imported press and molds, and the team struggled to find a lathe large enough to finish the molds ([Erhuanga et al., IntechOpen, 2020](https://www.intechopen.com/chapters/71402)) |
| United States | The University of Pittsburgh runs research and service-learning projects on filter manufacturing variables, such as sawdust particle size and firing rate, and gives technical support to NGOs that make filters ([University of Pittsburgh](https://www.engineering.pitt.edu/subsites/projects/ceramic-filter/research--activities/)); an open press gives such labs a common reference |

## What sparked the idea

The starting point was the Potters for Peace filter workshop in Nicaragua. Ron Rivera coordinated the organization's work there from 1989, and after Hurricane Mitch tore through Central America in October 1998, Potters for Peace became much more involved in the low-cost filter and set up its first filter production workshop, which distributed over 5,000 filters within six months ([University of Pittsburgh](https://www.engineering.pitt.edu/subsites/projects/ceramic-filter/history/); [Potters for Peace](https://www.pottersforpeace.org/ceramic-water-filter-project)). Its filters are formed with a hand-operated hydraulic truck jack and a two-piece aluminum mold, and filters based on that technology package are now made at over 50 independent factories in over 30 countries ([Potters for Peace](https://www.pottersforpeace.org/ceramic-water-filter-project)). PotPress takes that jack-and-mold principle and asks what it would look like as an openly maintained, parametric design, so that the next workshop can build its press and molds from shared files rather than from a one-off drawing.

## Problem

Ceramic pot filters work well, but local producers have no low-cost way to form them consistently. Imported presses cost about $3,000 to $3,500, locally built ones are one-off designs, and filter quality depends on an even wall and a consistent flow-rate check. Design with, not for: requirements must come from co-design sessions and trials with a working filter factory through a local partner.

## Concept

A 20 t bottle jack on the base lifts a guided platen carrying a cast aluminum female mold against a fixed male mold, forming one filter (280 mm inner rim and 9.9 L working volume when fired) per stroke. The male mold is held by one 60 mm load pin in the top crossbeam for pressing and raised by a hand crank for loading, and the female mold slides out on a carriage for demolding. One parametric filter geometry drives the molds, their 3D-printed casting patterns and a printed T-gauge for the four-station, one-hour flow-rate test rack. The molds are 1.087 times the fired filter, so the pot comes out of the kiln at size after the clay shrinks (8 % assumed until the partner clay is measured). TRL 3 calculations (PPR-CAL-001 v0.13): a cycle of about 5.2 min and about 69 pots per 6 h, a frame that stays below yield at 1.5 times the jack rating, 0.66 mm of deflection between the molds at 10 t, a working force limited to 5.4 t by the pump handle, and every part over 25 kg lifted on a chain block. The press works inside fixed mesh guards with an interlocked front gate; the ISO 13857 desk check of every guard opening passes on paper, and nothing above hand pressure is allowed until a competent person signs it. Value-engineering target: USD 1,060. Estimated cost: USD 1,279 (USD 219 over the target).

Full design precis: [docs/02-concept.md](docs/02-concept.md)

## STEM check

Every claim PotPress makes was checked against known physics, chemistry, biology, mathematics and engineering, and an independent reviewer tried to refute each verdict ([PPR-STM-001](docs/01b-stem-check.md)). The first check found four details that failed: the molds allowed no clay shrinkage, the heaviest parts were too heavy for two people, the pump handle was hard work above about 6 t, and the scrap alloy was not checked. Each is now fixed in the design ([PPR-DDR-006](docs/decisions/0006-stem-check-fixes.md)), the reviewer's corrections to the fixes included. Eight claims for options B and C were added on 2026-10-24 from their detailed models, and a second independent review the same day tightened the bolted joints to preload and found that the pump handle had no effort margin at the 6.4 t working force limit once the jack's efficiency is counted. Amish decided on 2026-10-25 to lower the limit to 5.4 t (about 148 N at the handle). 36 of 37 claims pass; that one stays open until an EN 1005-3 assessment with the bought jack's data.

## Concept options

![Three ways to make the pressing force, side by side at one scale](media/options.png)

Three working principles were compared against the user requirements ([PPR-OPT-001](docs/02a-concept-options.md)): the hydraulic bottle-jack press (the current design, 125 of 160), a toggle lever press (112) and a power-screw press (104). Amish chose the hydraulic press on 2026-10-25, the recommended option, because it is the only option where the operator, not the clay charge or hand torque, sets the pressing force, which trials have yet to find. All three are modelled at the same level of detail (D3, kit 1.9): option A in 301 parts with 186 ISO fasteners and 35 weld beads, B in 267 parts and C in 261, sharing A's molds, carriage and QC rack.

## Key components

- Steel channel frame in welded subassemblies: two UPN 160 beams and back-to-back UPN 100 uprights, bolted at the upright joints with 4 x M16 10.9 each, with spacer tubes and shims
- 20 t bottle jack, guided moving platen and return springs
- Cast aluminum shell molds sized for clay shrinkage (female 39.6 kg on its steel base plate, male 26.3 kg), cast from 3D-printed flat-back patterns in sorted A356 wheel scrap, located by two dowels and lifted on eye bolts
- Mold carriage on slide rails with a hinged front extension that folds down, and male mold slide with hand crank, one load pin and a pin-presence interlock
- Four-station (2 x 2) QC flow-test rack with printed T-gauges and collection buckets

Every bolt, nut, washer, stud, dowel and screw is modelled in its hole, with the weld beads, from `cad/src/model.py`. The working bill of materials is in [bom/bom.csv](bom/bom.csv).

## Building the prototype

![Every component of the PotPress prototype, pulled apart and numbered in build order](docs/05-build-plan/overview.png)

The [prototype build plan](docs/05-build-plan.md) (PPR-BLD-001, plan, not yet built) shows how to make each component and fit it to the next, in 14 making sketches, 11 joint close-ups and 18 assembly steps drawn from the model. The frame, platen, carriage and guards are sawn, drilled and stick welded from steel channel, plate and galvanized mesh; the two molds are sand cast by a local foundry from 3D-printed flat-back patterns and sorted, melt-checked A356 scrap, then lapped and hand finished, with no lathe needed. Writing the plan made the design constructable: seventeen changes, such as an open-topped male mold, dowel location for the molds, M16 joint bolts with spacer tubes and a floating lead screw nut, are recorded in [PPR-DDR-004](docs/decisions/0004-design-for-construction.md). The STEM check fixes of 2026-10-23 ([PPR-DDR-006](docs/decisions/0006-stem-check-fixes.md)) added the clay shrinkage allowance, a lifting set and a melt check. The parts now cost about $1,279, $219 over the $1,060 value-engineering target, a hypothetical control target; the design decisions register lists the savings worth trying.

## Safety

> **Safety:** Hydraulic presses store significant energy. Guard pinch points, press only with the gate closed and the load pin fully home (the interlock enforces this), and never exceed the 5.4 t working force limit or fit an extension to the pump handle. Lift every part over 25 kg on the chain block. Molds are heavy; clay dust contains silica; silver compounds are corrosive. Passing the flow test does not prove a filter removes pathogens. See the safety section of the [design precis](docs/02-concept.md).

## Repository layout

| Folder | Contents |
| --- | --- |
| `docs/` | Problem, concept, requirements, calculations and design decisions |
| `cad/src/` | build123d Python source, the source of truth for all geometry: `model.py` (options A, B and C, kit 1.9, detail level D3), `options_bc.py`, `ppr_parts.py`, `product_model.py`, `sheets.py`, `build_plan_media.py`, `concept_media.py` |
| `cad/step/`, `cad/stl/` | STEP per part of option A (`cad/step/A/`) and an assembly per option; STL for printing and viewing |
| `cad/drawings/` | 2D sketches and dimensioned drawings |
| `bom/` | Bill of materials |
| `electronics/` | KiCad schematics and PCB layouts |
| `firmware/` | Microcontroller code |
| `media/` | Renders, perspectives and photos |
| `build-log/` | Dated prototyping notes |

## Documentation

| Document | ID |
| --- | --- |
| [Problem statement](docs/01-problem.md) | PPR-PRB-001 |
| [STEM check](docs/01b-stem-check.md) | PPR-STM-001 |
| [Design precis](docs/02-concept.md) | PPR-PRC-001 |
| [Concept options](docs/02a-concept-options.md) | PPR-OPT-001 |
| [User requirements](docs/03a-user-requirements.md) | PPR-URS-001 |
| [Product requirements and specifications](docs/03-requirements.md) | PPR-PRS-001 |
| [Traceability matrix](docs/03b-traceability.md) | PPR-RTM-001 |
| [Calculation note](docs/04-calcs/01-sizing.md) | PPR-CAL-001 |
| [Prototype build plan](docs/05-build-plan.md) | PPR-BLD-001 |
| [Design decisions register](docs/06-design-decisions.md) | PPR-DEC-001 |
| [STEM check fixes](docs/decisions/0006-stem-check-fixes.md) | PPR-DDR-006 |
| [Regulatory and standards register](docs/07-regulatory.md) | PPR-REG-001 |
| [Feasibility](docs/08-feasibility.md) | PPR-FEA-001 |
| [Risk register, hazard analysis and design FMEA](docs/09-risk.md) | PPR-RSK-001 |
| [Market and viability](docs/10-market.md) | PPR-MKT-001 |
| [Project plan](docs/11-plan.md) | PPR-PLN-001 |

Pipeline stage: P3 of P0 to P6 (the portfolio cap). Run `python .kit/render.py --check` to validate the documents, `python .kit/cad_check.py --export` for the CAD fidelity check, `python cad/src/model.py --check --detail` for the fit, motion and ISO 13857 checks and `python docs/04-calcs/sizing.py` for the calculations. Controlled documents follow the portfolio [documentation standard](.kit/STANDARDS.md). Each carries a document ID (PPR-PRC-001 for the precis), a version and a revision history. Branded PDFs are built with `python .kit/render.py` and attached to GitHub Releases when a document is tagged, for example `PPR-PRC-001/v1.0`.

## Credits

Designed by Amish Chadha. See [CONTRIBUTORS.md](CONTRIBUTORS.md) for roles. To cite this design, use [CITATION.cff](CITATION.cff) (GitHub shows it as "Cite this repository").

AI assistance (Claude) was used to accelerate concept renders, prototype documentation and first-pass sizing calculations. Design direction and all decisions are Amish Chadha's, recorded in this repository's decision records (`docs/decisions/`).

## Licenses

- **Hardware** (CAD, drawings, BOM, electronics): [CERN-OHL-S v2](LICENSE)
- **Software** (firmware, scripts, notebooks): [MIT](LICENSE-SOFTWARE)

A project of the [Design Molecule](https://designmolecule.com) lab.
