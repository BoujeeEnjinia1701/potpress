---
doc_id: PPR-DDR-001
title: PotPress TRL 2 review decisions
project: PotPress
doc_type: Design decision record
version: "0.2"
status: Draft
date: '2026-09-25'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-09-25'
  author: Amish Chadha
  change: Record Amish's 2026-09-25 decisions on the TRL 2 review and the items that remain open
- version: "0.2"
  date: '2026-09-25'
  author: Amish Chadha
  change: Recommendations accepted by Amish (DDR-002); items 10 to 15 decided, item 9 still open
---

# 0001: TRL 2 review decisions

- **Date:** 2026-09-25
- **Status:** accepted (items 1 to 8 and, by PPR-DDR-002, items 10 to 15); item 9 remains proposed, awaiting Amish

## Context

The TRL 2 review note (`docs/REVIEW.md`, session 2026-09-25, /populate) listed nine items as "Proposed, awaiting Amish". On 2026-09-25 Amish reviewed the review points for every portfolio repo and wrote: "proceed with all of your recommendations across all batches. Make sure we don't proceed to TRL 4 on any of them." The same instruction set a portfolio rule that community designs pick co-design partners per area later, so partner choices stay open. PotPress does not use SwapCell, so the SwapCell interface items do not apply.

This record lists what that instruction decides and what it leaves open. Later on 2026-09-25 Amish wrote: "i accept all your recommendations, go with them across all repos." Items 10 to 15 are therefore decided as recommended; PPR-DDR-002 records that decision and what it changed. TRL 4 is on hold by Amish's instruction.

## Options considered

The options for items 1 to 9 are set out in the TRL 2 review note and in PPR-PRC-001 v0.2, "Key design choices". Items 10 to 15 come from the TRL 3 calculations (PPR-CAL-001) and are listed below with their options.

## Decision

*Table 1. Items decided by Amish on 2026-09-25.*

| # | Item | Decision |
| --- | --- | --- |
| 1 | Architecture | Decided by Amish, 2026-09-25: go with recommendation. A bottle jack on the base lifts the platen and female mold against a fixed male mold. |
| 2 | Male mold lift | Decided by Amish, 2026-09-25: go with recommendation. Hand crank and lead screw lift the male mold; a load pin carries the press force; standard 20 t bottle jack. |
| 3 | Mold material | Decided by Amish, 2026-09-25: go with recommendation. Molds cast in aluminum from 3D-printed patterns. The fiber-reinforced concrete backed variant stays documented as a low-cost alternative; building it for comparison is TRL 4 work and is on hold. |
| 4 | Frame | Decided by Amish, 2026-09-25: go with recommendation. Welded frame; a bolted variant to be documented later (see item 12). |
| 5 | Demolding | Decided by Amish, 2026-09-25: go with recommendation. The carriage slides out and tilts to turn the pot onto a board. |
| 6 | QC | Decided by Amish, 2026-09-25: go with recommendation. Manual rack with printed T-gauges; a load-cell logger stays a later option. |
| 7 | Default acceptance band | Decided by Amish, 2026-09-25: go with recommendation. 1.0 to 2.5 L/h in the first hour, corrected to 25 °C, adjustable per factory. |
| 8 | Budget | Decided by Amish, 2026-09-25: go with recommendation (a). `budget_usd` raised from $600 to $720 in `project.yaml`; R10 target is now $720. |

*Table 2. Item that remains open, "Proposed, awaiting Amish".*

| # | Item | Options | Recommendation |
| --- | --- | --- | --- |
| 9 | First co-design partner | Existing Potters for Peace network factory; NGO planning a new factory; university ceramics lab | Left open under the portfolio rule that partners are picked per area later. The TRL 2 preference for an existing factory is noted, not decided. |

*Table 3. TRL 3 items decided by Amish on 2026-09-25 (PPR-DDR-002).*

| # | Item | Options | Decision |
| --- | --- | --- | --- |
| 10 | R3 deflection target | (a) keep "under 1 mm at 294 kN" (not met: 1.8 mm); (b) "under 1 mm at the 10 t maximum working force", with the molds closing on a metal stop so frame stretch does not set the wall (met: 0.6 mm); (c) stiffen to 2 x UPN 200 beams (1.34 mm at 294 kN, still not met, about 22 kg and $30 more) | Decided by Amish, 2026-09-25: go with recommendation (b) |
| 11 | R11 QC rack area | (a) keep 0.8 x 0.5 m (four 345 mm rims cannot fit); (b) 0.8 x 0.8 m for a 2 x 2 rack as modeled, with a hinged front rail extension for the press depth; (c) single row 1.5 x 0.45 m | Decided by Amish, 2026-09-25: go with recommendation (b) |
| 12 | Frame joints | (a) fully welded (finished frame about 147 kg); (b) welded subassemblies bolted at the four upright joints with 4 x M20 8.8 bolts each (75 MPa at 294 kN), so no part over 40 kg | Decided by Amish, 2026-09-25: go with recommendation (b) |
| 13 | Load pin | (a) one 60 mm 42CrMo4 pin with a pin-presence interlock, as modeled; (b) two pins at two stations in a taller beam; the TRL 2 pair of 30 mm pins fails in bending (about 1,030 MPa at 294 kN) | Decided by Amish, 2026-09-25: go with recommendation (a) |
| 14 | Cost gap | BOM was $926 against $720: (a) raise `budget_usd` to about $930; (b) cost the QC rack ($81) outside the press budget and build the concrete-backed molds first (press about $730); (c) keep $720 and record R10 as not met | Decided by Amish, 2026-09-25: go with recommendation (a); `budget_usd` is $930 |
| 15 | Scrap aluminum specification | (a) require lead-free scrap (for example cast wheels or pistons, no free-machining bar); (b) buy new A356 ingot at about $1 to $2/kg more | Decided by Amish, 2026-09-25: go with recommendation (a) |

## Consequences

- PPR-PRC-001, PPR-REQ-001 and PPR-PRB-001 move to v0.3 with these decisions; the design choices in items 1 to 8 are no longer marked proposed.
- R10 is judged against $720; the priced BOM is $926, so R10 is not met (PPR-CAL-001).
- Items 10 to 15, decided later on 2026-09-25, are applied in PPR-DDR-002: bolted upright joints and a hinged rail extension in the model, the requirement changes in PPR-REQ-001 v0.4 and `budget_usd` of $930. The model already showed the single 60 mm pin (item 13) because the TRL 2 pins fail by calculation.
- No TRL 4 work (test articles, build procedures, purchasing lists, test plans) follows from this record.
