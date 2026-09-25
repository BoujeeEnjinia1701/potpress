---
doc_id: PPR-REQ-001
title: PotPress requirements
project: PotPress
doc_type: Requirements
version: "0.2"
status: Draft
date: '2026-09-25'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-09-24'
  author: Amish Chadha
  change: Initial scaffold
- version: "0.2"
  date: '2026-09-25'
  author: Amish Chadha
  change: First measurable requirements for TRL 2, with concept status
---

# PotPress requirements

These are first-pass requirements for the concept. Targets are proposals for review, not yet validated with a filter factory, and will be checked by calculation at TRL 3 and revised after co-design sessions (see PPR-PRB-001). One requirement is not met by the concept (R10, cost) and three are at risk (R2, R5 and R7); see Table 2.

The **reference filter** used throughout is the common flowerpot form: inner rim diameter 280 mm, inner depth 240 mm, wall 15 mm, flat rim about 345 mm across, about 12 L to the brim and about 10 L working volume (dimensions are estimates based on the 280 by 250 mm form reported by [Potters for Peace](https://www.pottersforpeace.org/ceramic-water-filter-project)).

*Table 1. Requirements.*

| ID | Requirement | Target | Verification (TRL 3 or later) |
| --- | --- | --- | --- |
| R1 | Form the reference filter | Inner rim 280 mm, inner depth 240 mm, wall 15 mm, flat rim; geometry set by parameters in one source file | Model check; later measurement of pressed pots |
| R2 | Even wall | Wall thickness within ±1 mm around the circumference and from pot to pot; molds self-center to within 0.5 mm | Tolerance stack and guide design; later sectioned pots |
| R3 | Pressing force and frame strength | 20 t (196 kN) rated jack; frame, pins and platen carry 1.5 times the jack rating (294 kN) without yield and with deflection under 1 mm at the mold | Beam and pin calculation; later proof load |
| R4 | Throughput | Press cycle of 6 min or less with two operators, so 50 or more pots per 6 h of pressing | Cycle breakdown; later timed trial |
| R5 | Mold opening | Male mold lifts at least 30 mm clear of the female rim so the mold carriage slides out for loading and demolding; pressing stroke within one jack stroke | Kinematic layout |
| R6 | Flow-rate QC | Rack tests 4 soaked filters at once; T-gauge reads flow over 1 h to 0.1 L/h; repeatability ±0.1 L/h; acceptance band set per factory (default 1.0 to 2.5 L/h in the first hour, proposed) | Gauge calibration by volume; later repeat tests |
| R7 | Molds made locally | Molds cast from 3D-printed patterns printed on a 250 x 250 mm class printer; finishing with hand tools and a drill press; no lathe over 300 mm swing | Pattern split and finishing review with a foundry |
| R8 | Frame built locally | Standard steel channel and plate; stick welding and drilling only; heaviest single part 40 kg or less for two-person handling | Part list and mass estimate |
| R9 | Safe operation | Fixed guards on the sides and back, interlocked front gate; jack pump and release outside the guard; load pins must be in place before pressing | Hazard review; later guard check |
| R10 | Affordable | Press plus QC rack $600 or less in parts | Priced BOM (`bom/bom.csv`) |
| R11 | Footprint | Press within 1.0 x 0.7 m floor area and 2.0 m height; QC rack within 0.8 x 0.5 m | Model check |
| R12 | Product-safe materials | Faces that touch clay or test water are aluminum, food-grade polyethylene or stainless steel; no lead-based paint or oiled release agents on mold faces | Material list review |

*Table 2. Concept status against each requirement (estimates from PPR-PRC-001).*

| ID | Concept estimate | Status |
| --- | --- | --- |
| R1 | Geometry parameters in `cad/src/concept_media.py` | Met on paper |
| R2 | Depends on guide sleeve clearance and mold alignment, not yet designed | **At risk**, unverified |
| R3 | Top beam of two UPN 160 channels (about 232 cm³): about 127 MPa at the 196 kN rating and about 190 MPa at 294 kN, below 275 MPa yield | Met on paper; deflection and pins not checked |
| R4 | About 5 min per cycle | Met on paper, thin margin |
| R5 | Needs about 270 mm of relative travel; a standard bottle jack gives about 150 mm, so the male mold is lifted separately by a crank | **At risk** until the lift and jack are chosen |
| R6 | Printed T-gauge, 4 stations | Met on paper |
| R7 | Female pattern about 410 mm across must be printed in segments; finish of the cast cavity without a lathe is unproven | **At risk** |
| R8 | Heaviest part is the top beam at about 35 kg (estimate) | Met on paper |
| R9 | Guards and gate in the BOM, not modeled | Met on paper |
| R10 | About $716 in parts (press about $645, QC rack about $71) | **Not met**, about 19 % over |
| R11 | Press about 920 x 640 x 1,655 mm; rack 800 x 440 mm | Met |
| R12 | Aluminum molds, polyethylene liners and buckets | Met on paper |

## Assumptions

- Pressing force needed for a well-consolidated wall is not published in the sources found; 5 to 10 t is assumed as the working range and the 20 t jack rating is used as the design load (estimate, to be confirmed with a partner factory).
- Mix and mass per pot follow the factory recipes reported by [Rayner (2009)](https://bdd.pseau.org/outils/ouvrages/wedc_current_practices_in_manufacturing_locally_made_ceramic_pot_filters_2009.pdf): about 8 kg of mix per pot.
- The default flow acceptance band of 1.0 to 2.5 L/h follows Nicaraguan practice and the Potters for Peace range of 1.5 to 2.5 L/h; each factory sets its own band.
- Allowable stress in structural steel is taken as 165 MPa (S275 with a factor of about 1.67).
