---
doc_id: PPR-PRC-001
title: PotPress design precis
project: PotPress
doc_type: Design precis
version: "0.5"
status: Draft
date: '2026-09-26'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-09-24'
  author: Amish Chadha
  change: Initial scaffold
- version: "0.2"
  date: '2026-09-25'
  author: Amish Chadha
  change: Populate to TRL 2 (architecture, first-order numbers, material flow, safety, media)
- version: "0.3"
  date: '2026-09-25'
  author: Amish Chadha
  change: TRL 3 update; design choices decided by Amish (PPR-DDR-001); numbers corrected to PPR-CAL-001 (shell molds, 2 x UPN 160 base, one 60 mm pin, 2 x 2 QC rack, cost)
- version: "0.4"
  date: '2026-09-25'
  author: Amish Chadha
  change: Recommendations accepted by Amish (DDR-002); bolted upright joints, hinged rail extension, pin-presence interlock, lead-free scrap, budget $930; numbers from PPR-CAL-001 v0.2
- version: "0.5"
  date: '2026-09-26'
  author: Amish Chadha
  change: Budget top-up approved by Amish; budget $990, R10 met on paper
---

# PotPress design precis

PotPress is a hand-pumped hydraulic press that forms one ceramic pot filter per stroke between a cast aluminum female mold and male mold, plus a four-station rack for the standard one-hour flow-rate test. A 20 t bottle jack on the base lifts a guided platen carrying the female mold against a fixed male mold, whose stem is held by one load pin in the top crossbeam for pressing and raised by a hand crank for loading. One parametric filter geometry drives the molds, the 3D-printed casting patterns and the printed flow gauge. The TRL 3 calculations (PPR-CAL-001) give a cycle of about 5.2 min and about 69 pots per 6 h, a strong frame at 1.5 times the jack rating, every part under 40 kg with the frame bolted at the upright joints, and a parts cost of $984 against the $990 budget (topped up by Amish on 2026-09-26), a $6 margin. The design choices below were decided by Amish on 2026-09-25 (PPR-DDR-001 and PPR-DDR-002).

![Hero render](../media/hero.png)

*Figure 1. PotPress with the 2 x 2 QC flow-test rack and a 1.75 m person for scale. The press is shown closed at the end of a pressing stroke.*

## How it works

1. **Load.** With the platen down, the female mold rim is at about 921 mm. The operator swings the hinged rail extension up onto its stop lugs, slides the carriage out 430 mm on the rails, lays a polyethylene release liner in the female mold, places a weighed charge of about 7.5 kg of clay, burnout and water mix, and slides the carriage back to its end stop.
2. **Lower the male mold.** A handwheel on top of the frame turns a self-locking Tr24 x 5 lead screw that runs the male mold stem down 200 mm (40 turns) through the top crossbeam until the pin bores line up. The operator inserts the 60 mm load pin through the beam and stem. From then on the pin, not the screw, carries the press force.
3. **Press.** The operator closes the front gate and pumps the jack, about 70 strokes. The platen, guided by sleeves on both uprights, lifts the female mold about 110 mm and squeezes the charge into the gap between the molds. The male flange centers in a tapered lip on the female mold and lands on a stop face, so the 15 mm wall and rim are set by the molds, not by how hard the operator pumps. Excess mix squeezes into a flash groove at the rim for trimming.
4. **Open and demold.** The operator opens the jack release; the platen's weight and two springs return it. The operator pulls the pin and cranks the male mold up, leaving its tip 70 mm above the female rim. The carriage slides out toward the operator and tilts on its pivots so the pot, still in its liner, turns out onto a drying board. Between loads the rail extension folds down, so the press stands 840 x 655 mm.
5. **Dry, fire, treat.** Drying, firing and silver treatment follow the factory's existing practice and are outside PotPress.
6. **Test.** Fired pots are soaked, hung by their rims in the QC rack over collection buckets, filled to 10 mm below the rim and read after one hour with the printed T-gauge. The reading is corrected to 25 °C with the water temperature.

![Cutaway](../media/cutaway.png)

*Figure 2. Cutaway through the closed press and the QC rack, showing the pressed pot between the molds, the shell molds and the load path.*

![Material flow](../media/flow.png)

*Figure 3. Material flow for one filter, from mixed charge to a filter that passes QC, in kg. All values are estimates from PPR-CAL-001.*

## Main components

Numbers match the exploded view (Figure 4), `bom/bom.csv` and the general arrangement drawing PPR-DWG-001.

*Table 1. Main components.*

