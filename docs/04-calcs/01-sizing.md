---
doc_id: PPR-CAL-001
title: PotPress sizing and first-principles checks
project: PotPress
doc_type: Calculation note
version: "0.10"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-09-25'
  author: Amish Chadha
  change: First TRL 3 sizing note (geometry, mix, frame and pin, deflection, travel, cycle, alignment, patterns, QC gauge, masses, tipping, cost) against every requirement
- version: "0.2"
  date: '2026-09-25'
  author: Amish Chadha
  change: Recommendations accepted by Amish (DDR-002); bolted upright joints, hinged rail extension, R3 at 10 t, R11 rack 0.8 x 0.8 m, budget $930, cost $984
- version: "0.3"
  date: '2026-09-26'
  author: Amish Chadha
  change: Budget top-up approved by Amish; budget $990, R10 met on paper with a $6 margin
- version: "0.4"
  date: '2026-09-26'
  author: Amish Chadha
  change: Guarded version costs (PPR-DDR-003)
- version: "0.5"
  date: '2026-09-27'
  author: Amish Chadha
  change: Cost overrun decided by Amish on 2026-09-27; budget $1,060, R10 met on paper with a $9 margin
- version: "0.6"
  date: '2026-09-30'
  author: Amish Chadha
  change: Design for construction (PPR-DDR-004); new checks for the male flange on the stop, M16 joints, rails, lead screw float, demolding tilt; masses and costs from the constructable model; R10 not met on paper
- version: "0.7"
  date: '2026-10-01'
  author: Amish Chadha
  change: Budget treated as a value-engineering target; R10 reported against the target
- version: "0.8"
  date: '2026-10-02'
  author: Amish Chadha
  change: 'Decisions of 2026-10-02: R9 status at risk until the pump slot shield is designed; working force as a process setting found in trials'
- version: "0.9"
  date: '2026-10-02'
  author: Amish Chadha
  change: 'Approved follow-ups carried out: mean pressure at 2 t in Table 3; pump slot shield costed; ISO 13857 desk check (section 15); R9 at risk to not met on paper; cost $1,149, $89 over the value-engineering target'
- version: "0.10"
  date: '2026-10-03'
  author: Amish Chadha
  change: 'Four guard fixes decided by Amish (2026-10-03) modelled and costed; desk check rerun for every opening (section 15), all 23 meet on paper; R9 not met to met on paper (check not yet signed); cost $1,169, $109 over the value-engineering target'
---

# PotPress sizing and first-principles checks

On paper the press forms the reference filter, opens far enough, keeps up the output and stays strong at 1.5 times the jack rating, but it is heavier and dearer than the TRL 2 estimates said. With the recommendations Amish accepted on 2026-09-25 (PPR-DDR-002) and the guarded version he decided on 2026-09-26 (PPR-DDR-003), ten of the twelve requirements are met on paper and two are at risk. The value-engineering target stood at $990 on 2026-09-26, which the $984 BOM was within; the fixed guards and interlocked front gate then added $67, and the target was set at $1,060 on 2026-09-27 (PPR-DDR-003), so R10 was within the target at $1,051 with a $9 (0.8 %) margin. Making the design constructable on 2026-09-30 (PPR-DDR-004) added the parts a build needs and raised the parts cost to $1,143, $83 (7.8 %) over the $1,060 value-engineering target, so R10 was over the target by $83; the design decisions register lists the cost drivers and savings worth trying. The fixed inner shield behind the pump slot, decided by Amish on 2026-10-02, adds $6 (now $1,149, $89 over the target), and the ISO 13857 desk check done the same day (section 15) found guard openings that fall short of the standard. Amish decided on 2026-10-03 to make the four guard fixes it proposed and accepted their cost: they add $20 (now $1,169, $109 over the target), and with them every one of the 23 openings in the rerun desk check meets ISO 13857 Table 4 on paper, so R9 is met on paper; the check still has to be signed by a competent person before any force above hand pressure. R3 is now judged at the 10 t working force with the molds closing on a metal stop (0.61 mm), R11 allows 0.8 x 0.8 m for the QC rack and a hinged rail extension keeps the press 655 mm deep, and bolting the four upright joints keeps every part under 40 kg (R8). The calculations also found three TRL 2 errors that the model now corrects: the base beam (a single UPN 100) would have been stressed to about 1,071 MPa, the two 30 mm load pins would have failed in bending (about 1,030 MPa), and solid aluminum molds would have weighed about 57 and 41 kg, so the molds are now cast shells.

Every number in this note is printed by `docs/04-calcs/sizing.py` (run from the repo root: `python docs/04-calcs/sizing.py`). The script reads the geometry from `PARAMS`, `SECTIONS` and `levels()` in `cad/src/model.py`, takes part masses from the model solids, and reads the prices from `bom/bom.csv`, so the model, the drawing PPR-DWG-001, the BOM and this note agree. All values are first-principles estimates; nothing here is measured.

## 1. Assumptions

*Table 1. Inputs. All are assumptions for a paper design unless marked as decided.*

