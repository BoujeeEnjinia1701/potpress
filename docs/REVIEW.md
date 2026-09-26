# Review note: PotPress

## Session 2026-09-25: recommendations accepted

Authority: Amish wrote on 2026-09-25, "i accept all your recommendations, go with them across all repos." Every item with a recommendation is now **Decided by Amish, 2026-09-25: go with recommendation** (recorded in `docs/decisions/0002-recommendations-accepted.md`, PPR-DDR-002 v0.1, and in PPR-DDR-001 v0.2). `project.yaml` keeps `trl: 3` and `trl_target: 3`.

### Decisions applied and what changed

| # | Decision | Before | After |
| --- | --- | --- | --- |
| 10 | R3 judged at the 10 t working force, molds closing on a metal stop | Under 1 mm at 294 kN: 1.84 mm, not met | Under 1 mm at 10 t: 0.61 mm, met on paper (stop face already modeled) |
| 11 | R11 rack 0.8 x 0.8 m, hinged front rail extension | Rack limit 0.8 x 0.5 m, not met; press 970 mm deep | Rack 780 x 780 mm fits; rails fixed to 320 mm with a 330 mm folding extension, press 840 x 655 mm; met on paper |
| 12 | Upright joints bolted, 4 x M20 8.8 each | Welded frame 147 kg in one piece; R8 at risk | 16 bolts modeled; 75 MPa shear, 123 MPa bearing at 294 kN; largest frame part 37.4 kg; R8 met on paper |
| 13 | One 60 mm pin with a pin-presence interlock | Interlock "switch or blocking plate" | Mechanical pin-presence interlock on the jack release (BOM item 16, R9 text) |
| 14 | Raise the budget | `budget_usd` $720 | `budget_usd` $930 |
| 15 | Lead-free scrap for the molds | Proposed | In R12 and the PPR-PRB-001 constraints |

Files changed: `project.yaml` (budget, evidence list); `README.md` (numbers, components, four new write-up sections); `docs/01-problem.md` v0.4; `docs/02-concept.md` v0.4; `docs/03-requirements.md` v0.4; `docs/04-calcs/01-sizing.md` v0.2 and `sizing.py` (bolt bearing, hinge moment, folded envelope, bolt and hinge costs); `docs/decisions/0001-trl2-review-decisions.md` v0.2; new `docs/decisions/0002-recommendations-accepted.md`; `cad/src/model.py` (joint bolts, hinged rail extension) with STEP and STL re-exported; `cad/src/sheets.py` and PPR-DWG-001 at Rev P2; `cad/src/concept_media.py` and all `media/` regenerated; `bom/bom.csv` (items 2, 7, 8, 9, 16) and `bom/bom-notes.md`; all PDFs in `docs/pdf/` re-rendered.

Cost: items 2 ($77 to $124, joint bolts) and 7 ($34 to $45, hinges and lugs) take the BOM from $926 to **$984**, $54 (6 %) over the new $930 budget.

### Requirements now (not met first)

| ID | Status |
| --- | --- |
| R10 | **Not met**: $984 against $930 |
| R2, R7, R9 | At risk (wall evenness depends on hand finishing; cavity finishing without a lathe unproven; guards and interlocks not modeled) |
| R1, R3, R4, R5, R6, R8, R11, R12 | Met on paper |

Summary: 1 not met, 3 at risk, 8 met on paper (was 3, 4 and 5).

### Still awaiting Amish

1. First co-design partner (item 9): no recommendation; stays "Proposed, awaiting Amish".
2. Decided by Amish, 2026-09-26: budget top-up to $990 (option a). Remaining cost gap (new item 16): $984 against $930. Options: (a) raise `budget_usd` to about $990 (recommended, since the added cost is the joints and hinges just decided); (b) cost the QC rack ($81) outside the press budget; (c) keep $930 and record R10 as not met.

### Cross-repo actions

None. No decision here needs a change in another repo.

### TRL 4

**TRL 4 remains on hold by Amish's instruction.** No build, proof load test, bolt torque check, measurement, trial or purchasing was started.

### Write-up and media

