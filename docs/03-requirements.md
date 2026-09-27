---
doc_id: PPR-REQ-001
title: PotPress requirements
project: PotPress
doc_type: Requirements
version: "0.7"
status: Draft
date: '2026-09-27'
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
- version: "0.4"
  date: '2026-09-25'
  author: Amish Chadha
  change: Recommendations accepted by Amish (DDR-002); R3 at 10 t with a metal stop, R9 pin interlock, R10 $930, R11 rack 0.8 x 0.8 m and folded rails, R12 lead-free scrap; status from PPR-CAL-001 v0.2
- version: "0.5"
  date: '2026-09-26'
  author: Amish Chadha
  change: Budget top-up approved by Amish; R10 target $990, status met on paper
- version: "0.6"
  date: '2026-09-26'
  author: Amish Chadha
  change: Guarded version (decided by Amish 2026-09-26)
- version: "0.7"
  date: '2026-09-27'
  author: Amish Chadha
  change: Cost overrun decided by Amish on 2026-09-27; R10 target $1,060, status met on paper
---

# PotPress requirements

These requirements were checked by calculation at TRL 3 (PPR-CAL-001 v0.5). They are not yet validated with a filter factory and will be revised after co-design sessions (see PPR-PRB-001). With the guarded version and the budget raised to $1,060, none is not met, two are at risk (R2 and R7) and ten are met on paper; see Table 2. Amish's decisions of 2026-09-25 are recorded in PPR-DDR-001 and PPR-DDR-002: the R6 default band, R3 judged at the 10 t working force, the R10 target of $930 (topped up to $990 by Amish on 2026-09-26 and raised to $1,060 by Amish on 2026-09-27, PPR-DDR-003), the R11 rack area of 0.8 x 0.8 m, the pin-presence interlock in R9 and lead-free scrap in R12. The guarded version and the guarding detail in R9 were decided by Amish on 2026-09-26 (PPR-DDR-003).

