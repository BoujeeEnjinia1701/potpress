---
doc_id: PPR-PRS-001
title: PotPress product requirements and specifications
project: PotPress
doc_type: Product requirements and specifications
version: '0.16'
status: Draft
date: '2026-10-25'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: '0.1'
  date: '2026-09-24'
  author: Amish Chadha
  change: Initial scaffold
- version: '0.2'
  date: '2026-09-25'
  author: Amish Chadha
  change: First measurable requirements for TRL 2, with concept status
- version: '0.3'
  date: '2026-09-25'
  author: Amish Chadha
  change: Apply Amish's 2026-09-25 decisions (PPR-DDR-001); R10 target $720, R6 band decided; status from PPR-CAL-001; proposed changes to R3 and R11
- version: '0.4'
  date: '2026-09-25'
  author: Amish Chadha
  change: Recommendations accepted by Amish (DDR-002); R3 at 10 t with a metal stop, R9 pin interlock, R10 $930, R11 rack 0.8 x 0.8 m and folded rails, R12 lead-free scrap; status from PPR-CAL-001 v0.2
- version: '0.5'
  date: '2026-09-26'
  author: Amish Chadha
  change: Budget top-up approved by Amish; R10 target $990, status met on paper
- version: '0.6'
  date: '2026-09-26'
  author: Amish Chadha
  change: Guarded version (decided by Amish 2026-09-26)
- version: '0.7'
  date: '2026-09-27'
  author: Amish Chadha
  change: Cost overrun decided by Amish on 2026-09-27; R10 target $1,060, status met on paper
- version: '0.8'
  date: '2026-09-30'
  author: Amish Chadha
  change: Status from PPR-CAL-001 v0.6 after the design for construction (PPR-DDR-004); R10 not met on paper; no requirement text changed
- version: '0.9'
  date: '2026-10-01'
  author: Amish Chadha
  change: Budget treated as a value-engineering target; R10 reported against the target
- version: '0.10'
  date: '2026-10-02'
  author: Amish Chadha
  change: 'Decisions of 2026-10-02: R9 at risk until the pump slot shield is designed and the ISO 13857 desk check is signed; R9 verification and the force assumption restated'
- version: '0.11'
  date: '2026-10-02'
  author: Amish Chadha
  change: 'Approved follow-ups carried out: pump slot shield designed and modelled; ISO 13857 desk check done from the model (PPR-CAL-001 v0.9), R9 at risk to not met on paper until the guard changes it
    found are made and the check is signed; R10 $1,149, $89 over the target'
- version: '0.12'
  date: '2026-10-03'
  author: Amish Chadha
  change: Four guard fixes decided by Amish (2026-10-03) modelled; desk check rerun (PPR-CAL-001 v0.10), all 23 openings meet on paper; R9 not met to met on paper (check not yet signed); R10 $1,169, $109
    over the target
- version: '0.13'
  date: '2026-10-23'
  author: Amish Chadha
  change: 'Kit 1.8 upgrade: PPR-REQ-001 becomes PPR-PRS-001; R1 to R12 become PR-001 to PR-012, each traced to a user requirement (PPR-URS-001) with target, tolerance and units; status updated from the
    STEM check (PPR-STM-001): PR-001 and PR-012 met on paper to at risk. No requirement text changed'
- version: '0.14'
  date: '2026-10-23'
  author: Amish Chadha
  change: 'STEM check fixes made under Amish''s standing instruction of 2026-10-23 (PPR-DDR-006): PR-001 sizes are fired sizes with the molds scaled for clay shrinkage; PR-004 working force limited to 6.4
    t; PR-008 lifting aid over 25 kg; PR-012 scrap sorting and melt check; PR-001 and PR-012 at risk to met on paper; PR-010 $1,279, $219 over the target'
- version: '0.15'
  date: '2026-10-24'
  author: Amish Chadha
  change: 'Kit 1.9.1 upgrade: PR-013 (local spares) added for UR-013, which had no product requirement; proposed, awaiting Amish. No other requirement changed'
- version: '0.16'
  date: '2026-10-25'
  author: Amish Chadha
  change: 'Amish''s decisions of 2026-10-25 (D8, D9): PR-003 states 10 t as a structural check case; PR-004 working force limit 6.4 to 5.4 t with 85 % pump efficiency; PR-013 text accepted. No status changed'