| # | Component | Choice | Notes |
| --- | --- | --- | --- |
| 1 | Base beam and feet | Two UPN 160 channels 840 mm with a 100 mm gap, 20 mm jack plate, two UPN 100 feet bolted on | Same section as the top beam; the TRL 2 single UPN 100 would reach about 1,071 MPa |
| 2 | Uprights | Two UPN 100 channels back to back each side, about 1.40 m, sandwiched in the beam gaps at 600 mm centers and bolted to both beams with 4 x M20 8.8 per joint | 54 MPa in tension, bolts 75 MPa in double shear at 294 kN; 29.4 kg per pair |
| 3 | Top crossbeam | Two UPN 160 channels, 12 mm web doublers and a 62 mm pin bore at the center, UHMW-PE stem guides | 190 MPa at 294 kN |
| 4 | 20 t bottle jack | Standard jack, 150 mm stroke, about 60 mm ram | Uses 110 mm of stroke |
| 5 | Moving platen | Two UPN 140 channels, 6 mm deck, jack pad, 150 mm guide sleeves on the uprights | 38.9 kg, the heaviest part as fabricated |
| 6 | Return springs | Two tension springs | Gravity returns the platen; the springs keep it seated |
| 7 | Rails, hinged extension and carriage | Four flat-bar rails at 60 and 170 mm each side, fixed to 320 mm in front of the axis, with a 330 mm extension on barrel hinges and stop lugs that folds down; carriage frame with handle and tilt pivots | Moves the female mold out of the pinch zone; 43 N·m on the hinge with the carriage out |
| 8 | Female mold | Cast aluminum shell, 20 mm behind the cavity, 30 mm solid base, 410 mm flange with a locating lip, rim counterbore and flash groove; 24.3 kg | A solid block would weigh about 57 kg |
| 9 | Male mold | Cast aluminum hollow plug, 15 mm shell and 30 mm tip, 390 mm rim-forming flange; 17.9 kg | A solid plug would weigh about 41 kg |
| 10 | Male mold slide | SHS 90 x 8 stem with a pin block, one 60 mm 42CrMo4 load pin, crank bracket, Tr24 x 5 lead screw and 260 mm handwheel | The screw only lifts; the pin carries the load |
| 11 | Pressed filter pot | The product, shown for context | Not costed |
| 12 | QC flow-test rack | 2 x 2 stations, 780 x 780 x 550 mm, steel angle and plywood | Within R11's 0.8 x 0.8 m |
| 13 | Printed T-gauge | PETG dipstick; 1.0 L is 16.7 mm on the scale | Scale generated from the geometry |
| 14 | Collection buckets | 20 L food-grade HDPE | |

Casting patterns, guards and front gate with interlocks, release liners, fasteners and consumables, and the QC timer and thermometer are BOM items 15 to 19 and are not modeled.

![Exploded view](../media/exploded.png)

*Figure 4. Exploded view with numbered callouts matching the BOM.*

## Key numbers

All values are estimates from PPR-CAL-001, which lists its assumptions and the results against every requirement.

*Table 2. Key numbers at TRL 3.*

| Quantity | Value | Basis |
| --- | --- | --- |
| Filter volume | 12.30 L to the brim; 9.91 L working | Inner rim 280 mm, floor 230 mm, depth 240 mm |
| Pot masses | Charge 7.47 kg; pressed 6.79 kg; fired 3.61 kg | RDI-C recipe, 1.64 kg/L pressed |
| Mean pressure | 0.52 to 1.05 MPa at 5 to 10 t; 2.10 MPa at 20 t | 0.0935 m² projected |
| Frame at 294 kN | Beams 190 MPa, uprights 54 MPa, pin 258 MPa (yield 650), joint bolts 75 MPa | S275; 42CrMo4 pin; M20 8.8 bolts |
| Deflection between molds | 0.61 mm at 10 t; 1.84 mm at 294 kN | R3 (1 mm at 10 t) met on paper |
| Travel | 110 mm pressing of 150 mm stroke; 310 mm opening against 270 mm needed | R5 met |
| Cycle | 5.2 min; 69 pots per 6 h | R4 met |
| Wall evenness | ±1.40 mm as cast; ±0.43 mm finished to templates | R2 at risk |
| Flow gauge | 0.1 L is 1.69 mm; 2.3 % per °C near 25 °C | R6 met |
| Size and mass | Press 840 x 655 x 1,806 mm with the rail extension folded, 298 kg plus 7 kg of joint bolts; heaviest part 38.9 kg; rack 780 x 780 mm | R8 and R11 met on paper |
| Cost | Press $903, QC rack $81, total $984 | R10 ($990) met on paper, 0.6 % margin |