The **reference filter** used throughout is the common flowerpot form: inner rim diameter 280 mm, inner depth 240 mm, wall 15 mm, flat rim about 345 mm across, about 12 L to the brim and about 10 L working volume (dimensions are estimates based on the 280 by 250 mm form reported by [Potters for Peace](https://www.pottersforpeace.org/ceramic-water-filter-project)).

*Table 1. Requirements.*

| ID | Requirement | Target | Verification (TRL 3 or later) |
| --- | --- | --- | --- |
| R1 | Form the reference filter | Inner rim 280 mm, inner depth 240 mm, wall 15 mm, flat rim; geometry set by parameters in one source file | Model check; later measurement of pressed pots |
| R2 | Even wall | Wall thickness within ±1 mm around the circumference and from pot to pot; molds self-center to within 0.5 mm | Tolerance stack and guide design; later sectioned pots |
| R3 | Pressing force and frame strength | 20 t (196 kN) rated jack; frame, pin, bolts and platen carry 1.5 times the jack rating (294 kN) without yield; deflection between the molds under 1 mm at the 10 t maximum working force, with the molds closing on a metal stop so frame stretch does not set the wall (decided by Amish, 2026-09-25) | Beam and pin calculation; later proof load |
| R4 | Throughput | Press cycle of 6 min or less with two operators, so 50 or more pots per 6 h of pressing | Cycle breakdown; later timed trial |
| R5 | Mold opening | Male mold lifts at least 30 mm clear of the female rim so the mold carriage slides out for loading and demolding; pressing stroke within one jack stroke | Kinematic layout |
| R6 | Flow-rate QC | Rack tests 4 soaked filters at once; T-gauge reads flow over 1 h to 0.1 L/h; repeatability ±0.1 L/h; acceptance band set per factory (default 1.0 to 2.5 L/h in the first hour, corrected to 25 °C; decided by Amish, 2026-09-25) | Gauge calibration by volume; later repeat tests |
| R7 | Molds made locally | Molds cast from 3D-printed patterns printed on a 250 x 250 mm class printer; finishing with hand tools and a drill press; no lathe over 300 mm swing | Pattern split and finishing review with a foundry |
| R8 | Frame built locally | Standard steel channel and plate; stick welding, drilling and bolting only; heaviest single part 40 kg or less for two-person handling | Part list and mass estimate |
| R9 | Safe operation | Fixed welded-mesh guards on the sides, back and roof and a hinged front gate enclose every pinch point of the molds, platen, jack and carriage; guard openings and their distance from moving parts prevent finger reach into the pinch zone, judged against ISO 13857; a guard-locking gate interlock stops the jack release closing (so the jack cannot be pumped to build pressure) unless the gate is shut, and keeps the gate shut while the release is closed; jack pump and release worked from outside the guard; a pin-presence interlock prevents pressing unless the load pin is fully home (pin interlock decided by Amish, 2026-09-25; guarding decided by Amish, 2026-09-26) | Hazard review and guard layout in the model; later guard check against ISO 13857 |
| R10 | Affordable | Press plus QC rack $1,060 or less in parts (raised from $600 to $720 and then to $930 by Amish, 2026-09-25; topped up to $990 by Amish, 2026-09-26; raised to $1,060 by Amish, 2026-09-27) | Priced BOM (`bom/bom.csv`) |
| R11 | Footprint | Press within 1.0 x 0.7 m floor area and 2.0 m height, with the rail extension folded; QC rack within 0.8 x 0.8 m (relaxed from 0.8 x 0.5 m by Amish, 2026-09-25) | Model check |
| R12 | Product-safe materials | Faces that touch clay or test water are aluminum, food-grade polyethylene or stainless steel; no lead-based paint or oiled release agents on mold faces; molds cast from lead-free scrap (no free-machining alloys; decided by Amish, 2026-09-25) | Material list review |

*Table 2. Status against each requirement at TRL 3 (from PPR-CAL-001 v0.5 and, for R9, R10 and R11, the guarded model and BOM; least certain first).*

| ID | TRL 3 value | Status |
| --- | --- | --- |
| R2 | Wall ±1.40 mm as cast; ±0.43 mm with molds hand-finished to templates; coaxial ±0.43 mm via the locating lip | **At risk** |
| R7 | 16 pattern segments for a 250 mm printer; cavity finishing without a lathe unproven | **At risk** |
| R9 | Guards, gate and interlocks modeled (PPR-DDR-003): 12.7 mm welded mesh with nearest moving parts about 105 to 110 mm behind it; guard-locking gate interlock and pin-presence plunger on the jack release lock bar; pump through a 25 mm slot, release T-handle outside | Met on paper; openings and distances assumed against ISO 13857, not checked (proposed, awaiting Amish) |
| R10 | Priced BOM $1,051 (press $970, QC rack $81) against $1,060 with the guarded version | Met on paper, $9 (0.8 %) margin |
| R1 | Reference filter from `PARAMS` in `cad/src/model.py`: 12.30 L to the brim, 9.91 L working | Met on paper |
| R3 | No yield at 294 kN: beams 190 MPa, uprights 54 MPa, 60 mm pin 258 MPa (yield 650), joint bolts 75 MPa. Deflection between the molds 0.61 mm at 10 t (1.84 mm at 294 kN) | Met on paper |
| R4 | 5.2 min cycle, 69 pots per 6 h | Met on paper, thin margin |
| R5 | 310 mm opening against 270 mm needed; 110 of 150 mm jack stroke | Met on paper |
| R6 | 4 stations; 0.1 L is 1.69 mm on the gauge; temperature correction to 25 °C | Met on paper; repeatability not verifiable at TRL 3 |
| R8 | Heaviest part 38.9 kg (platen); upright joints bolted, largest frame part 37.4 kg | Met on paper |
| R11 | Press 940 x 700 mm guarded with the rail extension folded (840 x 655 mm unguarded; 970 mm deep deployed, gate open), 1,806 mm tall; QC rack 780 x 780 mm | Met on paper, at the 0.7 m depth limit with no margin |
| R12 | Aluminum faces, polyethylene liners, HDPE buckets; lead-free scrap alloy | Met on paper |

### Requirement changes decided by Amish, 2026-09-25 (PPR-DDR-002)

- **R3:** deflection judged at the 10 t maximum working force, with the molds closing on a metal stop (was 294 kN; status not met to met on paper).
- **R10:** target raised from $720 to $930. The decided bolted joints and hinged rail extension bring the BOM to $984, so R10 was still not met; Amish topped up the budget to $990 on 2026-09-26 (see below).
- **R11:** QC rack area relaxed from 0.8 x 0.5 m to 0.8 x 0.8 m; the press footprint is judged with the hinged rail extension folded (status not met to met on paper).
- **R9 and R12:** the pin-presence interlock and lead-free scrap are now part of the requirement text.

### Requirement change decided by Amish, 2026-09-26

- **R10:** budget topped up from $930 to $990 ("I am ok with the budget top ups"; PPR-DDR-002 v0.2, item 16). The priced BOM of $984 now meets R10 on paper with a $6 (0.6 %) margin, which is thin; any price rise moves R10 back to at risk. The guarded version later the same day took the BOM to $1,051 (see below).

### Requirement change decided by Amish, 2026-09-26 (guarded version, PPR-DDR-003)

- **R9:** now states the guarding: fixed welded-mesh guards, a hinged front gate with a guard-locking interlock on the jack release, openings judged against ISO 13857, and controls outside the guard (status at risk to met on paper, with the ISO 13857 distances still an assumption).
- **R10:** the guards, gate and interlock add $67, so the BOM is $1,051 against $990 (status met on paper to not met). The budget was left unchanged that day; Amish decided the overrun on 2026-09-27 (see below).
- **R11:** the guarded press is 940 x 700 mm, exactly at the 0.7 m depth limit (status unchanged, no margin).

### Requirement change decided by Amish, 2026-09-27 (PPR-DDR-003 v0.2)

- **R10:** budget raised from $990 to $1,060 ("i agree with the budget for potpress"; option (a) in PPR-DDR-003). The priced BOM of $1,051 meets R10 on paper with a $9 (0.8 %) margin, which is thin; any price rise moves R10 back to at risk (status not met to met on paper).

## Assumptions

- Pressing force needed for a well-consolidated wall is not published in the sources found (one low-cost press forms round-bottom filters with a 2 t jack, [Henry, Maley and Mehta, 2013](https://ojs.library.queensu.ca/index.php/ijsle/article/view/4532)); 5 to 10 t is assumed as the working range and the 20 t jack rating is used as the design load (estimate, to be confirmed with a partner factory).
- Mix follows the RDI-C recipe reported by [Rayner (2009)](https://bdd.pseau.org/outils/ouvrages/wedc_current_practices_in_manufacturing_locally_made_ceramic_pot_filters_2009.pdf); the reference filter needs about 7.5 kg of mix per pot, below the 8 to 9.5 kg factories report (PPR-CAL-001).
- The default flow acceptance band of 1.0 to 2.5 L/h follows Nicaraguan practice and the Potters for Peace range of 1.5 to 2.5 L/h; each factory sets its own band.
- Allowable stress in structural steel is taken as 165 MPa (S275 with a factor of about 1.67).
- Guard openings: 12.7 mm (1/2 in) square welded mesh, about 11 mm clear, with moving parts at least about 105 mm behind the mesh, is assumed to keep fingers out of the pinch zone. ISO 13857 is the reference; its tables were not checked here, so this is a stated assumption.
