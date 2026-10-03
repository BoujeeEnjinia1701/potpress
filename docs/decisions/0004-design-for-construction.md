---
doc_id: PPR-DDR-004
title: PotPress design for construction
project: PotPress
doc_type: Design decision record
version: "0.5"
status: Draft
date: '2026-10-02'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-09-30'
  author: Amish Chadha
  change: Changes that make the concept physically buildable, with the reason for each, made under Amish's 2026-09-30 instruction
- version: "0.2"
  date: '2026-09-30'
  author: Amish Chadha
  change: Accepted by Amish; items that would change what the press does, its pitch, its safety case or its budget stay proposed (Table 3)
- version: "0.3"
  date: '2026-10-01'
  author: Amish Chadha
  change: Budget treated as a value-engineering target
- version: "0.4"
  date: '2026-10-02'
  author: Amish Chadha
  change: 'Q2, Q3 and Q5 decided by Amish on 2026-10-02 as recommended (Q2 amended: 30 mm slot only with a fixed inner shield, ISO 13857 check now); record stays Draft'
- version: "0.5"
  date: '2026-10-02'
  author: Amish Chadha
  change: 'Decisions carried into the design: pump slot shield modelled, slot lengthened to 272 mm, handle operating space on the GA floor layout; record stays Draft'
---

# 0004: Design for construction

- **Date:** 2026-09-30
- **Status:** accepted. Amish, 2026-09-30: "i accept your recommended changes on design that are currently being sent across for my approval". This covers every change in Tables 1 and 2. The questions in Table 3 would change the pitch or the safety case, or note value engineering, so they stay **proposed, awaiting Amish**. On 2026-10-02 Amish approved the recommendations for Q2, Q3 and Q5 ("i approve your recommendations for all 555 open decisions."); they are decided as recorded in Table 3 and in the design decisions register (PPR-DEC-001). Q1 is a value-engineering note, not a decision, and Q4 (the interlock notch) is set to the jack bought, under "To confirm when parts are bought" in the register.

## Context

On 2026-09-30 Amish rejected a text-only build plan and asked for one that shows, stage by stage and in pictures, how each component is made and how it fits the next, adding: "If you are realising that the design cannot be built as per concept - fix the design assumptions to match and be physically feasible as you draw the illustrations." An earlier planning pass that day found ten problems (P1 to P10) in the TRL 3 concept model of PPR-DDR-003. Checking the model with build123d in its closed, open and demolding positions found seven more (P11 to P17).

The changes keep what the press does: the same filter shape, 20 t jack, 600 mm frame, pressing travel, crank lift, guards, gate and QC rack, and the same pitch. The safety case is unchanged except where Table 3 says so. Every change is in `cad/src/model.py`, which now runs its constructability checks with `python cad/src/model.py --check`: no two of the 51 components overlap with the press closed, open or set for demolding; the 47 joints that must touch do touch; the pump handle clears the guard over its whole stroke; the carriage hooks meet the tipping pins; and the lock rod drops into the lock disc's notch. All pass.

## Decision

*Table 1. Changes made to the model, the BOM and the calculations.*

