---
doc_id: PPR-BLD-001
title: PotPress prototype build plan
project: PotPress
doc_type: Build plan
version: "0.4"
status: Draft
date: '2026-10-01'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-09-30'
  author: Amish Chadha
  change: First build plan at TRL 3, text only (withdrawn)
- version: "0.2"
  date: '2026-09-30'
  author: Amish Chadha
  change: Rewritten from the template with pictures by component and step; design made constructable (PPR-DDR-004)
- version: "0.3"
  date: '2026-09-30'
  author: Amish Chadha
  change: Open decisions moved to the design decisions register
- version: "0.4"
  date: '2026-10-01'
  author: Amish Chadha
  change: Budget treated as a value-engineering target
---

# PotPress prototype build plan

**Plan, not yet built.** How to build the first proof-of-concept prototype, component by component. Building and testing to it is TRL 4 work. Decisions still to be made are kept in the design decisions register ([docs/06-design-decisions.md](06-design-decisions.md)), not here.

## 1. What you are building

![Figure 1. Every component, pulled apart and numbered in build order](05-build-plan/overview.png)

*Figure 1. Every component pulled apart and numbered in build order.*

The prototype is a 20 t bottle-jack press that squeezes a clay charge between two cast aluminium molds to form a ceramic water filter pot, inside welded mesh guards with an interlocked front gate, plus a separate four-station rack for flow-testing finished pots. Figure 1 shows the 19 groups of parts in the order you make or fit them. The steel frame is a base beam and a top crossbeam, each two channels side by side, joined by two upright pairs with bolts; the jack pushes a moving platen up the uprights, and the platen carries rails on which a carriage slides the lower (female) mold in and out. The upper (male) mold hangs from a square stem that is pinned to the top crossbeam for pressing and wound up and down by a hand crank. The work is sawing, drilling and stick welding steel channel, plate and bar; 3D printing two casting patterns; having a local foundry sand-cast the two molds; hand finishing and lapping the molds; printing a gauge; and fitting bought parts (jack, springs, bolts, lead screw, mesh, buckets). The parts cost about $1,143 from the bill of materials, which is $83 over the $1,060 value-engineering target.

> **Safety:** PotPress is a 20 t hydraulic press. A crushing hazard exists wherever the platen, molds or stem move. Its build involves stick welding, grinding galvanised mesh (zinc fume), lifts of up to 40 kg to 1.5 m, and a foundry pour done by others. Never pump the jack with anyone's hands inside the guard, never pump with the load pin out or half in, and do not go past hand pressure before the safety stops in section 6 allow it. Nothing in this plan authorises a pressing test; that is TRL 4 work and on hold.

## 2. What changed to make it buildable

The concept showed what the press does; some of its parts could not be made or fitted as drawn. Each change keeps what the press does and is recorded in decision record PPR-DDR-004, accepted by Amish on 2026-09-30. Five smaller questions stay open; see the design decisions register.

*Table 1. Changes from the concept.*

| Component | The concept had | The buildable design has | Why |
| --- | --- | --- | --- |
| Male mold | A closed hollow shell a foundry could not core | A plug open at the top; its inside forms its own sand core (Figure 15) | A one-piece flat-back pattern, no core box |
| Male mold flange | 25 mm thick; about 487 MPa at full load on the stop | 45 mm thick, 450 mm across; the stem's disc bears on the plug floor; 62 MPa (Figure 16) | Cast aluminium yields at about 90 MPa |
| Mold location | A 390 mm lip turned to 0.1 mm, needing a 420 mm lathe | Two 16 mm dowels and two steel bushes, drilled with the molds clamped together; stop faces lapped flat (Figure 14) | A pillar drill and a bench do it |
| Female mold | One casting with a thick base | A cast cup bedded and screwed on a 15 mm steel base plate (Figure 13) | The plate takes the rails and the retaining pins |
| Jack and pump slot | Pump socket in a return spring; handle path through an upright | Jack turned 25 degrees to the right front; slot moved onto the handle's line and widened to 30 mm (Figure 20) | The handle clears everything over its stroke |
| Lead screw | Would have carried press force | Captive nut with 8 mm of free travel; press force goes through the pin (Figure 18) | The screw only lifts |
| Pin block | Hit the fixed screw when cranked up | A 28 mm hole down its middle | The screw passes as the stem rises 200 mm |
| Uprights in the beams | 100 mm uprights in a 100 mm gap | 104 mm gap with 2 mm shims (Figure 7) | Rolled channel varies |
| Joint bolts | M20, too big for the channel flange, clamping across a hollow | Four M16 grade 10.9 per joint with spacer tubes inside (Figure 7) | Correct edge distance; flanges do not fold |
| Stem guidance | 7 mm of play front to back | Plastic strips on the top beam webs, 1 mm each side (Figure 9) | The dowels always find their bushes |
| Carriage | Tilt bosses with nothing to pivot on; no mold retention; handle in the wrong place | Hooks on tipping pins, retaining pins, two lift handles (Figure 12) | The mold can be tipped out safely |
| Rail extension | Folded into the gate when the platen went down | Hinge line 30 mm further back | Clears the gate and lower panel |
| Feet | Channels lying on their flange tips; no fixings | Channels web up with welded studs and anchor tubes; four floor anchors (Figure 4) | A flat face to bolt through |
| Interlock | Outline shapes | A lock disc, lock rod, gate slider and pin slider round the jack's release screw (Figures 23 and 24) | Purely mechanical, detailed enough to make |
| QC rack | Buckets overlapping the hanging pots | Pot shelf raised to 720 mm; 35 mm between pot and bucket (Figure 25) | Room for the water to drip |
| Assembly order | Not worked out | The order of section 4, set by what fits past what | The stem and molds only go in this way |

## 3. Making the components

Make and check each component before the assembly step that needs it. Sizes are in millimetres. "Left" and "right" are as seen standing in front of the press, at the gate; "front" is the gate side. Workshop tolerance is 0.5 mm unless a step says otherwise. Weld with 3.2 mm E6013 electrodes; unless stated, fillets are 6 mm. Load-path welds (doublers, jack pad, sleeves, pin block, stem to disc) should be made by a competent welder. Mark every part with its name in paint marker as you make it.

