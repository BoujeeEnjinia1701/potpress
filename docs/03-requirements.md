---
doc_id: PPR-REQ-001
title: PotPress requirements
project: PotPress
doc_type: Requirements
version: "0.3"
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
- version: "0.3"
  date: '2026-09-25'
  author: Amish Chadha
  change: Apply Amish's 2026-09-25 decisions (PPR-DDR-001); R10 target $720, R6 band decided; status from PPR-CAL-001; proposed changes to R3 and R11
---

# PotPress requirements

These requirements were checked by calculation at TRL 3 (PPR-CAL-001). They are not yet validated with a filter factory and will be revised after co-design sessions (see PPR-PRB-001). Three are **not met** on paper (R3 deflection, R10 cost and R11 for the QC rack), four are at risk (R2, R7, R8 and R9) and five are met on paper; see Table 2. Amish's decisions of 2026-09-25 are recorded in PPR-DDR-001: the R10 target is now $720 and the R6 default band is decided. Changes to R3 and R11 are proposed, awaiting Amish.

The **reference filter** used throughout is the common flowerpot form: inner rim diameter 280 mm, inner depth 240 mm, wall 15 mm, flat rim about 345 mm across, about 12 L to the brim and about 10 L working volume (dimensions are estimates based on the 280 by 250 mm form reported by [Potters for Peace](https://www.pottersforpeace.org/ceramic-water-filter-project)).

*Table 1. Requirements.*

| ID | Requirement | Target | Verification (TRL 3 or later) |
| --- | --- | --- | --- |
| R1 | Form the reference filter | Inner rim 280 mm, inner depth 240 mm, wall 15 mm, flat rim; geometry set by parameters in one source file | Model check; later measurement of pressed pots |
| R2 | Even wall | Wall thickness within ±1 mm around the circumference and from pot to pot; molds self-center to within 0.5 mm | Tolerance stack and guide design; later sectioned pots |
| R3 | Pressing force and frame strength | 20 t (196 kN) rated jack; frame, pins and platen carry 1.5 times the jack rating (294 kN) without yield and with deflection under 1 mm at the mold | Beam and pin calculation; later proof load |
| R4 | Throughput | Press cycle of 6 min or less with two operators, so 50 or more pots per 6 h of pressing | Cycle breakdown; later timed trial |
| R5 | Mold opening | Male mold lifts at least 30 mm clear of the female rim so the mold carriage slides out for loading and demolding; pressing stroke within one jack stroke | Kinematic layout |
| R6 | Flow-rate QC | Rack tests 4 soaked filters at once; T-gauge reads flow over 1 h to 0.1 L/h; repeatability ±0.1 L/h; acceptance band set per factory (default 1.0 to 2.5 L/h in the first hour, corrected to 25 °C; decided by Amish, 2026-09-25) | Gauge calibration by volume; later repeat tests |
| R7 | Molds made locally | Molds cast from 3D-printed patterns printed on a 250 x 250 mm class printer; finishing with hand tools and a drill press; no lathe over 300 mm swing | Pattern split and finishing review with a foundry |
| R8 | Frame built locally | Standard steel channel and plate; stick welding and drilling only; heaviest single part 40 kg or less for two-person handling | Part list and mass estimate |
| R9 | Safe operation | Fixed guards on the sides and back, interlocked front gate; jack pump and release outside the guard; load pins must be in place before pressing | Hazard review; later guard check |
| R10 | Affordable | Press plus QC rack $720 or less in parts (raised from $600 by Amish, 2026-09-25) | Priced BOM (`bom/bom.csv`) |
| R11 | Footprint | Press within 1.0 x 0.7 m floor area and 2.0 m height; QC rack within 0.8 x 0.5 m | Model check |
| R12 | Product-safe materials | Faces that touch clay or test water are aluminum, food-grade polyethylene or stainless steel; no lead-based paint or oiled release agents on mold faces | Material list review |

*Table 2. Status against each requirement at TRL 3 (from PPR-CAL-001, not met first).*

| ID | TRL 3 value | Status |
| --- | --- | --- |
| R3 | No yield: beams 190 MPa, uprights 54 MPa, 60 mm pin 258 MPa (yield 650) at 294 kN. Deflection between the molds 1.84 mm at 294 kN, 1.23 mm at 196 kN, 0.61 mm at 10 t | **Not met** (deflection) |
| R10 | Priced BOM $926 (press $845, QC rack $81) | **Not met**, $206 (29 %) over |
| R11 | Press frame 840 x 640 mm, 970 mm deep with the fixed rail extension, 1,806 mm tall; QC rack 780 x 780 mm | **Not met** for the rack; press depth needs a hinged rail extension |
| R2 | Wall ±1.40 mm as cast; ±0.43 mm with molds hand-finished to templates; coaxial ±0.43 mm via the locating lip | **At risk** |
| R7 | 16 pattern segments for a 250 mm printer; cavity finishing without a lathe unproven | **At risk** |
| R8 | Heaviest part as fabricated 38.9 kg (platen); welded frame 147 kg in one piece | **At risk** |
| R9 | Guards, gate, jack-release interlock and pin-presence interlock in the BOM, not modeled | **At risk** |
| R1 | Reference filter from `PARAMS` in `cad/src/model.py`: 12.30 L to the brim, 9.91 L working | Met on paper |
| R4 | 5.2 min cycle, 69 pots per 6 h | Met on paper, thin margin |
| R5 | 310 mm opening against 270 mm needed; 110 of 150 mm jack stroke | Met on paper |
| R6 | 4 stations; 0.1 L is 1.69 mm on the gauge; temperature correction to 25 °C | Met on paper; repeatability not verifiable at TRL 3 |
| R12 | Aluminum faces, polyethylene liners, HDPE buckets; scrap alloy must be lead-free | Met on paper |

### Proposed requirement changes (awaiting Amish)

- **R3:** judge deflection at the 10 t maximum working force (0.61 mm, met) and close the molds on a metal stop so frame stretch does not set the wall. Recommended (PPR-DDR-001 item 10).
- **R11:** allow 0.8 x 0.8 m for the four-station QC rack. Recommended (PPR-DDR-001 item 11).
- **R10:** raise the budget to about $930, or cost the QC rack separately (PPR-DDR-001 item 14).

## Assumptions

- Pressing force needed for a well-consolidated wall is not published in the sources found (one low-cost press forms round-bottom filters with a 2 t jack, [Henry, Maley and Mehta, 2013](https://ojs.library.queensu.ca/index.php/ijsle/article/view/4532)); 5 to 10 t is assumed as the working range and the 20 t jack rating is used as the design load (estimate, to be confirmed with a partner factory).
- Mix follows the RDI-C recipe reported by [Rayner (2009)](https://bdd.pseau.org/outils/ouvrages/wedc_current_practices_in_manufacturing_locally_made_ceramic_pot_filters_2009.pdf); the reference filter needs about 7.5 kg of mix per pot, below the 8 to 9.5 kg factories report (PPR-CAL-001).
- The default flow acceptance band of 1.0 to 2.5 L/h follows Nicaraguan practice and the Potters for Peace range of 1.5 to 2.5 L/h; each factory sets its own band.
- Allowable stress in structural steel is taken as 165 MPa (S275 with a factor of about 1.67).
