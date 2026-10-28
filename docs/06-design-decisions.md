---
doc_id: PPR-DEC-001
title: PotPress design decisions register
project: PotPress
doc_type: Design decisions register
version: '0.9'
status: Draft
date: '2026-10-25'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: '0.1'
  date: '2026-09-30'
  author: Amish Chadha
  change: Register opened; open decisions moved out of the build plan
- version: '0.2'
  date: '2026-10-01'
  author: Amish Chadha
  change: Budget treated as a value-engineering target
- version: '0.3'
  date: '2026-10-02'
  author: Amish Chadha
  change: Amish approved the recommendations for all five open decisions (2026-10-02); moved to decisions made
- version: '0.4'
  date: '2026-10-02'
  author: Amish Chadha
  change: 'Approved follow-ups carried out: four guard changes found by the ISO 13857 desk check added as open decisions; handle stroke added to the items to confirm; value engineering at USD 1,149'
- version: '0.5'
  date: '2026-10-03'
  author: Amish Chadha
  change: Amish decided the four guard fixes (2026-10-03); moved to decisions made; value engineering at USD 1,169
- version: '0.6'
  date: '2026-10-23'
  author: Amish Chadha
  change: 'Kit 1.8 upgrade: concept selection (D1) and the four STEM check fixes (D2 to D5) added as open decisions, proposed, awaiting Amish'
- version: '0.7'
  date: '2026-10-23'
  author: Amish Chadha
  change: D2 to D5 made under Amish's standing instruction of 2026-10-23 (PPR-DDR-006) and moved to decisions made; D6 (remote two-speed pump) proposed; D1 still open; value engineering at USD 1,279
- version: '0.8'
  date: '2026-10-24'
  author: Amish Chadha
  change: 'Kit 1.9.1 upgrade: D7 (guard panel corners, a dimension corrected in the model after the D3 interference check), D8 (PR-013, local spares) and D9 (working force and handle effort, from the independent review) added, proposed, awaiting Amish; joint bolt preload made under the standing instruction; value engineering figures carried forward'
- version: '0.9'
  date: '2026-10-25'
  author: Amish Chadha
  change: 'Amish decided D1 (option A), D7, D8 and D9 as recommended on 2026-10-25 ("i concur with your recommendations"); moved to decisions made; D6 stays open (no pick: decide after trials)'
---

# PotPress design decisions register

Every design decision still to be made, and every decision made, in one place. Each decision is argued in full in its decision record under `docs/decisions/`; this register is the index Amish works from. The build plan (`docs/05-build-plan.md`) describes the design as it stands and does not list open decisions.

## Open decisions

| # | Decision | Options | Recommendation | Cost and effect | Source |
| --- | --- | --- | --- | --- | --- |
| D6 | If pressing trials need more than the working force limit (5.4 t since D9 was decided on 2026-10-25; 6.4 t when D6 was proposed) | (a) A separate two-speed hand pump at waist height on a hose to a single-acting ram, which removes the pump slot from the right guard; (b) a jack with a larger ram for less handle force per tonne; (c) keep 6.4 t and adjust the mix or dwell instead | Decide after trials; (a) if more force is needed | (a) replaces the slot and shield Amish approved on 2026-10-02 and changes the interlock; price to assess | PPR-DDR-006 (D4); PPR-STM-001 S8 |

D6 is still **Proposed, awaiting Amish**: its recommendation is to decide after pressing trials, so it carried no pick. D1, D7, D8 and D9 were decided by Amish on 2026-10-25 as recommended and are in the table of decisions made. D2 to D5, the four STEM check fixes, were made on 2026-10-23 under Amish's standing instruction and are in the table of decisions made.

## To confirm when parts are bought

| # | What to confirm | Why it matters | Source |
| --- | --- | --- | --- |
| 1 | Buy the bottle jack first | Its base, release screw and pump socket set the locating blocks, the interlock coupling and the notch angle | PPR-DDR-004, Q4 |
| 2 | Mold cavity finish that releases the liner cleanly | Sets the hand finishing of both molds | PPR-DDR-004 |
| 3 | The pump handle's stroke on the jack bought, and its play in the socket | The slot and shield leave 25 mm beyond each end of the modelled stroke and 5 mm each side; a longer stroke or more play shortens those gaps | PPR-CAL-001, section 15 |

## Value engineering

Value-engineering target: USD 1,060 (a hypothetical control target, not a limit). Estimated cost of the constructable design: USD 1,279 (USD 219 over the target). Main cost drivers and savings worth trying:

- The STEM check fixes (PPR-DDR-006, 2026-10-23) added USD 110: larger molds and patterns for the clay shrinkage allowance (items 8, 9 and 15, USD 42), the taller uprights and stem (USD 2) and the lifting set (item 22, USD 66). Hiring the chain block instead of buying it saves most of the USD 66.

