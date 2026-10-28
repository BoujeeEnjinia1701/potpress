---
doc_id: PPR-RSK-001
title: PotPress risk register and hazard analysis
project: PotPress
doc_type: Risk register
version: '0.3'
status: Draft
date: '2026-10-25'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: '0.1'
  date: '2026-10-23'
  author: Amish Chadha
  change: First risk register, hazard analysis and design FMEA (kit 1.8 upgrade), including the four risks the independent STEM review found
- version: '0.2'
  date: '2026-10-23'
  author: Amish Chadha
  change: Hazards and risks updated for the STEM check fixes (PPR-DDR-006); eye bolt hazard H11 added
- version: '0.3'
  date: '2026-10-25'
  author: Amish Chadha
  change: 'P2 and H10 at the 5.4 t working force limit decided by Amish (D9, 2026-10-25)'
---

# PotPress risk register and hazard analysis

The top project risk is that the forming force and clay shrinkage are unknown until pressing trials with a partner, which could change the mold size and the operator effort. The top hazard is crushing at the molds, controlled by the fixed guards and the two interlocks; the highest design FMEA scores are charge mass against the stop and side load on the jack. Method: STANDARDS section 23 and ISO 12100. Likelihood, impact, severity and occurrence are scored 1 (low) to 5 (high); detection 1 (certain to be caught) to 5 (unlikely to be caught).

## Project risk register

Table 1. Project risks.

| # | Risk | Cause | Effect | Likelihood | Impact | Owner (role) | Response |
| --- | --- | --- | --- | --- | --- | --- | --- |
| P1 | No partner factory | Partners are picked per area later (PRB open questions) | Requirements stay unvalidated; no TRL 4 | 3 | 5 | Amish | Keep the design at TRL 3; approach a network factory when TRL 4 opens |
| P2 | Forming force higher than expected | Not published; one press forms at 2 t | Working force capped at 5.4 t by the handle (D9, decided 2026-10-25); cycle time rises | 3 | 3 | Design lead | Trials start near 2 t; separate two-speed pump (D6, proposed, still open) if above 5.4 t |
| P3 | Fired pot size wrong | No clay shrinkage allowance (STEM M6) | Pots do not fit receptacles | 2 | 4 | Design lead | Molds scaled for 8 % assumed shrinkage (PPR-DDR-006); test bar on the partner clay before patterns are printed |
| P4 | No foundry within reach | Aluminium casting is city-based | Molds must be imported or made another way | 3 | 4 | Partner | Ask at partner selection; keep pattern files open for any foundry |
| P5 | Cost stays over target | Guarding and construction details | Weaker case against imported presses | 4 | 2 | Amish | Value-engineering list in PPR-DEC-001 |
| P6 | Guard check not signed | Needs a competent person | No force above hand pressure | 2 | 4 | Amish | Find a signatory with the partner before TRL 4 |

## Preliminary hazard analysis

Table 2. Hazards.

| # | Hazard | Cause | Harm | Severity | Likelihood | Control | Residual |
| --- | --- | --- | --- | --- | --- | --- | --- |
| H1 | Crushing between the molds | Hand in the press while pumping | Crushed hand or fingers | 5 | 2 | Fixed guards to ISO 13857, gate interlock on the release, controls outside the guard | 1 (desk check unsigned) |
| H2 | Shear at the platen guides and carriage | Reaching through the gate gap | Finger injury | 4 | 2 | 6.35 mm mesh on front, gate edge gaps checked | 1 |
| H3 | Load pin not home | Pin left out after a mold change | Male mold slips under load | 5 | 2 | Pin-presence interlock | 1 |
| H4 | Ejected part under load | Bolt or pin failure at 20 t | Impact injury | 5 | 1 | 1.5 times rating without yield; roof guard | 1 |
| H5 | Hydraulic oil release | Seal failure or overpressure | Skin injection, slip, clay contamination | 3 | 2 | Jack's own relief valve; drip tray under the jack (proposed) | 2 |
| H6 | Manual handling of heavy parts | 39.6 kg platen and female mold, 38 kg top beam | Back injury | 3 | 3 | Chain block for every part over 25 kg; eye bolts in the female base plate and male flange; holes plugged before pressing (PPR-DDR-006) | 1 |
| H11 | Eye bolt left in a mold | Mold change not finished | Bolt crushed under the male flange or striking the plug as the carriage slides; ejected fragment | 4 | 2 | Eye bolts out and holes plugged before the press moves (build plan S4); female lift points in the base plate, not the stop face | 1 |
| H7 | Press tipping | Pushed or pulled while unanchored | Crushing | 5 | 1 | Four M12 floor anchors; tipping moment 844 N m checked | 1 |
| H8 | Silica and burnout dust | Dry clay and rice husk ash | Lung disease over years | 4 | 3 | Wet methods, masks; the factory's process (STEM B3) | 2 |
| H9 | Zinc fume | Welding galvanized mesh frames | Metal fume fever | 3 | 2 | Grind off zinc at welds, ventilation (STEM B4) | 1 |
| H10 | Repetitive strain | Pump handle force at high settings | Shoulder and wrist strain | 3 | 3 | Working force limited to 5.4 t (about 148 N with 85 % pump efficiency; D9, decided by Amish 2026-10-25); no handle extensions; EN 1005-3 assessment to do (PPR-DDR-006) | 2 |

## Design FMEA (first pass, P3)

Table 3. Failure modes. RPN = severity x occurrence x detection.

| # | Item | Function | Failure mode | Effect | Cause | S | O | D | RPN | Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F1 | Clay charge | Fill the cavity | Charge too heavy for the stop | Molds do not reach the stop; wall too thick; frame sees full jack force | Charge weighed by eye; mix moisture varies | 4 | 4 | 3 | 48 | Weigh each charge to a tolerance found in trials; add charge tolerance to PR-002 |
| F2 | Bottle jack | Make the force | Side load on the ram | Seal wear, leak, bent ram | Platen guides bind; female mold off centre | 4 | 3 | 3 | 36 | Check guide clearance against jack side-load limit; centre the adapter disc |
| F3 | Floor anchors | Hold the press | Anchor pulls out | Press tips when the carriage is pulled | Weak or cracked floor | 5 | 2 | 3 | 30 | State minimum floor (concrete grade and thickness) in the build plan; pull test at install |
| F4 | QC rack | Measure flow | Falling-head reading taken as steady flow | Wrong accept or reject | Flow falls as the head drops over the hour | 3 | 3 | 3 | 27 | State the head and time the band refers to; same fill height every test |
| F5 | Molds | Set the wall | Cavity off size after casting | Uneven wall; PR-002 not met | Shrink, porosity, template error | 4 | 3 | 2 | 24 | Template check after finishing; print error in the tolerance budget (STEM E2) |
| F6 | Joint bolts | Hold the frame | Loosening under cycles | Frame misaligns | 63 MPa stress range near the 71 MPa fatigue limit (STEM S9) | 4 | 2 | 3 | 24 | Hardened washers, torque marks, retorque at intervals |
| F7 | Gate interlock | Stop pressing with the gate open | Interlock defeated | Hand reaches the molds under force | Operator ties it open | 5 | 2 | 2 | 20 | Assess against ISO 14119 defeat rules (G3) |
| F8 | Return springs | Lower the platen | Spring breaks | Platen stays up; demolding slows | Fatigue, corrosion | 2 | 2 | 1 | 4 | Spares in the kit |