- README now has "Concept rationale", "Burning platform" (WHO and UNICEF JMP 2025, WHO drinking-water fact sheet, Brown et al. 2008, IntechOpen press costs), "Where it could be used" and "What sparked the idea" (Ron Rivera's tire-jack clay press and filter mold for Potters for Peace, Nicaragua).
- All generated files (docs PDFs, PPR-DWG-001, `media/`) were regenerated so they carry designmolecule.com.

### Safety concerns

- Unchanged from the TRL 3 session, plus: check the bolted upright joints for tightness before each shift; keep fingers clear of the rail extension hinges and deploy it only onto its stop lugs.

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

### Proposed, awaiting Amish (status updated in the session "recommendations accepted")

1. First co-design partner (item 9): left open under the portfolio rule; no choice made. Still proposed, awaiting Amish.
2. Decided by Amish, 2026-09-25: go with recommendation. R3: judge deflection at the 10 t working force with the molds closing on a metal stop (recommended), rather than at 294 kN.
3. Decided by Amish, 2026-09-25: go with recommendation. R11: allow 0.8 x 0.8 m for the 2 x 2 QC rack (recommended); also a hinged front rail extension for the press depth.
4. Decided by Amish, 2026-09-25: go with recommendation. Frame joints: bolt the four upright joints (4 x M20 8.8 each) so no part exceeds 40 kg (recommended).
5. Decided by Amish, 2026-09-25: go with recommendation. Load pin: one 60 mm 42CrMo4 pin with a pin-presence interlock (recommended, as modeled) or two pins at two stations.
6. Decided by Amish, 2026-09-25: go with recommendation. Cost gap of $206: raise `budget_usd` to about $930 (recommended), or cost the QC rack separately and build the concrete-backed molds first.
7. Decided by Amish, 2026-09-25: go with recommendation. Scrap aluminum must be lead-free (recommended) or new A356 ingot.

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

### Proposed, awaiting Amish (items 1 to 8 since decided; see PPR-DDR-001)

1. Decided by Amish, 2026-09-25: go with recommendation. **Architecture:** jack below lifting the female mold against a fixed male mold (recommended), versus an inverted-rated jack pushing down, or a screw press.
2. Decided by Amish, 2026-09-25: go with recommendation. **Male mold lift:** hand crank with load pins and a standard jack (recommended), versus a 20 t long-stroke cylinder with hand pump (about $150 to $250 more), versus a counterweighted lever.
3. Decided by Amish, 2026-09-25: go with recommendation. **Mold material:** cast aluminum from printed patterns (recommended), with printed shells backed by fiber-reinforced concrete built as a low-cost variant (about $115 cheaper, durability unknown).
4. Decided by Amish, 2026-09-25: go with recommendation. **Frame:** welded (recommended), with a bolted variant documented later.
5. Decided by Amish, 2026-09-25: go with recommendation. **Demolding:** slide-out carriage that tilts to turn the pot onto a board (recommended), versus air-assisted release or leaving the pot on the male mold.
6. Decided by Amish, 2026-09-25: go with recommendation. **QC:** manual rack and printed T-gauge (recommended); load-cell logger per station as a later option.
7. Decided by Amish, 2026-09-25: go with recommendation. **Default acceptance band:** 1.0 to 2.5 L/h in the first hour, corrected to 25 °C, adjustable per factory.
8. Decided by Amish, 2026-09-25: go with recommendation. **Budget:** (a) raise `budget_usd` from $600 to about $720; (b) keep $600 and adopt the concrete-backed molds for the first prototype (about $600); (c) keep $600 for the press only and cost the QC rack separately (the press alone is about $645, still over). Recommendation: (a), because the aluminum molds are the part of the design most likely to work first time. `project.yaml` is unchanged at $600.
9. Still proposed, awaiting Amish (no recommendation adopted under the portfolio rule). **First partner:** an existing filter factory in the Potters for Peace network, an NGO planning a new factory, or a university ceramics lab. Recommendation: an existing factory, since it can tell us the pressing force and acceptance band.

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

## Session 2026-09-26: sources strengthened

### Sources replaced

| Where | Old source | New source |
| --- | --- | --- |
| README, What sparked the idea | Wikipedia (Ron Rivera) with University of Pittsburgh history page; claims that Rivera designed the tire-jack press and mold and set up 30 microenterprises | Potters for Peace, Ceramic Water Filter Project page (first workshop after Hurricane Mitch in October 1998, over 5,000 filters in six months, hand-operated hydraulic truck jack and two-piece aluminum mold, over 50 factories in over 30 countries) with the University of Pittsburgh history page (Rivera coordinated PFP's Nicaragua work from 1989; PFP's filter involvement from 1998). The unverifiable Rivera-specific claims were removed. |
| README, Burning platform | Brown, Sobsey and Loomis (2008), LSHTM repository | Potters for Peace (over 50 factories in over 30 countries); the trial could not be re-fetched this session (repository blocked), so it was dropped from the README |
| README, Nicaragua row | Pitt history page and Rayner (2009), WEDC | Potters for Peace and Pitt history page; the flow band claim (Rayner) could not be re-fetched and was dropped from the row |
| README, Cambodia row | Brown, Sobsey and Loomis (2008) | Potters for Peace (training in Cambodia) |
| README, United States row | Henry, Maley and Mehta (2013), IJSLE | University of Pittsburgh ceramic filter project, Research and Activities page |
| README, Nigeria row and Burning platform | IntechOpen, unnamed | Same chapter, now credited as Erhuanga et al. (2020); cost figures re-checked and "before shipping and duties" removed as unsupported |

- `INSPIRATIONS.md`: potpress line updated to the Potters for Peace post-Mitch workshop and its truck-jack press and aluminum mold.
- `docs/01-problem.md` does not cite Wikipedia, so its sources were not changed. It still cites Brown (2008), Rayner (2009) and Henry et al. (2013), which could not be re-fetched this session because of network restrictions; they were not re-verified.

### Budget top-up

Budget top-up to $990: decided by Amish, 2026-09-26. `budget_usd` $930 to $990; R10 moves from not met to met on paper, $984 against $990 (a thin $6, 0.6 %, margin). Updated: `project.yaml`, PPR-REQ-001 v0.5, PPR-CAL-001 v0.3 and `sizing.py` (re-run; now prints the margin), PPR-DDR-002 v0.2 (item 16 decided), PPR-PRC-001 v0.5, PPR-PRB-001 v0.5, `README.md` (budget badge line and concept numbers). Requirement status: 0 not met, 3 at risk (R2, R7, R9), 9 met on paper.