### 3.1 Feet (make 2)

![Figure 2. Making sketch of the foot](../cad/drawings/PPR-DWG-101.png)

*Figure 2. Foot making sketch (PPR-DWG-101).*

**What it is and what it is made from.** The two feet carry the whole press and fix it to the floor. UPN 100 steel channel, S275, 640 mm long each; 26.9 x 3.2 mm steel tube; M12 x 40 bolts.

**How to make it.**

1. Saw two 640 mm lengths of channel with square ends; deburr.
2. Lay each web up (the flat 6 mm web on top, the two 50 mm flanges down).
3. Anchor holes: a 14 mm hole through the web on the centre line, 260 mm each side of the middle.
4. Weld a 26.9 x 3.2 mm tube, 44 mm long, under each anchor hole, from the floor up to the web, so the anchor has a sleeve.
5. Stud holes: four 13 mm holes, 25 mm each side of the centre line and 88 mm each side of the middle (a rectangle 50 x 176).
6. Push an M12 x 40 bolt up through each stud hole from below and weld its head to the underside of the web, square.

**How it fits the parts next to it.** The base beam's bottom flanges sit flat on the web; the studs go up through them and take a washer and nut (Figure 4). The upright pair stands on the web between the beam's channels. The anchors go down the tubes into the floor.

**Check before moving on.** The web is flat within 1 mm; the four studs stand square to it at 50 and 176 mm centres.

### 3.2 Base beam and jack plate

![Figure 3. Making sketch of the base beam and jack plate](../cad/drawings/PPR-DWG-102.png)

*Figure 3. Base beam and jack plate making sketch (PPR-DWG-102).*

**What it is and what it is made from.** The lower beam that the jack pushes down on and the uprights bolt into, with the bolted plate the jack stands on. Two UPN 160 channels, S275, 840 mm long; 10 mm plate for the end blocks; 20 mm plate for the jack plate; 8 mm flat bar for the spring lugs; 10 x 40 bar for the locating blocks.

**How to make it.**

1. Saw both channels to 840 mm. Lay them flanges out, webs 104 mm apart (inside faces), on a flat table.
2. Cut two blocks 10 x 104 x 139 mm and weld one between the webs at each end, flush with the ends. The gap now stays 104 mm.
3. Joint holes, 18 mm, through both webs: 272 and 328 mm each side of the middle, at 50 and 110 mm up from the bottom of the beam. Drill each web from outside with the beam on its side, or both at once with a magnetic drill.
4. Stud holes, 14 mm, in the bottom flanges: 335 and 385 mm each side of the middle, 88 mm each side of the centre line. Check them against the studs on the feet.
5. Spring lugs: two 30 x 150 x 8 mm bars across the top flanges, centred 190 mm each side of the middle, a 12 mm hole in the centre of each. Weld both ends.
6. Jack plate holes, 14 mm, in the top flanges: 105 mm each side of the middle, 90 mm each side of the centre line.
7. Jack plate: cut 240 x 234 x 20 mm; drill four 14 mm holes to match step 6. Stand the jack you have bought on it, centred and turned so its pump socket and release valve point to the right front, 25 degrees in front of the right-hand direction. Weld three 10 x 40 x 15 mm blocks round its base, about 2 mm off it, at 90 degrees to each other, leaving the right front open.

**How it fits the parts next to it.**

![Figure 4. Joint 7: base beam on a foot](05-build-plan/joint-07.png)

*Figure 4. Joint 7. The beam's bottom flange sits on the foot's web; the studs pass up through it.*

![Figure 5. Joint 4: the jack seat](05-build-plan/joint-04.png)

*Figure 5. Joint 4. The jack plate bridges the two top flanges and is held by four M12 bolts with nuts under the flanges; the blocks stop the jack turning.*

**Check before moving on.** Webs parallel within 1 mm end to end; an offcut of upright pair with a 2 mm shim each side slides into the gap by hand.

### 3.3 Upright pairs (make 2)

![Figure 6. Making sketch of the upright pair](../cad/drawings/PPR-DWG-103.png)

*Figure 6. Upright pair making sketch (PPR-DWG-103), drawn lying down.*

**What it is and what it is made from.** The two posts that carry the press force from the top crossbeam down to the base beam, and guide the platen. Each is two UPN 100 channels back to back. S275; 25 x 3 mm tube; 2 mm steel sheet; M16 x 150 grade 10.9 bolts with hardened washers and nuts.

**How to make it.**

1. Saw four channels to 1,401 mm with square ends; the ends set the top beam height.
2. Clamp two channels web to web, flanges pointing sideways, ends flush. Stitch weld both seams: 50 mm welds every 300 mm. The pair is 100 x 100 mm.
3. Holes, 18 mm, through all four flanges, 28 mm each side of the web seam, at 50, 110, 1,291 and 1,351 mm up from the bottom end. Drill the two flanges of each channel as a pair so they line up.
4. Cut eight spacer tubes 83 mm long from 25 x 3 mm tube per pair (the distance between the flanges inside the channel).
5. Cut eight shims per pair from 2 mm sheet, 100 x 120 mm, each with two 18 mm holes 56 mm apart, matching the flange holes.

**How it fits the parts next to it.**

![Figure 7. Joint 1: upright bolted into the base beam](05-build-plan/joint-01.png)

*Figure 7. Joint 1, cut open on one bolt line. Each bolt passes beam web, shim, upright flange, spacer tube, upright flange, shim, beam web.*

The bottom end stands on the foot's web. The pair sits between the beam webs with a shim each side; the spacer tubes slide into the open side of each channel and line up with the holes, so tightening the bolts cannot fold the flanges. The top joint into the top crossbeam is the same. If a joint is loose, add shim; if tight, thin it.

**Check before moving on.** Straight within 1 mm over its length; about 29 kg, so two people carry it.

### 3.4 Top crossbeam with doublers and guides

![Figure 8. Making sketch of the top crossbeam](../cad/drawings/PPR-DWG-104.png)

*Figure 8. Top crossbeam making sketch (PPR-DWG-104).*

