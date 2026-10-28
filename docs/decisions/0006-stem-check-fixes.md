---
doc_id: PPR-DDR-006
title: PotPress STEM check fixes
project: PotPress
doc_type: Design decision record
version: '0.1'
status: Draft
date: '2026-10-23'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: '0.1'
  date: '2026-10-23'
  author: Amish Chadha
  change: Four STEM check fixes made under Amish's standing instruction of 2026-10-23, corrected after an independent review
---

# 0006: STEM check fixes

- **Date:** 2026-10-23
- **Status:** accepted under Amish's standing instruction (Amish can reverse any item)

## Context

The first STEM check (PPR-STM-001 v0.1) found four details that failed with a fix that keeps the working principle. Amish, 2026-10-23: "i approve the pilot, and whenever a STEM check fails propose and implement the best fix to the design and constructability." This record gives the options weighed for each, the fix made, and what an independent reviewer found when it tried to refute the fixes. The rerun check passes (PPR-STM-001 v0.2).

## Options considered and fixes made

### D2: clay shrinkage (STEM M6)

1. **Scale the molds.** Treat the 280 mm reference as the fired size and make the cavities larger by 1/(1 - s). Keeps the filter users get; the molds, patterns and frame grow.
2. **Call 280 mm the green size.** Nothing changes in the press, but the fired filter shrinks to about 258 mm and 9.6 L, which changes what the user gets (scope), so this option would go to Amish.

**Made: option 1**, with s = 8 % assumed (`CLAY_SHRINK` in `cad/src/model.py`) until a test bar of the partner's production mix is fired in its kiln (ASTM C326 method). Consequences, all in the model and checked by `model.py --check`:
- Molds 1.087 times the fired size: cavity rim 304 mm, depth 261 mm, wall 16.3 mm, rim 375 mm.
- Flanges 450 to 480 mm, flash groove radius 180 to 195 mm, dowels at 216 mm; 13.4 mm from the flanges to the uprights.
- Top crossbeam and everything above 22 mm higher (press 1,828 mm tall).
- Opening clearance 70 to 49 mm (30 mm needed); charge 9.6 kg; press 352 kg.
- The QC rack holds fired pots and is unchanged.
- Cost +$44 (molds, patterns, uprights, stem).

### D3: heavy lifts (STEM B2)

1. **Lifting aid** for every part over 25 kg.
2. **Split the platen, molds and beams** below 25 kg, which adds joints to the load path and the mold faces.

**Made: option 1.** A 0.5 t chain block with a two-leg sling and shackles, a round sling, and two M12 DIN 580 eye bolts (BOM item 22, $66, or hire). The female mold lifts by two holes tapped through its steel base plate on a diagonal; the male mold by two tapped holes in its flange top at 214 mm. Eye bolts come out and the holes are plugged before pressing. The 40 kg limit in PR-008 stays as a transport limit.

### D4: pump handle force (STEM S8)

1. **Slip-on handle extension**, first chosen and then refuted by the independent review (below).
2. **Working force limit** at the handle's 150 N screening limit.
3. **Separate two-speed hand pump** at waist height on a hose, which removes the pump slot from the guard but reverses the slot and shield Amish approved on 2026-10-02.

**Made: option 2.** The working force is limited to 6.4 t (PR-004), above the 2 t where trials start. Option 3 goes to Amish as D6 for the case where trials need more than 6.4 t.

### D5: scrap alloy (STEM C3)

1. **Melt check only.**
2. **Sorted A356 wheel scrap plus a melt check.**
3. **Bought ingot** of a certified alloy.

**Made: option 2.** Lead balance weights, brass valve stems, steel inserts and paint are removed before melting. A chill sample of each melt is checked by spark OES, or by handheld XRF for lead where OES is not available, against the EN 601 food-contact limits for lead and cadmium, and recorded per heat (PR-012). The limit values and the foundry's charge are to confirm. Cast aluminium is now taken at 80 MPa yield as cast (was 90); the male flange works at 60 MPa at 1.5 times the jack rating.

## Independent review

A second agent, given the model, calculations, STEM script and BOM but not the reasoning, tried to refute each fix.

| Fix | Verdict | What it found | Change made |
| --- | --- | --- | --- |
| D2 shrinkage | Holds | Uniform scaling right to first order; travel and opening still work. The larger pot needs about 11.8 t for the mean pressure the earlier design gave at 10 t; charge just above the factory range; BOM text stale | Pressure and charge recorded in PPR-CAL-001; BOM text corrected |
| D3 lifting | Weak | Female eye holes in the lapped stop face; an eye bolt left in would be crushed under the male flange; collar overhung the flange; no proper two-leg rig | Female lift points moved to the steel base plate; male holes to 214 mm; two-leg sling with shackles; holes plugged before pressing |
| D4 handle | Refuted | A slip-on sleeve must overlap the handle (163 N, over the limit); the extended tip comes within about 60 mm of the floor and crosses the QC rack; jack makers prohibit extensions | Extension dropped; working force limited to 6.4 t; remote pump proposed as D6 |
| D5 alloy | Weak | Melt testing alone catches contamination too late; XRF misses magnesium; LM6 has little strength margin | Scrap sorting added; OES preferred; A356 only; yield 80 MPa |

## Consequences

- PR-001 and PR-012 at risk to met on paper. PR-004, PR-008 and PR-012 requirement text extended (PPR-PRS-001 v0.14).
- BOM $1,169 to $1,279, $219 (20.7 %) over the $1,060 value-engineering target. The lifting set ($66) can be hired.
- Drawings PPR-DWG-001 (Rev P8), 010 (P4), 103, 107, 108, 109, 111, 112 (P2 or P3) and 110 (P4), build plan pictures, STEP files and concept media regenerated.
- The photoreal renders and storefront cards still show the frame 22 mm lower; they are rendered on Amish's Mac and are queued for the next render batch.
