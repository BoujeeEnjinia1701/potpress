# Review note: PotPress

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
