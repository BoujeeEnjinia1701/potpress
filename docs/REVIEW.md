# Review note: PotPress

## Session 2026-10-03: four guard fixes made

Authority: Amish, 2026-10-03: "PotPress - move forward with the four guard fixes. I accept the cost." The four fixes were open decisions 1 to 4 in PPR-DEC-001 v0.4, proposed by the ISO 13857 desk check of 2026-10-02. `trl` and `trl_target` stay at 3. No commit or push.

### What was done

- **Model** (`cad/src/model.py`): (1) 6.35 mm (1/4 in) welded mesh, 0.9 mm wire, on the front strips, lower front panel, front gate and roof (`FINE_*` parameters, `mesh_spec()`; sides and rear keep 12.7 mm; frames sit directly behind each mesh); (2) small-hole plates behind the front right strip, a 20 mm hole round the 12 mm release shaft and a 10 mm grommeted hole round the 6 mm pin cable; (3) a 3 mm cover plate 320 x 180 mm each side of the top beam, from the crank bracket to the beam end; (4) 2 mm sheet covers on the front and back of the crank bracket (`guard_closures()`; components `opening_plates`, `beam_covers`, `bracket_covers`, all BOM 16). New checks in `--check`: `check_guard_fixes()` moves the platen over its full 110 mm travel, the male mold over its full 200 mm crank lift, the demold set-up and the pump handle stroke against the new parts, and swings the gate 0 to 105 degrees in 15 degree steps; and the ISO 13857 desk check must pass for every opening. STEP and STL re-exported. `guard_solids()` and `gate_geometry()` now take `every_wire=True` in place of `pitch=`.
- **Found while modelling:** each upright is two channels back to back whose 44 x 83 mm insides were open from above, between the beam gap openings; the v0.9 desk check missed them. The cover plates were lengthened to run over the upright tops to close them (this is why fix 3 costs $7, not about $3). The desk check now also lists the crank bracket front and back, the roof's 5 mm cut-out round the beam and the gate's 4 mm edge gaps.
- **BOM** (`bom/bom.csv`, `bom/bom-notes.md`): item 16 $73 to $90, item 20 $22 to $25, with the basis in each line (6.35 mm mesh at about $10.50/m² against $6/m², plates and covers by model mass at $1.30/kg plus bolts).
- **Documents:** PPR-CAL-001 v0.10 (section 15 rerun, sections 10, 12, 13, 14; `sizing.py` prices the fixes and prints the guard mass change); PPR-REQ-001 v0.12; PPR-PRC-001 v0.11; PPR-BLD-001 v0.6 (sections 3.10 and 3.11, steps 14 to 16, checks table); PPR-DEC-001 v0.5; README cost and desk-check sentences.
- **Drawings and pictures regenerated:** GA PPR-DWG-001 Rev P7 (isometric moved down 7 mm so the seventh revision row no longer clips it); PPR-DWG-110 Rev P3; PPR-DWG-111 Rev P2; build plan `overview.png`, `joint-06.png` (grommet plate added), `step-14.png` (plates and covers shown pulled out), `step-15.png`, `step-16.png`; concept `hero.png`, `exploded.png`, `concept-blueprint.*` (Rev P3), `model.glb` and `viewer.html`. Looked at: GA, DWG-110, DWG-111, overview, joint 6, step 14, hero and the blueprint. `cutaway.png` and `flow.png` are unchanged (guards are left out of the cutaway). The blueprint's last note line fell behind the title block on first draw (the text check did not catch it); the guard notes were merged into one line and the isometric moved below the third revision row. `step-15.png` and `step-16.png` were regenerated but not looked at. `python3 .kit/drawing.py --check-text` passes on every drawing and the blueprint; `python3 .kit/render.py` then `--check`: no FAIL.
- **Appearance model** (`cad/src/product_model.py`): the plates and covers added to the guard group; mesh drawn every wire at 12.7 mm on the sides and rear and 6.35 mm on the front, gate and roof. Render scenes re-exported to `/home/claude/renders/potpress/` (hero, exploded, lineup, gate-open, jobs). `.kit/export_views.py` cannot carry a manual camera option, so the hero's `--focus` (on the guards, handwheel, mat and person, from the 2026-10-02 render session) is still not in `potpress__jobs.json` and must be passed by hand when the hero is re-rendered on the Mac. Photoreal renders and cards are stale until then.

### Key results

