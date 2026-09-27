---
doc_id: PPR-DDR-003
title: PotPress guarded version
project: PotPress
doc_type: Design decision record
version: "0.1"
status: Draft
date: '2026-09-26'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-09-26'
  author: Amish Chadha
  change: Guarded version (decided by Amish 2026-09-26)
---

# 0003: Guarded version

- **Date:** 2026-09-26
- **Status:** accepted (the guarded version, decided by Amish on 2026-09-26); the cost overrun it causes is proposed, awaiting Amish

## Context

Until now the press was modeled and rendered without its mesh guards and front gate. They were a $55 allowance in BOM item 16, R9 was at risk because they were not designed, and the 2026-09-26 product render session (`docs/REVIEW.md`) flagged that renders without them suggest the press runs unguarded. On 2026-09-26 Amish wrote: "for pot press build a guarded version and make sure the render follows." The press therefore gets guards at TRL 3 concept level, and the design model, drawing, concept media and product renders show them. No existing part or main dimension changes. TRL 4 remains on hold.

## Options considered

How to stop the jack being pumped while hands can reach the pinch zone between the molds, platen and carriage:

1. **Fixed mesh guards and an interlocked front gate (chosen).** Welded mesh on the sides, back and roof; a hinged front gate for loading and demolding; a mechanical guard-locking interlock on the jack release valve. A hand-pumped bottle jack builds pressure only while its release valve is closed, so locking the valve open is a reliable way to make pumping do nothing. The same lock bar keeps the gate shut while the valve is closed, and the decided pin-presence plunger (PPR-DDR-001 item 13) acts on it too. No electrics, no power supply, and it can be built in a local fabrication shop.
2. **Two-hand control.** Needs two actuators held at once, but the jack is worked by one pump lever. It would mean a second lever, a valve linkage or a powered pump, which adds cost and parts. It also protects only the operator, not a second person loading the carriage.
3. **Hold-to-run only.** A hand pump already is hold-to-run: the platen moves only while the lever is pumped. But the other hand is free to reach the molds, and the platen falls under its own weight when the release is opened, so hold-to-run alone does not keep hands out.
4. **Electrical interlock switch.** A standard tongue switch would need a powered valve or pump to act on. The press has no power, so a switch would have nothing to switch.

## Decision

Option 1, as modeled in `cad/src/model.py` and priced in `bom/bom.csv`:

- **Fixed guards (BOM 16):** galvanized welded mesh 12.7 x 12.7 x 1.6 mm (1/2 in, about 11 mm clear) on 25 x 25 x 3 angle frames: both sides (mesh planes at ±470 mm), back (+325 mm), two front strips and a lower front panel (-350 mm), and a roof around the top beam. Standoffs tie the panels to the beams. The pump handle works through a framed 25 mm slot with a brush strip in the right side guard, below the platen.
- **Front gate (BOM 20):** 532 x 1,063 mm, 20 x 20 x 2 tube frame with the same mesh, two lift-off hinges on the left front post, opening outward. The 540 mm opening clears the carriage, molds and rail extension, and the extension cannot be deployed with the gate shut.
- **Gate interlock (BOM 21):** spring-loaded locking bolt on the right front post, engaged by a striker on the gate, linked to a blocking cam on a jack release extension rod whose T-handle sits outside the lower front panel. Gate open: the release cannot be closed, so the jack cannot build pressure. Release closed: the gate cannot be opened.
- **Guard openings (stated assumption):** the nearest moving parts are about 105 mm behind the rear mesh (platen deck), 109 mm behind the side mesh (platen sleeves) and 110 mm behind the front mesh (carriage handle). ISO 13857, on safety distances to prevent hazard zones being reached by the upper and lower limbs, is the reference. Its tables were not checked in this session, so the adequacy of the 11 mm opening at these distances, of the 25 mm pump slot and of the roof height is an assumption to be checked. If the standard asks for more, use finer mesh or move the panels out.

## Consequences

- **R9** moves from at risk to met on paper, with the ISO 13857 check open.
- **R11:** the guarded press is 940 x 700 mm with the rail extension folded, exactly at the 0.7 m depth limit (840 x 655 mm unguarded). There is no margin.
- **Mass:** about 45 kg of guards (estimate); no guard panel is heavier than about 10 kg. The press frame masses and the tipping figure in PPR-CAL-001 do not include the guards.
- **R10:** the guards, gate and interlock cost $122 in place of the $55 allowance, so the BOM rises by $67 from $984 to $1,051, which is $61 (6.2 %) over the $990 budget. The budget was not changed. **Proposed, awaiting Amish:** (a) raise `budget_usd` to about $1,060, since the guards are a safety requirement (recommended); (b) cost the QC rack ($81) outside the press budget, which brings the press to $970 against $990; (c) keep $990 and record R10 as not met.
- The mesh is drawn at every eighth wire (101.6 mm) in the design model, drawing and concept media, and wire by wire in the appearance model.
- PPR-DWG-001 moves to Rev P3; PPR-PRC-001 and PPR-REQ-001 move to v0.6.

> **Safety:** Guards and interlocks reduce but do not remove the crushing hazard of a 20 t press. Never remove a guard or defeat the interlock, inspect both before each shift, and have a competent person check the guard openings against ISO 13857 before any use.