| # | Problem in the concept | Change made | Why this way |
| --- | --- | --- | --- |
| P1 | The male mold was a closed hollow: a sand core inside it could not be supported or removed. | The plug is open at the top. Its inside is a cone, 206 mm across at the floor and 259 mm at the flange, with the wall's own 6° draft. The pattern is flat-backed, flange face down, so the sand forms the inside as a green-sand core; no core box. | The simplest casting a jobbing foundry makes. The 15 mm shell and 30 mm tip are unchanged. |
| P2 | The 25 mm male flange, loaded on the stop ring and backed only by a 180 mm adapter, would reach about 487 MPa at 294 kN (as-cast yield about 90 MPa). | The flange is 45 mm thick and 450 mm across. The stem's 190 mm disc bears on the plug floor inside, bedded on steel epoxy putty and held by four M12 bolts, so the flange is a ring cantilevered from the plug wall: 62 MPa at 294 kN with all the force on the stop. | Thickening the flange is simpler than ribs and keeps the pattern flat-backed. The male mold is 23 kg, inside R8. |
| P3 | The molds located on a 390 mm lip fitted to 0.1 mm, which needs a 420 mm lathe; the patterns had no machining allowance, draft or core prints. | Two 16 mm hardened dowels pressed into the female flange at 202 mm each side, and two steel bushes in the male flange, drilled with the molds clamped together on printed 15 mm wall spacers. The stop faces are lapped flat on abrasive paper on float glass. Patterns carry 1.3 % shrink, 3 mm lapping allowance on the stop faces and the female base, and 2° draft on the flange rims. The female mold is a cast cup bedded and screwed on a 350 x 350 x 15 mm steel base plate. | Every operation fits a pillar drill and a bench. The dowels hold the wall even to about ±0.44 mm, as the lip did. The steel plate takes the rail contact and the retaining pins. |
| P4 | The jack's pump socket overlapped the right return spring, and the handle's path to the guard slot ran through the right upright. | The jack is turned 25° so its pump socket and release valve face the right front. The pump slot in the right side guard moves to 218 mm in front of the axis, on the handle's line, and widens from 25 to 30 mm so the 20 mm handle passes the 6 mm guard at 25° with about 2 mm clear. | The handle now misses the spring by 57 mm and the upright by 49 mm over its whole stroke. The 30 mm slot stays in the same ISO 13857 slot band (over 20 up to 30 mm); see Table 3, Q2. |
| P5 | The lead screw would have carried press force through the pin's 2 mm play. | The Tr24 nut is captive in a box at the top of the stem with 8 mm of free travel below it. Cranking up, the nut lifts the cap plate; pressing, the stem rides up about 2 mm onto the pin and the nut stays free. | No extra parts or bearings; the press force goes through the pin, never the screw. |
| P6 | The 100 mm uprights filled the 100 mm beam gap with no clearance. | The beam gap is 104 mm, with a 2 mm shim pack each side of each joint. | Rolled channel varies by a millimetre or two; shims take it up. |
| P7 | M20 bolts were too big for the 50 mm UPN 100 flange and clamped across an 83 mm hollow. | Four M16 grade 10.9 bolts per joint, 28 mm from the web (22 mm edge distance against 21.6 mm needed), with a 25 x 3 mm spacer tube inside the channel between the flanges. Double shear 117 MPa at 294 kN. | M16 is the largest bolt the flange takes; 10.9 gives the strength back. The tube stops the flanges folding when the bolts are tightened. |
| P8 | The carriage had tilt bosses but nothing to pivot on and nothing holding the mold in. | Two 12 mm bright steel tipping pins on the ends of the rail extension; two hooks on the carriage with slots open to the front that slide onto them; two 10 mm retaining pins through the carriage into the base plate; two lift handles near the back of the carriage. | The mold tips forward about the pins; about 283 N on the two handles starts the tip. The hooks cannot slide off under the mold's own weight. |
| P9 | The interlock was outline shapes only. | A concrete mechanism round a standard bottle jack release screw: a coupling on the screw, a 12 mm shaft with two universal joints out to a front knob, an 80 mm lock disc with one notch, a 12 mm lock rod on a guide post, a gate slider pushed back by the gate's tongue, and a pin slider pulled aside by a push-pull cable from a plunger on the load pin's head. With the valve open the rod drops into the notch; the valve can be closed only by lifting the rod, which needs the gate shut and the pin home; with the valve closed the rod stands through the gate tongue. | Purely mechanical, no electrics, as PPR-DDR-003 decided. The notch angle must be set to the jack bought (Table 3, Q4). |
| P10 | The feet had no flat face to bolt through; floor anchors, spring anchors, spacer tubes and shims were missing from the BOM; the QC buckets overlapped the hanging pots. | Feet turned web up with welded anchor tubes and four welded M12 studs each; four M12 floor anchors; spring lugs on the base beam and under the platen; tubes and shims modelled and in the BOM. The QC pot shelf is raised to 720 mm, leaving 35 mm between the pots and 325 mm buckets on the 120 mm shelf. | All in the model and `bom/bom.csv`. |
| P11 | Found in checking: the folded rail extension would hit the gate's bottom rail and the lower front panel's frame when the platen goes down. | The rail hinge line moves back from 320 to 290 mm in front of the axis; the extension is 335 mm long so the tipping pins stay where they were. | The folded extension now clears both with the platen down. The stop lug load rises to about 2.9 kN (10.8 kN with the mold tipped over). |
| P12 | Found in checking: when the crank lifts the stem, the pin block inside it would hit the fixed lower end of the lead screw after about 56 mm. | A 28 mm hole down the middle of the pin block and the nut box floor. | The screw passes freely over the full 200 mm lift. Pin bearing on the block rises from 54 to 79 MPa at 294 kN. |
| P13 | Found in checking: the stem had 7 mm of play front to back in the beam gap, more than the dowels' 3 mm lead-in. | Two 6 mm plastic strips on the inside faces of the top beam webs, with 62 mm holes for the pin, give 1 mm each side. | The dowels now always find their bushes. |
| P14 | Found in checking: the jack's pump handle was not part of the design. | A 20 mm handle, at least 700 mm long, bought with the jack or extended with tube, modelled over its stroke. | It stands 158 mm outside the right guard while in use (Table 3, Q3). |
| P15 | Found in checking: the stem could not be fitted with the molds in place, and the female mold could not slide in under a stem pinned at pressing height. | Assembly order set by the model: stand the stem on the rails before the top beam goes on; pin it; crank it up; put both molds together on the carriage out on the swung-out extension; slide them in; crank down; pin; jack up and bolt the male mold to the stem. | Shown step by step in PPR-BLD-001. |
| P16 | Found in checking: the female mold's plate would have borne on plastic slide strips under the full press force. | The base plate slides on the greased steel rails; the rails with the platen deck are checked across the platen's centre gap (101 MPa at 294 kN). | Plastic would creep under 294 kN. |
| P17 | Found in checking: the only carriage handle was in front of the tipping pins, so it could not tip the mold. | The two lift handles of P8. | |