**What it is and what it is made from.** The upper beam that the load pin hangs the male mold from; it takes the full press force. Two UPN 160 channels 840 mm, S275; 12 mm plate doublers; 10 mm end blocks; UHMW-PE plastic for the stem guides.

**How to make it.**

1. Make the two channels, end blocks and joint holes exactly as the base beam (section 3.2, steps 1 to 3), but do not weld the end blocks yet.
2. Doublers: two plates 12 x 200 x 139 mm. Weld one to the outside of each web, in the middle, 6 mm fillet all round. This is a load-path weld.
3. Pin bore: clamp the two channels web to web and cut a 62 mm hole through both webs and both doublers, in the middle, 80 mm up (half height). Use a 62 mm annular cutter in a hired magnetic drill.
4. Set the channels 104 mm apart again with a 60 mm steel bar through both bores, and weld the end blocks in. The bar keeps the bores in line.
5. Bracket holes: four 14 mm holes in the top flanges, 40 mm each side of the middle, 100 mm each side of the centre line.
6. Guides: two UHMW-PE blocks 29 x 104 x 160 mm, placed between the webs 46 to 75 mm each side of the middle; two UHMW-PE strips 6 x 92 x 139 mm on the inside faces of the webs between the blocks, each with a 62 mm hole on the pin bore. Fix each with two M6 countersunk screws through the web.

**How it fits the parts next to it.**

![Figure 9. Joint 2: the load pin through the top beam and the stem](05-build-plan/joint-02.png)

*Figure 9. Joint 2, cut on the pin's axis. The pin passes the doubler, web, guide strip, stem wall and pin block, then the same on the far side.*

The uprights bolt in as Figure 7. The stem slides between the four guides with 1 mm each side. The crank bracket bolts on top.

**Check before moving on.** A 60 mm bar slides through both bores by hand; the two bores are in line within 0.5 mm.

### 3.5 Moving platen, rails and hinged extension

![Figure 10. Making sketch of the platen, rails and extension](../cad/drawings/PPR-DWG-105.png)

*Figure 10. Platen, rails and hinged extension making sketch (PPR-DWG-105), extension shown swung out.*

**What it is and what it is made from.** The platen is pushed up by the jack and slides on the uprights; the rails on it carry the mold carriage, and the extension swings out in front to take the carriage for loading and demolding. Two UPN 140 channels 479 mm; 6, 8, 10 and 20 mm plate; 30 x 15 mm flat bar; two weld-on barrel hinges; 12 mm bright steel bar (EN8 or 1045). S275 unless stated. About 40 kg, the heaviest part.

**How to make it.**

1. Saw the channels to 479 mm; set them flanges out, webs 104 mm apart.
2. Jack pad: 200 x 104 x 20 mm, welded between the webs at the bottom, in the middle. The ram pushes here.
3. Deck: 479 x 440 x 6 mm, welded on the top flanges.
4. Sleeves: for each upright, wrap the real upright pair in 0.5 mm shim, clamp four 10 mm plates round it to make a square tube 121 x 121 mm outside and 150 mm tall, tack, slide it off, remove the shim, weld the corners. This gives about 1 mm clearance on the real, not nominal, upright.
5. Stand both uprights 600 mm apart (centres) in a jig, slide the sleeves on, and weld them to the channel ends with each sleeve's bottom 20 mm below the channels.
6. Spring lugs: 30 x 160 x 8 mm under the bottom flanges, 190 mm each side of the middle, 12 mm hole in the centre.
7. Rails: four 30 x 15 mm bars 510 mm long, flat on the deck, centred 60 and 170 mm each side of the middle, running from 290 mm in front of the middle to 220 mm behind it (they overhang the deck 70 mm at the front). Weld both sides. Weld a 400 x 15 x 40 mm end stop across them at the back.
8. Hinge bars: a 16 x 12 mm bar under each pair of rails at the front ends.
9. Extension: four 30 x 15 mm bars 335 mm long, joined in pairs by a 20 x 12 mm cross tie 150 mm from the hinge end. Weld the barrel hinges between the hinge bars and the extension so it swings down to hang in front of the platen, and weld 20 x 30 mm stop lugs so that, swung out, it stops level with the rails. The stop lugs carry up to about 11 kN each when a mold is tipped: weld them all round.
10. Tipping pins: weld a 12 mm bright steel pin across the far end of each outer extension bar, sticking out 67 mm to the side.
11. Grease the rail tops.

**How it fits the parts next to it.** The sleeves slide on the uprights; the jack pad sits on the ram; the springs hook into the lugs; the carriage slides on the rails between its side lips.

**Check before moving on.** On two uprights in the jig the platen slides the full 110 mm by hand without binding; the extension, swung out, is level with the rails within 1 mm and folds down freely.

### 3.6 Mold carriage

![Figure 11. Making sketch of the mold carriage](../cad/drawings/PPR-DWG-106.png)

*Figure 11. Mold carriage making sketch (PPR-DWG-106).*

**What it is and what it is made from.** A square steel ring that slides the female mold in and out on the rails and tips it out for demolding. 25 x 12 and 20 x 10 mm flat bar, 12 mm plate, 10 mm round bar; S275.

**How to make it.**

1. Ring: 25 x 12 mm bar, 410 mm square outside and 360 mm inside, welded flat.
2. Pull handle: a 140 x 35 x 12 mm tab at the front with a 140 x 15 mm upright 98 mm tall.
3. Side lips: 6 x 12 mm bar under the ring, 186 to 192 mm out from the middle, along the back half; they run just outside the outer rails and keep the carriage straight.
4. Tipping hooks: a 12 mm arm from each side of the ring out to 252 mm from the middle, 190 mm in front of the middle, and a 40 x 27 x 12 mm plate hanging from it with a slot 14 mm tall and 23 mm deep, open to the front.
5. Lift handles: 20 x 10 mm bar bent to a loop 70 mm tall, welded to the ring's outer edge 110 to 180 mm behind the middle, one each side.
6. Retaining pins: a 12 mm hole across each side of the ring at the middle; two 10 mm pins with T handles.

**How it fits the parts next to it.**

![Figure 12. Joint 8: carriage hook on the tipping pin](05-build-plan/joint-08.png)

