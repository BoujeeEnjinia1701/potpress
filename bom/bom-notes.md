# BOM notes

Prices are indicative 2026 estimates for regional small-town suppliers, derived in PPR-CAL-001 (`python docs/04-calcs/sizing.py`) from the model masses: steel at $1.30/kg, cast aluminum at 1.35 kg poured per kg of casting and $2.00/kg scrap plus a $1.50/kg foundry fee, and PLA at $20/kg. Bought items are regional retail estimates. They are not quotes. Item numbers match the exploded view (`media/exploded.png`). Items 15 and 17 to 19 are not modeled. Items 16, 20 and 21 are the guarded version decided by Amish on 2026-09-26 (PPR-DDR-003): guard steel is priced at $1.30/kg, galvanized welded mesh at about $6/m² for the 12.7 mm mesh and about $10.50/m² for the 6.35 mm mesh (estimate, 2026-10-03), and hinges, springs and cable as regional retail estimates.

Item 11, the pressed filter pot, is the product. It is listed so the numbering matches the exploded view and is priced at $0.

| Group | Items | Cost |
| --- | --- | --- |
| Press | 1 to 10, 15 to 18, 20, 21 | $1,086 |
| QC rack | 12 to 14, 19 | $83 |
| **Total** | all | **$1,169** |

Value-engineering target: USD 1,060. Estimated cost of the constructable design: USD 1,169 (USD 109 over the target). The target is the hypothetical control target in `project.yaml` (`budget_usd`), not a spending limit; the design decisions register (PPR-DEC-001) lists the cost drivers and the savings worth trying.

Changes on 2026-10-03: the four guard fixes from the ISO 13857 desk check, decided by Amish on 2026-10-03 ("move forward with the four guard fixes. I accept the cost."). Item 16 goes from $73 to $90: 6.35 mm (1/4 in) welded mesh with 0.9 mm wire on the front strips, lower front panel and roof (1.1 m², the price difference from the 12.7 mm mesh, $5); two small-hole plates behind the front right strip with a 20 mm hole round the release shaft and a 10 mm grommeted hole round the pin cable ($2); two 3 mm cover plates on the top beam from the crank bracket to the beam ends, which also close the open tops of the upright channels ($7); and 2 mm sheet covers on the front and back of the crank bracket ($4). Item 20 goes from $22 to $25 for the 6.35 mm mesh on the gate (0.61 m²). The plates and covers are priced by their mass in the model at $1.30/kg plus their bolts. Together the fixes add $20, against the "about USD 15" estimate in the register; the cover plates cost more than estimated because they now also cover the upright channel tops. The total goes from $1,149 to $1,169. The guards, gate and interlock now weigh about 51 kg (estimate): the plates and covers add 4.4 kg from the model and the finer mesh is 1.6 kg lighter than the mesh it replaces.

Changes on 2026-10-02: item 16 gains the fixed inner shield behind the pump slot that Amish decided on 2026-10-02 (a 2 mm folded sheet tunnel with a flange and a stay, 2.8 kg from the model at $1.30/kg plus $2 for bolts, $6), and the slot is lengthened to 272 mm so each end stands 25 mm beyond the handle at the ends of its stroke. The brush strip is dropped; the shield is the guard. Item 16 goes from $67 to $73 and the total from $1,143 to $1,149. The guards, gate and interlock weigh about 48 kg with the shield (estimate; the model draws the mesh at every eighth wire).

Earlier changes: the constructable design (PPR-DDR-004, 2026-09-30) took the total from $1,051 to $1,143 (steel base plate under the female mold, thicker mold flanges, dowels and bushes, floor anchors, bolted jack plate and heavier feet, adapter disc and nut box, interlock details). The guarded version (PPR-DDR-003, 2026-09-26) took it from $984 to $1,051. Mold scrap must be lead-free (decided, PPR-DDR-001 item 15), and item 21 includes the decided pin-presence interlock (PPR-DDR-001 item 13).