The working force is still an assumption. Henry, Maley and Mehta (2013) formed round-bottom filters with a 2 t car jack ([IJSLE 8 (1)](https://ojs.library.queensu.ca/index.php/ijsle/article/view/4532)), which suggests the real force may be well below 5 to 10 t; the frame is sized for the full 20 t jack either way.

## Key design choices

All of these were decided by Amish on 2026-09-25: go with recommendation (PPR-DDR-001 items 1 to 8 and 10 to 15; PPR-DDR-002).

- **Jack below, pushing the female mold up.** A bottle jack must stand upright, so it sits on the base and lifts the platen, and the male mold hangs from the top beam.
- **Male mold lift by hand crank with one load pin and an interlock.** A standard jack gives only 150 mm of stroke, so the crank provides the other 200 mm of opening. The TRL 2 pair of 30 mm pins fails in bending by calculation; one 60 mm alloy-steel pin carries the force, and a mechanical pin-presence interlock stops the jack release valve closing unless the pin is fully home.
- **Molds cast in aluminum from printed patterns, from lead-free scrap.** Cast as shells to keep them under 25 kg, with the cavity finished by hand to printed templates. Scrap must be lead-free (for example cast wheels or pistons; no free-machining bar). The fiber-reinforced concrete backed variant stays documented as a low-cost alternative; building it is TRL 4 work and on hold.
- **Welded subassemblies, bolted at the upright joints.** The base beam, top beam, uprights and platen are welded separately and joined with 4 x M20 8.8 bolts at each of the four upright joints, so no part exceeds 40 kg. Fully welded, the frame would be one 147 kg piece.
- **Molds close on a metal stop.** The male flange lands on the female stop face, so frame stretch does not set the wall; R3 judges deflection at the 10 t working force.
- **Demold by sliding out and tilting the carriage,** on a rail extension that folds down between loads.
- **Manual QC rack with printed T-gauge.** The rack is 2 x 2 stations in 0.8 x 0.8 m; a load-cell logger stays a later option.
- **Default acceptance band 1.0 to 2.5 L/h in the first hour, corrected to 25 °C.** Each factory may set its own band.
- **Budget $990.** The priced BOM is $984 after the bolted joints and rail hinges; Amish topped up the budget from $930 to $990 on 2026-09-26 (PPR-DDR-002 item 16).

## Safety

> **Safety:** PotPress is a 20 t hydraulic press with heavy moving parts, and the workshop around it handles silica-bearing clay dust and silver compounds. Treat each of these as a hazard at every stage.

- **Crushing and pinch points.** The gap between the molds, the platen and the uprights, and the carriage rails can crush fingers and hands. Press only with the side guards on and the front gate closed; the jack pump and release valve sit outside the guard; the carriage has an end stop so it cannot be pushed past the male mold. Keep fingers clear of the rail extension hinges when folding it, and deploy it only onto its stop lugs.
- **Load pin and stored energy.** One 60 mm pin carries the whole press force. Never press unless the pin is fully home through both beam webs and the stem; the guard includes a pin-presence interlock that stops the jack release closing until the pin is home. Check the bolted upright joints for tightness before each shift. Never exceed the jack rating, never add a cheater bar to the pump handle, and never adjust the jack's relief valve. Release pressure fully before opening the gate or pulling the pin.
- **Falling and tipping.** The molds weigh about 24 and 18 kg and the press about 305 kg with its bolts, with its center of mass about 0.8 m up. A push of about 750 N at 1 m tips it forward, so anchor the base to the floor, lift molds with two people and wear safety boots. The lead screw is self-locking, so the male mold holds its height if the handwheel is released; still keep hands out from under it.
- **Silica dust.** Dry clay and rice husk ash contain crystalline silica, which causes silicosis. Keep mixing and trimming wet, sweep damp, and wear a fitted P2 or N95 respirator for dry work.
- **Molten aluminum and alloy.** Casting is done by a foundry, not at the press. Scrap containing lead (free-machining alloys) must not be used for mold faces that touch a drinking-water product.
- **Silver compounds.** Silver nitrate is corrosive to skin and eyes and toxic to aquatic life; handle colloidal silver with gloves and eye protection and never pour it into waterways. Silver treatment is outside PotPress but happens in the same workshop.
- **Heat.** Kilns reach about 900 °C. Kilns are outside PotPress but share the site.
- **Water safety claims.** PotPress makes consistent pots; it does not certify them. A filter that passes the flow test is not proven to remove pathogens. Factories must verify bacteria removal by laboratory testing and follow the CMWG recommendations.

## Open questions

- What pressing force gives a well-consolidated wall with a typical mix? Ask a partner factory; the 2 t figure above suggests it may be low.
- Can hand finishing to printed templates reach ±0.3 mm on a 400 mm casting (R2, R7)?
- Handwheel height of about 1.8 m: a side crank through a bevel gear would be easier to reach.
- Confirm the demolding method with potters; check whether a liner leaves marks that affect flow.
- Choose the first partner factory or organization (left open under the portfolio rule).

Concept media: [blueprint sheet](../media/concept-blueprint.pdf), [interactive 3D model](../media/viewer.html). General arrangement: [PPR-DWG-001](../cad/drawings/PPR-DWG-001.pdf).