*Figure 12. Joint 8, with the carriage pulled out. The slot slides onto the pin; lifting the handles tips the mold forward about the pin.*

The ring lies on the rails round the female mold's base plate; the retaining pins go through it into holes in the plate's edges. Pulled fully out, 430 mm, the hooks meet the tipping pins; lifting both handles (about 14 kg each to start) turns the mold over forward onto a board.

**Check before moving on.** Slides the full length of the rails and extension without catching at the hinge.

### 3.7 Casting patterns and the female mold

![Figure 13. Making sketch of the female mold](../cad/drawings/PPR-DWG-107.png)

*Figure 13. Female mold making sketch (PPR-DWG-107).*

**What it is and what it is made from.** The lower mold, which forms the outside of the pot. A sand-cast aluminium cup made by a local foundry from a 3D-printed pattern, from lead-free scrap (cast wheels or pistons, never free-machining bar), bedded and screwed on a steel base plate. About 36.5 kg with its plate.

**How to make it.**

1. **Pattern.** Print the cup in PLA, scaled up 1.3 % for shrinkage, with 3 mm extra on the flange face (for lapping) and 2 degrees of draft on the flange rim. It is 456 mm across and 274 mm tall, so print it as four quarters in two layers (8 pieces) on a 250 mm printer. Glue with epoxy, fill the seams, sand to 240 grit, seal and wax.
2. **Casting.** The pattern is flat-backed: it sits flange face down on the moulding board, and the cavity stands up as a sand core of its own, so no core box is needed. Ask the foundry to record the scrap it melts.
3. **Stop face.** Lap the flange face (the ring from 360 to 450 mm across, outside the flash groove) flat: glue 80, then 120 grit wet-and-dry paper to a sheet of 6 mm float glass at least 500 mm square, lay the cup face down on it and rub in figure-eights until marking blue shows even contact all round.
4. **Cavity.** Finish the cavity to printed contour templates within 0.3 mm (radius 128.5 at the floor, 155.1 at the rim, 255 deep), with a die grinder, files and abrasive paper. Rim counterbore 345 mm across and 15 deep; flash groove to 360 mm across, 3 deep.
5. **Base plate.** Cut 350 x 350 x 15 mm steel plate. Drill four 9 mm holes on the diagonals, 137 mm from the middle, countersunk from below for M8. Drill a 14 mm hole 20 deep into the middle of the left and right edges for the retaining pins.
6. **Bedding.** Drill and tap the cup's underside M8, 16 deep, through the plate's holes. Spread steel-filled epoxy putty on the plate, press the cup down on it, fit the four screws, wipe off the excess and let it cure.
7. **Dowels.** Drilled with the male mold (section 3.8, step 5).

**How it fits the parts next to it.**

![Figure 14. Joint 3: how the molds locate](05-build-plan/joint-03.png)

*Figure 14. Joint 3, cut through the right dowel. The flanges meet on the lapped stop ring; the dowel in its bush keeps the wall even.*

The base plate sits on the rails inside the carriage ring. The male mold closes onto the stop ring; the pot's rim fills the counterbore.

**Check before moving on.** Templates touch the cavity within 0.3 mm at eight places round each of four heights; no porosity on the cavity or stop face; the foundry's lead-free note on file. **Hold point:** measure before assembly.

### 3.8 Male mold

![Figure 15. Making sketch of the male mold and its pattern](../cad/drawings/PPR-DWG-108.png)

*Figure 15. Male mold making sketch (PPR-DWG-108).*

**What it is and what it is made from.** The upper mold, a plug that forms the inside of the pot. Sand-cast aluminium from lead-free scrap, from a printed pattern; two steel bushes. About 23 kg.

**How to make it.**

1. **Pattern.** Print the plug in PLA, scaled up 1.3 %, with 3 mm extra on the flange underside and 2 degrees of draft on the flange rim. It is 456 mm across and 289 mm tall: 8 pieces on a 250 mm printer. The plug is open at the top: its inside is a cone 206 mm across at the floor and 259 mm at the top, which already has 6 degrees of draft.
2. **Casting.** Flat-backed like the female: flange top face down on the board, plug pointing up; the sand fills the inside as its own core. No core box.
3. **Plug.** Finish to printed templates within 0.3 mm (radius 115 at the tip, 140 at the flange, 240 long).
4. **Stop face.** Lap the flange underside onto the female mold's lapped face: a little valve grinding paste between them, the plug in the cavity, turn the male back and forth a quarter turn at a time until marking blue shows even contact all round.
5. **Dowels and bushes.** Print eight spacer pads exactly 15.0 mm thick, shaped to the wall. Set them round the plug at two heights, lower the male into the female until the flanges meet, and clamp the flanges together. On a pillar drill, drill an 8 mm pilot through the male flange and 30 mm into the female flange at 202 mm each side of the middle on the left-right line. Separate them. Open the male holes to 22 mm right through and set 22 x 16 x 45 mm steel bushes in them with retaining compound. Open the female holes to 15.8 mm, ream 16 mm, and press in 16 x 50 mm hardened dowels, 30 deep, 20 standing proud.
6. **Stem holes.** Four M12 holes in the plug floor (drill 10.2, tap 20 deep) at 75 mm from the middle, on the left-right and front-back lines.

**How it fits the parts next to it.**

![Figure 16. Joint 10: stem to male mold](05-build-plan/joint-10.png)

*Figure 16. Joint 10, cut on the axis. The stem's disc is bedded on steel epoxy putty on the plug floor and held by four M12 bolts.*

The bushes slide over the dowels (Figure 14); the flange lands on the female's stop ring. The stem bolts in from above (step 13).

**Check before moving on.** The plug is within 0.3 mm of the templates; the male drops onto the dowels and lifts off without force; with the spacer pads in, the wall gap is 15 mm, give or take 0.5, all round.

### 3.9 Male mold slide: stem, load pin and crank

![Figure 17. Making sketch of the stem, load pin and crank](../cad/drawings/PPR-DWG-109.png)

*Figure 17. Stem, load pin and crank making sketch (PPR-DWG-109).*

