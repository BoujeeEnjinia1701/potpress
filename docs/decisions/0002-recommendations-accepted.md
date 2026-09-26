---
doc_id: PPR-DDR-002
title: PotPress recommendations accepted
project: PotPress
doc_type: Design decision record
version: "0.1"
status: Draft
date: '2026-09-25'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-09-25'
  author: Amish Chadha
  change: Recommendations accepted by Amish (DDR-002); record the newly decided items, what changed in the repo and the items still open
---

# 0002: Recommendations accepted

- **Date:** 2026-09-25
- **Status:** accepted (items 10 to 15 of PPR-DDR-001); item 9 and new item 16 remain proposed, awaiting Amish

## Context

After the TRL 3 session, PPR-DDR-001 and the review note (`docs/REVIEW.md`) listed six items with a recommendation that were "Proposed, awaiting Amish" (items 10 to 15) and one with no recommendation (item 9, the first co-design partner). On 2026-09-25 Amish wrote: "i accept all your recommendations, go with them across all repos." Every item that has a recommendation is therefore decided as recommended; where the recommendation named one of several options, that option is the decision. Items without a recommendation stay open. TRL 4 remains on hold by Amish's instruction, and `trl` and `trl_target` stay at 3.

## Options considered

The options for items 10 to 15 are set out in PPR-DDR-001, Table 3, and in PPR-CAL-001.

## Decision

*Table 1. Items decided by Amish on 2026-09-25: go with recommendation.*

| # | Item | Decision | What changed in the repo |
| --- | --- | --- | --- |
| 10 | R3 deflection target | (b) deflection under 1 mm at the 10 t maximum working force, with the molds closing on a metal stop | R3 text restated in PPR-REQ-001 v0.4; the model already has the stop face outside the flash groove. R3 moves from not met (1.84 mm at 294 kN) to met on paper (0.61 mm at 10 t). Strength is still checked at 294 kN. |
| 11 | R11 QC rack area | (b) 0.8 x 0.8 m for the 2 x 2 rack, with a hinged front rail extension for the press depth | R11 text relaxed. Rails now fixed to 320 mm in front of the axis with a 330 mm extension on two barrel hinges and stop lugs (`RAIL_HINGE`, `EXT_FOLDED` in `cad/src/model.py`); BOM item 7 from $34 to $45. Press depth 970 mm to 655 mm with the extension folded; rack 780 x 780 mm fits. R11 moves from not met to met on paper. |
| 12 | Frame joints | (b) welded subassemblies bolted at the four upright joints, 4 x M20 8.8 each | 16 M20 bolts added to the model (`JOINT_BOLT_*`); BOM item 2 from $38.50 to $62.00 each ($77 to $124); bolt shear 75 MPa and bearing 123 MPa (beam web) and 108 MPa (upright flange) at 294 kN in PPR-CAL-001 v0.2. Largest frame part 37.4 kg; R8 moves from at risk to met on paper. |
| 13 | Load pin | (a) one 60 mm 42CrMo4 pin with a pin-presence interlock | Already modeled. BOM item 16 now specifies a mechanical pin-presence interlock on the jack release valve; R9 text updated. R9 stays at risk because guards and interlocks are not modeled. |
| 14 | Cost gap | (a) raise `budget_usd` to about $930 | `budget_usd` from $720 to $930 in `project.yaml`; R10 target $930. |
| 15 | Scrap aluminum | (a) lead-free scrap (for example cast wheels or pistons; no free-machining bar) | R12 and the PPR-PRB-001 constraints updated; BOM items 8 and 9 already required it. |

The decided bolted joints and rail hinges add $58, so the priced BOM rises from $926 to $984 and is $54 (6 %) over the new $930 budget. R10 remains not met.

*Table 2. Items still open, "Proposed, awaiting Amish".*

| # | Item | Options | Recommendation |
| --- | --- | --- | --- |
| 9 | First co-design partner | Existing Potters for Peace network factory; NGO planning a new factory; university ceramics lab | None; left open under the portfolio rule that partners are picked per area later |
| 16 | Remaining cost gap ($984 against $930) | (a) raise `budget_usd` to about $990; (b) cost the QC rack ($81) outside the press budget, leaving the press at $903 within $930; (c) keep $930 and record R10 as not met | (a), because the added cost is the bolted joints and hinges that Amish has just decided on for handling and footprint |

## Consequences

- PPR-PRB-001 v0.4, PPR-PRC-001 v0.4, PPR-REQ-001 v0.4, PPR-CAL-001 v0.2 and PPR-DDR-001 v0.2 carry these decisions.
- `cad/src/model.py` adds the joint bolts and the hinged rail extension; STEP and STL files are re-exported; the general arrangement PPR-DWG-001 moves from Rev P1 to Rev P2.
- Requirement status at TRL 3: 1 not met (R10), 3 at risk (R2, R7, R9), 8 met on paper (R1, R3, R4, R5, R6, R8, R11, R12).
- No cross-repo actions arise from these decisions.
- Nothing here starts TRL 4 work. The proof load test, measured deflection, bolt torque checks and any purchasing stay on hold by Amish's instruction.
