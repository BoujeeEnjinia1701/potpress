---
doc_id: PPR-DEC-001
title: PotPress design decisions register
project: PotPress
doc_type: Design decisions register
version: "0.2"
status: Draft
date: '2026-10-01'
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
---

# PotPress design decisions register

Every design decision still to be made, and every decision made, in one place. Each decision is argued in full in its decision record under `docs/decisions/`; this register is the index Amish works from. The build plan (`docs/05-build-plan.md`) describes the design as it stands and does not list open decisions.

## Open decisions

| # | Decision needed | Options | Recommendation | Affects in the build | Source |
| --- | --- | --- | --- | --- | --- |
| 1 | Pump slot width | 30 mm (as built in the model) or back to 25 mm | 30 mm, with the guard distance check completed | Guard panel and slot | PPR-DDR-004, Q2; PPR-DDR-003 |
| 2 | Pump handle outside the guard | Treat the 158 mm the handle stands out as operating space, or redesign | Treat it as operating space | Floor space beside the press | PPR-DDR-004, Q3 |
| 3 | Demolding by tipping the mold on its pins | Confirm with a partner factory's potters, or change the method | Confirm with potters | Carriage and rail extension | PPR-DDR-004, Q5 |
| 4 | Working pressing force | 5 to 10 t assumed; confirm with a partner factory | Confirm before any pressing test | Jack, frame and mold checks | PPR-DDR-001, item 9 |
| 5 | Guard opening check to ISO 13857 | Check the slot and mesh distances against the tables | Complete the check | Guard panels | PPR-DDR-003 |

## To confirm when parts are bought

| # | What to confirm | Why it matters | Source |
| --- | --- | --- | --- |
| 1 | Buy the bottle jack first | Its base, release screw and pump socket set the locating blocks, the interlock coupling and the notch angle | PPR-DDR-004, Q4 |
| 2 | Mold cavity finish that releases the liner cleanly | Sets the hand finishing of both molds | PPR-DDR-004 |

## Value engineering

Value-engineering target: USD 1,060 (a hypothetical control target, not a limit). Estimated cost of the constructable design: USD 1,143 (USD 83 over the target). Main cost drivers and savings worth trying:

- The press alone is USD 1,060 and the QC rack USD 83. Read against the press alone, the estimate matches the target.
- Making the design constructable added USD 92 (PPR-DDR-004): the steel base plate under the female mold, the thicker 450 mm mold flanges, dowels and bushes (items 8 and 9, USD 44), floor anchors, the bolted jack plate and heavier feet (item 1, USD 22), the adapter disc and nut box (item 10, USD 9) and interlock details (item 21, USD 7).
- The fixed guards, front gate and interlock added USD 67 earlier (PPR-DDR-003); they are a safety requirement, so savings are sought elsewhere.
- Savings worth trying: cheaper dowels and bushes, and plywood QC rack shelves cut from offcuts.

## Decisions made

| Date | Decision | Decided by | Record |
| --- | --- | --- | --- |
| 2026-09-25 | TRL 2 review items and recommendations | Amish: "i accept all your recommendations, go with them across all repos." | PPR-DDR-001, PPR-DDR-002 |
| 2026-09-27 | Guarded version with mesh guards and an interlocked front gate; budget USD 1,060 | Amish | PPR-DDR-003 |
| 2026-09-30 | Design for construction: open-topped male mold, dowel location, M16 joints with spacer tubes, captive lead screw nut, interlock design and other changes that make the press buildable | Amish: "i accept your recommended changes on design that are currently being sent across for my approval" | PPR-DDR-004 |