**What it is and what it is made from.** The square stem the male mold hangs from, the single pin that locks it to the top crossbeam for pressing, and the hand crank that lifts it 200 mm to open the molds. SHS 90 x 90 x 8 mm tube; 42CrMo4 quenched and tempered bar (pin); 10, 15 and 20 mm plate; bought Tr24 x 5 lead screw with nut, two thrust collars and a 260 mm handwheel.

**How to make it.**

1. **Stem.** Saw the tube to 670 mm, square ends. Weld it square in the middle of a 190 x 20 mm disc; drill four 13 mm holes in the disc at 75 mm from the middle, lined up with the tube's faces.
2. **Pin block.** A 74 x 74 x 120 mm steel block that slides inside the tube. Drill a 28 mm hole down its middle (the lead screw passes through it when the stem is cranked up). Weld it inside the tube with its centre 530 mm above the disc.
3. **Pin bore.** Bore 62 mm across the tube walls and the block at the block's centre, square to two faces (a machine shop, or the magnetic drill used for the top beam).
4. **Nut box.** Weld a 10 mm floor plate, with a 28 mm hole in the middle, inside the tube 58 mm below the top. Drop the Tr24 nut (60 x 60 x 40 mm) in on top of it, then weld a 90 x 90 x 10 mm cap plate with a 26 mm hole on the top of the tube. The nut is now captive with 8 mm of free travel below it.
5. **Load pin.** Turn the 60 mm pin with a 173 mm shank and an 80 x 12 mm head from one piece (do not weld quenched and tempered alloy steel), a pull knob on the head, and a 6 mm cross hole for the R-clip 20 mm from the tail.
6. **Crank bracket.** A 200 x 240 x 10 mm base plate with a 100 mm square hole and four 14 mm holes (matching the top beam); two 10 mm side plates 270 mm tall, 80 mm each side of the middle; a 200 x 160 x 15 mm top plate with a 26 mm hole in the middle.
7. **Screw.** The Tr24 x 5 screw, about 360 mm, is held in the top plate by a collar above and below, with the handwheel on top. 40 turns lift the mold 200 mm; the thread is self-locking, so the mold cannot drop if the wheel is let go.

**How it fits the parts next to it.**

![Figure 18. Joint 9: lead screw nut and its float](05-build-plan/joint-09.png)

*Figure 18. Joint 9, cut on the axis. Cranking up, the nut lifts the cap plate; pressing, the stem rides up about 2 mm onto the pin and the nut stays free, so the screw never takes press force.*

**Check before moving on.** The pin slides through the top beam and the stem together by hand when their bores line up; the stem slides between the guides over 200 mm without binding.

### 3.10 Fixed mesh guards

![Figure 19. Making sketch of the fixed guards](../cad/drawings/PPR-DWG-110.png)

*Figure 19. Fixed guards making sketch (PPR-DWG-110), with the right side guard drawn.*

**What it is and what it is made from.** Seven welded-mesh panels that fence the press on all sides and the top. Galvanised welded mesh 12.7 x 12.7 x 1.6 mm (half-inch, about 11 mm clear); 25 x 25 x 3 mm steel angle; 40 x 6 mm flat bar; brush strip.

**How to make it.**

1. Weld a frame of angle for each panel, one leg flat behind the mesh and one pointing inward: right side 635 x 1,391 mm; left side 675 x 1,391; rear 940 x 1,391; two front strips 180 x 1,391; lower front 580 x 320; roof 940 x 675 with a cut-out round the top beam.
2. Fix the mesh to each frame. Clamping it under bolted flat strips avoids zinc fume; if you weld it, grind the zinc off at each weld first (safety stop S3).
3. Pump slot in the right side guard: 30 mm wide from 200 to 420 mm up, centred 218 mm in front of the middle. Frame it with 3 mm strip and fit a brush strip.
4. In the right front strip: a 44 mm square opening for the release shaft and a 40 mm square for the pin cable.
5. Eight standoffs of 40 x 6 mm flat bar, bolted to the outside of the beam webs, reaching out to the side guards.

**How it fits the parts next to it.**

![Figure 20. Joint 11: the pump handle passes the right side guard](05-build-plan/joint-11.png)

*Figure 20. Joint 11. The handle crosses the guard at 25 degrees with about 2 mm clear each side over its whole stroke.*

The side panels bolt to the standoffs; the panels bolt to each other at every corner with M8 bolts. The right front strip sits 40 mm back from the front line, leaving a pocket in front of it for the interlock.

**Check before moving on.** Each panel flat within 3 mm and no heavier than about 10 kg; no loose or sharp wire ends.

### 3.11 Front gate

![Figure 21. Making sketch of the front gate](../cad/drawings/PPR-DWG-111.png)

*Figure 21. Front gate making sketch (PPR-DWG-111).*

**What it is and what it is made from.** The hinged mesh door the operator opens to load and unload. 20 x 20 x 2 mm square tube; the same mesh; two weld-on lift-off hinges; a bent bar handle; 6 mm plate.

**How to make it.**

1. Weld a 572 x 1,063 mm frame of tube with a mid rail; diagonals equal within 2 mm.
2. Fix the mesh on the front face.
3. Weld the gate leaves of two lift-off hinges to the left post, 120 mm in from the top and bottom.
4. Weld the pull handle near the right edge, 905 mm up.
5. Tongue: an arm off the right-hand post and a 6 mm plate that reaches over the lock rod, with a 14 mm hole centred on the rod.

**How it fits the parts next to it.** The gate closes the opening from 380 to 1,451 mm up between the front strips and opens outward to the left, about 105 degrees. With the gate shut and the valve closed, the lock rod stands through the tongue's hole (Figure 24).

**Check before moving on.** It swings without touching the folded rail extension; the tongue hole drops over the rod without forcing.

### 3.12 Gate and pin interlock

![Figure 22. Making sketch of the interlock](../cad/drawings/PPR-DWG-112.png)

*Figure 22. Interlock making sketch (PPR-DWG-112); the views show the lower end.*

**What it is and what it is made from.** A purely mechanical lock round the jack's release valve: the valve can be closed (so the jack can build pressure) only with the gate shut and the load pin fully home, and the gate cannot be opened while the valve is closed. 12 mm steel bar; 20 x 8 mm flat bar; 6 mm plate; two bought universal joints; springs; a push-pull cable.

