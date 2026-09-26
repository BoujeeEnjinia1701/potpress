---
doc_id: PPR-CAL-001
title: PotPress sizing and first-principles checks
project: PotPress
doc_type: Calculation note
version: "0.2"
status: Draft
date: '2026-09-25'
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
---

# PotPress sizing and first-principles checks

On paper the press forms the reference filter, opens far enough, keeps up the output and stays strong at 1.5 times the jack rating, but it is heavier and dearer than the TRL 2 estimates said. With the recommendations Amish accepted on 2026-09-25 (PPR-DDR-002), eight of the twelve requirements are met on paper, three are at risk and one is **not met**: R10 (priced BOM $984 against the $930 budget, 6 % over). R3 is now judged at the 10 t working force with the molds closing on a metal stop (0.61 mm), R11 allows 0.8 x 0.8 m for the QC rack and a hinged rail extension keeps the press 655 mm deep, and bolting the four upright joints keeps every part under 40 kg (R8). The calculations also found three TRL 2 errors that the model now corrects: the base beam (a single UPN 100) would have been stressed to about 1,071 MPa, the two 30 mm load pins would have failed in bending (about 1,030 MPa), and solid aluminum molds would have weighed about 57 and 41 kg, so the molds are now cast shells.

Every number in this note is printed by `docs/04-calcs/sizing.py` (run from the repo root: `python docs/04-calcs/sizing.py`). The script reads the geometry from `PARAMS`, `SECTIONS` and `levels()` in `cad/src/model.py`, takes part masses from the model solids, and reads the prices from `bom/bom.csv`, so the model, the drawing PPR-DWG-001, the BOM and this note agree. All values are first-principles estimates; nothing here is measured.

## 1. Assumptions

*Table 1. Inputs. All are assumptions for a paper design unless marked as decided.*

| Input | Value | Basis |
| --- | --- | --- |
| Architecture, lift, molds, frame, demolding, QC, band | As decided | PPR-DDR-001 items 1 to 8 |
| R3 basis, rack area, bolted joints, single pin with interlock, budget $930, lead-free scrap | As decided | PPR-DDR-001 items 10 to 15; PPR-DDR-002 |
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