- **Desk check (ISO 13857:2019 Table 4, as read), rerun for every opening:** 23 openings, **all meet on paper**. Front strips, gate, lower front and roof: 5.45 mm clear mesh needs 5 mm, nearest moving part 39 to 77 mm. Release shaft: 4 mm gap needs 2 mm, 80 mm found. Pin cable: 2 mm gap, 176 mm. Top beam gap, upright channel tops and crank bracket: covered (0 mm opening), 36 to 217 mm from moving parts. Roof cut-out 5 mm slot needs 10 mm, 72 mm found. Gate edges 4 mm, 44 mm. Side and rear mesh and the shielded pump slot unchanged (meet).
- **Motion checks:** nearest moving part 46 mm from the small-hole plates (lock rod), 55 mm from the beam covers and 35 mm from the bracket covers (stem); release shaft 4.0 mm and cable 2.0 mm all round in their holes; gate 0 overlaps over its swing, 23 mm from the folded rail extension. `model.py --check`: 55 components, 0 overlaps, 0 missing contacts, all state checks, guard fix checks and the desk check pass: **PASS**.
- **R9: not met on paper to met on paper.** The desk check is still **not signed**; the competent-person signature block is left blank, and signing stays a hold point before any force above hand pressure (S8).
- **Cost:** Value-engineering target: USD 1,060. Estimated cost of the constructable design: USD 1,169 (USD 109 over the target). The fixes add $20, against the "about USD 15" estimate Amish accepted; the $5 difference is the longer cover plates. `budget_usd` unchanged.
- **Mass:** press 344 kg unchanged; guards about 51 kg (was about 48): plates and covers +4.4 kg from the model, finer mesh -1.6 kg. Heaviest part still the platen, 39.6 kg.
- Summary: 1 over the value-engineering target (R10), 2 at risk (R2, R7), 9 met on paper.

### Proposed, awaiting Amish

None new. Note for Amish: the fixes came in $5 over the estimate he accepted (see Cost).

### Safety concerns

- The desk check is unsigned; nothing above hand pressure until a competent person signs it (S8).
- 0.9 mm wire mesh is light. The competent person should confirm it keeps its shape when pushed (ISO 14120), since the front right strip stands only 39 mm from the folding rail extension; heavier wire of the same opening would be the fallback (not proposed here).
- The top beam cover plates and crank bracket covers are removable guards held by bolts; the build plan says to remove them only with the press at rest and the release open.

### Recommended next step

A competent person reviews and signs the desk check; render the hero, lineup and gate-open views on the Mac (hero with `--focus`).

## Session 2026-10-02: Photoreal renders redone on the constructable design

Amish, 2026-10-02: "Photoreal renders are out of date in most repos ... COMPLETE THESE". Rendered with Blender Cycles on Amish's Mac (batch F1) from the scenes exported from `cad/src/product_model.py`, captioned with `.kit/photo_caption.py`; `media/card.png` and `media/social-preview.png` regenerated with `.kit/cards.py`. Each raw render was looked at once. No commit or push; `trl` unchanged.

- Views: `media/render-hero.png`, `media/render-exploded.png`, `media/render-lineup.png`, `media/render-gate-open.png`.
- Re-renders: hero (twice), lineup and gate-open. The mannequin stood at the front right, in line with the hero camera, and hid most of the press and the pump handle; in the lineup it stood in front of the press's right side. `cad/src/product_model.py` now stands it at the front left facing the press (clear of the open gate by at least 0.2 m) and extends the floor slab to suit; the hero note says "1.75 m person at the front left for scale". The hero was then re-rendered with `--focus` on the guards, handwheel, mat and person, because the larger slab left most of the frame empty. `.kit/export_views.py` does not carry `--focus`, so a re-render of the hero needs it passed by hand.
- Appearance deviations already logged (2026-10-02, render only): mesh drawn at every wire; coiled springs with hooks; jack split into red body and polished ram; nameplate and load rating label; hazard label; floor slab, anti-fatigue mat and 1.75 m mannequin (now at the front left rather than the front right); floor anchors left out.
- `python3 .kit/image_qc.py`: 6 images, 0 problems. `python3 .kit/render.py --check`: no FAIL, no storefront warning.
- The "Stale, to regenerate on Amish's Mac (Blender)" note (2026-09-30 session) is removed; this work resolves it.

## Session 2026-10-02: approved follow-ups carried out