**How to make it.**

1. **Coupling.** Buy the jack first. Make a coupling that fits over its release screw (most take the slotted end of the pump handle; a tube with a cross pin or a tongue that fits the slot will do).
2. **Release shaft.** 12 mm bar from the coupling out to the right front, two universal joints, then straight forward through the front right strip to a 60 mm knob just outside the guard.
3. **Lock disc.** 80 mm across and 6 mm thick, fixed on the shaft just behind the knob, with one notch 12.5 mm wide and 15.5 mm deep. Set the notch so it comes to the top when the valve has been opened about a third of a turn (check this on the jack you have).
4. **Post.** 20 x 8 mm flat bar from 60 to 1,451 mm up, 330 mm right of the middle, bolted to the right front strip's frame, with guide tabs at 330, 600, 742 and 899 mm up.
5. **Lock rod.** 12 mm bar from the disc rim up through the tabs to 920 mm, with a lift handle at 680 mm and a 24 mm collar at 757 mm.
6. **Gate slider.** A small plate that a spring pushes over the top of the rod when the gate opens; the closing gate's tongue pushes it back.
7. **Pin slider.** A notched plate under the collar that a spring pushes into the rod's path. A plunger on the top beam rests on the load pin's head; when the pin is fully home, the plunger lifts and pulls the slider aside through the push-pull cable.

**How it fits the parts next to it.**

![Figure 23. Joint 5: interlock at the release valve](05-build-plan/joint-05.png)

*Figure 23. Joint 5, seen from behind the disc, valve closed. Turning the knob a third of a turn to open brings the notch to the top; the rod drops into it and the valve is locked open.*

![Figure 24. Joint 6: interlock at the gate](05-build-plan/joint-06.png)

*Figure 24. Joint 6, gate shut, valve closed, rod up. The rod stands through the gate tongue, so the gate stays shut until the valve is opened.*

In use: open the valve, and the rod drops into the notch (valve locked open, gate free). To close the valve you must lift the rod out of the notch, which the gate slider blocks unless the gate is shut and the pin slider blocks unless the pin is home. With the rod lifted, turn the knob to close; the rod rides on the disc rim and stands through the gate tongue.

**Check before moving on.** See the interlock checks in section 5, done with the jack's release valve open and no pressure.

### 3.13 QC flow-test rack

![Figure 25. Making sketch of the QC rack](../cad/drawings/PPR-DWG-113.png)

*Figure 25. QC rack making sketch (PPR-DWG-113).*

**What it is and what it is made from.** A stand that holds four fired pots, full of water, over four buckets for the one-hour flow test. 40 x 40 x 4 mm steel angle; 18 mm exterior plywood.

**How to make it.**

1. Weld two square frames of angle, 780 x 780 mm outside, horizontal leg flat on top.
2. Weld four legs of angle 702 mm long inside the corners, one frame at the top and one with its top 102 mm up.
3. Pot shelf: 780 x 780 mm plywood with four 316 mm holes at 390 mm centres, 195 mm in from each edge; its top is 720 mm up.
4. Bucket shelf: 780 x 780 mm plywood notched round the legs; its top is 120 mm up.
5. Seal the plywood.

**How it fits the parts next to it.** The pot rims (345 mm) rest on the pot shelf and the pots hang through the holes; 20 L buckets no taller than 330 mm stand under them with 35 mm to spare.

**Check before moving on.** A 345 mm rim bears at least 14 mm all round each hole; the rack stands level.

### 3.14 Printed T-gauge (make 4)

![Figure 26. Making sketch of the T-gauge](../cad/drawings/PPR-DWG-114.png)

*Figure 26. T-gauge making sketch (PPR-DWG-114).*

**What it is and what it is made from.** A dipstick that rests across a pot's rim and reads how much water has passed in the hour. PETG, printed.

**How to make it.** Print a 340 x 12 x 12 mm crossbar and an 8 x 8 mm stem 100 mm long below it, with the scale in litres: 0.1 L about every 1.7 mm, 1.0 L at 16.7 mm and 2.5 L at 42.6 mm below the rim. Print the crossbar on the diagonal of a 250 mm bed, or in two halves glued; print the scale in a second colour.

**Check before moving on.** From a pot filled to 10 mm below the rim, draw off exactly 1.0 L; the level reads 16.7 mm within 1 mm.

### 3.15 Bought components

Buy to specification, not brand. Line numbers are those of the bill of materials.

- **Bottle jack (line 4).** 20 t hydraulic bottle jack, about 150 mm stroke and 60 mm ram, base about 160 mm square, with its release screw on the same side as the pump socket, and a pump handle at least 700 mm long and about 20 mm across (or a 20 mm tube extension). Buy it before making the jack plate blocks and the interlock coupling.
- **Return springs (line 6).** Two tension springs, about 300 N each, free length under 250 mm, stretching to about 360 mm between hook ends with the platen up.
- **Joint bolts (line 2).** 16 x M16 x 150 grade 10.9 bolts with nuts and 32 hardened washers.
- **Lead screw set (line 10).** Tr24 x 5 screw about 360 mm with its nut (60 mm square or turned to fit the 74 mm stem bore), two thrust collars and a 260 mm handwheel with a crank knob.
- **Dowels and bushes (lines 8 and 9).** Two 16 x 50 mm hardened dowel pins; two 22 x 16 x 45 mm steel bushes.
- **Floor anchors and fixings (lines 1 and 18).** Four M12 anchors for 80 mm in concrete; M12 bolts, nuts and washers for the studs, jack plate and bracket; M8 bolts for the guards and cup; M6 countersunk screws for the guides.
- **Universal joints, springs and push-pull cable (line 21).** Two 12 mm universal joints; small compression springs for the sliders; a push-pull cable about 1 m.
- **Mesh and hinges (lines 16 and 20).** 12.7 x 12.7 x 1.6 mm galvanised welded mesh, about 5 m² from a 1.2 m roll; two pairs of weld-on lift-off hinges; two weld-on barrel hinges (line 7).
- **QC items (lines 14, 17 and 19).** Four 20 L food-grade buckets, 300 mm across and no more than 330 mm tall; release liners, wire trim tool and sponge; kitchen timer and a 0 to 50 °C thermometer.
- **Consumables (line 18).** E6013 electrodes, grinding discs, steel-filled epoxy putty, marking blue, valve grinding paste, wet-and-dry paper, lead-free primer and paint (never on mold faces).