| Input | Value | Basis |
| --- | --- | --- |
| Architecture, lift, molds, frame, demolding, QC, band | As decided | PPR-DDR-001 items 1 to 8 |
| R3 basis, rack area, bolted joints, single pin with interlock, budget $1,060, lead-free scrap | As decided | PPR-DDR-001 items 10 to 15; PPR-DDR-002 (budget topped up to $990 by Amish, 2026-09-26); PPR-DDR-003 (budget raised to $1,060 by Amish, 2026-09-27) |
| Joint bolts and hinges | M20 x 150 grade 8.8 with nut and washers $3.00 each, 16 in all; rail extension hinges and stop lugs $10 | Regional retail estimate |
| Reference filter | Inner rim 280 mm, inner floor 230 mm, inner depth 240 mm, wall 15 mm normal to the surface, flat rim 345 mm x 15 mm | R1; [Potters for Peace](https://www.pottersforpeace.org/ceramic-water-filter-project) form of about 280 by 250 mm |
| Mix | 59 % clay, 16 % rice husk, 25 % water by mass; particle densities 2,600, 1,400 and 1,000 kg/m³; 3 % entrapped air | RDI-C recipe in [Rayner (2009)](https://bdd.pseau.org/outils/ouvrages/wedc_current_practices_in_manufacturing_locally_made_ceramic_pot_filters_2009.pdf); densities typical |
| Process losses | Trim 10 % of pressed mass (recycled); 2 % water left after drying; clay loss on ignition 10 %; 10 % QC rejects | Estimates |
| Working force | 5 to 10 t (49 to 98 kN); design load 1.5 x 20 t = 294 kN | Not sourced; see section 3 |
| Steel | S275, yield 275 MPa, allowable 165 MPa at the jack rating; E = 200 GPa, G = 80 GPa | Standard values |
| Load pin | 42CrMo4 quenched and tempered, yield 650 MPa | Typical for 40 to 100 mm bar |
| Cast aluminum | Al-Si scrap alloy, yield about 90 MPa as cast, density 2,680 kg/m³ | Conservative |
| Welds | E6013, 6 mm fillets, allowable 129 MPa on the throat (0.3 x 430 MPa) | Common stick electrode |
| Jack | 60 mm ram, 16 mm pump piston with 22 mm stroke, lever ratio 30 | Typical 20 t bottle jack; not from a data sheet |
| Casting tolerance | ISO 8062 CT10 for about 400 mm: ±0.8 mm on radius, plus ±0.3 mm print error and ±0.5 mm core shift | Sand casting typical |
| Loose charge | 1.5 kg/L as placed | Estimate |
| Prices (2026) | Steel $1.30/kg; scrap aluminum $2.00/kg, 1.35 kg poured per kg of casting, foundry fee $1.50/kg; PLA $20/kg at 25 % of solid mass | Indicative regional prices |

## 2. Filter geometry and mass

The reference filter holds 12.30 L to the brim and 9.91 L to 40 mm below the rim, which matches R1 and the 9.84 L Cambodian filter. The wall is tapered at 5.9°, so a 15 mm normal wall moves the outer surface 15.1 mm out; the outer floor radius is 128.5 mm and the outer rim radius 155.1 mm, over an outer depth of 255 mm.

*Table 2. Pot geometry and masses.*

| Quantity | Value | Basis |
| --- | --- | --- |
| Wall and rim volume | 4.14 L | Outer frustum minus inner, plus rim ring |
| Mix density | 1.69 kg/L solid; 1.64 kg/L pressed | Rule of mixtures, 3 % air; husk is 19 % by volume |
| Pressed pot | 6.79 kg | 4.14 L x 1.64 kg/L |
| Charge | 7.47 kg | Plus 0.68 kg trim |
| Dried pot | 5.20 kg | Loses 1.60 kg of water |
| Fired pot | 3.61 kg | Loses 1.59 kg (husk burnout, clay loss on ignition, residual water) |
| Passes QC | 3.25 kg per pot made | 0.36 kg rejected at 10 % |

The charge of about 7.5 kg is below the 8 to 9.5 kg that factories report (Rayner, 2009). Either their walls are thicker than 15 mm, their filters are larger, or they trim more. A partner factory's own mold dimensions should replace the reference filter before TRL 4.

## 3. Force and pressure

The pressing force needed for a well-consolidated wall was still not found. Henry, Maley and Mehta (2013) note that the Potters Without Borders press uses a 20 t jack, but their own low-cost press forms round-bottom filters with a 2 t car jack ([Henry, Maley and Mehta, *IJSLE* 8 (1), 2013](https://ojs.library.queensu.ca/index.php/ijsle/article/view/4532)). The working force may therefore be well below the assumed 5 to 10 t. The frame is sized for the full jack rating either way. Decided by Amish on 2026-10-02: every structural check stays at the full 20 t jack, and the working force is a process setting found in pressing trials with a partner factory, starting near 2 t and stepping up.

*Table 3. Mean pressure over the 0.0935 m² projected area of the pot.*

| Force | kN | Mean pressure |
| --- | --- | --- |
| 2 t (start of pressing trials) | 19.6 | 0.21 MPa |
| 5 t | 49.0 | 0.52 MPa |
| 10 t | 98.1 | 1.05 MPa |
| 20 t (rating) | 196.2 | 2.10 MPa |
| 30 t (1.5 x rating) | 294.3 | 3.15 MPa |

Pressing trials start near 2 t, where the mean pressure on the pot is 0.21 MPa, a fifth of the 1.05 MPa at 10 t. That is the starting reference for the trials; the force is then stepped up until the wall is well consolidated.

## 4. Frame and load path

The press force runs from the jack through the platen, the female mold, the pot and the male mold into the stem, across one load pin into the top crossbeam, down both uprights in tension and back through the base beam to the jack. Each beam is two UPN 160 channels with a 104 mm gap between the webs (the 100 mm uprights plus a 2 mm shim each side, PPR-DDR-004); the uprights (two UPN 100 channels back to back, 100 x 100 mm) and the stem sit in that gap. The TRL 2 base was a single UPN 100 (41 cm³); under the same 44 kN·m it would reach about 1,071 MPa, so the base beam now matches the top beam.

*Table 4. Stresses. Beam span 600 mm (upright centers), center load.*

| Item | 10 t | 20 t (rating) | 30 t (design) | Limit |
| --- | --- | --- | --- | --- |
| Beam bending (2 x UPN 160, 232 cm³), top and base | 63 MPa | 127 MPa | 190 MPa | 165 at rating; 275 yield at design |
| Beam web shear | 20 MPa | 41 MPa | 61 MPa | |
| Uprights, tension (2 x 2,700 mm²) | 18 MPa | 36 MPa | 54 MPa | |
| Load pin, 60 mm, bending (arm 39.25 mm) | | 182 MPa | 272 MPa | 650 yield |
| Load pin, shear (double) | | | 52 MPa | |
| Pin bearing on web plus 12 mm doubler | | | 126 MPa (327 MPa without doubler) | |
| Pin bearing on the stem pin block, less its 28 mm lead screw hole | | | 79 MPa | |
| Web tear-out above the pin (38.5 mm ligament) | | | 98 MPa | |
| Stem, SHS 90 x 8, compression | | | 112 MPa | |
| Upright joint welds, welded option (556 mm of 6 mm fillet) | | | 62 MPa | 129 |
| Upright joints as built, 4 x M16 10.9 in double shear per joint (thread in the shear plane) | | | 117 MPa | 400 resistance |
| Joint bolt bearing on beam web (7.5 mm) / upright flange (8.5 mm) | | | 153 / 135 MPa | |
| Male mold flange, 45 mm, with all the force on the stop ring (ring cantilever from the plug at 140 mm radius) | | 41 MPa | 62 MPa | about 90 yield |
| Male plug shell in compression / stop ring bearing / adapter disc on the plug floor | | | 24 / 5.1 / 10.4 MPa | |
| Female steel base plate, 15 mm, across the rails | | 101 MPa | 151 MPa | 275 yield |
| Rails with the 6 mm deck, across the 104 mm gap between the platen webs | | 68 MPa | 101 MPa | 275 yield |
| Platen (2 x UPN 140), rails at ±60 and ±170 mm | | 65 MPa | 98 MPa | |
| Female mold floor (30 mm, span 120 mm) | 13 MPa | 25 MPa | 38 MPa | about 90 yield |
| Male mold tip plate (30 mm, radius 100 mm) | 15 MPa | 29 MPa | 44 MPa | about 90 yield |
| Mold shell hoop, female / male | 8 / 10 MPa | 16 / 20 MPa | 24 / 29 MPa | about 90 yield |

The TRL 2 pair of 30 mm pins passes in shear (104 MPa) but not in bending: with the same web, gap and stem geometry each pin would see about 1,030 MPa. One 60 mm pin in quenched and tempered alloy steel passes with a factor of 2.5 on yield at the design load. It is a single load path, so the guard must include a pin-presence interlock (PPR-DDR-001 item 13, decided by Amish on 2026-09-25).

The mold stresses use the mean pressure; local pressure near the rim, where the clay extrudes, may be higher. Fatigue at about 20,000 cycles a year is not assessed at TRL 3.

### Deflection between the molds

*Table 5. Axial deflection that opens the gap between the molds, mm.*

| Contribution | 10 t | 20 t | 30 t |
| --- | --- | --- | --- |
| Top beam (bending plus shear) | 0.20 | 0.39 | 0.59 |
| Base beam (bending plus shear) | 0.20 | 0.39 | 0.59 |
| Uprights | 0.11 | 0.23 | 0.34 |
| Stem | 0.10 | 0.20 | 0.30 |
| Platen | 0.02 | 0.04 | 0.06 |
| Pin allowance | 0.03 | 0.07 | 0.10 |
| **Total** | **0.66** | **1.31** | **1.97** |

The v0.1 R3 target of less than 1 mm at 294 kN was not met. Shear deflection is about 40 % of each beam's share because the beams are short and deep, so a deeper section helps little: 2 x UPN 200 would still give 1.46 mm for 21.8 kg more steel. The wall thickness does not depend on this deflection if the molds close on a metal stop: the male flange lands on the female stop face outside the flash groove, and the rim thickness is set by the 15 mm counterbore. Amish accepted the recommendation on 2026-09-25 (PPR-DDR-001 item 10, PPR-DDR-002): R3 now judges deflection at the 10 t maximum working force, where it is 0.66 mm (0.61 mm before the stem was lengthened to reach down to the plug floor, PPR-DDR-004), so R3 is met on paper. Strength is still checked at 294 kN.

### Checks added for construction (PPR-DDR-004)

- **Male flange on the stop.** The TRL 3 model's 25 mm flange, loaded at the stop ring and supported by a 180 mm adapter, would have reached about 487 MPa at 294 kN. The constructable plug carries the stem's disc on its floor and the flange as a 45 mm ring cantilevered from the plug wall: 41 MPa at 20 t and 62 MPa at 30 t with all the force on the stop, against about 90 MPa as-cast yield.
- **Joint bolts.** M16 grade 10.9 replaces M20 8.8, which did not fit the UPN 100 flange. The hole centre is 28 mm from the web, 22 mm from the flange tip (EN 1993-1-8 asks 21.6 mm for an 18 mm hole), and the 25 mm spacer tube inside the channel clears the web root radius by 1.0 mm. Double shear is 117 MPa at 30 t against a resistance of 400 MPa.
- **Lead screw.** The captive nut has 8 mm of free travel in its box; the pin has at most 2 mm of play in its bores, so the pin takes the press force before the nut can touch the box floor, and the screw carries only the slide's weight. A 28 mm hole down the pin block lets the fixed screw pass as the stem rises 200 mm; it reduces the pin's bearing length in the block from 90 to 62 mm (79 MPa at 30 t).
- **Demolding tilt.** With the carriage pulled out onto the tipping pins and the mold turned right over, about 51 kg sits 520 mm past the rail hinge: 260 N·m on the hinge, 10.8 kN on each 20 x 30 mm stop lug. Starting the tip needs about 283 N on the two lift handles together. The 12 mm tipping pins see about 180 MPa with a shock factor of 2, so they are bright medium-carbon bar (EN8 or 1045). The press still stands with 654 N·m to spare before the floor anchors are counted.

## 5. Travel, jack and crank

A loose 7.5 kg charge at 1.5 kg/L forms a slug about 90 mm deep in the cavity, so the jack needs about 84 mm of pressing travel (slug depth less the 15 mm floor, plus 10 mm of approach). The model uses 110 mm, leaving 40 mm of the 150 mm jack stroke. To open, the male tip must rise 270 mm relative to the closed position (240 mm plug plus 30 mm clearance, R5); the jack retracts 110 mm and the crank lifts 200 mm, for 310 mm and a 70 mm clearance above the female rim. The female rim sits at 921 mm for loading.

The Tr24 x 5 lead screw needs 40 turns each way. It is self-locking (lead angle about 4° against a friction angle of about 8.5°), so the male mold cannot drop if the crank is released. The screw lifts only the male mold (17.9 kg) and its stem; it never carries the press force.

With the assumed jack, each pump stroke lifts the ram 1.56 mm, so closing takes about 70 strokes. The handle force is about 233 N at 10 t and 465 N at the 20 t rating (hydraulic pressure 69 MPa); the high value is reached only at the end of a stroke and only if the working force really is near the rating.

## 6. Cycle and output

*Table 6. Cycle with two operators.*

| Step | Time |
| --- | --- |
| Load charge and liner, slide carriage in | 60 s |
| Crank male mold down (40 turns at 1.5 turns/s), insert pin | 27 s |
| Pump to close (70 strokes at 1.2 s) | 84 s |
| Dwell | 15 s |
| Release | 10 s |
| Pull pin, crank up | 27 s |
| Slide out, tilt, demold and trim | 90 s |
| **Total** | **313 s (5.2 min)** |

That gives about 69 pots per 6 h of pressing, above the 50 in R4, but the margin rests on the pumping estimate.

## 7. Alignment and wall evenness

The molds locate on two 16 mm hardened dowels in the female flange and two steel bushes in the male flange (PPR-DDR-004; this replaces the 390 mm turned lip, which needed a 420 mm lathe). The holes are drilled with the molds clamped together on printed 15 mm wall spacers, so the dowels hold the setting made with the spacers; the pin in its bush has 0.05 mm of diametral play. The carriage and stem clearances do not set the mold alignment. What remains is the accuracy of each mold's cavity relative to the other.

- As cast, each mold carries about ±0.99 mm radial error (RSS of CT10, print error and core shift), so the wall varies by about ±1.40 mm. R2 (±1 mm) is not met as cast.
- Finished by hand to printed templates at ±0.3 mm, the wall varies by about ±0.44 mm and the molds are coaxial to about ±0.44 mm, inside R2's ±1 mm and 0.5 mm.

R2 is therefore **at risk**: it depends on hand finishing reaching ±0.3 mm on a 400 mm casting without a lathe, which cannot be shown at TRL 3.

## 8. Casting patterns (R7)

With a 1.3 % shrink allowance, the female pattern is 456 mm across by 274 mm tall and the male 456 mm by 289 mm. On a 250 mm printer each splits into four quadrants in two tiers, 16 segments in all, using about 5.4 kg of PLA at 25 % of solid mass. Both are flat-back patterns: each mold's inside opens at the flange face, so the sand forms its own core and no core box is needed (PPR-DDR-004). The patterns carry 3 mm to lap off the stop faces and the female base and 2° draft on the flange rims. No part needs a lathe; the stop faces are lapped on abrasive paper on float glass. Printing is within reach of a maker space; finishing the cast cavity to ±0.3 mm by hand is not proven, so R7 is **at risk**.

## 9. Flow-rate QC

Filled to 10 mm below the rim, the pot holds 11.69 L with a water surface of 0.0607 m².

*Table 7. T-gauge scale.*

| Volume passed in 1 h | Level drop |
| --- | --- |
| 0.1 L | 1.7 mm |
| 1.0 L | 16.7 mm |
| 2.5 L | 42.6 mm |
| 3.0 L | 51.4 mm |

A 0.1 L/h step is 1.69 mm near 1.0 L/h and 1.76 mm near 2.5 L/h, so printed 1 mm ticks resolve it; a 1 mm reading error is 0.061 L. The resolution meets R6; repeatability of ±0.1 L/h depends on how the gauge is read and is to be shown later.

Water viscosity (Vogel equation) is 1.002, 0.890 and 0.797 mPa·s at 20, 25 and 30 °C, so flow changes by about 2.3 % per °C near 25 °C, and water at 30 °C flows 1.26 times as fast as water at 20 °C. To correct to 25 °C, multiply a reading by 1.125 at 20 °C and 0.895 at 30 °C (decided band, PPR-DDR-001 item 7).

Four 345 mm rims need at least 1.46 m in one row, or about 0.78 x 0.78 m in a 2 x 2 grid. The modeled rack is 780 x 780 x 720 mm (pot shelf raised so the hanging pots clear the 325 mm buckets by 35 mm, PPR-DDR-004), inside the 0.8 x 0.8 m that R11 now allows for the rack (decided by Amish, 2026-09-25, PPR-DDR-001 item 11).

## 10. Masses and handling

*Table 8. Masses from the model solids, kg (constructable model, PPR-DDR-004).*

| Item | Mass |
| --- | --- |
| 1 Base beam, feet and jack plate | 58.2 (base beam 34.2, jack plate 8.9, each foot 7.1, plus anchors and bolts) |
| 2 Uprights | 67.4 (29.4 per pair, plus spacer tubes, shims and 5.1 of M16 bolts) |
| 3 Top crossbeam with guides | 39.1 (38.0 as handled) |
| 4 Jack | 13.0 (typical) |
| 5 Platen with sleeves | 39.6 |
| 7 Rails, hinged extension and carriage | 22.0 (rails 9.5, carriage 7.1) |
| 8 Female mold with its steel base plate | 36.5 |
| 9 Male mold | 23.0 |
| 10 Male mold slide and crank | 44.6 (stem 21.9, bracket 13.4, pin 4.5) |
| **Press, items 1 to 10** | **344** |
| 12 QC rack | 30.1 |
| 21 Interlock | 3.9 |
| 16 Pump slot shield (with the guards) | 2.8 |
| 16 Guard fixes (2026-10-03): small-hole plates, top beam cover plates, crank bracket covers (with the guards) | 0.13, 2.71, 1.52 (4.4) |

The TRL 2 estimate of 180 kg was low, and solid molds would have weighed about 77 kg (female) and 52 kg (male); shells bring them to 22 and 23 kg. As fabricated, the heaviest part is the platen at 39.6 kg, inside R8's 40 kg with 0.4 kg to spare. The female mold is lifted as 36.5 kg with its base plate. Fully welded, the frame (items 1 to 3) would be one piece of about 165 kg that two people cannot move. As decided (PPR-DDR-001 item 12), the four upright joints are bolted, now with 4 x M16 10.9 each (PPR-DDR-004), so the frame arrives as a 34.2 kg base beam, an 8.9 kg jack plate, two 7.1 kg feet, two 29.4 kg upright pairs and a 38.0 kg top beam, and R8 is met on paper.

## 11. Tipping

The press center of mass sits 6 mm in front of the frame center and 791 mm up. With the carriage, mold and charge slid 430 mm to the front it moves to 70 mm in front, well behind the front foot edge at 320 mm. The restoring moment is about 844 N·m, so a horizontal push of about 844 N at 1 m height would tip it forward. The feet are now anchored to the floor with four M12 anchors (PPR-DDR-004).

The rails are fixed to 290 mm in front of the axis and a 335 mm extension on two barrel hinges folds down inside the guards when the press is not being loaded or demolded (the hinge moved back 30 mm so the folded extension clears the gate and the lower front panel with the platen down, PPR-DDR-004). The press stands 940 x 700 mm inside its guards; the pump handle stands 158 mm outside the right guard while in use. That 158 mm is operating space, like a door swing (decided by Amish, 2026-10-02), outlined on the floor in the general arrangement PPR-DWG-001 (Rev P6). With the carriage fully out, about 50.9 kg sits 140 mm past the hinge line, a moment of about 70 N·m that two stop lugs carry at about 2.9 kN each; tipped for demolding the lugs carry 10.8 kN each (section 4).

## 12. Cost

*Table 9. Cost by item, USD (matches `bom/bom.csv`).*

| Item | Cost | Item | Cost |
| --- | --- | --- | --- |
| 1 Base, feet, jack plate, anchors | 88 | 10 Slide and crank | 101 |
| 2 Uprights with M16 bolts, tubes, shims | 128 | 12 QC rack | 47 |
| 3 Top crossbeam with guides | 57 | 13 T-gauges | 8 |
| 4 Jack | 60 | 14 Buckets | 16 |
| 5 Platen | 51 | 15 Patterns | 118 |
| 6 Springs | 10 | 16 Fixed mesh guards, pump slot shield and guard fixes | 90 |
| 7 Rails, hinged extension and carriage | 41 | 17 Liners and trim tool | 10 |
| 8 Female mold with steel base plate and dowels | 119 | 18 Fasteners, consumables, finish | 45 |
| 9 Male mold with bushes | 102 | 19 Timer and thermometer | 12 |
| | | 20 Front gate with hinges | 25 |
| | | 21 Gate interlock and release extension | 41 |

The press costs $1,086 and the QC rack $83, for **$1,169**. Amish raised the budget from $720 to $930 on 2026-09-25 (PPR-DDR-001 item 14), topped it up to $990 on 2026-09-26 (PPR-DDR-002 item 16), and raised it to $1,060 on 2026-09-27 for the guarded version (PPR-DDR-003, option (a)), when R10 was met on paper at $1,051. Making the design constructable (PPR-DDR-004) added $92: the steel base plate under the female mold, the thicker 450 mm mold flanges, dowels and bushes (items 8 and 9, +$44), floor anchors, the bolted jack plate and heavier feet (item 1, +$22), the adapter disc and nut box (item 10, +$9), interlock details (item 21, +$7), and smaller changes elsewhere. The fixed inner shield behind the pump slot (decided by Amish on 2026-10-02) adds $6: 2.8 kg of 2 mm sheet and flat bar at $1.30/kg plus $2 for bolts. The four guard fixes (decided by Amish on 2026-10-03: "PotPress - move forward with the four guard fixes. I accept the cost.") add $20: the 6.35 mm mesh on the front strips, lower front panel and roof (1.11 m²) and on the gate (0.61 m²) at about $10.50/m² in place of $6/m² ($5 on item 16, $3 on item 20); the small-hole plates, 0.13 kg plus six M5 bolts and a grommet ($2); the two top beam cover plates, 2.71 kg plus eight M8 bolts and tapping ($7); and the crank bracket covers, 1.52 kg plus eight M6 bolts ($4). The register estimated about $15; the cover plates cost more because they now also close the open tops of the upright channels (section 15). Value-engineering target: USD 1,060. Estimated cost of the constructable design: USD 1,169 (USD 109 over the target), so **R10 is over the value-engineering target by $109 (10.3 %).** The target is a hypothetical control target and is not changed here; the design decisions register lists the cost drivers and savings worth trying (PPR-DDR-004, Q1). Guard solids are left out of the mass table in section 10, because the model draws their mesh at every eighth wire; the guards weigh about 45 kg (estimate), plus 2.8 kg for the pump slot shield and 4.4 kg for the plates and covers of the guard fixes, which are solid sheet and plate and so are taken from the model, less 1.6 kg because the 6.35 mm mesh (about 1.57 kg/m²) is lighter than the 12.7 mm mesh it replaces (about 2.49 kg/m²): about 51 kg in all with the gate and interlock.

## 13. Results against the requirements

*Table 10. Every requirement, by status (least certain first).*

| ID | Value | Target | Status |
| --- | --- | --- | --- |
| R2 | ±1.40 mm as cast; ±0.44 mm wall and ±0.44 mm coaxial when finished to templates, located by match-drilled dowels | ±1 mm wall; 0.5 mm coaxial | At risk |
| R7 | 16 flat-back pattern segments for a 250 mm printer, no core boxes; no lathe needed (dowels, lapped stop faces); cavity hand finishing unproven | Printed patterns, hand and drill press finishing, no lathe over 300 mm swing | At risk |
| R10 | $1,169 (press $1,086, QC rack $83), constructable design (PPR-DDR-004) with the pump slot shield and the guard fixes | $1,060 value-engineering target | **Over the value-engineering target by $109** (10.3 %) |
| R9 | Guards, gate and interlocks modeled (PPR-DDR-003); fixed inner shield behind the pump slot; the four guard fixes of 2026-10-03 modelled. ISO 13857 desk check (section 15): all 23 openings meet Table 4 on paper | Guards, interlocked gate, controls outside, pin in place and interlocked; openings to ISO 13857 | Met on paper; the desk check is not yet signed by a competent person (a hold point before any force above hand pressure) |
| R1 | 280 mm rim, 240 mm deep, 15 mm wall, 345 mm rim; 12.30 L brim, 9.91 L working; all from `PARAMS` | Reference filter from one source file | Met on paper |
| R3 | No yield at 294 kN: 190 MPa beams, 272 MPa pin (yield 650), 54 MPa uprights, 117 MPa M16 joint bolts, 62 MPa male flange on the stop. Deflection 0.66 mm at 10 t (1.97 mm at 294 kN); molds close on a metal stop | No yield at 294 kN; under 1 mm deflection at 10 t | Met on paper |
| R4 | 5.2 min cycle; 69 pots per 6 h | 6 min or less; 50 or more per 6 h | Met on paper |
| R5 | 310 mm opening against 270 mm needed (70 mm clear of the rim); 110 of 150 mm jack stroke | 30 mm clear; press within one stroke | Met on paper |
| R6 | 4 stations; 1.69 mm per 0.1 L; 0.061 L per 1 mm reading error; 25 °C correction | 0.1 L/h resolution, ±0.1 L/h repeatability | Met on paper (repeatability not verifiable at TRL 3) |
| R8 | Heaviest part 39.6 kg (platen); frame bolted at the four upright joints, largest frame part 38.0 kg | 40 kg or less | Met on paper |
| R11 | Press 940 x 700 mm guarded with the rail extension folded (the pump handle stands 158 mm outside the right guard while in use), 1,806 mm tall; QC rack 780 x 780 mm | Press 1.0 x 0.7 m and 2.0 m; rack 0.8 x 0.8 m | Met on paper, at the 0.7 m depth limit |
| R12 | Aluminum mold faces, polyethylene liners, HDPE buckets, no oils on molds; lead-free scrap alloy (decided) | Product-safe faces | Met on paper |

Summary: 1 over the value-engineering target (R10), 2 at risk (R2, R7), 9 met on paper (R1, R3, R4, R5, R6, R8, R9, R11, R12). R9 moved from not met to met on paper in v0.10, when the four guard fixes were modelled and every opening met Table 4 in the rerun desk check. In v0.9 the count was 1 over the target, 1 not met on paper (R9), 2 at risk and 8 met; R9 moved from at risk to not met on paper in v0.9, when the ISO 13857 desk check found openings short of the standard. In v0.8 the count was 3 at risk (R2, R7, R9) and 8 met; R9 had moved to at risk in v0.8, when Amish decided on 2026-10-02 that the 30 mm pump slot needs a fixed inner shield. In v0.7 the count was 2 at risk and 9 met. In v0.5 the count was 0 not met, 2 at risk and 10 met. In v0.4 the count was 1 not met (R10), 2 at risk and 9 met; in v0.3 the count was 0 not met, 3 at risk and 9 met; in v0.2 the count was 1 not met (R10), 3 at risk and 8 met; in v0.1 the count was 3 not met (R3, R10, R11), 4 at risk and 5 met.

## 14. Changes to earlier numbers

These TRL 2 figures in PPR-PRC-001 v0.2 and PPR-REQ-001 v0.2 disagreed with this note and are corrected in v0.3: pressed pot 7.3 kg (now 6.79), charge 8.0 kg (7.47), fired pot 4.2 kg (3.61), 1.0 L level drop 16 mm (16.7), 2.5 L drop 41 mm (42.6), base beam UPN 100 (now 2 x UPN 160), two 30 mm pins at 104 MPa (fail in bending; now one 60 mm pin), molds 20 and 12 kg (now 24 and 18 kg shells), press 920 x 640 x 1,655 mm and 180 kg (now 840 x 640 x 1,806 mm and 298 kg), cycle 5 min and 70 pots (5.2 min and 69), QC rack 800 x 440 mm for four stations (cannot fit; now 780 x 780 mm), cost $716 (now $926).

Changes in v0.2 (PPR-DDR-002): uprights bolted to both beams with 16 M20 8.8 bolts (item 2 cost $77 to $124); rails fixed to 320 mm in front of the axis with a 330 mm hinged extension (item 7 cost $34 to $45; press depth 970 mm to 655 mm with the extension folded); budget $720 to $930; total $926 to $984; R3 judged at 10 t (not met to met on paper); R8 (at risk to met on paper); R11 rack limit 0.8 x 0.5 m to 0.8 x 0.8 m (not met to met on paper).

Changes in v0.3 (budget top-up approved by Amish, 2026-09-26): budget $930 to $990; R10 not met to met on paper, $6 (0.6 %) margin. `sizing.py` now prints the margin when the BOM is within budget.

Changes in v0.4 (guarded version, PPR-DDR-003): item 16 $55 to $67 (fixed mesh guards); new items 20 ($21, front gate) and 21 ($34, gate interlock and release extension); total $984 to $1,051; R10 met on paper to not met; R9 at risk to met on paper (guard openings assumed against ISO 13857, not checked); R11 judged on the guarded 940 x 700 mm envelope. `sizing.py` counts items 20 and 21 as press cost and leaves the guard solids out of the mass table.

Changes in v0.5 (cost overrun decided by Amish, 2026-09-27, PPR-DDR-003): budget $990 to $1,060; R10 not met to met on paper, $9 (0.8 %) margin. No geometry, mass or cost figure changed.

> **Safety:** These are paper calculations for a 20 t press. The single load pin is the one part whose failure ejects the male mold; it must be in place, fully home and interlocked before pressing. Nothing here replaces a proof load test by a competent person before use, which is TRL 4 work and on hold.

Changes in v0.6 (design for construction, PPR-DDR-004; Amish, 2026-09-30: "i accept your recommended changes on design that are currently being sent across for my approval"): beam gap 100 to 104 mm with shims; joint bolts M20 8.8 to M16 10.9 with spacer tubes (75 to 117 MPa); male flange 25 to 45 mm on a 450 mm diameter, now checked on the stop (487 to 62 MPa); pin block bearing 54 to 79 MPa (screw hole); stem lengthened to reach the plug floor (total deflection 0.61 to 0.66 mm at 10 t); new checks for the female base plate, the rails over the platen gap, the tipped mold, the stop lugs and the tipping pins; masses 298 to 344 kg for the press, heaviest part 38.9 to 39.6 kg; patterns 16 segments, 5.1 to 5.4 kg; QC rack 550 to 720 mm tall; cost $1,051 to $1,143, R10 within the value-engineering target to $83 over it.

Changes in v0.7 (budget treated as a value-engineering target, 2026-10-01): R10 is reported against the $1,060 value-engineering target, $83 over, and no longer as a requirement that is not met. No number changed.

Changes in v0.8 (decisions of 2026-10-02): R9 met on paper to at risk until the pump slot shield is designed and the ISO 13857 desk check is signed; the working force is a process setting found in trials from about 2 t.

Changes in v0.10 (four guard fixes decided by Amish, 2026-10-03): 6.35 mm mesh on the front strips, lower front panel, front gate and roof; small-hole plates at the release shaft and pin cable; 3 mm cover plates on the top beam from the crank bracket to the beam ends; 2 mm covers on the front and back of the crank bracket. Item 16 $73 to $90, item 20 $22 to $25; total $1,149 to $1,169, $89 to $109 over the target; guards about 48 to about 51 kg; press mass unchanged at 344 kg. Desk check rerun: 15 openings in v0.9 (9 not meeting) to 23 in v0.10 (all meeting), the new rows being the open tops of the upright channels (missed in v0.9), the crank bracket front and back, the roof's cut-out round the top beam and the gate's edge gaps. R9 not met on paper to met on paper.

Changes in v0.9 (approved follow-ups, 2026-10-02): mean pressure at 2 t added to Table 3 (0.21 MPa); the pump slot shield is modelled and costed (item 16 $67 to $73, 2.8 kg; total $1,143 to $1,149, $83 to $89 over the target); the pump slot is lengthened from 220 to 272 mm so its ends stand 25 mm beyond the handle at the ends of its stroke; the ISO 13857 desk check is added (section 15); R9 at risk to not met on paper.

## 15. ISO 13857 desk check of the guard openings

Decided by Amish on 2026-10-02: the check is done now, from the tables and the model's distances, signed by a competent person, and it is a hold point before any force above hand pressure. This section is the desk check. The first run (v0.9, 2026-10-02) found openings that fall short of the standard and proposed four fixes; Amish decided on 2026-10-03: "PotPress - move forward with the four guard fixes. I accept the cost." The fixes are now in the model and the check below is rerun for every opening. **It is not yet signed**; until it is, nothing above hand pressure is allowed (build plan safety stop S8).

**Method.** For each opening, the opening size e and its kind (slot, square or round) give the safety distance sr from ISO 13857:2019, Table 4 (upper limbs, persons 14 years and older), as read for this check: e up to 4 mm needs 2 mm; over 4 up to 6 mm, 10 mm for a slot and 5 mm for a square; over 10 up to 12 mm, 100 mm for a slot and 80 mm for a square; over 12 up to 20 mm, 120 mm; over 20 up to 30 mm, 850 mm for a slot and 120 mm for a square; over 30 up to 40 mm, 850 mm for a slot and 200 mm for a square; over 40 up to 120 mm, 850 mm for every kind. The distance found is the straight line from the outer face of the opening to the nearest part that moves, with the press closed and open, measured on the model by `cad/src/model.py --iso` (called by `sizing.py`). The parts that move are the platen and everything it carries (rails, folding extension, carriage, female mold and pot) and the springs, moved by the jack, and the male mold and stem, moved by the crank. The load pin is moved only by hand with the press open and is left out. Where a fix closes an opening, the opening is measured as it now stands: e is the gap the closure leaves (the annular gap round a shaft or cable, or 0 where a plate covers it completely) and the distance is taken from the closure's outer face. A real reach round an obstacle is longer than the straight line, so the distances are conservative.

**The four fixes as modelled.**

1. **Finer mesh.** The two front strips, the lower front panel, the front gate and the roof carry 6.35 mm (1/4 in) galvanized welded mesh of 0.9 mm wire, 5.45 mm clear, in place of the 12.7 mm mesh; the side and rear guards keep the 12.7 mm mesh. Each angle frame sits directly behind its mesh (1.8 mm behind the outer face for the finer mesh).
2. **Small-hole plates.** Behind the front right strip, two 3 mm plates bolted through the mesh: one 55 x 60 mm with a 20 mm hole round the 12 mm release shaft (4 mm all round), butting the strip's frame; one 50 x 50 mm with a 10 mm grommeted hole round the 6 mm pin cable (2 mm all round).
3. **Top beam cover plates.** A 3 mm plate 320 x 180 mm each side, bolted to the top flanges with four M8, from the edge of the crank bracket's base plate (100 mm from the middle) to the beam end. Each covers the beam gap on both sides of the upright and the open tops of the upright's two channels, which the v0.9 check had missed: each upright is two channels back to back whose 44 x 83 mm insides were open from above.
4. **Crank bracket covers.** 2 mm sheet, 170 x 285 mm, screwed to the front and back edges of the bracket's side plates from the base plate to the top plate, so the bracket is closed on four sides; the stem's cap plate, the thrust collar and the screw turn inside it.

*Table 11. Every opening against ISO 13857 Table 4, with the four fixes (rerun 2026-10-03).*

| Opening | Kind and size e | sr needed | Nearest moving part | Result |
| --- | --- | --- | --- | --- |
| Mesh, right and left side guards (12.7 mm, 1.6 mm wire) | Square, 11.1 mm | 80 mm | 110 mm, platen | Meets |
| Mesh, rear guard (12.7 mm) | Square, 11.1 mm | 80 mm | 100 mm, female mold | Meets |
| Mesh, front right strip (6.35 mm, 0.9 mm wire) | Square, 5.45 mm | 5 mm | 39 mm, folding rail extension | Meets (was 11.1 mm, needing 80) |
| Mesh, front gate (6.35 mm) | Square, 5.45 mm | 5 mm | 44 mm, folding rail extension | Meets (was 11.1 mm) |
| Mesh, lower front panel (6.35 mm) | Square, 5.45 mm | 5 mm | 45 mm, folding rail extension (press open) | Meets (was 11.1 mm) |
| Mesh, front left strip (6.35 mm) | Square, 5.45 mm | 5 mm | 60 mm, folding rail extension | Meets (was 11.1 mm) |
| Mesh, roof guard (6.35 mm) | Square, 5.45 mm | 5 mm | 77 mm, stem (moved by the crank) | Meets (was 11.1 mm) |
| Pump slot with the fixed inner shield | Slot, 30 mm | 850 mm | The slot opens only into the shield; no moving part enters the space inside it in any position | Meets: the shield encloses the reach |
| Release shaft, small-hole plate | Annular gap, 4 mm round the 12 mm shaft | 2 mm | 80 mm, folding rail extension (press open) | Meets (was a 44 mm square, gaps of 16 mm) |
| Pin cable, grommet plate | Annular gap, 2 mm round the 6 mm cable | 2 mm | 176 mm, carriage | Meets (was a 40 mm square) |
| Top beam gap, 100 to 250 mm each side of the middle | Covered, 0 mm | 2 mm | 55 mm, stem (moved by the crank) | Meets (was 104 x 150 mm, open from above) |
| Upright channel tops, 250 to 294 and 306 to 350 mm each side | Covered, 0 mm | 2 mm | 179 mm, male mold (press open) | Meets (were 44 x 83 mm, open from above; not in the v0.9 table) |
| Top beam gap, 350 to 410 mm each side | Covered, 0 mm | 2 mm | 217 mm, male mold (press open) | Meets (was 104 x 60 mm) |
| Crank bracket, front and back | Covered, 0 mm | 2 mm | 36 mm, stem (moved by the crank) | Meets (were 150 x 270 mm, open) |
| Roof cut-out round the top beam | Slot, 5 mm all round | 10 mm | 72 mm, stem (moved by the crank) | Meets (first checked in v0.10) |
| Front gate edges, sides, bottom and top | Slot, 4 mm | 2 mm | 44 mm, folding rail extension (press open) | Meets (first checked in v0.10) |

The model prints 23 rows, counting the left and right of each top beam row separately: all 23 meet.

**Pump slot and shield.** Unchanged from v0.9. The shield is a tunnel of 2 mm folded steel sheet, 30 mm wide inside, from the slot along the handle's line to 3.0 mm off the jack body, with a flange bolted through the slot frame and a flat-bar stay to the base beam. Through the slot only the pump handle and the end of the jack's pump socket can be reached; the platen, molds, springs and ram are behind steel, the nearest of them 51 mm outside the shield. The handle runs 5 mm from the side walls over its whole stroke, a sliding pass with no closing gap, and stops 25 mm short of the slot ends and of the tunnel's roof and floor at both ends of its stroke (ISO 13854 gives 25 mm as the minimum gap that does not crush a finger). The 3 mm gap between the tunnel and the jack body is between fixed parts.

**The pump handle passing the slot frame.** The handle crosses the guard at 25 degrees and passes the sides of the slot frame at 2.3 mm at the ends of its stroke, closer near mid-stroke, moving along the slot. A gap of 4 mm or less does not admit a fingertip (Table 4, first row), so this pass is not a finger shear point on paper; the competent person should confirm it on the jack bought, since the handle's own play sets the real gap.

**Roof reach.** The roof mesh stands 28 mm above the top beam, its cut-out 5 mm clear of the beam all round (a 5 mm slot, 72 mm from the stem). Above the beam, the cover plates and the crank bracket's base plate now close the beam from above everywhere outside the stem guides, so an arm reaching down meets only fixed steel; the male flange, which stands 15 mm under the top beam at full lift, is under the cover plates. Above the roof, the stem's cap plate still rises to 10 mm under the crank bracket's top plate at full lift, but now inside a bracket closed on all four sides.

**Nothing moving touches the fixes.** `model.py --check` moves the platen and everything it carries over the whole 110 mm pressing travel, then cranks the male mold over its whole 200 mm lift with the platen down and the pin parked, then sets the press for demolding, and moves the pump handle over its stroke: the nearest moving part comes 46 mm from the small-hole plates (the lock rod), 55 mm from the top beam cover plates and 35 mm from the crank bracket covers (the stem). The release shaft turns with 4.0 mm all round in its hole and the pin cable slides with 2.0 mm. The front gate, now carrying the finer mesh, is swung from shut to 105 degrees in 15 degree steps with the press closed and open: no overlap with any part, and it comes no nearer than 23 mm to anything other than the guards and the interlock it engages (the folding rail extension, gate shut). All constructability checks pass.

**Points for the competent person.** Confirm the Table 4 values against the published standard; confirm that the 0.9 mm wire mesh is stiff enough that it cannot be pushed in towards the moving parts (39 mm is the smallest distance behind it; ISO 14120 asks guards to stay in place and keep their shape); and confirm the handle's pass by the slot frame on the jack bought.

| Desk check | Name | Signature | Date |
| --- | --- | --- | --- |
| Prepared from the model | Amish Chadha (calculation note author) | | 2026-10-03 |
| Checked and signed by a competent person | | Not yet signed | |