*Table 2. Knock-on changes.*

| Item | Change | Reason |
| --- | --- | --- |
| Masses | Press 298 to 344 kg; heaviest part the platen at 39.6 kg (R8, 40 kg); female mold with its base plate 36.5 kg; male mold 23.0 kg. | Added parts, thicker flanges, steel base plate. |
| Calculations | PPR-CAL-001 v0.6: new checks for the male flange, the M16 joints, the lead screw float, the rails, the tipped mold, the stop lugs and the tipping pins; deflection 0.66 mm at 10 t. R3 stays met on paper. | Follows the model. |
| Requirements | PPR-REQ-001 v0.8: R10 now over the value-engineering target by $83; figures for R2, R3, R7, R8, R9 and R11 updated. No requirement text changed. | Follows the calculations. |
| BOM | Lines 1, 2, 3, 4, 7, 8, 9, 10, 12, 15, 16, 18, 20 and 21 rewritten to the buildable parts; total $1,051 to $1,143. | Parts added for construction. |
| Drawing | PPR-DWG-001 Rev P5; making sketches PPR-DWG-101 to 114 added. | Follows the model. |
| Media | Concept images, blueprint and 3D viewer regenerated. The photoreal renders (`media/render-*.png`) and `cad/src/product_model.py` still show the concept and need updating in Blender on Amish's Mac. | |

*Table 3. Questions that would change the pitch or the safety case; Q2, Q3 and Q5 decided by Amish on 2026-10-02.*

| # | Question | Options | Recommendation |
| --- | --- | --- | --- |
| Q1 | Value engineering (a note, not a decision). The constructable BOM is $1,143, $83 (7.8 %) over the $1,060 value-engineering target (`budget_usd`, a hypothetical control target). | (a) look for savings (for example cheaper dowels and bushes, plywood QC shelves from offcuts); (b) read the target against the press alone ($1,060). | (a); the added parts are what a build needs, so savings come from how they are bought. |
| Q2 | The pump slot widens from 25 to 30 mm. Both are in the same ISO 13857 band, but the guard distance check itself is still open (PPR-DDR-003). | (a) accept 30 mm with a brush strip and do the ISO 13857 check at TRL 4; (b) keep 25 mm and fit a thinner (16 mm) handle. | (a), as amended. **Decided by Amish, 2026-10-02:** keep the 30 mm slot, approved only with a fixed inner shield or tunnel behind the slot that keeps the platen and molds out of arm's reach, sized in the ISO 13857 desk check, which is done now rather than at TRL 4 (PPR-DDR-003). A brush strip does not count as a guard. |
| Q3 | The pump handle stands 158 mm outside the right guard while in use, beyond the 1.0 m width of R11. | (a) treat the handle as operating space, like a door swing, and keep R11 on the guarded box; (b) use a two-piece handle removed between cycles. | (a). **Decided by Amish, 2026-10-02:** the handle's 158 mm is operating space, marked on the floor layout; R11 applies to the guarded box. |
| Q4 | The interlock notch is 120° (a third of a turn) round from the rod. Bottle jacks open their release between about a quarter and a half turn. | (a) set the notch to the jack bought, at TRL 4; (b) fix it at 120° and buy a jack to suit. | (a). |
| Q5 | The mold is tipped over by hand on pins at the end of the extension to demold (about 51 kg in all). The method was always to be confirmed with potters (PPR-PRC-001). | (a) keep the tipping pins; (b) lift the pot out in its liner instead. | (a) for the prototype; confirm with a partner factory. **Decided by Amish, 2026-10-02:** keep the tipping pins; the potters at the first partner factory confirm the method, and if they object the pot is lifted out in its liner. |

## Carried into the design, 2026-10-02

- **Q2.** The fixed inner shield is in the model (`pump_shield`, BOM item 16): a tunnel of 2 mm folded sheet, 30 mm wide inside, along the handle's line from the slot to 3 mm off the jack body, with a flange bolted through the slot frame and a flat-bar stay to the base beam. The slot is lengthened from 220 to 272 mm (174 to 446 mm up) so that the handle stops 25 mm short of its ends and of the tunnel's roof and floor at both ends of its stroke. The constructability checks pass with the shield in all positions. Sized in the ISO 13857 desk check, PPR-CAL-001 section 15, which also found other openings short of the standard (now open decisions in PPR-DEC-001).
- **Q3.** The handle's operating space outside the right guard (158 mm) is outlined on the floor in the general arrangement PPR-DWG-001, Rev P6.
- **Q5.** No change to the design; confirmed with the partner factory's potters when one is chosen.

## Consequences

- `design_state: constructable` in `project.yaml`. The build plan PPR-BLD-001 (`docs/05-build-plan.md`) shows every component and step in pictures drawn from the model by `cad/src/build_plan_media.py`.
- Requirement status: 1 over the value-engineering target (R10), 2 at risk (R2, R7), 9 met on paper (PPR-CAL-001 v0.6).
- The photoreal renders and the appearance model are stale until they are rebuilt in Blender.
- TRL 4 remains on hold by Amish's instruction.
