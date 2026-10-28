---
doc_id: PPR-DDR-005
title: PotPress concept selection
project: PotPress
doc_type: Design decision record
version: '0.3'
status: Draft
date: '2026-10-25'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: '0.1'
  date: '2026-10-23'
  author: Amish Chadha
  change: Concept selection after the kit 1.8 concept options; proposed, awaiting Amish
- version: '0.2'
  date: '2026-10-23'
  author: Amish Chadha
  change: Option A figures updated for the STEM check fixes (PPR-DDR-006); still proposed, awaiting Amish
- version: '0.3'
  date: '2026-10-25'
  author: Amish Chadha
  change: 'Decided by Amish (2026-10-25, "i concur with your recommendations"): option A'
---

# 0005: Concept selection

- **Date:** 2026-10-23
- **Status:** decided by Amish, 2026-10-25: option A

## Context

Kit 1.8 asks every design to compare at least two working principles before it commits (STANDARDS section 21). PotPress was designed before kit 1.8 as a hydraulic bottle-jack press, so that design is option A and is not changed without Amish's go. The comparison is in PPR-OPT-001; the STEM check is PPR-STM-001.

## Options considered

1. **Option A, hydraulic bottle-jack press (current design).** Weighted score 125 of 160. Force set by the operator, up to the 6.4 t working limit of the pump handle (20 t jack); 5.2 min cycle; $1,279 priced BOM.
2. **Option B, toggle (scissor) lever press.** Score 112. Fast and oil-free, but the force at the stop is set by the clay charge: about 0.2 t 30 mm before the links straighten, 2 t at 0.35 mm.
3. **Option C, power-screw press with capstan.** Score 104. Self-locking, but about 3.6 t with two people and about 43 turns over a 300 mm opening; the screw and nut need a lathe or an import.

## Decision

Decided by Amish on 2026-10-25 ("i concur with your recommendations"): keep option A, as recommended. A is 10.4 % ahead of B, just over the 10 % line at which both would go to Amish without a pick. The deciding reason is that the working force is still unknown until pressing trials (decided 2026-10-02), and only A lets the operator set it. Reopen B if trials show the clay forms fully at under about 0.5 t.

## Consequences

- Accepted on 2026-10-25: no design change. The runner-up's best idea, a quick approach before the jack takes the load, goes to the value-engineering list as a suggestion.
- If Amish picks B or C instead: a redesign of the force path, frame top and interlocks, and a new CAL, build plan and BOM; the molds, guard layout and QC rack carry over.
