---
doc_id: PPR-OPT-001
title: PotPress concept options
project: PotPress
doc_type: Concept options
version: '0.4'
status: Draft
date: '2026-10-25'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: '0.1'
  date: '2026-10-23'
  author: Amish Chadha
  change: Three options scored against the user requirements (kit 1.8 upgrade); option A recommended, awaiting Amish
- version: '0.2'
  date: '2026-10-23'
  author: Amish Chadha
  change: Option A figures updated for the STEM check fixes (PPR-DDR-006); B and C estimates carry the same mold and lifting changes; scores unchanged
- version: '0.3'
  date: '2026-10-24'
  author: Amish Chadha
  change: 'Kit 1.9.1: every option modelled at detail level D3 in cad/src/model.py; part counts and model masses added; B and C force figures restated from their detailed models (STEM rows OB1 to OC3); scores and recommendation unchanged'
- version: '0.4'
  date: '2026-10-25'
  author: Amish Chadha
  change: 'D1 decided by Amish (2026-10-25): option A; option A force and effort at the 5.4 t working limit of D9'
---

# PotPress concept options

Recommendation: keep option A, the hydraulic bottle-jack press, which scores 125 of 160 against 112 for option B and 104 for option C (10 % ahead of the runner-up). Amish decided D1 on 2026-10-25 as recommended: "i concur with your recommendations" (PPR-DEC-001, PPR-DDR-005). `concept_chosen` is A. Method: STANDARDS section 21. PotPress was designed before kit 1.8, so the current design is option A and nothing here changes it without Amish's go.

![PotPress concept options side by side at one scale](../media/options.png)

*Figure 1. The three options side by side at one scale, each with a 1.75 m person (`python .kit/options.py`). From kit 1.9 the picture is a Blender Cycles render of each option's detailed model, `components(option)` in `cad/src/model.py`; the coordinator re-renders it from the D3 models of 2026-10-24.*

Every option is modelled at detail level D3 (STANDARDS section 24; `cad/fidelity.json`, passed 2026-10-24): real UPN, SHS, plate and bar stock, every ISO bolt, nut, washer, stud, dowel and pin in its hole, weld beads, bushes and edge breaks. Option A is the constructable design part by part; options B and C are in `cad/src/options_bc.py` and share A's mold set, rails, carriage, pressed pot and QC rack, moved to their place. The mesh guard of A applies to all three but is drawn on A only, so the mechanisms of B and C can be seen.

## The options

All three press the same reference filter between the same cast aluminium molds, close on the same metal stop, sit inside the same guard and use the same QC rack. They differ only in how the pressing force is made.

### Option A: hydraulic bottle-jack press (current design)

A 20 t hand-pumped bottle jack lifts the platen and female mold onto a fixed male mold in a bolted steel channel frame. The operator sets the force by pumping and releases it with the valve. First-order numbers come from PPR-CAL-001 v0.11: priced BOM $1,279, press mass 352 kg, 5.2 min cycle, 69 pots per 6 h, handle force about 55 N at 2 t and 148 N at the 5.4 t working force limit with 85 % pump efficiency (STEM check S8, PPR-DDR-006, D9 decided 2026-10-25). Key risks: handle effort above about 6 t, jack side load if the platen guides bind (PPR-RSK-001), oil on the molds if the jack leaks. A co-design partner confirms the working force in trials, starting near 2 t.

### Option B: toggle (scissor) lever press

A 1.1 m hand lever, rigid with the upper link, turns a toggle of two 400 mm links about its top pin; the knee drives a guided crosshead that carries the male mold down onto the female mold, which sits on a bed plate on the base beam. A toggle's force rises steeply as its links straighten: with 300 N at the lever the detailed model gives about 0.16 t 30 mm before the links are straight, 0.5 t at 3 mm, 1.4 t at 0.35 mm and 7 t at 0.014 mm (STEM row OB1; the kit 1.8 estimate was about 40 % high). Scissor presses of this kind are used by Potters Without Borders. It is fast (one lever stroke) and needs no hydraulics, but the force at the stop depends on the clay charge, not on the operator. A heavy charge stalls the links before they straighten or loads them past the frame rating; a light one closes on the stop with little consolidation. Key risks: wall evenness, kick-back of the lever, and an overcharge that loads the links past the frame rating, since the operator does not bound the force; a shear pin or spring stop would be needed. The detailed model uses 40 mm clevis pins in bronze bushes and 80 mm links, sized after the independent review found the 30 mm pins first drawn near 510 MPa in bending (STEM rows OB3 and OB4). A partner would need to show that their clay forms fully at under about 0.5 t.

### Option C: power-screw press with capstan

A hand-turned four-bar capstan drives a 40 mm trapezoidal-thread screw (Tr40 x 7) through a flanged bronze nut in the crown; the screw pushes the crosshead and male mold down through a thrust ball bearing. Taking a thread friction coefficient of 0.15, two people pulling 300 N each at a 450 mm radius give about 6.7 t with the thrust bearing of the detailed model (STEM row OC1), or about 3.6 t with a plain collar; one person about half that. The screw is self-locking, so it holds any position. It is slow, about 43 turns over a 300 mm opening, unless a fast-approach nut or a two-start thread is added. Key risks: throughput, screw and nut wear, and a specialist part that needs a lathe or an import. The screw does not buckle at 1.5 times 10 t over its open free length (STEM row OC4); the static rating of the thrust bearing at the two-person force is to assess. A partner would need a machine shop.

## First-order numbers

