# BOM notes

Prices are indicative 2026 estimates for regional small-town suppliers, derived in PPR-CAL-001 (`python docs/04-calcs/sizing.py`) from the model masses: steel at $1.30/kg, cast aluminum at 1.35 kg poured per kg of casting and $2.00/kg scrap plus a $1.50/kg foundry fee, and PLA at $20/kg. Bought items are regional retail estimates. They are not quotes. Item numbers match the exploded view (`media/exploded.png`). Items 15 and 17 to 19 are not modeled. Items 16, 20 and 21 are the guarded version decided by Amish on 2026-09-26 (PPR-DDR-003): guard steel is priced at $1.30/kg, galvanized welded mesh at about $6/m², and hinges, springs and cable as regional retail estimates.

Item 11, the pressed filter pot, is the product. It is listed so the numbering matches the exploded view and is priced at $0.

| Group | Items | Cost |
| --- | --- | --- |
| Press | 1 to 10, 15 to 18, 20, 21 | $970 |
| QC rack | 12 to 14, 19 | $81 |
| **Total** | all | **$1,051** |

The total is $1,051 against the $1,060 budget in `project.yaml`, so requirement R10 is met on paper with a $9 (0.8 %) margin. Before the guarded version the total was $984 against $990. The guards and gate replace the earlier $55 allowance in item 16 with priced lines: fixed mesh guards $67 (4.3 m² of mesh and 24 m of angle), the front gate with hinges $21 and the gate interlock with the release valve extension and the pin-presence plunger $34, a net rise of $67. That put the BOM $61 (6.2 %) over $990; Amish raised the budget to $1,060 on 2026-09-27 (PPR-DDR-003). The largest items are the uprights with their bolts ($124), the patterns ($112), the female mold ($102) and the male mold slide with its alloy-steel pin and lead screw ($92). Mold scrap must be lead-free (decided, PPR-DDR-001 item 15), and item 21 includes the decided pin-presence interlock (PPR-DDR-001 item 13).