The pressing force needed for a well-consolidated wall was still not found. Henry, Maley and Mehta (2013) note that the Potters Without Borders press uses a 20 t jack, but their own low-cost press forms round-bottom filters with a 2 t car jack ([Henry, Maley and Mehta, *IJSLE* 8 (1), 2013](https://ojs.library.queensu.ca/index.php/ijsle/article/view/4532)). The working force may therefore be well below the assumed 5 to 10 t. The frame is sized for the full jack rating either way.

*Table 3. Mean pressure over the 0.0935 m² projected area of the pot.*

| Force | kN | Mean pressure |
| --- | --- | --- |
| 5 t | 49.0 | 0.52 MPa |
| 10 t | 98.1 | 1.05 MPa |
| 20 t (rating) | 196.2 | 2.10 MPa |
| 30 t (1.5 x rating) | 294.3 | 3.15 MPa |

## 4. Frame and load path

The press force runs from the jack through the platen, the female mold, the pot and the male mold into the stem, across one load pin into the top crossbeam, down both uprights in tension and back through the base beam to the jack. Each beam is two UPN 160 channels with a 100 mm gap between the webs; the uprights (two UPN 100 channels back to back, 100 x 100 mm) and the stem sit in that gap. The TRL 2 base was a single UPN 100 (41 cm³); under the same 44 kN·m it would reach about 1,071 MPa, so the base beam now matches the top beam.

*Table 4. Stresses. Beam span 600 mm (upright centers), center load.*

| Item | 10 t | 20 t (rating) | 30 t (design) | Limit |
| --- | --- | --- | --- | --- |
| Beam bending (2 x UPN 160, 232 cm³), top and base | 63 MPa | 127 MPa | 190 MPa | 165 at rating; 275 yield at design |
| Beam web shear | 20 MPa | 41 MPa | 61 MPa | |
| Uprights, tension (2 x 2,700 mm²) | 18 MPa | 36 MPa | 54 MPa | |
| Load pin, 60 mm, bending (arm 37.25 mm) | | 172 MPa | 258 MPa | 650 yield |
| Load pin, shear (double) | | | 52 MPa | |
| Pin bearing on web plus 12 mm doubler | | | 126 MPa (327 MPa without doubler) | |
| Pin bearing on the stem pin block | | | 54 MPa | |
| Web tear-out above the pin (38.5 mm ligament) | | | 98 MPa | |
| Stem, SHS 90 x 8, compression | | | 112 MPa | |
| Upright joint welds, welded option (556 mm of 6 mm fillet) | | | 62 MPa | 129 |
| Upright joints as decided, 4 x M20 8.8 in double shear per joint | | | 75 MPa | |
| Joint bolt bearing on beam web (7.5 mm) / upright flange (8.5 mm) | | | 123 / 108 MPa | |
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
| Stem | 0.06 | 0.11 | 0.17 |
| Platen | 0.02 | 0.04 | 0.06 |
| Pin allowance | 0.03 | 0.07 | 0.10 |
| **Total** | **0.61** | **1.23** | **1.84** |

The v0.1 R3 target of less than 1 mm at 294 kN was not met. Shear deflection is about 40 % of each beam's share because the beams are short and deep, so a deeper section helps little: 2 x UPN 200 would still give 1.34 mm for 21.8 kg more steel. The wall thickness does not depend on this deflection if the molds close on a metal stop: the male flange lands on the female stop face outside the flash groove, and the rim thickness is set by the 15 mm counterbore. Amish accepted the recommendation on 2026-09-25 (PPR-DDR-001 item 10, PPR-DDR-002): R3 now judges deflection at the 10 t maximum working force, where it is 0.61 mm, so R3 is met on paper. Strength is still checked at 294 kN.

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

The male flange centers in a 10 mm tapered lip on the female flange, finished to a 0.1 mm diametral fit, so the carriage and stem clearances do not set the mold alignment. What remains is the accuracy of each mold's cavity relative to its locating surface.

- As cast, each mold carries about ±0.99 mm radial error (RSS of CT10, print error and core shift), so the wall varies by about ±1.40 mm. R2 (±1 mm) is not met as cast.
- Finished by hand to printed templates at ±0.3 mm, the wall varies by about ±0.43 mm and the molds are coaxial to about ±0.43 mm, inside R2's ±1 mm and 0.5 mm.

R2 is therefore **at risk**: it depends on hand finishing reaching ±0.3 mm on a 400 mm casting without a lathe, which cannot be shown at TRL 3.

## 8. Casting patterns (R7)

With a 1.3 % shrink allowance, the female pattern is 415 mm across by 299 mm tall and the male 395 mm by 268 mm. On a 250 mm printer each splits into four quadrants in two tiers, 16 segments in all, using about 5.1 kg of PLA at 25 % of solid mass. Printing is within reach of a maker space; finishing the cast cavity without a lathe is not proven, so R7 is **at risk**.

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

Four 345 mm rims need at least 1.46 m in one row, or about 0.78 x 0.78 m in a 2 x 2 grid. The modeled rack is 780 x 780 x 550 mm, inside the 0.8 x 0.8 m that R11 now allows for the rack (decided by Amish, 2026-09-25, PPR-DDR-001 item 11).

## 10. Masses and handling

*Table 8. Masses from the model solids, kg.*

| Item | Mass |
| --- | --- |
| 1 Base beam, feet and jack plate | 50.9 (beam weldment 37.4, each bolted foot 6.8) |
| 2 Uprights | 58.7 (29.4 per pair), plus 7.2 of joint bolts |
| 3 Top crossbeam | 36.9 |
| 4 Jack | 13.0 (typical) |
| 5 Platen with sleeves | 38.9 |
| 7 Rails, hinged extension and carriage | 20.6 |
| 8 Female mold | 24.3 |
| 9 Male mold | 17.9 |
| 10 Male mold slide and crank | 35.9 (pin 5.1) |
| **Press, items 1 to 10** | **298** |
| 12 QC rack | 31.1 |

The TRL 2 estimate of 180 kg was low, and solid molds would have weighed about 57 kg (female) and 41 kg (male); shells bring them to 24 and 18 kg. As fabricated, the heaviest part is the platen at 38.9 kg, inside R8's 40 kg. Fully welded, the frame (items 1 to 3) would be one piece of about 147 kg that two people cannot move. As decided (PPR-DDR-001 item 12), the four upright joints are bolted with 4 x M20 8.8 each, so the frame arrives as a 37.4 kg base beam, two 6.8 kg feet, two 29.4 kg upright pairs and a 36.9 kg top beam, and R8 is met on paper.

## 11. Tipping

The press center of mass sits 7 mm in front of the frame center and 790 mm up. With the carriage, mold and charge slid 430 mm to the front it moves to 64 mm in front, well behind the front foot edge at 320 mm. The restoring moment is about 747 N·m, so a horizontal push of about 747 N at 1 m height would tip it forward. Anchoring to the floor is still advised.

The rails are fixed to 320 mm in front of the axis, in line with the front foot edge, and a 330 mm extension on two barrel hinges folds down when the press is not being loaded or demolded, so the press stands 840 x 655 mm (970 mm deep with the extension deployed). With the carriage fully out, about 39.7 kg sits 110 mm past the hinge line, a moment of about 43 N·m that two stop lugs carry at about 1.8 kN each.

## 12. Cost

*Table 9. Cost by item, USD (matches `bom/bom.csv`).*

| Item | Cost | Item | Cost |
| --- | --- | --- | --- |
| 1 Base | 66 | 10 Slide and crank | 92 |
| 2 Uprights with joint bolts | 124 | 12 QC rack | 45 |
| 3 Top crossbeam | 56 | 13 T-gauges | 8 |
| 4 Jack | 60 | 14 Buckets | 16 |
| 5 Platen | 51 | 15 Patterns | 112 |
| 6 Springs | 10 | 16 Guards and gate | 55 |
| 7 Rails, hinged extension and carriage | 45 | 17 Liners and trim tool | 10 |
| 8 Female mold | 102 | 18 Fasteners, consumables, finish | 45 |
| 9 Male mold | 75 | 19 Timer and thermometer | 12 |

The press costs $903 and the QC rack $81, for **$984**. Amish raised the budget from $720 to $930 on 2026-09-25 (PPR-DDR-001 item 14), which covered the v0.1 total of $926; the decided bolted joints (16 bolt sets, $48) and hinged rail extension ($10, with a little less steel) add $58, so the total is $54 (6 %) over and R10 is **not met**. The growth since TRL 2 comes from about 120 kg of extra load-path steel, the single alloy-steel pin and lead screw, patterns sized from the real mold shells, and now the joint bolts. Options for the remaining gap are proposed in PPR-DDR-002.

## 13. Results against the requirements

*Table 10. Every requirement, by status (not met first).*

| ID | Value | Target | Status |
| --- | --- | --- | --- |
| R10 | $984 (press $903, QC rack $81) | $930 or less | **Not met**, $54 (6 %) over |
| R2 | ±1.40 mm as cast; ±0.43 mm wall and ±0.43 mm coaxial when finished to templates | ±1 mm wall; 0.5 mm coaxial | At risk |
| R7 | 16 pattern segments for a 250 mm printer; cavity finishing without a lathe unproven | Printed patterns, hand and drill press finishing, no lathe over 300 mm swing | At risk |
| R9 | Guards, gate, jack-release interlock and pin-presence interlock in the BOM; not modeled | Guards, interlocked gate, controls outside, pin in place and interlocked | At risk |
| R1 | 280 mm rim, 240 mm deep, 15 mm wall, 345 mm rim; 12.30 L brim, 9.91 L working; all from `PARAMS` | Reference filter from one source file | Met on paper |
| R3 | No yield at 294 kN: 190 MPa beams, 258 MPa pin (yield 650), 54 MPa uprights, 75 MPa joint bolts. Deflection 0.61 mm at 10 t (1.84 mm at 294 kN); molds close on a metal stop | No yield at 294 kN; under 1 mm deflection at 10 t | Met on paper |
| R4 | 5.2 min cycle; 69 pots per 6 h | 6 min or less; 50 or more per 6 h | Met on paper |
| R5 | 310 mm opening against 270 mm needed (70 mm clear of the rim); 110 of 150 mm jack stroke | 30 mm clear; press within one stroke | Met on paper |
| R6 | 4 stations; 1.69 mm per 0.1 L; 0.061 L per 1 mm reading error; 25 °C correction | 0.1 L/h resolution, ±0.1 L/h repeatability | Met on paper (repeatability not verifiable at TRL 3) |
| R8 | Heaviest part 38.9 kg (platen); frame bolted at the four upright joints, largest frame part 37.4 kg | 40 kg or less | Met on paper |
| R11 | Press 840 x 655 mm with the rail extension folded (970 mm deployed), 1,806 mm tall; QC rack 780 x 780 mm | Press 1.0 x 0.7 m and 2.0 m; rack 0.8 x 0.8 m | Met on paper |
| R12 | Aluminum mold faces, polyethylene liners, HDPE buckets, no oils on molds; lead-free scrap alloy (decided) | Product-safe faces | Met on paper |

Summary: 1 not met (R10), 3 at risk (R2, R7, R9), 8 met on paper (R1, R3, R4, R5, R6, R8, R11, R12). In v0.1 the count was 3 not met (R3, R10, R11), 4 at risk and 5 met.

## 14. Changes to earlier numbers

These TRL 2 figures in PPR-PRC-001 v0.2 and PPR-REQ-001 v0.2 disagreed with this note and are corrected in v0.3: pressed pot 7.3 kg (now 6.79), charge 8.0 kg (7.47), fired pot 4.2 kg (3.61), 1.0 L level drop 16 mm (16.7), 2.5 L drop 41 mm (42.6), base beam UPN 100 (now 2 x UPN 160), two 30 mm pins at 104 MPa (fail in bending; now one 60 mm pin), molds 20 and 12 kg (now 24 and 18 kg shells), press 920 x 640 x 1,655 mm and 180 kg (now 840 x 640 x 1,806 mm and 298 kg), cycle 5 min and 70 pots (5.2 min and 69), QC rack 800 x 440 mm for four stations (cannot fit; now 780 x 780 mm), cost $716 (now $926).

Changes in v0.2 (PPR-DDR-002): uprights bolted to both beams with 16 M20 8.8 bolts (item 2 cost $77 to $124); rails fixed to 320 mm in front of the axis with a 330 mm hinged extension (item 7 cost $34 to $45; press depth 970 mm to 655 mm with the extension folded); budget $720 to $930; total $926 to $984; R3 judged at 10 t (not met to met on paper); R8 (at risk to met on paper); R11 rack limit 0.8 x 0.5 m to 0.8 x 0.8 m (not met to met on paper).

> **Safety:** These are paper calculations for a 20 t press. The single load pin is the one part whose failure ejects the male mold; it must be in place, fully home and interlocked before pressing. Nothing here replaces a proof load test by a competent person before use, which is TRL 4 work and on hold.