supersedes: PPR-REQ-001
---

# PotPress product requirements and specifications

What the press and QC rack must do, each requirement traced to a user need in PPR-URS-001 (links in PPR-RTM-001). Until kit 1.8 this document was PPR-REQ-001, and R1 to R12 are now PR-001 to PR-012 with the same text. These requirements were checked by calculation at TRL 3 (PPR-CAL-001 v0.11). They are not yet validated with a filter factory and will be revised after co-design sessions (see PPR-PRB-001). With the design made constructable (PPR-DDR-004, 2026-09-30), one is over the value-engineering target (R10, the parts cost now $1,279 against the $1,060 target, $219 over), two are at risk (R2 and R7) and nine are met on paper, R9 among them since the four guard fixes Amish decided on 2026-10-03 close every opening the ISO 13857 desk check found short (the check is not yet signed by a competent person); see Table 1. The STEM check of 2026-10-23 (PPR-STM-001) moved PR-001 (clay shrinkage) and PR-012 (scrap melt check) to at risk; the same day their fixes were made in the design under Amish's standing instruction (PPR-DDR-006), so both are met on paper again. With them, PR-010 stands at $1,279, $219 over the target. Amish's decisions of 2026-09-25 are recorded in PPR-DDR-001 and PPR-DDR-002: the R6 default band, R3 judged at the 10 t working force, the R10 target of $930 (topped up to $990 by Amish on 2026-09-26 and raised to $1,060 by Amish on 2026-09-27, PPR-DDR-003), the R11 rack area of 0.8 x 0.8 m, the pin-presence interlock in R9 and lead-free scrap in R12. The guarded version and the guarding detail in R9 were decided by Amish on 2026-09-26 (PPR-DDR-003).

