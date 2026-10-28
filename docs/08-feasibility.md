---
doc_id: PPR-FEA-001
title: PotPress feasibility assessment
project: PotPress
doc_type: Feasibility
version: '0.3'
status: Draft
date: '2026-10-25'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: '0.1'
  date: '2026-10-23'
  author: Amish Chadha
  change: First assessment (kit 1.8 upgrade)
- version: '0.2'
  date: '2026-10-23'
  author: Amish Chadha
  change: Updated for the STEM check fixes (PPR-DDR-006)
- version: '0.3'
  date: '2026-10-25'
  author: Amish Chadha
  change: 'Working force limit 5.4 t (D9, decided by Amish 2026-10-25)'
---

# PotPress feasibility assessment

PotPress is feasible on paper: the structure, hydraulics and guarding pass their checks, and the open items are process knowledge (forming force, clay shrinkage) and local supply (a foundry, a true 250 mm printer) that only a partner factory can settle. Method: STANDARDS section 23.

Table 1. Feasibility by aspect.

| Aspect | Assessment | Rating | Risks and notes | Evidence |
| --- | --- | --- | --- | --- |
| Design | Frame, pin and bolts carry 1.5 times the 20 t jack without yield; 0.66 mm deflection at 10 t; molds close on a metal stop | High | Forming force unknown until trials (decided 2026-10-02), capped at 5.4 t by the handle (D9, 2026-10-25); clay shrinkage now in the mold size at an assumed 8 %, to be measured (PPR-DDR-006) | PPR-STM-001, PPR-CAL-001 |
| Materials | S275 channel and plate, grade 10.9 bolts, cast aluminium molds, polyethylene liners | Medium | A356 wheel scrap sorted and each melt checked (PPR-DDR-006); foundry OES or XRF availability to assess; casting porosity on mold faces | PPR-CAL-001, BOM |
| Manufacturing and assembly | Stick welding, drilling and bolting; 16 printed pattern segments; molds hand-finished to templates | Medium | Wall evenness depends on hand finishing (PR-002 at risk); patterns need a true 250 x 250 mm bed (PR-007 at risk); parts over 25 kg go on a chain block (PPR-DDR-006) | PPR-BLD-001 |
| Power and controls | Hand-pumped hydraulics; no mains power; mechanical interlocks | High | Working force limited to 5.4 t by the 150 N handle limit with 85 % pump efficiency (D9, decided 2026-10-25); more needs a separate pump (D6, open) | PPR-STM-001 S8 |
| Supply of parts | Steel, bottle jacks and hardware in most regional towns; aluminium casting may need a city foundry | Medium | Foundry access is the first partner question (PRB open questions) | BOM, PPR-PRB-001 |
| Cost | Priced BOM $1,279 against the $1,060 value-engineering target | Medium | $219 over; the lifting set ($66) can be hired; savings listed in PPR-DEC-001 | BOM, PPR-PRS-001 PR-010 |

Ratings: High, Medium, Low.
