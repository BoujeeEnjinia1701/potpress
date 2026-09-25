---
doc_id: PPR-PRB-001
title: PotPress problem statement
project: PotPress
doc_type: Problem statement
version: "0.2"
status: Draft
date: '2026-09-25'
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
  change: Populate to TRL 2 (users, context, constraints, out of scope, prior work with sources, co-design checklist)
---

# PotPress problem statement

Ceramic pot filters work well, but local producers have no low-cost way to form them consistently. The presses in use are either imported at about $3,000 to $3,500 or built one at a time from drawings that are not openly maintained, and filter quality depends on how evenly each pot is pressed and on a manual flow-rate check. PotPress is an open, garage-buildable filter press with parametric mold geometry, paired with a simple flow-rate test rack, so that a small factory can make and check filters consistently for well under the cost of an imported press. Design with, not for: requirements must come from co-design sessions and field trials with the intended users through a local partner.

## The problem

About 2.1 billion people still lacked safely managed drinking water in 2024, and 106 million drank untreated surface water ([WHO and UNICEF JMP, 2025](https://www.who.int/news/item/26-08-2025-1-in-4-people-globally-still-lack-access-to-safe-drinking-water---who--unicef)). Household water treatment fills the gap where piped, treated water will not arrive soon.

The ceramic pot filter is one of the best-studied household options. It is a flowerpot-shaped vessel of fired clay mixed with a burnout material such as sawdust or rice husk, usually coated with colloidal silver or silver nitrate, that sits in a plastic or ceramic receptacle with a tap. The design dates from 1981, when Dr. Fernando Mazariegos developed it at ICAITI in Guatemala; Potters for Peace spread it after Hurricane Mitch in 1998, and it is now made by more than 50 independent workshops in over 30 countries, typically about 280 mm wide by 250 mm deep (11 by 10 in) with a flow of 1.5 to 2.5 L/h ([Potters for Peace](https://www.pottersforpeace.org/ceramic-water-filter-project)). In a randomized trial in Cambodia, households using locally made filters had about half as much diarrheal disease as controls (longitudinal prevalence ratio 0.51) ([Brown, Sobsey and Loomis, 2008](https://researchonline.lshtm.ac.uk/id/eprint/1699/)), and laboratory tests of the same filters showed a mean E. coli reduction of about 99 % ([Brown and Sobsey, 2010](https://iwaponline.com/jwh/article/8/1/1/1877/Microbiological-effectiveness-of-locally-produced)).

The technology is proven, but making it well is hard for a small workshop:

1. **The press is the costly item.** The Potters for Peace press uses a 20 t hydraulic jack, a removable female mold and a male mold on a movable shaft, and costs about $3,000 to $3,500 imported before shipping and duties. A press built locally in Nigeria from cast iron, steel and scrap aluminum cost about $1,000 ([Manufacturing a Ceramic Water Filter Press for Use in Nigeria, IntechOpen](https://www.intechopen.com/chapters/71402)), and a Penn State team showed a proof-of-concept press that two people built in two days for about one-tenth of the cost of popular presses ([Henry, Maley and Mehta](https://sites.psu.edu/hese/2016/03/16/designing-a-low-cost-ceramic-water-filter-press/); [paper, IJSLE](https://ojs.library.queensu.ca/index.php/ijsle/article/view/4532)). Neither is maintained as an open, parametric design.
2. **Mold making needs tools the workshop may not have.** The Nigerian team had trouble finding a lathe large enough to finish the cast molds, and dimensioning errors in the drawings had to be corrected during machining (IntechOpen chapter above).
3. **Consistency decides whether a filter works.** Flow rate and bacteria removal depend on the burnout ratio, burnout particle size and firing temperature; for example, larger rice husk particles raised flow but cut E. coli log reduction from 2.8 to 0.7 ([Heijman et al., 2015](https://www.academia.edu/68960939/Critical_parameters_in_the_production_of_ceramic_pot_filters_for_household_water_treatment_in_developing_countries)). An even wall, pressed to the same thickness every time, is the part of that chain the press controls.
4. **Quality control is manual and varies by factory.** Factories soak each fired filter for 4 to 24 h, fill it and measure the drop after one hour with a calibrated dipstick (a "T-device"), but acceptance bands differ: 2.0 to 3.0 L/h at one factory, 1.5 to 3.0 L/h at another and 1.0 to 2.5 L/h in the first hour in Nicaragua ([Rayner, 2009, WEDC](https://bdd.pseau.org/outils/ouvrages/wedc_current_practices_in_manufacturing_locally_made_ceramic_pot_filters_2009.pdf)). Industry guidance is gathered in the Ceramics Manufacturing Working Group's best practice recommendations ([CMWG, 2011](https://www.ircwash.org/sites/default/files/CMWG-2011-Best.pdf)).

## Users and context

| User | Need | Context |
| --- | --- | --- |
| Small filter factory or pottery cooperative | Press 50 or more filters a day with even walls; replace or repair the press locally | Three to four workers, a kiln, a mixing area and drying racks |
| NGO or social enterprise starting a factory | A press and QC rig it can build or commission locally instead of importing | Start-up budget, often in a region without a filter factory yet |
| Local fabrication shop | Build the frame and have the molds cast from open drawings | Stick welder, drill press, hand tools; access to an aluminum foundry is uncertain |
| QC technician | Test every fired filter for flow and record the result the same way each time | Soaking tanks, buckets, a timer; results logged by hand |
| University or research lab | A repeatable press to study mix, pressing and firing variables | Lab bench or workshop; needs repeatability more than throughput |

### Operating environment

- **Material:** a damp, stiff mix of about 60 to 70 % clay by mass with rice husk or sawdust and water; about 8 to 9.5 kg of mix per filter ([Rayner, 2009](https://bdd.pseau.org/outils/ouvrages/wedc_current_practices_in_manufacturing_locally_made_ceramic_pot_filters_2009.pdf)). Clay and burnout dust is abrasive and wet.
- **Workshop:** open-sided shed, 15 to 40 °C, high humidity in the wet season, earth or concrete floor, intermittent or no mains power.
- **Duty:** one pressing about every 5 min over a shift, 6 days a week (estimate).
- **Supply chain:** steel channel, plate, bottle jacks and hardware are available in most regional towns; aluminum casting may mean a trip to a city foundry; 3D printing is available at universities and maker spaces.

## Constraints

- Garage-buildable prototype, about $600 USD in parts.
- Frame buildable with a stick welder, grinder and drill press; no machining that needs a large lathe or mill.
- No mains power needed to press or to run the flow test; hand-pumped hydraulics only.
- Mold geometry defined parametrically so that a factory can change size or wall thickness and generate new patterns and gauges from the same source.
- Everything that touches the clay or the test water must not contaminate a drinking-water product.

## Out of scope

- The filter formulation, kiln, firing schedule and silver treatment. PotPress presses and checks the pot; it does not change the recipe. Silver application is noted only for safety.
- The receptacle, lid and tap of the household unit.
- Certification of the filters. Factories should follow the CMWG recommendations and the WHO scheme for evaluating household water treatment products ([WHO](https://www.who.int/tools/international-scheme-to-evaluate-household-water-treatment-technologies)).
- Powered or automated presses.

## Prior work

- **Potters for Peace press and factory model.** The reference design and factory practice that most filter workshops use; a 20 t jack press with a removable female mold ([IntechOpen chapter](https://www.intechopen.com/chapters/71402); [Potters for Peace](https://www.pottersforpeace.org/ceramic-water-filter-project)).
- **Locally built presses.** The Nigerian press at about one-third of the imported cost, and the Penn State low-cost press ([Henry, Maley and Mehta](https://sites.psu.edu/hese/2016/03/16/designing-a-low-cost-ceramic-water-filter-press/)).
- **Manufacturing practice surveys.** Rayner's survey of factory practice, including presses (screw and hydraulic), mold materials (aluminum, cast iron, wood and cement), mixes, firing and QC ([Rayner, 2009](https://bdd.pseau.org/outils/ouvrages/wedc_current_practices_in_manufacturing_locally_made_ceramic_pot_filters_2009.pdf)), and the CMWG best practice recommendations ([CMWG, 2011](https://www.ircwash.org/sites/default/files/CMWG-2011-Best.pdf)).
- **Performance studies.** Health and microbiological effect ([Brown, Sobsey and Loomis, 2008](https://researchonline.lshtm.ac.uk/id/eprint/1699/); [Brown and Sobsey, 2010](https://iwaponline.com/jwh/article/8/1/1/1877/Microbiological-effectiveness-of-locally-produced)) and production parameters ([Heijman et al., 2015](https://www.academia.edu/68960939/Critical_parameters_in_the_production_of_ceramic_pot_filters_for_household_water_treatment_in_developing_countries)).

## Open questions

- Which partner factory or organization first (for example an existing Potters for Peace network factory, an NGO planning a new factory, or a university ceramics lab)? Proposed, awaiting Amish.
- Which reference filter size to model first: the common 280 by 250 mm form, or the partner's own mold?
- Is a local aluminum foundry within reach of the first partner, or must the molds use another material?
- What flow acceptance band does the partner use, and does it correct for water temperature?

## User research and co-design

This design is for communities the author is not part of, so requirements come from the people who will use it.

- [ ] Identify a local partner organization (Helpful Engineering network, NGO or university)
- [ ] Run co-design sessions with intended users; record who, where and what was learned
- [ ] Validate filter size, throughput, pressing and cost assumptions with a working filter factory
- [ ] Revise requirements (REQ) from findings before freezing the design