Table 1. Options compared (A from PPR-CAL-001; B and C are first-order estimates; part counts and masses from `cad/fidelity.json`, 2026-10-24. Model masses take every part at its material density, so the bottle jack drawn as a solid steel envelope reads heavier than the 13 kg jack PPR-CAL-001 uses, and they include the 2 x 2 QC rack).

| Quantity | Option A | Option B | Option C |
| --- | --- | --- | --- |
| Estimated parts cost (USD) | 1,279 (priced BOM) | About 1,290 | About 1,340 |
| Mass (kg) | 352 | About 310 | About 340 |
| Force available | 0 to 5.4 t by the handle limit (20 t jack), set by the operator | Rises from 0.16 t to 7 t over the last 30 mm, set by the charge | Up to about 6.7 t with two people (thrust bearing) |
| Cycle and output | 5.2 min, 69 pots per 6 h | About 4 min estimated | Several minutes for the screw travel alone; under 50 pots per 6 h without a fast approach |
| Effort | 55 N at 2 t, 148 N at the 5.4 t limit at the pump handle (85 % efficiency) | 300 N at the lever end | 300 N per person at the capstan rim |
| Parts count (BOM lines) | 21 | About 21 | About 22 |
| Detailed model, D3 (parts; fasteners; welds) | 301; 186; 35 | 267; 164; 26 | 261; 171; 22 |
| Model mass, press with QC rack, no guard on B and C (kg) | 466.4 | 466.2 | 420.7 |
| STEM check | Pass after the four fixes (PPR-STM-001 v0.2) | Within known science; force depends on charge | Within known science; force limited by hand torque |

## Scoring

Table 2. Weighted scoring (weights: High UR 3, Medium 2, Low 1; scores 1 to 5).

| Criterion | Source | Weight | A | B | C | Reason |
| --- | --- | --- | --- | --- | --- | --- |
| Forms the reference filter | UR-001 | 3 | 5 | 4 | 5 | All three close the same molds on a stop. B only reaches high force in the last fraction of a millimetre, so a full-depth press relies on the clay flowing at under 0.4 t |
| Even walls pot to pot | UR-002 | 3 | 4 | 2 | 4 | A and C set force by the operator and close on the stop. In B, force rises from 0.2 t to 10 t over the last 30 mm, so a charge a few percent heavy stalls short of the stop or overloads the links |
| 50 or more filters a day | UR-003 | 3 | 4 | 5 | 2 | A: 5.2 min cycle (PPR-CAL-001). B: one lever stroke, about 4 min estimated. C: a Tr40 x 7 screw needs about 43 turns each way over 300 mm, several minutes a cycle |
| Frame built and repaired locally | UR-004 | 3 | 4 | 4 | 2 | A and B: channel, plate, pins and bolts. C needs a 40 mm square-thread screw and bronze nut, which need a lathe or an import |
| Molds made locally | UR-005 | 2 | 3 | 3 | 3 | Same cast molds in all three |
| Two people can handle every part | UR-006 | 2 | 3 | 3 | 3 | Similar frame parts; the platen and female mold set the heaviest lift in all three; all need the chain block (PPR-DDR-006) |
| Operators cannot reach pinch points under force | UR-007 | 3 | 4 | 2 | 4 | A and C move slowly and hold position. B stores energy in the lever and links, can kick back if the charge is heavy, and moves the lever through the operator's space |
| Flow test of every fired filter | UR-008 | 3 | 4 | 4 | 4 | Same QC rack in all three |
| Affordable against the value-engineering target | UR-009 | 3 | 3 | 3 | 2 | Estimates: A $1,279 (priced BOM), B about $1,290, C about $1,340 (plus or minus 20 %), each with the shrinkage-scaled molds and lifting set; all over the $1,060 target |
| Fits an existing workshop | UR-010 | 1 | 4 | 3 | 3 | B's 1.1 m lever swings outside the guard; C's 0.9 m capstan sits at head height |
| Nothing harmful reaches the clay or water | UR-011 | 3 | 4 | 5 | 4 | A has jack oil and C has screw grease near the molds; B has neither |
| Repeatable settings for lab studies | UR-012 | 1 | 5 | 2 | 4 | A's force can be read with a pressure gauge on the jack; C by torque; B's force depends on charge mass |
| Wear parts from local markets | UR-013 | 2 | 4 | 4 | 2 | Bottle jacks are sold in every hardware market; B uses pins and bushes; C's screw and nut wear and are specialist parts |
| **Weighted total** | | | **125** | **112** | **104** | Out of 160 |

## Recommendation

Keep option A. It is the only option whose pressing force is set by the operator rather than by the charge or by hand torque, and the working force is still unknown until trials with a partner factory (decided 2026-10-02). Option B is ahead on speed and has no oil near the molds. Its best idea to graft onto A is a quick-approach move before the jack takes the load, which would cut the pumping time. Option C's best idea is self-locking: A already holds pressure on the jack's check valve. B or C is worth reopening only if pressing trials show the clay forms fully at under about 0.5 t (B) or 3 t (C). The margin is 10.4 %, only just over the 10 % line in STANDARDS section 21, so a single recommendation went to Amish as D1 with option B named as a close runner-up. **Decided by Amish, 2026-10-25: option A** ("i concur with your recommendations").

## Safety

All three options are pressing machines with crush and pinch hazards at the molds. The guard, gate interlock and pin interlock of PPR-DDR-003 apply to each. Option B adds stored energy in the lever and links; option C adds a rotating capstan at head height.