- The press alone is USD 1,196 and the QC rack USD 83. The USD 1,060 target was set on 2026-09-27 to cover the whole BOM, QC rack included, so the like-for-like gap is USD 219.
- The fixed inner shield behind the pump slot (decided 2026-10-02) added USD 6. The four guard fixes (decided 2026-10-03, cost accepted by Amish) added USD 20 against the USD 15 estimated: finer mesh USD 8 (items 16 and 20), small-hole plates USD 2, top beam cover plates USD 7 (longer than estimated, to close the upright channel tops too), crank bracket covers USD 4. They are a safety requirement, so savings are sought elsewhere.
- Making the design constructable added USD 92 (PPR-DDR-004): the steel base plate under the female mold, the thicker 450 mm mold flanges, dowels and bushes (items 8 and 9, USD 44), floor anchors, the bolted jack plate and heavier feet (item 1, USD 22), the adapter disc and nut box (item 10, USD 9) and interlock details (item 21, USD 7).
- The fixed guards, front gate and interlock added USD 67 earlier (PPR-DDR-003); they are a safety requirement, so savings are sought elsewhere.
- Savings worth trying: cheaper dowels and bushes, and plywood QC rack shelves cut from offcuts.
- Idea from concept option B (PPR-OPT-001), a suggestion only: a quick approach move before the jack takes the load, to cut pumping time.

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
| 2026-10-03 | Front and roof mesh: 6.35 mm (1/4 in) welded mesh, 0.9 mm wire, on the front strips, lower front panel, front gate and roof (option (a)); the side and rear guards keep the 12.7 mm mesh | Amish: "PotPress - move forward with the four guard fixes. I accept the cost." | PPR-CAL-001, section 15; BOM items 16 and 20 |
| 2026-10-03 | Release shaft and pin cable openings: bolted plates behind the front right strip with a 20 mm hole round the 12 mm shaft and a 10 mm grommeted hole round the 6 mm cable (option (a)) | Amish: "PotPress - move forward with the four guard fixes. I accept the cost." | PPR-CAL-001, section 15; BOM item 16 |
| 2026-10-03 | Top beam gap: 3 mm steel cover plates bolted to the top flanges (option (a)); as modelled, one plate each side from the crank bracket to the beam end, which also closes the open tops of the upright channels | Amish: "PotPress - move forward with the four guard fixes. I accept the cost." | PPR-CAL-001, section 15; BOM item 16 |
| 2026-10-03 | Crank bracket: 2 mm sheet covers on its open front and back (option (a)); costed with the guards, BOM item 16 | Amish: "PotPress - move forward with the four guard fixes. I accept the cost." | PPR-CAL-001, section 15; BOM item 16 |
| 2026-10-23 | D2 clay shrinkage: reference filter is the fired size; molds 1.087 times larger for 8 % assumed shrinkage, to be measured on the partner clay; 480 mm flanges; frame 22 mm taller | Made under Amish's standing instruction: "i approve the pilot, and whenever a STEM check fails propose and implement the best fix to the design and constructability." | PPR-DDR-006; PPR-STM-001 M6 |
| 2026-10-23 | D3 heavy lifts: chain block, two-leg sling and eye bolts for every part over 25 kg; female lift points in the steel base plate; holes plugged before pressing | Made under the same instruction | PPR-DDR-006; PPR-STM-001 B2; BOM item 22 |
| 2026-10-23 | D4 handle force: working force limited to 6.4 t (PR-004); the handle extension first chosen was dropped after the independent review | Made under the same instruction | PPR-DDR-006; PPR-STM-001 S8 |
| 2026-10-23 | D5 scrap alloy: A356 wheel scrap sorted before melting; each melt checked by OES or XRF against EN 601; cast yield taken as 80 MPa | Made under the same instruction | PPR-DDR-006; PPR-STM-001 C3 |
| 2026-10-24 | Joint bolt preload: the 16 M16 10.9 upright joint bolts are tightened to preload (about 300 N·m, 110 kN), so the joints carry 294 kN by friction and do not slip in their 18 mm holes (STEM row S11; finding 4 of the independent review) | Made under Amish's standing instruction of 2026-10-23 (fix rule); no cost change; Amish can reverse it | PPR-STM-001 v0.3 S11; PPR-BLD-001 v0.8 step 8; PPR-CAL-001 v0.12 |
| 2026-10-25 | D1 concept: keep option A, the hydraulic bottle-jack press (125 of 160, 10.4 % ahead of B); reopen B if trials show the clay forms fully at under about 0.5 t | Amish: "i concur with your recommendations" | PPR-DDR-005 v0.3; PPR-OPT-001 v0.4; `project.yaml` `concept_chosen: A` |
| 2026-10-25 | D7 guard panel corners: option (a), as modelled on 2026-10-24: rear guard 884 mm wide, front left strip 152 mm, right side guard 607 mm long, each corner closed by the neighbouring frame's 3 mm edge leg; 23 of 23 openings meet ISO 13857 Table 4 | Amish: "i concur with your recommendations" | `cad/src/model.py` `guard_layout()`; PPR-DWG-110 Rev P5; PPR-CAL-001 section 15 |
| 2026-10-25 | D8 PR-013 local spares: option (a), the text as drafted; the named spares list is confirmed with the partner factory at TRL 4 | Amish: "i concur with your recommendations" | PPR-PRS-001 v0.16 |
| 2026-10-25 | D9 working force: option (a), working force limit lowered from 6.4 to 5.4 t (handle about 148 N with 85 % pump and seal efficiency) and 10 t stated in PR-003 as a structural check case only; EN 1005-3 assessment in the next calculation session; the two-speed pump (b) stays with D6 if trials need more than 5.4 t | Amish: "i concur with your recommendations" | PPR-PRS-001 v0.16 PR-003, PR-004; PPR-CAL-001 v0.13 sections 3 and 5; PPR-STM-001 v0.4 S5, S8; PPR-RSK-001 v0.3 P2, H10 |
