---
doc_id: PPR-DEC-001
title: PotPress design decisions register
project: PotPress
doc_type: Design decisions register
version: "0.1"
status: Draft
date: '2026-09-30'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-09-30'
  author: Amish Chadha
  change: Register opened; open decisions moved out of the build plan
---

# PotPress design decisions register

Every design decision still to be made, and every decision made, in one place. Each decision is argued in full in its decision record under `docs/decisions/`; this register is the index Amish works from. The build plan (`docs/05-build-plan.md`) describes the design as it stands and does not list open decisions.

## Open decisions

| # | Decision needed | Options | Recommendation | Affects in the build | Source |
| --- | --- | --- | --- | --- | --- |
| 1 | Budget | Raise to about USD 1,150; find savings; judge the budget on the press alone | Raise to about USD 1,150 | Parts cost USD 1,143 against USD 1,060 | PPR-DDR-004, Q1 |
| 2 | Pump slot width | 30 mm (as built in the model) or back to 25 mm | 30 mm, with the guard distance check completed | Guard panel and slot | PPR-DDR-004, Q2; PPR-DDR-003 |
| 3 | Pump handle outside the guard | Treat the 158 mm the handle stands out as operating space, or redesign | Treat it as operating space | Floor space beside the press | PPR-DDR-004, Q3 |
| 4 | Demolding by tipping the mold on its pins | Confirm with a partner factory's potters, or change the method | Confirm with potters | Carriage and rail extension | PPR-DDR-004, Q5 |
| 5 | Working pressing force | 5 to 10 t assumed; confirm with a partner factory | Confirm before any pressing test | Jack, frame and mold checks | PPR-DDR-001, item 9 |
| 6 | Guard opening check to ISO 13857 | Check the slot and mesh distances against the tables | Complete the check | Guard panels | PPR-DDR-003 |

## To confirm when parts are bought

| # | What to confirm | Why it matters | Source |
| --- | --- | --- | --- |
| 1 | Buy the bottle jack first | Its base, release screw and pump socket set the locating blocks, the interlock coupling and the notch angle | PPR-DDR-004, Q4 |
| 2 | Mold cavity finish that releases the liner cleanly | Sets the hand finishing of both molds | PPR-DDR-004 |

## Decisions made

| Date | Decision | Decided by | Record |
| --- | --- | --- | --- |
| 2026-09-25 | TRL 2 review items and recommendations | Amish: "i accept all your recommendations, go with them across all repos." | PPR-DDR-001, PPR-DDR-002 |
| 2026-09-27 | Guarded version with mesh guards and an interlocked front gate; budget USD 1,060 | Amish | PPR-DDR-003 |
| 2026-09-30 | Design for construction: open-topped male mold, dowel location, M16 joints with spacer tubes, captive lead screw nut, interlock design and other changes that make the press buildable | Amish: "i accept your recommended changes on design that are currently being sent across for my approval" | PPR-DDR-004 |