## 4. Putting it together

In each picture the parts already fitted are grey and the part being fitted is in colour, with an arrow showing the way it goes in. Two people throughout; a hoist for the platen and the top crossbeam.

### Step 1: set out and anchor the feet

![Step 1](05-build-plan/step-01.png)

Place the feet 720 mm apart between centres, parallel and square, and level them with steel shims. Drill the floor through the anchor tubes and fit the four M12 anchors, 80 mm deep, to the anchor maker's torque.

### Step 2: base beam onto the feet

![Step 2](05-build-plan/step-02.png)

Lower the beam over the eight studs (Figure 4). A washer and M12 nut on each, snug. Check level both ways within 1 mm.

### Step 3: jack plate and jack

![Step 3](05-build-plan/step-03.png)

Bolt the jack plate on with four M12 bolts, nuts under the flanges. Stand the jack in its blocks with the pump socket and release valve to the right front (Figure 5).

### Step 4: uprights into the base beam

![Step 4](05-build-plan/step-04.png)

Stand each upright pair on its foot between the beam webs, with a shim each side and the spacer tubes inside, and fit four M16 bolts (Figure 7), snug only. Prop the uprights plumb.

### Step 5: platen over the uprights

![Step 5](05-build-plan/step-05.png)

**Hold point:** safety stop S4. Hoist the platen above the uprights and lower its sleeves over them until the jack pad rests on the ram, fully down.

### Step 6: return springs

![Step 6](05-build-plan/step-06.png)

Hook each spring into the lug on the base beam and the lug under the platen.

### Step 7: stand the stem on the rails

![Step 7](05-build-plan/step-07.png)

With the platen fully down, stand the stem upright on its disc in the middle of the rails and tie it to an upright. It must go in now: its disc is too big to pass through the top beam later.

### Step 8: top crossbeam onto the uprights

![Step 8](05-build-plan/step-08.png)

Hoist the top beam level and lower it over the upright tops, letting the stem's top slide up between its guides. Fit shims, spacer tubes and four M16 bolts each side. Check the uprights plumb within 1 mm per metre and the frame's diagonals equal within 2 mm, then tighten all 16 joint bolts to the bolt maker's torque for M16 grade 10.9. **Hold point:** safety stop S5.

### Step 9: lift the stem, pin it, fit the crank

![Step 9](05-build-plan/step-09.png)

Lift the stem 185 mm until its bore lines up with the top beam's, and push the load pin through with its R-clip. Bolt the crank bracket to the top beam with four M12 bolts and wind the lead screw down into the nut. Then pull the R-clip, draw the pin out 150 mm to its parked position (it stays in the front bores), and crank the stem to the top: 40 turns.

### Step 10: carriage and female mold, out on the extension

![Step 10](05-build-plan/step-10.png)

Swing the extension out. Slide the carriage onto the rails and out until its hooks meet the tipping pins. Two people lift the female mold (36.5 kg) into the carriage; fit both retaining pins.

### Step 11: male mold onto the female mold

![Step 11](05-build-plan/step-11.png)

Two people lower the male mold (23 kg) onto the dowels until the flanges meet. No pot, no clay. Then spread a 3 mm layer of slow-setting steel-filled epoxy putty (at least 30 minutes working time) on the plug floor inside, and go straight on to steps 12 and 13.

### Step 12: slide the molds in, crank down, pin

![Step 12](05-build-plan/step-12.png)