Authority: Amish, 2026-10-02: "497 follow-up actions that need CAD, drawing, picture, BOM or calculation work ... APPROVED CHANGES, COMPLETE THESE", and "Photoreal renders are out of date in most repos ... COMPLETE THESE" (render scenes prepared here; the renders themselves are made on Amish's Mac). Follow-ups from the 2026-10-02 list below and `/home/claude/review/applied/potpress.json`. `trl` and `trl_target` stay at 3. No commit or push.

### Approved follow-ups carried out

| # | Follow-up | Done | Where |
| --- | --- | --- | --- |
| 1 | Design the fixed inner shield behind the 30 mm pump slot; check the handle clears it over its stroke | Done. A tunnel of 2 mm folded sheet, 30 mm wide inside, along the handle's line from the slot to 3 mm off the jack body, with a 3 mm flange bolted through the slot frame and a 30 x 6 mm stay to the base beam (2.8 kg). Sized in the desk check: the slot is lengthened from 220 to 272 mm (174 to 446 mm up) and the tunnel's roof and floor follow the handle, so the handle stops 25 mm short of them and of the slot ends at both ends of its stroke (ISO 13854 finger gap); 5 mm to the side walls; 2.3 mm past the slot frame. Constructability checks PASS (52 components, no overlaps, all 49 contacts, open and demold states, handle stroke, hooks, lock notch); new checks for the shield's contacts, side clearance and stroke-end gaps | `cad/src/model.py` (`pump_shield`, `HANDLE_STROKE`, `guard_solids`), STEP and STL re-exported |
| 1 | Add the shield to the GA and the right side guard sketch | Done | PPR-DWG-001 Rev P6; PPR-DWG-110 Rev P2 |
| 1 | Show the shield in the build plan guard section, item 3 | Done: section 3.10 items 3 and 6, Figure 20 (joint 11, shield cut along the handle), steps 14 and 16 | `docs/05-build-plan.md` v0.5; `docs/05-build-plan/joint-11.png`, `step-14.png`, `step-16.png`, `overview.png` |
| 1 | Add the shield to BOM line 16 | Done: $67 to $73 (2.8 kg x $1.30/kg plus $2 bolts); brush strip dropped | `bom/bom.csv`, `bom/bom-notes.md` |
| 1 | Re-judge R9 once the shield is modelled | Done: R9 **at risk to not met on paper** (see below) | PPR-CAL-001 v0.9, PPR-REQ-001 v0.11 |
| 2 | Mark the pump handle's 158 mm operating space on a floor layout | Done: outlined on the floor beside the right guard in the GA (159 x 122 mm zone) and noted in the build plan workspace | PPR-DWG-001 Rev P6; PPR-BLD-001 section 7 |
| 4 | Mean pressure at 2 t in PPR-CAL-001 Table 3 | Done: 19.6 kN, 0.21 MPa, the starting reference for pressing trials | PPR-CAL-001 v0.9 section 3; `sizing.py` |
| 5 | ISO 13857 desk check of the mesh, pump slot, roof reach and the handle's pass by the slot frame, signed by a competent person | Desk check done from the model's distances (`model.py --iso`, printed by `sizing.py`), every guard opening included. **Not signed**: a competent person must review it against the published table and sign; the signature block is left blank | PPR-CAL-001 v0.9 section 15 |

### Key results

- **Desk check (ISO 13857:2019 Table 4, as read):** side and rear mesh 100 to 110 mm from moving parts (80 needed): meets. Pump slot: opens only into the shield; no moving part enters it in any position: meets. Handle past the slot frame: 2.3 mm, a gap too small for a fingertip: meets on paper. **Does not meet:** front right strip 39 mm, front gate 44 mm, lower front panel 45 mm, front left strip 60 mm (all to the folding rail extension, which moves with the platen), roof mesh 77 mm (stem); release shaft opening (16 mm gaps, 120 needed, 61 found) and pin cable opening (40 mm square, 200 needed, 166 found); the top beam gap is open from above (104 x 150 and 104 x 60 mm openings) and reaches the stem and, cranked up, the male flange 15 mm under the beam; above the roof, the stem cap rises to 10 mm under the crank bracket top in a bracket open front and back.
- **Requirement status changes:** R9 at risk to **not met on paper**. R10 stays over the value-engineering target, now by $89. Summary: 1 over the target (R10), 1 not met on paper (R9), 2 at risk (R2, R7), 8 met on paper.
- **Cost:** Value-engineering target: USD 1,060. Estimated cost of the constructable design: USD 1,149 (USD 89 over the target). `budget_usd` unchanged.
- **Mass:** press 344 kg unchanged; guards about 48 kg with the 2.8 kg shield (was about 45 kg); heaviest part still the platen at 39.6 kg.

### Proposed, awaiting Amish

Added as open decisions 1 to 4 in the design decisions register (PPR-DEC-001 v0.4), from the desk check: (1) 6.35 mm (1/4 in) mesh on the front strips, lower front panel, gate and roof; (2) small-hole plates at the release shaft and pin cable openings; (3) cover plates over the top beam gap; (4) covers on the front and back of the crank bracket. About USD 15 together (estimate). With all four, every opening meets Table 4 on paper. The handle's real stroke and play on the jack bought is added to "To confirm when parts are bought".

Appearance model deviations from `model.py` (render only): guard and gate mesh drawn at every wire (12.7 mm) instead of every 8th; coiled springs with hooks in place of the spring envelopes; jack split into a red body and a polished ram; nameplate and load rating label on the top beam; hazard label on the front right strip; floor slab, anti-fatigue mat and a 1.75 m mannequin standing to the front right; floor anchors left out (below the floor).

### Documents changed and new versions

- `docs/04-calcs/01-sizing.md` PPR-CAL-001 v0.9 and `docs/04-calcs/sizing.py`
- `docs/03-requirements.md` PPR-REQ-001 v0.11
- `docs/02-concept.md` PPR-PRC-001 v0.10
- `docs/06-design-decisions.md` PPR-DEC-001 v0.4
- `docs/decisions/0004-design-for-construction.md` PPR-DDR-004 v0.5
- `docs/05-build-plan.md` PPR-BLD-001 v0.5
- `bom/bom.csv`, `bom/bom-notes.md`, `README.md`
- `cad/src/model.py`, `sheets.py`, `build_plan_media.py`, `concept_media.py`, `product_model.py` (rebuilt from the constructable components)

### Pictures regenerated (each looked at)

GA PPR-DWG-001 Rev P6 (notes shortened to fit above the title block); making sketch PPR-DWG-110 Rev P2; build plan `overview.png`, `joint-11.png` (redrawn as a cut through the shield), `step-14.png` (shield shown pulled out to the right), `step-15.png` to `step-18.png`; concept `hero.png`, `cutaway.png`, `exploded.png` (guard line renamed so its legend no longer runs into the picture), `concept-blueprint.*` (Rev P2: force from trials at 2 t, shield), `model.glb` and `viewer.html`. `python3 .kit/drawing.py --check-text` passes on every drawing and the blueprint. No "pictures not yet updated" notes remained to remove.

### Render scenes

`cad/src/product_model.py` rebuilt from `model.components()` so every dimension is the constructable model's. Exported with `.kit/export_views.py` to `/home/claude/renders/potpress/`: `potpress__hero`, `__exploded`, `__lineup`, `__gate-open` (.npz and .json each) and `potpress__jobs.json`. Photoreal renders, `card.png` and `social-preview.png` are still the concept's until they are rendered on Amish's Mac.

### Cross-repo actions

None.

### Safety concerns

- The desk check is unsigned and finds openings short of ISO 13857; nothing above hand pressure until the proposed guard changes are made and a competent person signs the check (build plan safety stop S8).
- The folding rail extension, which moves with the platen, is the part nearest the front guards; this was not visible in the earlier "105 to 110 mm" figures.

### Recommended next step

Amish to decide open decisions 1 to 4; then model the chosen guard changes, re-run the desk check, and render on the Mac.

## Session 2026-10-02: open decisions decided by Amish

Authority: Amish, 2026-10-02: "i approve your recommendations for all 555 open decisions." The recommendations approved are those written for the five open decisions in the design decisions register (PPR-DEC-001). No model, BOM quantity or price, or picture was changed; where a decision needs one, it is listed below as a follow-up. `trl` and `trl_target` stay at 3. No commit or push.

### Decisions recorded

Five, all moved to "Decisions made" in `docs/06-design-decisions.md`, dated 2026-10-02:

1. Pump slot: keep 30 mm, approved only with a fixed inner shield or tunnel behind the slot, sized in the ISO 13857 check.
2. Pump handle: the 158 mm it stands outside the guard is operating space, marked on the floor layout; R11 applies to the guarded box.
3. Demolding: keep the tipping pins for the prototype; the first partner factory's potters confirm the method, with lifting out in the liner as the fallback.
4. Pressing force: structural checks stay at the full 20 t jack; the working force is found in pressing trials from about 2 t upward.
5. ISO 13857: desk check done now, signed by a competent person, a hold point before any force above hand pressure.

### Documents changed

- `docs/06-design-decisions.md` (PPR-DEC-001 v0.3)
- `docs/decisions/0004-design-for-construction.md` (PPR-DDR-004 v0.4): Q2, Q3 and Q5 recorded as decided; status stays Draft
- `docs/decisions/0003-guarded-version.md` (PPR-DDR-003 v0.3): ISO 13857 check decided
- `docs/02-concept.md` (PPR-PRC-001 v0.9)
- `docs/03-requirements.md` (PPR-REQ-001 v0.10): R9 now at risk until the pump slot shield is designed and the check is signed
- `docs/04-calcs/01-sizing.md` (PPR-CAL-001 v0.8): R9 status and summary count; force text

### Follow-up actions to carry approved decisions into the design

1. Decision 1 (model, drawings, build plan pictures, BOM): design the fixed inner shield or tunnel behind the 30 mm pump slot in `cad/src/model.py`, check that the pump handle still clears it over its stroke, add it to the GA drawing PPR-DWG-001, the right side guard sketch and the build plan pictures (section on the guards, step 3), and add it to BOM line 16.
2. Decision 1 (calcs): once the shield is modelled, re-judge R9 in PPR-CAL-001 and PPR-REQ-001.
3. Decision 2 (drawings): mark the pump handle's 158 mm operating space on a floor layout (GA drawing or build plan overview).
4. Decision 4 (calcs): add the mean pressure at 2 t to PPR-CAL-001, Table 3, so the pressing trials have a starting reference.
5. Decision 5 (calcs): do the ISO 13857 desk check of the mesh, the pump slot, the roof reach and the pump handle's 1.4 to 2 mm pass by the slot frame from the model's distances, and have a competent person sign it.

### Points found in the review

- Value engineering does not compare like with like: the USD 1,060 target was set on 2026-09-27 to cover the USD 1,051 BOM including the QC rack, so reading it against the press alone hides the real USD 83 gap.
- Decision 4 cites PPR-DDR-001 item 9, which is the first co-design partner, not the pressing force. The partner decision is still open (REVIEW 2026-09-30) but is missing from the open decisions table; it was not part of the decisions approved on 2026-10-02 and should be added back to the register.
- The pump handle runs 1.4 to 2 mm from the slot frame over its stroke; that is a finger shear point and should be covered by the ISO 13857 check (follow-up 5). A brush strip does not count as a guard.
- PPR-DDR-004 Q2 deferred the ISO 13857 check to TRL 4, while build plan safety stop S8 required it before any force. Decision 5 resolves this in favor of S8: the check is done now.
- PPR-DDR-004 Q4 (the interlock notch angle, set to the jack bought) remains proposed in that record; it is covered by "To confirm when parts are bought", item 1.

## Session 2026-09-30: constructable design and illustrated build plan (/build-plan)

Authority: the `/build-plan` command and Amish's instructions of 2026-09-30 ("Design concept and constructability are different states"; "fix the design assumptions to match and be physically feasible as you draw the illustrations"; "i accept your recommended changes on design that are currently being sent across for my approval"). This replaces the earlier text-only build plan and its review section, which Amish rejected. Commit and push were skipped by instruction. `trl` and `trl_target` stay at 3.

### What was done

- `cad/src/model.py`: design made constructable (P1 to P17 below). New checks with `python cad/src/model.py --check`: no overlaps among 51 components with the press closed, open (platen down, stem cranked up, pin parked) and set for demolding (extension out, carriage on the tipping pins, gate open); all 47 required contacts touch; the pump handle clears the guard over its whole stroke (1.4 mm nearest at the stroke ends); the carriage hooks meet the tipping pins (1.0 mm sliding fit); the lock rod drops into the disc notch. Result: PASS.
- `docs/decisions/0004-design-for-construction.md` (PPR-DDR-004 v0.2): every change with its reason; accepted by Amish 2026-09-30; Table 3 holds what stays proposed.
- `docs/04-calcs/sizing.py` and `01-sizing.md` (PPR-CAL-001 v0.6): new checks (male flange on the stop, M16 joints, rails over the platen gap, pin block with screw hole, tipped mold, stop lugs, tipping pins); masses, deflection and costs from the constructable model.
- `docs/03-requirements.md` (PPR-REQ-001 v0.8): status from CAL v0.6; no requirement text changed.
- `bom/bom.csv`: lines rewritten to the buildable parts (anchors, studs, jack plate, M16 10.9 bolts, spacer tubes, shims, steel base plate, dowels, bushes, adapter disc, captive nut, lift handles, tipping pins, interlock parts); total $1,143.
- `cad/src/build_plan_media.py` (new) and `docs/05-build-plan.md` (PPR-BLD-001 v0.2, rewritten from the template): overview, 14 making sketches `cad/drawings/PPR-DWG-101` to `114`, 11 joint close-ups and 18 assembly steps in `docs/05-build-plan/`, all drawn from the model and each looked at.
- `cad/src/sheets.py`: GA PPR-DWG-001 regenerated at Rev P5. STEP and STL re-exported.
- `cad/src/concept_media.py`: restructured so each picture renders in its own process (the full run had been killed for memory); cutaway leaves out the guards and gate. `media/hero.png`, `cutaway.png`, `exploded.png`, `flow.png`, `concept-blueprint.*`, `model.glb` (now about 12 MB) and `viewer.html` regenerated and checked.
- `.kit/build_views.py`: `overview()` gained a `key=True` option (numbered bubbles on the parts and a key column, in place of leader lines that crossed the picture with 19 parts). Proposed for the kit.
- `project.yaml`: `design_state: constructable`; PPR-DDR-004 added to `trl_evidence`. `README.md`: "Building the prototype" section with the overview picture; key components and concept figures updated.

### Design changes made for construction (PPR-DDR-004)

1. **P1 male mold:** open-topped plug, its inside a drafted cone that forms its own sand core; flat-back pattern, no core box.
2. **P2 male flange:** 45 mm thick, 450 mm across; the stem's 190 mm disc bears on the plug floor (bedded in epoxy putty, 4 x M12); 62 MPa at 294 kN on the stop (was about 487 MPa).
3. **P3 mold location:** two 16 mm dowels and two steel bushes, drilled with the molds clamped on 15 mm printed wall spacers; stop faces lapped on float glass; patterns with 1.3 % shrink, 3 mm lapping allowance and 2 degree draft; female cup bedded and screwed on a 15 mm steel base plate. No lathe.
4. **P4 jack and slot:** jack turned 25 degrees to the right front; slot on the handle's line, widened from 25 to 30 mm; handle clears spring and upright by about 50 mm.
5. **P5 lead screw:** captive nut with 8 mm float; press force through the pin only.
6. **P6 beam gap:** 104 mm with 2 mm shims.
7. **P7 joint bolts:** 4 x M16 10.9 per joint, 22 mm edge distance, 25 x 3 spacer tubes; 117 MPa double shear at 294 kN.
8. **P8 tipping:** tipping pins on the extension, hooks and retaining pins on the carriage, lift handles.
9. **P9 interlock:** lock disc, lock rod, gate slider, pin slider and plunger round the jack's release screw.
10. **P10 feet and BOM:** feet web up with studs and anchor tubes, four floor anchors, spring lugs, tubes and shims in the BOM; QC pot shelf raised to 720 mm (35 mm clear of the buckets).
11. **P11 (found):** rail hinge moved back from 320 to 290 mm so the folded extension clears the gate and lower panel with the platen down.
12. **P12 (found):** 28 mm hole down the pin block so the fixed lead screw passes when the stem is cranked up.
13. **P13 (found):** plastic guide strips on the top beam webs; stem play front to back 7 to 1 mm.
14. **P14 (found):** pump handle (20 mm, 700 mm) added to the design and checked over its stroke.
15. **P15 (found):** assembly order set by the model (stem in before the top beam; both molds together on the extension).
16. **P16 (found):** female base plate on greased steel rails, not plastic strips; rails checked over the platen gap (101 MPa).
17. **P17 (found):** lift handles behind the tipping pins (the only handle was in front of them).

### Key results

| Quantity | Value |
| --- | --- |
| Constructability checks | PASS: closed, open and demolding positions; handle stroke; hooks; lock notch |
| Frame at 294 kN | Beams 190 MPa, pin 272 MPa (yield 650), M16 joints 117 MPa, male flange 62 MPa (cast yield about 90) |
| Deflection at 10 t | 0.66 mm (R3 met on paper) |
| Masses | Press 344 kg plus about 45 kg of guards; heaviest part the platen at 39.6 kg (R8, 40 kg) |
| Parts cost | Estimated $1,143 against the $1,060 value-engineering target: **over the target by $83** (7.8 %) |
| Requirements | 1 over the value-engineering target (R10), 2 at risk (R2, R7), 9 met on paper |

### Proposed, awaiting Amish (PPR-DDR-004, Table 3)

1. **Value engineering:** the estimate is $83 over the $1,060 target; the savings worth trying are in the design decisions register. `budget_usd` is unchanged.
2. **Q2 pump slot 30 mm:** same ISO 13857 band as 25 mm; the ISO 13857 check itself is still open (PPR-DDR-003).
3. **Q3 pump handle:** stands 158 mm outside the right guard while in use (beyond R11's 1.0 m width). Recommendation: treat it as operating space.
4. **Q4 interlock notch angle:** set to the jack bought, at TRL 4.
5. **Q5 demolding by tipping:** confirm with a partner factory's potters.

Still open from earlier sessions: the ISO 13857 guard distance check and the first co-design partner (PPR-DDR-001 item 9).

### Safety concerns

- The build plan's safety stops cover welding, galvanised mesh, lifts up to 40 kg, standing the frame, and the only unguarded jack movement (step 13, by hand to first contact with the pin home). Nothing authorises pressing or any force above hand pressure.
- The single load pin still carries the whole press force; the pin-presence interlock is now detailed (plunger, cable, pin slider) but untested.
- The slot widening (Q2) and the handle outside the guard (Q3) touch the guarding and need Amish's decision and the ISO 13857 check.

### TRL

`trl` stays 3, now with a constructable design and an illustrated build plan. **TRL 4 remains on hold by Amish's instruction.** No build, purchase, measurement or test was started.

### Recommended next step

Amish to decide Q1 to Q5, then regenerate the photoreal renders from an updated appearance model on the Mac. After that, the repo is ready for a TRL 4 recommendation when Amish lifts the hold.

## Session 2026-09-27: owner decision applied

Authority: Amish wrote on 2026-09-27, "i agree with the budget for potpress." This applies recommendation (a) of item 1 in the 2026-09-26 session below: raise the budget to about $1,060 for the guarded version. Decided by Amish on 2026-09-27. Only this item is decided. `trl` and `trl_target` stay at 3.

### What changed

- `project.yaml`: `budget_usd` from 990 to 1060, with the history comment extended ("raised to 1,060 by Amish, 2026-09-27 (PPR-DDR-003)").
- `docs/decisions/0003-guarded-version.md` PPR-DDR-003 v0.2: the cost overrun is recorded as decided by Amish on 2026-09-27 (option (a)); status line updated; the ISO 13857 guard opening check is marked proposed, awaiting Amish.
- `docs/04-calcs/01-sizing.md` PPR-CAL-001 v0.5: summary, decisions table, cost section, Table 10 (R10 now met on paper) and a v0.5 change note. `sizing.py` needed no change; it reads the budget from `project.yaml` and now prints a $9 (0.8 %) margin.
- `docs/03-requirements.md` PPR-REQ-001 v0.7: R10 target $1,060, Table 2 status, new "Requirement change decided by Amish, 2026-09-27" subsection.
- `docs/02-concept.md` PPR-PRC-001 v0.7: summary, numbers table and "Budget $1,060" design choice.
- `docs/01-problem.md` PPR-PRB-001 v0.6: budget constraint $1,060.
- `bom/bom-notes.md` and `README.md`: budget and R10 lines. `bom/bom.csv` is unchanged.
- `cad/src/sheets.py`: PPR-DWG-001 Rev P4 ("Budget raised to $1,060 (DDR-003); R10 met; note only"); the cost note now reads "Cost $1,051 vs $1,060 budget: R10 met on paper"; the isometric view moved down 9 mm and shrank slightly so it clears the taller revision table. `cad/drawings/PPR-DWG-001.svg`, `.pdf`, `.png` regenerated and checked.
- `docs/pdf/`: rebuilt with `python .kit/render.py` (PRB v0.6, PRC v0.7, REQ v0.7, CAL v0.5, DDR-003 v0.2).
- No change to `cad/src/model.py` or `cad/src/product_model.py`: the decision is a budget figure only, so no geometry, dimension or interface changed. STEP, STL and concept media were not regenerated because nothing they show changed.

### Result

| Quantity | Value |
| --- | --- |
| Cost | $1,051 (press $970, QC rack $81) against $1,060 |
| R10 | Met on paper, $9 (0.8 %) margin; thin, any price rise moves it back to at risk |
| Requirements | 0 not met, 2 at risk (R2, R7), 10 met on paper |

### Photoreal renders

The decision does not require regenerating the renders: no part in any RENDER_VIEWS view changed shape, size or position. Separately, item 2 of the 2026-09-26 session still stands: `media/render-*.png` show the unguarded press and need re-rendering from the guarded RENDER_VIEWS before any public use.

### Still proposed, awaiting Amish

1. **ISO 13857 guard distances.** The adequacy of the 11 mm mesh at about 105 to 110 mm, the 25 mm pump slot and reach over the roof remains a stated assumption, not checked (PPR-DDR-003).
2. **Photoreal renders** re-rendered for the guarded press (2026-09-26 item 2).
3. **First co-design partner** (item 9): still open.

### TRL

`trl` stays 3. **TRL 4 remains on hold by Amish's instruction.** No build, measurement or purchasing was started.

## Session 2026-09-26: guarded version

Authority: Amish wrote on 2026-09-26, "for pot press build a guarded version and make sure the render follows." Recorded as decided in `docs/decisions/0003-guarded-version.md` (PPR-DDR-003 v0.1). No existing part or main dimension changed. `trl` and `trl_target` stay at 3.

### What changed

- `cad/src/model.py`: new guard parameters and helpers (`mesh_panel`, `angle_frame`, `guard_layout`, `gate_geometry`, `interlock_geometry`) and three new parts: fixed mesh guards (BOM 16), front gate (20), gate interlock and release valve extension (21). `press_only()` now includes them, so `cad/step/potpress-press.step`, `potpress-assembly.step` and the STLs are the guarded press. Mesh is drawn at every eighth wire (101.6 mm) so views stay readable.
- Guarding chosen: fixed welded-mesh guards (sides, back, roof, front strips, lower front panel) and a hinged front gate with a mechanical guard-locking interlock on the jack release. A hand pump has no power to switch, so the interlock holds the release valve open (pumping then builds no pressure) unless the gate is shut, and holds the gate shut while the valve is closed. The decided pin-presence plunger acts on the same lock bar. Two-hand control (does not suit a one-lever pump) and hold-to-run alone (leaves a hand free) were rejected; see PPR-DDR-003.
- `bom/bom.csv`: item 16 is now the fixed guards ($67, was a $55 allowance for all guarding); new item 20, front gate with hinges ($21); new item 21, gate interlock and release extension with the pin-presence plunger ($34). `bom/bom-notes.md` updated.
- `docs/04-calcs/sizing.py`: items 20 and 21 counted as press cost; guard solids left out of the mass table (their mesh is symbolic). The masses and tipping result are unchanged. PPR-CAL-001 moved to v0.4 with the guarded costs.
- `docs/02-concept.md` PPR-PRC-001 v0.6 and `docs/03-requirements.md` PPR-REQ-001 v0.6: guarding, safety, R9 text and status tables.
- `cad/src/sheets.py`: PPR-DWG-001 Rev P3, "Guards and interlocked front gate added"; notes condensed so they fit.
- `cad/src/concept_media.py` re-run: `media/hero.png`, `cutaway.png`, `exploded.png`, `flow.png`, `concept-blueprint.*`, `model.glb` now show the guarded press.
- `cad/src/product_model.py`: guard frames in safety-yellow powder coat, mesh wire by wire at 12.7 mm pitch, pump slot with brush strip, standoffs, hazard label, red guard-locking interlock with link rod, lock block, release extension and T-handle; gate in group `gate_closed` and, swung open 105 degrees, in `gate_open`. RENDER_VIEWS: hero and lineup now include the guards with the gate closed (hero note replaced); exploded keeps its parts and now says guards are not shown; new view `gate-open` (el 18, az -68). Triangles: hero and gate-open 683k, lineup 725k, exploded 612k. All 88 parts valid.
- `project.yaml`: PPR-DDR-003 added to the TRL evidence. Budget unchanged.

### Numbers

| Quantity | Value |
| --- | --- |
| Mesh | 12.7 x 12.7 x 1.6 mm welded (about 11 mm clear); 4.3 m² fixed plus 0.57 m² gate |
| Nearest moving part behind the mesh | Back 105 mm (platen deck), sides 109 mm (platen sleeves), front 110 mm (carriage handle) |
| Guarded press | 940 x 700 x 1,806 mm with the rail extension folded (840 x 655 mm unguarded) |
| Guard mass | About 45 kg (estimate) |
| Cost | $1,051 (press $970, QC rack $81) against $990: $61 (6.2 %) over |

### Requirements now

| ID | Status |
| --- | --- |
| R10 | **Not met**: $1,051 against $990 |
| R2, R7 | At risk (unchanged) |
| R9 | Met on paper; guard openings and distances assumed against ISO 13857, tables not checked |
| R11 | Met on paper at the 0.7 m depth limit, no margin |
| R1, R3 to R6, R8, R12 | Met on paper (unchanged) |

### Proposed, awaiting Amish

1. **Cost overrun ($61).** Options: (a) raise `budget_usd` to about $1,060, since guarding is a safety requirement (recommended); (b) cost the QC rack ($81) outside the press budget; (c) keep $990 and record R10 as not met. `budget_usd` was not changed.
2. **Photoreal renders.** `media/render-hero.png`, `render-exploded.png` and `render-lineup.png` still show the unguarded press; they need re-rendering from the updated RENDER_VIEWS (including the new `gate-open` view) before any public use.
3. Done later in this session: `README.md` and PPR-CAL-001 (now v0.4, "Guarded version costs (PPR-DDR-003)") were updated to the $1,051 guarded BOM.
4. First co-design partner (item 9): still open.

### Safety concerns

- The ISO 13857 adequacy of the 11 mm mesh at about 105 mm, the 25 mm pump slot and reach over the roof is an assumption; a competent person must check it before any use.
- The gate-open render draws the press in its pressing position for comparison; in use the gate opens only after the release is open and the platen is down.
- Guards and interlocks must be inspected each shift and never defeated. All other concerns from earlier sessions stand.

### TRL 4

**TRL 4 remains on hold by Amish's instruction.** No build, guard check, measurement or purchasing was started.

### Recommended next step

Amish to decide the cost overrun (item 1). Then re-render the product views.

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

## Session 2026-09-26: product appearance model and photoreal renders

Amish chose this repo for the first batch of product renders on 2026-09-26. This session adds an appearance model for photoreal product renders; it changes no dimension, interface, requirement or cost.

### What was done

- New `cad/src/product_model.py`: `product_parts()` (52 parts: 40 shell, 1 internal, 9 accessory, 2 context), `TITLE` and `RENDER_VIEWS` (hero, exploded, lineup). All levels, sections and interfaces come from `PARAMS`, `SECTIONS`, `levels()` and the helpers in `cad/src/model.py`, which is unchanged.
- `README.md`: hero image now points to `media/render-hero.png`, with an exploded render link at the start of the links line. The render files are produced later by the orchestrator.

### What the appearance model adds

- Frame: painted channels; the 16 upright joints drawn as separate hex-head M20 bolts, washers and nuts; end-capped feet with floor anchor nuts; UHMW-PE stem guide liners in white; a teal nameplate and a yellow 20 t load rating label on the top crossbeam.
- Bottle jack: red body with filleted base and cap ring, pump boss, black pump socket and plunger, polished ram, serrated saddle, release valve knob and rating label, all inside the model.py jack envelope.
- Return springs drawn as close-wound coils with end hooks; grease nipples on the platen sleeves; barrel hinges on the folding rail extension; a rubber grip on the carriage pull handle.
- Molds: cast aluminum finish with filleted flange and base edges, an ID plate with rivets on the female flange, and a radiused male mold tip.
- Male mold slide: teal SHS stem with true rounded corners, adapter plate screws, a bright load pin with a knurled head and retaining ring, a bronze lead screw nut, lightening windows in the crank bracket side plates, and a round-rim handwheel with a hub and black grip knob.
- The pressed pot between the molds is shown in green (unfired) clay; the QC rack test pots in fired terracotta.
- QC rack (accessory): angle-section legs, edge frames, plywood shelves, HDPE buckets with rolled rims and hoops, a teal T-gauge with scale marks, and water in one pot.
- Context: a compact concrete floor patch under the press and an anti-fatigue mat at the operator side.

### Where the appearance model differs from model.py

1. **Guards and front gate (BOM 16) are not shown**, as in model.py, so the jack, molds and platen stay visible. The hero note says so. Proposed, awaiting Amish: (a) keep them out of the product renders with the note (recommended for now, because the guards are not yet designed); (b) add a guarded variant view once the guard geometry exists at a later step. Recommendation: (a) now, (b) before the renders are used anywhere public-facing, so the images do not suggest the press runs unguarded.
2. **QC rack detail.** model.py draws solid 40 mm legs and 20 mm solid shelves; the appearance model draws 40 x 40 x 4 angle legs, a 4 mm edge frame and 18 mm plywood shelves, matching the BOM item 12 text. Footprint and shelf heights are unchanged. Proposed, awaiting Amish: accept as a display detail (recommended), or carry the same detail into model.py at the next CAD session.
3. **Handwheel rim** is a round-section ring (260 mm outer diameter kept) instead of model.py's flat ring, with four round spokes. **Buckets** taper slightly (300 mm top diameter kept). Proposed, awaiting Amish: accept as display detail (recommended).
4. **Labels, nameplate and ID plate** are new visual parts with no BOM line; they are drawn under the BOM line of the part they sit on. Proposed, awaiting Amish: leave them out of the BOM at TRL 3 (recommended); add a labels line at a later costing pass if wanted.
5. **Floor patch and mat** are context only, not in the BOM.

### Status

This is an appearance model only: no tolerances, no fabrication detail, CONCEPT, NOT FOR FABRICATION. `trl` stays 3 and TRL 4 remains on hold.

## Session 2026-09-27: kit 1.5.0 and image quality

- Kit 1.5.0 synced: STANDARDS v1.5 (sections 12 to 15: product renders, storefront images and image quality, public release, authorship and signing), `.kit/cards.py`, `.kit/image_qc.py`, `.kit/release_gate.py`, issue templates, and the `/render-product` and `/release` commands. `CLAUDE.md` now matches `.kit/CLAUDE.md`.
- Every `media/render-*.png` recaptioned from its original render with the new layout: the title, concept label and repository sit in a band above the render and the view note in a band below it, each line wrapped to the image width, so no text overlaps other text or the render or runs off the image. `media/card.png` and `media/social-preview.png` regenerated with the same rules.
- `python .kit/image_qc.py` and `python .kit/release_gate.py` pass. trl stays 3.

## 2026-10-02: photoreal renders redone on the constructable design

Rendered with Blender Cycles on Amish's Mac from the updated appearance model; captioned with `.kit/photo_caption.py`; `media/card.png` and `media/social-preview.png` regenerated with `.kit/cards.py`. Views: hero, exploded, lineup, gate-open. image_qc passes. Appearance deviations are those logged above as proposed, awaiting Amish.