The **reference filter** used throughout is the common flowerpot form: inner rim diameter 280 mm, inner depth 240 mm, wall 15 mm, flat rim about 345 mm across, about 12 L to the brim and about 10 L working volume (dimensions are estimates based on the 280 by 250 mm form reported by [Potters for Peace](https://www.pottersforpeace.org/ceramic-water-filter-project)).

*Table 1. Product requirements and specifications. Status at TRL 3 from PPR-CAL-001 v0.13 and the STEM check PPR-STM-001 v0.3 (2026-10-24). The "Was" column gives the requirement number used before kit 1.8, which the calculation note, build plan and earlier records still cite.*

| ID | Traces to | Category | Title | Requirement | Target | Tolerance | Units | Verification | Status | Was |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PR-001 | UR-001 | Performance | Reference filter | Fired filter: inner rim 280 mm, inner depth 240 mm, wall 15 mm, flat rim; geometry set by parameters in one source file; molds sized to the pressed (green) pot, the fired size divided by (1 - total clay shrinkage), with the shrinkage measured on the partner clay before patterns are printed (PPR-DDR-006) | 280 / 240 / 15 fired (rim / depth / wall); 8 % shrinkage assumed | Per PR-002 | mm | Model check; shrinkage test bar on the partner clay (ASTM C326 method); later measurement of fired pots | Met on paper: 12.30 L brim, 9.91 L working fired; molds 1.087 times the fired size; shrinkage still assumed | R1 |
| PR-002 | UR-002, UR-012 | Performance | Even wall | Wall thickness within ±1 mm around the circumference and from pot to pot; molds self-center to within 0.5 mm | 15 | ±1 (wall); 0.5 (centering) | mm | Tolerance stack and guide design; later sectioned pots | **At risk**: ±0.44 mm with hand-finished molds; template print error of 0.2 to 0.5 % not yet in the budget (STEM E2) | R2 |
| PR-003 | UR-001, UR-007 | Physical architecture | Pressing force and frame strength | 20 t (196 kN) rated jack; frame, pin, bolts and platen carry 1.5 times the jack rating (294 kN) without yield; deflection between the molds under 1 mm at 10 t, with the molds closing on a metal stop so frame stretch does not set the wall (decided by Amish, 2026-09-25); 10 t is a structural check case, not a working force, which PR-004 limits (decided by Amish, 2026-10-25, D9) | 294 kN without yield; under 1 mm deflection at the 10 t check case | max | kN; mm | Beam and pin calculation; later proof load | Met on paper: beams 190 MPa, pin 272 MPa, M16 bolts 117 MPa in shear, male flange 60 MPa (cast yield about 80); 0.66 mm at 10 t | R3 |
| PR-004 | UR-003 | Performance | Throughput | Press cycle of 6 min or less with two operators, so 50 or more pots per 6 h of pressing; working force no more than 5.4 t, where the pump handle force reaches 150 N with 85 % pump and seal efficiency (PPR-DDR-006; lowered from 6.4 t by Amish, 2026-10-25, D9) | 6 min cycle; 50 pots per 6 h; 5.4 t working force | max; min; max | min; pots; t | Cycle breakdown; later timed trial | Met on paper, thin margin: 5.2 min, 69 pots per 6 h; handle force about 148 N at the 5.4 t limit with 85 % efficiency (STEM S8; EN 1005-3 assessment to do) | R4 |
| PR-005 | UR-003 | Physical architecture | Mold opening | Male mold lifts at least 30 mm clear of the female rim so the mold carriage slides out for loading and demolding; pressing stroke within one jack stroke | 30 mm clear of the rim | min | mm | Kinematic layout | Met on paper: 310 mm opening against 291 mm needed (49 mm clear); 110 of 150 mm stroke | R5 |
| PR-006 | UR-008, UR-012 | Performance | Flow-rate QC | Rack tests 4 soaked filters at once; T-gauge reads flow over 1 h to 0.1 L/h; repeatability ±0.1 L/h; acceptance band set per factory (default 1.0 to 2.5 L/h in the first hour, corrected to 25 °C; decided by Amish, 2026-09-25) | 4 stations; 0.1 L/h resolution | ±0.1 L/h repeatability | L/h | Gauge calibration by volume; later repeat tests | Met on paper; repeatability to verify at TRL 4 | R6 |
| PR-007 | UR-005 | Materials | Molds made locally | Molds cast from 3D-printed patterns printed on a 250 x 250 mm class printer; finishing with hand tools and a drill press; no lathe over 300 mm swing | 250 x 250 mm printer bed | max | mm | Pattern split and finishing review with a foundry | **At risk**: 16 segments of 243 mm fit a true 250 x 250 mm bed only (STEM E1); hand finishing unproven | R7 |
| PR-008 | UR-004, UR-006 | Physical architecture | Frame built locally | Standard steel channel and plate; stick welding, drilling and bolting only; heaviest single part 40 kg or less for transport; every part over 25 kg lifted with a chain block on eye bolts or a sling, never by hand (PPR-DDR-006) | 40 kg heaviest part | max | kg | Part list and mass estimate | Met on paper: heaviest parts 39.6 kg (female mold with plate, platen); lifting set BOM item 22 | R8 |
| PR-009 | UR-007 | Safety | Safe operation | Fixed welded-mesh guards on the sides, back and roof and a hinged front gate enclose every pinch point of the molds, platen, jack and carriage; guard openings and their distance from moving parts prevent finger reach into the pinch zone, judged against ISO 13857; a guard-locking gate interlock stops the jack release closing (so the jack cannot be pumped to build pressure) unless the gate is shut, and keeps the gate shut while the release is closed; jack pump and release worked from outside the guard; a pin-presence interlock prevents pressing unless the load pin is fully home (pin interlock decided by Amish, 2026-09-25; guarding decided by Amish, 2026-09-26) | All openings meet ISO 13857 Table 4 | Pass or fail | n/a | Hazard review and guard layout in the model; ISO 13857 desk check signed by a competent person before any force above hand pressure (decided by Amish, 2026-10-02) | Met on paper: 23 of 23 openings; desk check not yet signed (hold point); Table 7 and floor gap not checked (STEM E3) | R9 |
| PR-010 | UR-009 | Cost | Affordable | Press plus QC rack at or under the $1,060 value-engineering target in parts (a hypothetical control target; raised from $600 to $720 and then to $930 by Amish, 2026-09-25; topped up to $990 by Amish, 2026-09-26; raised to $1,060 by Amish, 2026-09-27) | 1,060 (value-engineering target) | max | USD | Priced BOM (`bom/bom.csv`) | **Over the value-engineering target by $219** ($1,279) | R10 |
| PR-011 | UR-010 | Physical architecture | Footprint | Press within 1.0 x 0.7 m floor area and 2.0 m height, with the rail extension folded; QC rack within 0.8 x 0.8 m (relaxed from 0.8 x 0.5 m by Amish, 2026-09-25) | 1.0 x 0.7 x 2.0 (press); 0.8 x 0.8 (rack) | max | m | Model check | Met on paper: 940 x 700 x 1,828 mm guarded; at the 0.7 m depth limit with no margin | R11 |
| PR-012 | UR-011 | Materials | Product-safe materials | Faces that touch clay or test water are aluminum, food-grade polyethylene or stainless steel; no lead-based paint or oiled release agents on mold faces; molds cast from lead-free scrap (no free-machining alloys; decided by Amish, 2026-09-25): A356 cast alloy wheel scrap sorted before melting, with lead and cadmium within the EN 601 food-contact limits (PPR-DDR-006) | Aluminium, food-grade PE or stainless faces; lead-free scrap | Pass or fail | n/a | Material list review; a chill sample of each melt checked by spark OES, or handheld XRF for lead, before pouring, recorded per heat | Met on paper; EN 601 limit values to confirm | R12 |
| PR-013 | UR-013 | Maintenance | Local spares | Every wear part (bottle jack and its seals, return springs, UHMW-PE stem guides, release liners, locating dowels and bushes, lead screw nut, fasteners) is a standard catalogue item or cut from standard stock, specified by size and grade rather than by brand: ISO metric bolts, nuts and washers M5 to M16, a 20 t bottle jack with a base about 160 mm square, standard tension springs, 16 mm hardened dowels (ISO 8734) | All wear parts from regional hardware, bearing or plastics suppliers; no part only the original maker supplies | Pass or fail | n/a | BOM review (inspection, TRL 3); regional availability confirmed with a partner factory (TRL 4) | Met on paper; regional availability to confirm (text decided by Amish, 2026-10-25, D8) | |

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

### Status after the design for construction, 2026-09-30 (PPR-DDR-004)

- **R10:** the parts a build needs (steel base plate under the female mold, thicker mold flanges, dowels and bushes, floor anchors, bolted jack plate, adapter disc, interlock details) bring the BOM to $1,143 against $1,060 (status within the value-engineering target to over it by $83). The target is unchanged; the design decisions register lists the cost drivers and savings worth trying.
- No requirement text changed. R3, R8 and R11 figures are updated from PPR-CAL-001 v0.6; their status is unchanged.

### Status after the approved follow-ups, 2026-10-02 (PPR-CAL-001 v0.9)

- **R9:** the fixed inner shield behind the pump slot is designed and modelled, and the ISO 13857 desk check is done from the model's distances. The shield closes the pump slot (it opens only onto the handle and the jack's pump socket), but the check found other openings short of ISO 13857 Table 4: the 12.7 mm mesh on the front strips, lower front panel, front gate and roof is 39 to 77 mm from moving parts (80 mm needed), the release shaft and pin cable openings in the front right strip are too large for their distance, and the gap in the top beam is open from above between the parts in it. Status at risk to **not met on paper**. The changes that close these are proposed, awaiting Amish, in the design decisions register; the check is not yet signed by a competent person.
- **R10:** the shield adds $6, so the BOM is $1,149 against the $1,060 target ($83 to $89 over).
- No requirement text changed.

### Status after the guard fixes decided by Amish, 2026-10-03 (PPR-CAL-001 v0.10)

Amish, 2026-10-03: "PotPress - move forward with the four guard fixes. I accept the cost."

- **R9:** the four fixes are in the model: 6.35 mm (1/4 in) mesh with 0.9 mm wire on the front strips, lower front panel, front gate and roof; small-hole plates with a 4 mm gap round the release shaft and a 2 mm gap round the pin cable; 3 mm cover plates on the top beam from the crank bracket to the beam ends, which also close the open tops of the upright channels that the first check missed; 2 mm covers on the front and back of the crank bracket. The rerun desk check finds all 23 openings meet ISO 13857 Table 4 on paper, and no moving part touches the new parts over the full stroke, crank lift and gate travel. Status not met to **met on paper**. The check is not yet signed by a competent person; that signature remains a hold point before any force above hand pressure.
- **R10:** the fixes add $20, so the BOM is $1,169 against the $1,060 target ($89 to $109 over).
- No requirement text changed.

### Requirement changes made under Amish's standing instruction, 2026-10-23 (PPR-DDR-006)

Amish, 2026-10-23: "whenever a STEM check fails propose and implement the best fix to the design and constructability."

- **PR-001:** the 280 / 240 / 15 mm sizes are fired sizes; the molds are 1.087 times larger for an assumed 8 % total shrinkage, to be replaced by the partner clay's test-bar value (status at risk to met on paper).
- **PR-004:** the working force is limited to 6.4 t, where the pump handle force reaches the 150 N screening limit (status unchanged).
- **PR-008:** every part over 25 kg is lifted with a chain block; 40 kg stays as the transport limit (status unchanged).
- **PR-012:** the scrap is A356 wheel scrap, sorted, with each melt checked by OES or XRF against EN 601 (status at risk to met on paper).
- **PR-010:** the fixes add $110, so the BOM is $1,279 against the $1,060 target ($109 to $219 over).

### Requirement added in the kit 1.9.1 upgrade, 2026-10-24

- **PR-013 (new, traces to UR-013):** wear parts are standard catalogue items or standard stock, specified by size and grade. UR-013 had no product requirement after the kit 1.8 upgrade (the traceability matrix flagged it). The requirement text was proposed as decision D8 in PPR-DEC-001 and decided by Amish on 2026-10-25 (see below); status met on paper from the BOM, with regional availability to confirm with a partner.

### Requirement changes decided by Amish, 2026-10-25

Amish, 2026-10-25: "i concur with your recommendations" (PPR-DEC-001 D8 and D9).

- **PR-003 (D9):** 10 t is restated as a structural check case for the deflection limit, not a maximum working force; the requirement values are unchanged (status unchanged, met on paper: 0.66 mm at 10 t).
- **PR-004 (D9):** the working force limit is lowered from 6.4 t to 5.4 t, where the pump handle force reaches the 150 N screening limit once 85 % pump and seal efficiency is counted (about 148 N at 5.4 t; PPR-CAL-001 v0.13). Mean pressure on the pot at the limit falls from 0.57 to 0.48 MPa. Status unchanged, met on paper, with the EN 1005-3 assessment still to do. A separate two-speed pump if trials need more than 5.4 t stays open (D6).
- **PR-013 (D8):** the text as drafted on 2026-10-24 is accepted; the named spares list with a partner factory is confirmed at TRL 4.

## Assumptions

- Pressing force needed for a well-consolidated wall is not published in the sources found (one low-cost press forms round-bottom filters with a 2 t jack, [Henry, Maley and Mehta, 2013](https://ojs.library.queensu.ca/index.php/ijsle/article/view/4532)); 5 to 10 t is assumed as the working range and the 20 t jack rating is used as the design load. Decided by Amish on 2026-10-02: every structural check stays at the full 20 t jack, and the working force is a process setting found in pressing trials with a partner factory, starting near 2 t and stepping up.
- Mix follows the RDI-C recipe reported by [Rayner (2009)](https://bdd.pseau.org/outils/ouvrages/wedc_current_practices_in_manufacturing_locally_made_ceramic_pot_filters_2009.pdf); the reference filter, pressed 1.087 times oversize for clay shrinkage, needs about 9.6 kg of mix per pot, just above the 8 to 9.5 kg factories report (PPR-CAL-001).
- The default flow acceptance band of 1.0 to 2.5 L/h follows Nicaraguan practice and the Potters for Peace range of 1.5 to 2.5 L/h; each factory sets its own band.
- Allowable stress in structural steel is taken as 165 MPa (S275 with a factor of about 1.67).
- Guard openings: checked against ISO 13857:2019 Table 4 in the desk check of 2026-10-02, rerun with the guard fixes on 2026-10-03 (PPR-CAL-001, section 15), using straight-line distances from the model and the table as read for the check; a competent person confirms the table values and signs the check before any force above hand pressure.