Push the carriage with both molds in to the end stop (the male's top clears the raised stem by about 55 mm) and fold the extension down. Crank the stem down 200 mm and push the pin fully home with its R-clip.

### Step 13: jack up and bolt the male mold to the stem

![Step 13](05-build-plan/step-13.png)

**Hold point:** safety stop S6. Pump the jack slowly by hand until the plug floor just meets the stem's disc (about 110 mm of ram travel), and stop. Put the four M12 bolts down through the disc into the floor (a long extension through the open top of the plug) and tighten. Let the putty cure, then open the release valve and let the platen down. Crank the male mold up and down its full 200 mm to check it runs free.

### Step 14: fixed guards

![Step 14](05-build-plan/step-14.png)

Bolt the standoffs to the beam webs. Fit the side, rear and front panels, the lower front panel and the roof, with M8 bolts at every corner.

### Step 15: front gate

![Step 15](05-build-plan/step-15.png)

Weld the fixed hinge leaves to the left front strip's frame, lift the gate onto its hinges and check it swings clear of the folded extension.

### Step 16: interlock and pump handle

![Step 16](05-build-plan/step-16.png)

Fit the coupling on the release screw, the shaft with its universal joints, the disc and the knob; the post, lock rod and sliders; the plunger over the pin head and its cable to the pin slider. Put the pump handle through the slot into the socket. **Hold point:** safety stop S7.

### Step 17: QC rack

![Step 17](05-build-plan/step-17.png)

Stand the welded frame on a level, drained floor and drop in the two shelves.

### Step 18: buckets, pots and gauge

![Step 18](05-build-plan/step-18.png)

A bucket on the lower shelf under each hole; the pots hang by their rims; the gauge rests across a rim.

## 5. First checks

These are the checks a TRL 4 test report would record; this plan only lists them. Requirement numbers are those of PPR-REQ-001. None involves pressing clay or more than hand pressure.

*Table 2. First checks.*

| Check | Requirement | How | Pass when |
| --- | --- | --- | --- |
| Mold shape | R1 | Printed templates and callipers on both molds | Within 0.3 mm of the template radii |
| Mold closure and wall | R2 | Close the molds on the stop by hand with soft modelling-clay pads at eight places in the wall gap; open and measure the pads | Wall 15 mm, give or take 1; the molds line up within 0.5 mm |
| Stop contact | R3 | Marking blue on the female stop ring; close by hand | Even contact all round the ring |
| Opening | R5 | Jack down, crank up; measure the male tip above the female rim | At least 30 mm (70 mm designed) |
| Stroke used | R5 | Measure ram travel from first mold contact to closed | Within the jack's 150 mm stroke (110 mm designed) |
| Heaviest part | R8 | Weigh each part as lifted | 40 kg or less (platen 39.6 kg designed) |
| Gate interlock | R9 | Release open, no pressure: try to close the release with the gate open; close it with the gate shut, then try to open the gate | Neither is possible |
| Pin interlock | R9 | Gate shut, pin drawn back 10 mm: try to close the release | Not possible |
| Pump handle | R9 | Pump the handle over its full stroke by hand, release open | Never touches the slot frame |
| Guard openings | R9 | A competent person against ISO 13857 | Openings and distances meet the standard |
| Footprint | R11 | Measure the guarded press, extension folded, and the rack | Within 1.0 x 0.7 x 2.0 m and 0.8 x 0.8 m |
| Gauge scale | R6 | Draw off 1.0 L and 2.5 L measured volumes | 16.7 mm and 42.6 mm within 1 mm |
| Mold materials | R12 | Foundry scrap note; look at the mold faces | Lead-free; no paint or oil on the faces |
| Parts cost | R10 | Sum the receipts | Recorded against the value-engineering target |

## 6. Safety stops

Stop at each point. Carry on only when everything listed is true.

- **S1. Before any work.** Welding area ventilated, fire extinguisher at hand, welding helmet, leather gloves and apron, safety glasses and hearing protection in use; safety boots for all lifting.
- **S2. Before the foundry pour (done by the foundry).** The pattern is sealed and dry; the scrap is declared lead-free. Nobody from the build team stands near molten metal.
- **S3. Before welding or grinding galvanised mesh.** The zinc is ground off where you weld, extraction is running, and a P2 or N95 respirator is worn; or clamp the mesh instead of welding it.
- **S4. Before any lift over 25 kg** (platen 39.6 kg, top beam 38 kg, female mold 36.5 kg, base beam 34 kg, uprights 29 kg, male mold 23 kg). Two people or the hoist; clear floor; nobody under a load.
- **S5. Before letting go of the top beam.** Both top joints have all four bolts in; the frame is anchored to the floor.
- **S6. Before the first pump of the jack, even without clay.** All 16 joint bolts tightened; the load pin fully home with its R-clip; nobody's hands between the molds or on the stem; pump slowly and stop at the first contact. The guards are not yet on, so this is the only time the jack moves without them, and only by hand to contact.
- **S7. Before the jack is used again after step 16.** Every guard panel and the gate fitted; the gate and pin interlock checks of section 5 passed with the release open; the pump handle clears the slot; nobody inside the guard.
- **S8. Before any force above hand pressure.** TRL 4 authorisation by Amish, a competent person present, an exclusion zone round the press and the ISO 13857 check done. Never defeat an interlock or remove a guard.
- **S9. Clay work at the press.** Mix and trim wet; wear a P2 or N95 respirator for any dry clay work (silica).

## 7. Tools, skills and workspace

**Tools.** Metal bandsaw or 355 mm abrasive chop saw for channel up to UPN 160; 125 mm angle grinder with cut-off and flap discs; pillar drill to 22 mm with drills 6 to 22 mm; hired magnetic drill with 18 and 62 mm annular cutters; 16 mm reamer; M6, M8 and M12 taps; stick welder of about 160 to 200 A for 3.2 mm E6013; welding table, clamps and magnetic squares; torque wrench covering the M16 10.9 bolt torque (about 300 N·m, check the bolt maker's table); ring spanners 18, 19 and 24 mm; hoist or engine crane rated at least 250 kg (hire); two stepladders or a work platform; 3 m tape, 1 m steel rule, callipers to 300 mm, engineer's square, 600 mm spirit level, feeler gauges, marking blue; 3D printer with at least a 250 x 250 mm bed; die grinder with carbide burrs, files, abrasive paper to 240 grit, a sheet of 6 mm float glass at least 500 mm square; jigsaw or router with a trammel for the 316 mm shelf holes.

**Skills.** A competent stick welder for the load-path welds (doublers, jack pad, sleeves, pin block, stem to disc); ordinary shop skill for the rest. Care with a magnetic drill. Basic 3D printing and pattern finishing. A local aluminium foundry for the two castings, able to declare lead-free charge material. A machine shop only if you would rather have the pin turned and the stem bored than do it yourself. No electrical work: the press has no power.

**Workspace.** A covered, level concrete floor about 5 x 4 m with 3 m clear height for standing the uprights and lowering the top beam; a separate ventilated welding and grinding area; a clean bench for patterns and mold finishing; a level, drained spot for the QC rack.

**Personal protective equipment.** Welding helmet, leather gloves and apron; safety glasses for cutting, drilling and grinding; hearing protection; safety boots with toe caps for every lift; a fitted P2 or N95 respirator for galvanised mesh, PLA and filler sanding and dry clay; nitrile gloves for epoxy.

## 8. Where the numbers come from

- Model and constructability checks: `cad/src/model.py` (`python cad/src/model.py --check`, closed, open and demolding positions); STEP and STL exports in `cad/step/` and `cad/stl/`.
- Pictures: `cad/src/build_plan_media.py`, using `.kit/build_views.py`; written to `docs/05-build-plan/` and `cad/drawings/PPR-DWG-101` to `PPR-DWG-114`.
- General arrangement: `cad/drawings/PPR-DWG-001.pdf`, Rev P5.
- Calculations: `docs/04-calcs/01-sizing.md` (PPR-CAL-001 v0.6) and `docs/04-calcs/sizing.py`; frame and joints section 4, travel and crank section 5, alignment section 7, patterns section 8, masses section 10, tipping section 11.
- Bill of materials: `bom/bom.csv`.
- Decisions: `docs/decisions/0004-design-for-construction.md` (PPR-DDR-004), with PPR-DDR-001 to PPR-DDR-003.
- Requirements: `docs/03-requirements.md` (PPR-REQ-001 v0.8).
