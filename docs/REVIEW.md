# Review note: PotPress

## Session 2026-09-25: TRL 3

Authority: Amish wrote on 2026-09-25, "proceed with all of your recommendations across all batches. Make sure we don't proceed to TRL 4 on any of them." `project.yaml` now shows `trl: 3` and `trl_target: 3`. **TRL 4 is on hold by Amish's instruction.**

### What was done

- `docs/decisions/0001-trl2-review-decisions.md` (PPR-DDR-001 v0.1): TRL 2 items 1 to 8 recorded as decided by Amish, 2026-09-25: go with recommendation; item 9 and new items 10 to 15 left open.
- `docs/04-calcs/01-sizing.md` (PPR-CAL-001 v0.1) and `docs/04-calcs/sizing.py`: geometry, mix and masses, pressure, frame, pin, welds, mold shells, deflection chain, travel, jack, crank, cycle, alignment stack, patterns, QC gauge and temperature correction, masses from the model, tipping, cost, and a results table for R1 to R12. The script reads `cad/src/model.py` and `bom/bom.csv` and prints every quoted number.
- `cad/src/model.py`: parametric build123d model (filter, shell molds with locating lip and flash groove, UPN channel frame, platen with sleeves, rails and carriage, stem, 60 mm pin, lead screw and handwheel, 2 x 2 QC rack). Exports `cad/step/potpress-assembly.step`, `potpress-press.step`, `female-mold.step`, `male-mold.step`, `filter-pot.step`, `t-gauge.step` and matching STLs in `cad/stl/`.
- `cad/src/sheets.py` and `cad/drawings/PPR-DWG-001.svg`, `.pdf`, `.png`: general arrangement at Rev P1, 1:20, marked "CONCEPT, NOT FOR FABRICATION" and "PRELIMINARY, NOT FOR FABRICATION". The concept sheet keeps PPR-DWG-010.
- `bom/bom.csv`: 19 lines, all priced with supplier types, total $926; `bom/bom-notes.md` updated.
- `cad/src/concept_media.py` now builds from the model and the calc; all media in `media/` regenerated and checked; temporary `media/_views*` folders deleted.
- `docs/01-problem.md`, `docs/02-concept.md`, `docs/03-requirements.md` moved to v0.3; `README.md` updated; `project.yaml` set to TRL 3 with the evidence list and `budget_usd: 720`.

### Requirements at TRL 3 (not met first)

| ID | Result | Status |
| --- | --- | --- |
| R3 | Strength met (beams 190 MPa, pin 258 MPa of 650, uprights 54 MPa at 294 kN); deflection between molds 1.84 mm at 294 kN against 1 mm (0.61 mm at 10 t) | **Not met** |
| R10 | $926 against $720 (press $845, QC rack $81) | **Not met**, 29 % over |
| R11 | Four 345 mm rims need a 780 x 780 mm rack against 0.8 x 0.5 m; press frame 840 x 640 mm but 970 mm deep with the fixed rail extension | **Not met** |
| R2 | Wall ±1.40 mm as cast; ±0.43 mm if hand-finished to templates | At risk |
| R7 | 16 pattern segments on a 250 mm printer; finishing without a lathe unproven | At risk |
| R8 | Heaviest part 38.9 kg as fabricated, but the welded frame is 147 kg in one piece | At risk |
| R9 | Guards and interlocks only in the BOM, not modeled | At risk |
| R1, R4, R5, R6, R12 | Filter geometry from one file; 5.2 min cycle and 69 pots per 6 h; 310 mm opening against 270 mm; 1.69 mm per 0.1 L; product-safe faces | Met on paper |

TRL 2 errors corrected: the single UPN 100 base (about 1,071 MPa), the two 30 mm pins (about 1,034 MPa in bending), solid molds (would be 57 and 41 kg), the four-station rack in 800 x 440 mm (cannot fit), press mass 180 kg (now 298 kg) and cost $716 (now $926).

### Decisions recorded

Decided by Amish, 2026-09-25: go with recommendation (PPR-DDR-001): jack below; crank lift with a load pin and a standard jack; cast aluminum molds from printed patterns (concrete-backed variant documented only); welded frame; slide-out and tilt demolding; manual QC rack and T-gauge; default band 1.0 to 2.5 L/h corrected to 25 °C; `budget_usd` raised to $720.

### Proposed, awaiting Amish

