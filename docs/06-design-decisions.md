---
doc_id: PPR-DEC-001
title: PotPress design decisions register
project: PotPress
doc_type: Design decisions register
version: "0.4"
status: Draft
date: '2026-10-02'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-09-30'
  author: Amish Chadha
  change: Register opened; open decisions moved out of the build plan
- version: "0.2"
  date: '2026-10-01'
  author: Amish Chadha
  change: Budget treated as a value-engineering target
- version: "0.3"
  date: '2026-10-02'
  author: Amish Chadha
  change: 'Amish approved the recommendations for all five open decisions (2026-10-02); moved to decisions made'
- version: "0.4"
  date: '2026-10-02'
  author: Amish Chadha
  change: 'Approved follow-ups carried out: four guard changes found by the ISO 13857 desk check added as open decisions; handle stroke added to the items to confirm; value engineering at USD 1,149'
---

# PotPress design decisions register

Every design decision still to be made, and every decision made, in one place. Each decision is argued in full in its decision record under `docs/decisions/`; this register is the index Amish works from. The build plan (`docs/05-build-plan.md`) describes the design as it stands and does not list open decisions.

## Open decisions

The five decisions of 2026-10-02 are in the table of decisions made. The ISO 13857 desk check that Amish decided should be done now (PPR-CAL-001, section 15, 2026-10-02) found openings that fall short of the standard; the changes that close them are proposed, awaiting Amish.

| # | What is to be decided | Options | Recommendation | What it affects in the build | Source |
| --- | --- | --- | --- | --- | --- |
| 1 | Front and roof mesh: the 12.7 mm mesh on the front strips, lower front panel, front gate and roof is 39 to 77 mm from moving parts, against 80 mm needed | (a) 6.35 mm (1/4 in) welded mesh, 0.9 mm wire, on those panels (needs 5 mm); (b) move the front panels out by 41 mm (breaks the 0.7 m depth of R11) | (a); about USD 8 more mesh (estimate) | Guard panels, gate, BOM items 16 and 20 | PPR-CAL-001, section 15 |
| 2 | Release shaft and pin cable openings in the front right strip (44 and 40 mm) are too large for their distance from the rail extension and carriage | (a) a bolted plate with a 20 mm hole round the 12 mm shaft and a grommet plate with a 10 mm hole for the cable, gaps of 4 mm or less; (b) move the openings | (a); about USD 2 (estimate) | Front right strip, BOM item 16 | PPR-CAL-001, section 15 |
| 3 | Top beam gap: open from above between the stem guides, the uprights and the end blocks (104 x 150 and 104 x 60 mm), reaching the stem and the male flange | (a) 3 mm steel cover plates bolted to the top flanges over the four openings; (b) extend the roof mesh down into the gap | (a); about USD 3 (estimate) | Top crossbeam, BOM item 3 or 16 | PPR-CAL-001, section 15 |
| 4 | Crank bracket open at the front and back: the stem's cap plate rises to 10 mm under the bracket's top plate | (a) mesh or sheet covers on the bracket's front and back; (b) accept it as worked only by the operator at the handwheel | (a); about USD 2 (estimate) | Crank bracket, BOM item 10 | PPR-CAL-001, section 15 |

## To confirm when parts are bought

| # | What to confirm | Why it matters | Source |
| --- | --- | --- | --- |
| 1 | Buy the bottle jack first | Its base, release screw and pump socket set the locating blocks, the interlock coupling and the notch angle | PPR-DDR-004, Q4 |
| 2 | Mold cavity finish that releases the liner cleanly | Sets the hand finishing of both molds | PPR-DDR-004 |
| 3 | The pump handle's stroke on the jack bought, and its play in the socket | The slot and shield leave 25 mm beyond each end of the modelled stroke and 5 mm each side; a longer stroke or more play shortens those gaps | PPR-CAL-001, section 15 |

## Value engineering

Value-engineering target: USD 1,060 (a hypothetical control target, not a limit). Estimated cost of the constructable design: USD 1,149 (USD 89 over the target). Main cost drivers and savings worth trying:

- The press alone is USD 1,066 and the QC rack USD 83. The USD 1,060 target was set on 2026-09-27 to cover the whole BOM, QC rack included, so the like-for-like gap is USD 89.
- The fixed inner shield behind the pump slot (decided 2026-10-02) added USD 6. The guard changes proposed above would add about USD 15 (estimate); they are a safety requirement, so savings are sought elsewhere.
- Making the design constructable added USD 92 (PPR-DDR-004): the steel base plate under the female mold, the thicker 450 mm mold flanges, dowels and bushes (items 8 and 9, USD 44), floor anchors, the bolted jack plate and heavier feet (item 1, USD 22), the adapter disc and nut box (item 10, USD 9) and interlock details (item 21, USD 7).
- The fixed guards, front gate and interlock added USD 67 earlier (PPR-DDR-003); they are a safety requirement, so savings are sought elsewhere.
- Savings worth trying: cheaper dowels and bushes, and plywood QC rack shelves cut from offcuts.

## Decisions made

| Date | Decision | Decided by | Record |
| --- | --- | --- | --- |
| 2026-09-25 | TRL 2 review items and recommendations | Amish: "i accept all your recommendations, go with them across all repos." | PPR-DDR-001, PPR-DDR-002 |
| 2026-09-27 | Guarded version with mesh guards and an interlocked front gate; budget USD 1,060 | Amish | PPR-DDR-003 |
| 2026-09-30 | Design for construction: open-topped male mold, dowel location, M16 joints with spacer tubes, captive lead screw nut, interlock design and other changes that make the press buildable | Amish: "i accept your recommended changes on design that are currently being sent across for my approval" | PPR-DDR-004 |
| 2026-10-02 | Pump slot: keep the 30 mm slot, approved only with a fixed inner shield or tunnel behind the slot that keeps the platen and molds out of arm's reach, sized in the ISO 13857 check (item 5) | Amish: "i approve your recommendations for all 555 open decisions." | PPR-DDR-004, Q2; PPR-DDR-003 |
| 2026-10-02 | Pump handle: the 158 mm the handle stands outside the guard is operating space, like a door swing, marked on the floor layout; the 1.0 m width limit of R11 applies to the guarded box | Amish: "i approve your recommendations for all 555 open decisions." | PPR-DDR-004, Q3 |
| 2026-10-02 | Demolding: keep the tipping pins for the prototype; the potters at the first partner factory confirm the method, and if they object the pot is lifted out in its liner instead | Amish: "i approve your recommendations for all 555 open decisions." | PPR-DDR-004, Q5 |
| 2026-10-02 | Pressing force: every structural check stays at the full 20 t jack; the working force is a process setting found in pressing trials with a partner factory, starting near 2 t and stepping up | Amish: "i approve your recommendations for all 555 open decisions." | PPR-DDR-001, item 9 (as cited in the register); PPR-CAL-001, section 3 |
| 2026-10-02 | Guard openings: the ISO 13857 desk check is done now rather than at TRL 4, signed by a competent person, and is a hold point before any force above hand pressure | Amish: "i approve your recommendations for all 555 open decisions." | PPR-DDR-003; PPR-DDR-004, Q2 |
