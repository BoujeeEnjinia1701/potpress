---
doc_id: PPR-REG-001
title: PotPress regulatory and standards register
project: PotPress
doc_type: Regulatory register
version: '0.2'
status: Draft
date: '2026-10-23'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: '0.1'
  date: '2026-10-23'
  author: Amish Chadha
  change: First register (kit 1.8 upgrade); sources checked 2026-10-23
- version: '0.2'
  date: '2026-10-23'
  author: Amish Chadha
  change: EN 601, ASTM C326, DIN 580 and EN 1005-3 added with the STEM check fixes (PPR-DDR-006)
---

# PotPress regulatory and standards register

PotPress is workshop machinery that makes a drinking-water product, so two sets of rules matter: machine safety for the press, and product evaluation for the filters, which belongs to the factory. This register is not legal advice; anything marked "to assess" needs a qualified reviewer before any product claim. Method: STANDARDS section 23. Sources checked 2026-10-23.

Table 1. Regulatory and standards register.

| # | Standard or regulation | Jurisdiction | What it covers | Applicability to this design | Owner (role) | Status |
| --- | --- | --- | --- | --- | --- | --- |
| G1 | ISO 12100:2010, risk assessment and risk reduction | International | General principles of machine safety design | The hazard analysis in PPR-RSK-001 follows its method | Design lead | Applies; first pass in PPR-RSK-001 |
| G2 | ISO 13857:2019, safety distances | International | Reach through and over guards by upper and lower limbs | Fixed mesh guards and front gate (PR-009) | Design lead; competent person signs | Met by design for Table 4 (PPR-CAL-001, section 15); Table 7 and the floor gap to assess (STEM E3); signature is a hold point |
| G3 | ISO 14119:2024, interlocking devices with guards | International | Design and choice of guard interlocks, defeat resistance | Gate interlock on the jack release and the pin-presence interlock (PPR-DDR-003) | Design lead | To assess against the standard's defeat and coding rules |
| G4 | EU Machinery Directive 2006/42/EC, replaced by Machinery Regulation (EU) 2023/1230 from 20 January 2027 | European Union | Essential health and safety requirements and CE marking for machinery placed on the EU market | Only if a press is sold or put into service in the EU; the open design itself is not placed on the market | Builder who places it on the market | Does not apply to the open design; certification needed later for any EU sale |
| G5 | National workplace machinery rules in the partner's country | Partner country | Guarding and use of machinery at work | The partner factory's workshop | Partner factory | To assess when a partner is chosen |
| G6 | EN 1993-1-8 and EN 1993-1-9 (bolted joints, fatigue); EN 10025-2 (S275 steel); ISO 898-1 (bolt grades) | Europe and international | Structural design values | Frame checks in PPR-CAL-001 | Design lead | Applies; used as design values |
| G7 | WHO International Scheme to Evaluate Household Water Treatment Technologies | International | Performance targets for household water treatment: 3 stars at 4 log bacteria, 5 log viruses, 4 log protozoa; 2 stars at 2, 3 and 2 log | The filters a factory makes, not the press. PotPress makes no microbial claim (STEM B1) | Partner factory | Does not apply to the press; the factory owns any filter claim (PRB, out of scope) |
| G8 | WHO silver in drinking water, provisional reference value 0.1 mg/L | International | Silver in treated water | Silver treatment is the factory's process; the QC rack's test water is not for drinking | Partner factory | Does not apply to the press; cited for the QC rack's safety note |
| G9 | Food-contact material rules for parts touching clay or test water | Partner country | Plastics and metals in contact with drinking-water products | Polyethylene liners and buckets, aluminium molds (PR-012) | Design lead | To assess for the partner country; molds checked against EN 601 (G11) |
| G11 | EN 601, aluminium castings for use in contact with foodstuff (revised 2026) | Europe (used as the reference limit) | Chemical composition limits, including lead and cadmium, for castings that touch food | Mold castings: each melt checked by OES or XRF before pouring (PR-012, PPR-DDR-006) | Foundry; design lead | Applies as the reference; limit values to confirm |
| G12 | ASTM C326, drying and firing shrinkage of ceramic whiteware clays | International (test method) | Test-bar method for linear shrinkage | Partner clay shrinkage before patterns are printed (PR-001, PPR-DDR-006) | Partner factory | Applies as the method |
| G13 | DIN 580 lifting eye bolts; EN 1005-3 recommended force limits for machinery operation | Europe | Eye bolt use and loading; operator force limits | Lifting set (PR-008); pump handle limit (PR-004) | Design lead | Applies; EN 1005-3 assessment of the handle to do |
| G10 | CMWG best practice recommendations for ceramic pot filters (2011) | International (voluntary) | Factory practice, including filter size, flow testing and QC records | QC rack and flow band (PR-006) | Partner factory | Applies as guidance |

Status: to assess, applies, does not apply, met by design, certification needed later.

## Sources

- European Agency for Safety and Health at Work. "Regulation (EU) 2023/1230 on Machinery." https://osha.europa.eu/en/legislation/directive/regulation-eu-20231230-machinery (checked 2026-10-23).
- International Organization for Standardization. *ISO 12100:2010, Safety of Machinery: General Principles for Design.* https://www.iso.org/standard/51528.html (checked 2026-10-23).
- International Organization for Standardization. *ISO 14119:2024, Safety of Machinery: Interlocking Devices Associated with Guards.* https://www.iso.org/standard/75942.html (checked 2026-10-23).
- International Organization for Standardization. *ISO 13857:2019, Safety of Machinery: Safety Distances to Prevent Hazard Zones Being Reached by Upper and Lower Limbs.* As used in PPR-CAL-001.
- World Health Organization. *Results of Round I of the WHO International Scheme to Evaluate Household Water Treatment Technologies.* Geneva: WHO, 2016. Round II: https://www.who.int/publications/i/item/9789241516037 (checked 2026-10-23).
- World Health Organization. *Silver in Drinking-Water: Chemical Fact Sheet.* 2022.
- CEN. *EN 601, Aluminium and Aluminium Alloys: Castings; Chemical Composition of Castings for Use in Contact with Foodstuff.* Revised 2026. https://knowledge.bsigroup.com/products/aluminium-and-aluminium-alloys-castings-chemical-composition-of-castings-for-use-in-contact-with-foodstuff (checked 2026-10-23).
- ASTM International. *ASTM C326, Standard Test Method for Drying and Firing Shrinkages of Ceramic Whiteware Clays.*
- Ceramics Manufacturing Working Group. *Best Practice Recommendations for Local Manufacturing of Ceramic Pot Filters for Household Water Treatment.* 2011.