1. First co-design partner (item 9): left open under the portfolio rule; no choice made.
2. R3: judge deflection at the 10 t working force with the molds closing on a metal stop (recommended), rather than at 294 kN.
3. R11: allow 0.8 x 0.8 m for the 2 x 2 QC rack (recommended); also a hinged front rail extension for the press depth.
4. Frame joints: bolt the four upright joints (4 x M20 8.8 each) so no part exceeds 40 kg (recommended).
5. Load pin: one 60 mm 42CrMo4 pin with a pin-presence interlock (recommended, as modeled) or two pins at two stations.
6. Cost gap of $206: raise `budget_usd` to about $930 (recommended), or cost the QC rack separately and build the concrete-backed molds first.
7. Scrap aluminum must be lead-free (recommended) or new A356 ingot.

### Safety concerns

- The single load pin carries the whole press force; a missing or half-inserted pin ejects the male mold. The pin-presence interlock is essential, not optional.
- Guards, gate and interlocks are BOM lines, not yet modeled or designed (R9 at risk).
- The press is about 298 kg with its center of mass about 0.8 m up; about 740 N at 1 m tips it forward. Anchor it.
- Handwheel at about 1.8 m: awkward overhead cranking; the self-locking screw holds the mold if released.
- Lead in scrap aluminum could contaminate a drinking-water product; specify lead-free scrap.
- Silica dust, silver compounds and kiln heat in the same workshop; a passing flow test is not proof of pathogen removal.
- All strengths are paper values; a proof load test by a competent person is needed before any use, and that is TRL 4 work.

### Citations

- Henry, Maley and Mehta, "Designing a Low-Cost Ceramic Water Filter Press", *IJSLE* 8 (1), 2013: checked this session through a public PDF copy. It confirms the $2,300 Potters Without Borders press (over $3,000 with labor), a target under $200 built by two people in two days, and a 2 t car jack for round-bottom filters. The journal page itself blocks automated fetching.
- CMWG (2011) best practice recommendations: title confirmed by web search, but the PDF returned HTTP 403, so it is still cited for scope only, not for specific numbers. Flag kept.

### Existing TRL 4 material

None found. `build-log/README.md` is the scaffold header only; `electronics/` and `firmware/` are empty. Nothing was added to them.

### Recommended next step

Amish to decide items 2 to 7 above (and the partner when the area is ready), after which the requirement and cost changes can be folded into v0.4 of the documents at TRL 3. **TRL 4 is on hold by Amish's instruction.** For reference only, TRL 4 would need: a built press and molds, a proof load test to 294 kN with the pin interlock working, measured mold gap deflection and wall thickness on sectioned pots, a timed cycle trial, T-gauge calibration by volume, a test report (TST) with `environment: lab` and build log entries. None of this should start without a new instruction.

## Session 2026-09-25: /populate to a strong TRL 2 (overnight batch run)

### What was done

- `docs/01-problem.md` (PPR-PRB-001 v0.2): the problem with sourced facts (JMP 2025, Potters for Peace, the Cambodia trial and lab study, press costs from the Nigerian and Penn State presses, production parameters, factory QC practice), users and context, constraints, out of scope, prior work with links, open questions, and a co-design checklist (none existed before; the portfolio's standard checklist was added and tailored to a filter factory).
- `docs/03-requirements.md` (PPR-REQ-001 v0.2): 12 measurable requirements (R1 to R12) with targets and planned verification, and a status table against the concept.
- `docs/02-concept.md` (PPR-PRC-001 v0.2): how it works, components numbered to the BOM and exploded view, first-order numbers (geometry and charge, force and pressure, travel and cycle, flow QC, cost) with assumptions, design choices, safety and open questions.
- `cad/src/concept_media.py`: massing model of the press (base, uprights, top beam, jack, platen, springs, carriage, female and male molds, male mold slide, pressed pot) and the QC rack (rack, test pots, T-gauge, buckets), with the 1.75 m scale figure.
- `media/`: `hero.png`, `concept-blueprint.png`, `.pdf` and `.svg`, `cutaway.png`, `exploded.png` with BOM callouts, `flow.png` (material flow per filter, all values marked as estimates), `model.glb` and `viewer.html`.
- `bom/bom.csv`: 19 lines with indicative prices, items 1 to 14 numbered to match the exploded view; `bom/bom-notes.md` updated.
- `README.md`: hero image and links line added before "## Problem"; problem, concept, key components and safety updated to match.
- `docs/pdf/`: branded PDFs of the three controlled documents.
- `project.yaml`: unchanged. The pitch and problem still match what was found.

### Key results (estimates, to be checked at TRL 3)

| Quantity | Estimate | Requirement |
| --- | --- | --- |
| Reference filter | 280 mm inner rim, 240 mm deep, 15 mm wall; about 10 L working volume | R1 met on paper |
| Charge and pot mass | about 8.0 kg mix; about 7.3 kg pressed, about 4.2 kg fired | |
| Mean pressure | about 0.5 to 1.1 MPa at 5 to 10 t; 2.1 MPa at 20 t | Working force assumed, not sourced |
| Frame at 1.5 x jack rating (294 kN) | top beam about 190 MPa, uprights about 54 MPa, pins about 104 MPa | R3 met on paper; deflection unchecked |
| Opening travel | about 270 mm needed; jack gives about 150 mm | R5 **at risk**; crank lift proposed |
| Cycle and output | about 5 min; about 70 pots per 6 h of pressing | R4 met, thin margin |
| Flow gauge | 1.0 L is about 16 mm of level drop; 0.1 L about 1.6 mm | R6 met, resolution tight |
| Size and mass | press about 920 x 640 x 1,655 mm, about 180 kg | R8 and R11 met |
| Parts cost | about $716 (press about $645, QC rack about $71) | R10 **not met**, about 19 % over |

Requirements not met or at risk: **R10 (cost) is not met.** R2 (even wall) is at risk until the mold alignment is designed; R5 (opening travel) is at risk until the lift and jack are chosen; R7 (molds made locally without a large lathe) is at risk because cavity finishing is unproven.

### Proposed, awaiting Amish

1. **Architecture:** jack below lifting the female mold against a fixed male mold (recommended), versus an inverted-rated jack pushing down, or a screw press.
2. **Male mold lift:** hand crank with load pins and a standard jack (recommended), versus a 20 t long-stroke cylinder with hand pump (about $150 to $250 more), versus a counterweighted lever.
3. **Mold material:** cast aluminum from printed patterns (recommended), with printed shells backed by fiber-reinforced concrete built as a low-cost variant (about $115 cheaper, durability unknown).
4. **Frame:** welded (recommended), with a bolted variant documented later.
5. **Demolding:** slide-out carriage that tilts to turn the pot onto a board (recommended), versus air-assisted release or leaving the pot on the male mold.
6. **QC:** manual rack and printed T-gauge (recommended); load-cell logger per station as a later option.
7. **Default acceptance band:** 1.0 to 2.5 L/h in the first hour, corrected to 25 °C, adjustable per factory.
8. **Budget:** (a) raise `budget_usd` from $600 to about $720; (b) keep $600 and adopt the concrete-backed molds for the first prototype (about $600); (c) keep $600 for the press only and cost the QC rack separately (the press alone is about $645, still over). Recommendation: (a), because the aluminum molds are the part of the design most likely to work first time. `project.yaml` is unchanged at $600.
9. **First partner:** an existing filter factory in the Potters for Peace network, an NGO planning a new factory, or a university ceramics lab. Recommendation: an existing factory, since it can tell us the pressing force and acceptance band.

### Safety concerns

- Crushing at the molds, platen and carriage rails; guards, an interlocked gate and pump controls outside the guard are in the BOM but not yet designed.
- Load pins must be fully home before pressing; a sheared or walked-out pin can eject. A pin-presence interlock should be considered at TRL 3.
- Heavy molds (about 12 and 20 kg) and a tall 180 kg frame: tipping and dropped loads.
- Workshop hazards outside PotPress but near it: silica dust from clay and husk ash, silver nitrate, kiln heat.
- A passing flow test is not proof of pathogen removal; the documents say so and must keep saying so.

### Gaps and notes

- The pressing force needed for a good wall was not found in the sources reviewed; the 5 to 10 t working range is an assumption.
- The CMWG best practice PDF and the Penn State paper could not be opened from this session, so they are cited for scope only, not for specific numbers.

### Suggestions (not added to the repo)

- A parametric generator that outputs the pattern segments and the T-gauge scale from one filter definition would make the "printable mold geometry" in the pitch concrete at TRL 3.

### Recommended next step

Review this note and the media. If approved, run `/advance-trl3` to size the frame, pins and guides by calculation, settle the lift and jack choice, split and check the casting patterns, and produce the parametric model and drawing sheet.
