"""PotPress STEM check calculations (PPR-STM-001, STANDARDS section 20).

Run from the repo root:  python docs/04-calcs/stem_check.py
Writes docs/04-calcs/stem_results.csv. Design values are taken from PPR-CAL-001 v0.11
(docs/04-calcs/sizing.py); each check here is a first-order screen of a claim, not the sizing itself.
"""
import math, sys
sys.path.insert(0, ".kit")
from stem_check import Check, limits, G, WITHIN, PLAUSIBLE, FIX  # noqa: F401

c = Check()
JACK_N = 20e3 * G            # 20 t rated jack, 196 kN
DESIGN_N = 1.5 * JACK_N      # 294 kN design load (R3)

# Physics: strength of materials (values from PPR-CAL-001 sections 4 and 10)
c.claim("S1", "Top and base beams (2 x UPN 160, S275) stay below yield at 294 kN", "Physics", "Strength of materials",
        "Beam bending; S275 yield 275 MPa (EN 10025-2)", 190, 275, "MPa", closed_by="PPR-CAL-001 section 4")
c.claim("S2", "60 mm 42CrMo4 load pin carries 294 kN in bending without yield", "Physics", "Strength of materials",
        "Pin in double shear and bending; 42CrMo4 quenched and tempered yield about 650 MPa", 272, 650, "MPa",
        closed_by="PPR-CAL-001 section 4")
c.claim("S3", "M16 10.9 joint bolts carry their share of 294 kN in double shear", "Physics", "Strength of materials",
        "Bolt shear resistance 0.5 x fub / gamma_M2 = 0.5 x 1000 / 1.25 = 400 MPa (EN 1993-1-8)", 117, 400, "MPa", closed_by="PPR-CAL-001 section 4")
c.claim("S4", "Deflection between the molds below 1 mm at the 10 t structural check case", "Physics", "Mechanics and statics",
        "Beam and column elastic deflection, E = 200 GPa", 0.66, 1.0, "mm", closed_by="PPR-CAL-001 section 4")

# Joint slip (independent review, 2026-10-24): preloaded M16 10.9, two faying surfaces, slip factor 0.2 (class D)
preload = 0.7 * 1000 * 157 / 1e3                                     # kN
c.claim("S11", "The bolted upright joints do not slip in their 18 mm holes at 294 kN (preloaded M16 10.9)", "Physics", "Mechanics and statics",
        "Slip resistance n mu Fp,C with Fp,C = 0.7 fub As (EN 1993-1-8 category C practice); slip factor 0.2 for unprepared surfaces", DESIGN_N / 2 / 4 / 1e3,
        2 * 0.2 * preload, "kN per bolt", closed_by="PPR-BLD-001 step 8 (preload torque); PPR-CAL-001 v0.12 section 4")

# Physics: the pressing force the process needs is within what the jack delivers
c.claim("S5", "A pot filter can be formed within the 5.4 t working force limit", "Physics", "Mechanics and statics",
        "A low-cost press forms round-bottom pot filters with a 2 t jack (Henry, Maley and Mehta 2013); factories press flat-bottomed 280 mm pots on 20 t jack presses without a published working force. The pressed pot here is about 18 % larger than the factory form, so the force it needs is found in trials (decided 2026-10-02); 10 t is a structural check case, not a working force (D9, decided by Amish 2026-10-25)",
        2.0, 5.4, "t", closed_by="Pressing trials with a partner factory, starting near 2 t (decided 2026-10-02); working force limit 5.4 t (D9, decided by Amish 2026-10-25)")
area = 0.1104   # projected area of the pressed (green) pot, m2 (PPR-CAL-001 section 3)
c.order_of_magnitude("S6", "Mean pressure on the clay at 10 t is about 0.9 MPa", "Physics", "Mechanics and statics",
                     claimed=0.89, estimate=10e3 * G / area / 1e6, unit="MPa", law="Pressure = force / projected area",
                     closed_by="PPR-CAL-001 section 3")

# Physics: human effort on the pump (fluid power and ergonomics)
load_stroke_m, approach_m, pump_s = 0.02, 0.09, 60.0     # load builds over the last 20 mm; about 1 min of pumping per cycle
work_j = 10e3 * G * load_stroke_m / 2 + 0.5e3 * G * approach_m
c.claim("S7", "One operator can pump each pressing by hand (power, at 10 t with 85 % jack efficiency)", "Physics", "Fluid mechanics",
        "Work = force x distance: the load builds over the last 20 mm (half of 10 t on average) after a 90 mm approach at 0.5 t, about 1 min of pumping, 85 % pump and seal efficiency; sustained human output about 75 W", work_j / pump_s / 0.85, limits.HUMAN_SUSTAINED_W, "W",
        closed_by="PPR-CAL-001 section 6 (cycle breakdown)")
handle_n = lambda tonnes: tonnes * 1e3 * G / (math.pi * 0.030**2) * math.pi * 0.008**2 / 30   # 60 mm ram, 16 mm piston, lever ratio 30
c.cited("S8", "Pump handle force stays within repetitive-work guidance at the working force limit of 5.4 t", "Biology", "Ergonomics",
        "Handle force = jack force x piston-to-ram area ratio / lever ratio / efficiency: about 126 N at 5.4 t frictionless and about 148 N with 85 % pump and seal efficiency, inside the 150 N screening limit (the earlier 6.4 t limit gave about 175 N with efficiency); about 70 strokes a pressing at about 50 a minute; EN 1005-3 frequency and duration multipliers not yet applied",
        f"{handle_n(5.4):.0f} N frictionless, {handle_n(5.4) / 0.85:.0f} N at 85 % efficiency, against a 150 N screen; working force limit lowered from 6.4 to 5.4 t (D9, decided by Amish 2026-10-25)",
        PLAUSIBLE, "To confirm: EN 1005-3 assessment with the bought jack's piston, lever and efficiency data (PPR-CAL-001, next session); the two-speed pump (D6) stays open if trials need more than 5.4 t")

# fatigue screen at the 10 t structural check case (D9), about 20,000 pressings a year
c.claim("S9", "Pin, beams and cast molds survive 20,000 pressings a year at 10 t", "Physics", "Strength of materials",
        "Fatigue: beam welded detail category 71 MPa at 2 million cycles (EN 1993-1-9); 42CrMo4 endurance about 400 MPa; cast Al-Si about 50 MPa",
        190 / 3, 71, "MPa", closed_by="This file (stress at 10 t is one third of the 294 kN value)")

# Mathematics: geometry, rates and balances
r1, r2, h = 0.140, 0.115, 0.240
vol_l = math.pi * h / 3 * (r1**2 + r1 * r2 + r2**2) * 1000
c.order_of_magnitude("M1", "Reference filter holds 12.30 L to the brim", "Mathematics", "Units and dimensional analysis",
                     claimed=12.30, estimate=vol_l, unit="L", factor=1.05, law="Frustum volume", closed_by="PPR-CAL-001 section 2")
c.order_of_magnitude("M2", "69 pots per 6 h at a 5.2 min cycle", "Mathematics", "Orders of magnitude",
                     claimed=69, estimate=6 * 60 / 5.2, unit="pots", factor=1.05, law="Rate = time / cycle", closed_by="PPR-CAL-001 section 6")
gauge_area = 0.1e-3 / 1.69e-3
c.order_of_magnitude("M3", "0.1 L reads as 1.69 mm on the T-gauge", "Mathematics", "Units and dimensional analysis",
                     claimed=gauge_area, estimate=math.pi * 0.1375**2, unit="m2 of water surface", factor=1.1,
                     law="Volume = area x height (water surface about 275 mm across)", closed_by="PPR-CAL-001 section 9")
c.order_of_magnitude("M4", "Charge of 9.59 kg of mix per pot", "Mathematics", "Orders of magnitude",
                     claimed=9.59, estimate=8.75, unit="kg", law="Factory practice 8 to 9.5 kg per filter (Rayner 2009)",
                     closed_by="PPR-CAL-001 section 2")
tip_nm = 352 * G * (0.320 - 0.074)
c.order_of_magnitude("M5", "A push of about 850 N at 1 m tips the unanchored press (centre of mass 246 mm behind the front foot edge, carriage out)", "Physics", "Mechanics and statics",
                     claimed=850, estimate=tip_nm, unit="N m", factor=1.05, law="Restoring moment = weight x lever arm",
                     closed_by="PPR-CAL-001 section 11")

# Chemistry: mass balance through drying and firing
charge, pressed = 9.59, 8.72
clay = 0.59 * pressed
husk_ash = 0.16 * pressed * 0.175          # rice husk leaves 15 to 20 % ash, mostly silica
fired = clay * (1 - 0.10) + husk_ash
c.order_of_magnitude("C1", "Fired pot of 4.88 kg from an 8.72 kg pressed pot", "Chemistry", "Physical chemistry",
                     claimed=4.88, estimate=fired, unit="kg", factor=1.1,
                     law="Mass balance: water leaves, clay loses about 10 % on ignition, rice husk leaves 15 to 20 % silica ash (ash now in CAL)",
                     closed_by="PPR-CAL-001 v0.11 section 2 (ash added)")
c.cited("C2", "Rice husk or sawdust burns out on firing and leaves the pores that set flow", "Chemistry", "Materials and polymer chemistry",
        "Combustion of cellulose well below the 800 to 900 C firing; pore size set by burnout particle size (Heijman et al. 2015)",
        "PotPress controls wall thickness only; recipe and firing out of scope", WITHIN, "PPR-PRB-001")
c.cited("C3", "Aluminum mold faces and polyethylene liners do not contaminate the pot", "Chemistry", "Inorganic",
        "Aluminium worn off by wet clay oxidises to alumina, already a clay constituent; the real risk is lead, cadmium, copper or zinc in scrap alloy, and wheel scrap carries lead balance weights and brass valve stems",
        "A356 wheel scrap only, sorted before melting (weights, valve stems, steel and paint removed); a chill sample of each melt checked by spark OES, or handheld XRF for lead, before pouring; lead and cadmium within the EN 601 limits (values to confirm); recorded per heat (PR-012 verification)", WITHIN, "PPR-DDR-006 (D5); independent review 2026-10-23")
c.cited("C4", "Silver treatment is outside PotPress; a silver-treated filter can stay under WHO's 0.1 mg/L reference value", "Chemistry", "Environmental chemistry",
        "WHO silver chemical fact sheet (2022): provisional reference value 0.1 mg/L, no health-based guideline value",
        "No claim made by PotPress; noted for the factory", WITHIN, "Out of scope (PRB)")

# Temperature correction of flow (water viscosity)
mu = lambda t: 2.414e-5 * 10 ** (247.8 / (t + 273.15 - 140))    # Vogel-type fit for water, Pa s
per_c = (mu(24) / mu(26) - 1) / 2 * 100
c.order_of_magnitude("C5", "Flow changes about 2.3 % per C near 25 C", "Chemistry", "Physical chemistry",
                     claimed=2.3, estimate=per_c, unit="% per C", factor=1.25, law="Darcy flow scales with 1/viscosity of water",
                     closed_by="PPR-CAL-001 section 9")

# Biology: what is and is not claimed
c.cited("B1", "PotPress makes no pathogen-removal claim; locally made pot filters cut E. coli by about 99 %", "Biology", "Microbiology",
        "Brown and Sobsey 2010; WHO HWT scheme 2-star target is 2 log for bacteria",
        "The press makes consistent pots; removal must be lab-tested per batch (stated in PRC Safety)", WITHIN, "PPR-PRC-001 Safety")
c.cited("B2", "Parts over 25 kg (female mold 39.6 kg, platen 39.6 kg, top crossbeam 38.0 kg, base beam 34.2 kg, male mold 26.3 kg) are lifted safely", "Biology", "Human physiology and biomechanics",
        "Team lifting: two people carry about two thirds of their combined capacity (about 31 kg at 23 kg each), lower still at 1.5 m height and for bulky loads. M12 eye bolt in steel plate or 26 mm of Al-Si thread: tens of kN to strip against about 0.2 kN per leg",
        "Every part over 25 kg goes on a 0.5 t chain block: female mold by two M12 DIN 580 eye bolts in its steel base plate, male mold by two in its flange top, both on a two-leg sling with shackles and the eyes shimmed into the sling plane; beams and platen in a round sling. Eye bolts out and holes plugged before pressing. The 40 kg limit in PR-008 is a transport limit", WITHIN, "PPR-DDR-006 (D3); independent review 2026-10-23")
c.cited("B3", "Silica-bearing clay dust (and rice husk ash in fired trimmings) is a respiratory hazard controlled by wet work and P2 or N95 masks", "Biology", "Toxicology",
        "Crystalline silica causes silicosis; wet methods and respirators are standard controls; air monitoring shows whether they work", "Safety claim only", WITHIN, "PPR-PRC-001 Safety")
c.cited("B4", "Zinc fume from welding galvanised mesh is controlled by grinding the coating off and ventilation", "Biology", "Toxicology",
        "Zinc oxide fume causes metal fume fever", "Stated in the build plan safety notes", WITHIN, "PPR-BLD-001 Safety")
c.order_of_magnitude("M6", "The fired filter comes out at the 280 mm reference size", "Physics", "Thermodynamics",
        claimed=280.0, estimate=304.35 * (1 - 0.08), unit="mm inner rim", factor=1.02,
        law="Clay shrinks on drying and firing, typically 6 to 10 % linear for earthenware filter mixes; the mold cavity is the fired size divided by (1 - shrinkage). CMWG 2011 notes grog changing fired size enough that pots no longer fit receptacles",
        closed_by="PPR-DDR-006 (D2): cavity scaled for 8 % total shrinkage (CLAY_SHRINK in cad/src/model.py), to be replaced by the partner clay's test-bar value (ASTM C326 method) before patterns are printed")
c.cited("S10", "The mix fills the cavity, air escapes and the green pot releases and survives the demold tilt", "Physics", "Fluid mechanics",
        "Plastic clay pressing between two-part molds is established practice in over 50 factories; vents and liners are standard",
        "Within known science; mold vents and release confirmed in the first pressing trials (BLD first checks)", WITHIN, "PPR-BLD-001 first checks")

# Engineering and technology
c.claim("E1", "Casting patterns print on a printer with a true 250 x 250 mm bed", "Engineering and technology", "Manufacturing tolerances",
        "486 mm pattern split into quadrants; a 250 x 210 mm or 220 x 220 mm bed does not fit", 486 / 2, 250, "mm", closed_by="PPR-CAL-001 section 8")
c.cited("E2", "Hand lapping to printed templates reaches +/-0.3 mm on a 400 mm casting", "Engineering and technology", "Manufacturing tolerances",
        "Grinding and filing to templates reach +/-0.3 mm in toolroom practice; printed PLA templates can be off by 0.2 to 0.5 % over 400 mm, which the tolerance budget does not yet include",
        "Within known science; practical risk carried in RSK and requirement PR-002 (at risk)", WITHIN, "PPR-CAL-001 section 7; RSK R2")
c.cited("E3", "Guard openings meet ISO 13857 Table 4 for their distance from moving parts", "Engineering and technology", "Standards practice",
        "ISO 13857:2019 Table 4", "23 openings checked from the model; Table 7 (lower limbs) and the floor gap not yet checked; signature by a competent person is a hold point", WITHIN, "PPR-CAL-001 section 15")

# Concept options B and C (PPR-OPT-001), checked on their kit 1.9 detailed models (cad/src/options_bc.py, 2026-10-24)
# Option B: hand lever rigid with the upper toggle link; torque balance about the top pin gives F = T / (2 L sin(theta)),
# with the knee travel from straight delta = 2 L (1 - cos(theta))
T_lever, L_link = 300 * 1.1, 0.400                      # 300 N at the 1.1 m lever; 400 mm links
toggle_t = lambda delta_m: T_lever / (2 * L_link * math.sin(math.acos(1 - delta_m / (2 * L_link)))) / (1e3 * G)  # noqa: E731
c.order_of_magnitude("OB1", "Option B: the toggle gives about 1.4 t at 0.35 mm from straight (0.16 t at 30 mm, 7 t at 0.014 mm)", "Physics", "Mechanics and statics",
                     claimed=1.4, estimate=toggle_t(0.35e-3), unit="t", factor=1.1,
                     law="Virtual work on the toggle with the lever rigid on the upper link: F = T / (2 L sin theta); the kit 1.8 estimate (2 t at 0.35 mm) was about 40 % high",
                     closed_by="PPR-OPT-001 v0.3 (figures restated from the detailed model)")
I_link = 80 * 40**3 / 12                                 # lower link 80 x 40 mm, weak axis, mm4
c.claim("OB2", "Option B: the 80 x 40 mm lower link does not buckle at 1.5 times 10 t", "Physics", "Strength of materials",
        "Euler buckling of a pinned strut, P = pi^2 E I / L^2, E = 200 GPa", 1.5 * 10e3 * G / 1e3,
        math.pi**2 * 200e3 * I_link / 400**2 / 1e3, "kN", closed_by="This file (model link 80 x 40 x 400 mm)")
Fb = 1.5 * 10e3 * G
c.claim("OB3", "Option B: the 40 mm clevis pins carry 1.5 times 10 t in double shear", "Physics", "Strength of materials",
        "Pin shear 0.5 x fub / gamma_M2 with fub 600 MPa (EN 1993-1-8 pin practice)", Fb / (2 * math.pi * 20**2),
        0.5 * 600 / 1.25, "MPa", closed_by="This file (model pins 40 mm, ISO 2341 B)")
arm_b = (12 / 2 + 1 + 40 / 4)                            # top pin: 12 mm clevis plate, 1 mm gap, 40 mm of link bars over the knee
c.claim("OB4", "Option B: the 40 mm clevis pins stay below yield in bending at 1.5 times 10 t", "Physics", "Strength of materials",
        "Pin bending M = F/2 (a/2 + g + b/4), sigma = M / (pi d^3 / 32), yield about 640 MPa (8.8 class pin steel); the 30 mm pins first drawn reached about 510 MPa",
        Fb / 2 * arm_b / (math.pi * 40**3 / 32), 640 / 1.25, "MPa", closed_by="cad/src/options_bc.py (pins 30 to 40 mm after the independent review, 2026-10-24)")
dm, lead, mu = 36.5, 7.0, 0.15                           # Tr40 x 7: mean diameter, lead, thread friction
lam = math.atan(lead / (math.pi * dm)); phi = math.atan(mu / math.cos(math.radians(15)))
k_thread = dm / 2 / 1e3 * math.tan(lam + phi)            # N m per N of axial force
k_collar = 0.005 * 0.025                                 # thrust ball bearing 51108, friction about 0.005 at 25 mm
F_two = 2 * 300 * 0.450 / (k_thread + k_collar) / (1e3 * G)
c.order_of_magnitude("OC1", "Option C: two people at 300 N on the 450 mm capstan give about 6.7 t with the thrust ball bearing (3.6 t with a plain collar)", "Physics", "Mechanics and statics",
                     claimed=6.7, estimate=F_two, unit="t", factor=1.1,
                     law="Power screw torque T = F (dm / 2) tan(lambda + phi) plus collar friction; the detailed model's thrust ball bearing cuts the collar term, giving about 6.7 t",
                     closed_by="PPR-OPT-001 v0.3 (thrust bearing in the detailed model)")
c.claim("OC2", "Option C: the Tr40 x 7 screw self-locks (lead angle below the friction angle)", "Physics", "Mechanics and statics",
        "Self-locking when lambda < phi", math.degrees(lam), math.degrees(phi), "deg", closed_by="This file")
I_root = math.pi * 32.0**4 / 64                         # Tr40 x 7 root diameter about 32 mm
c.claim("OC4", "Option C: the screw does not buckle at 1.5 times 10 t over its free length of about 0.4 m closed (0.7 m open)", "Physics", "Strength of materials",
        "Euler buckling, pinned at the nut and the thrust swivel, P = pi^2 E I / L^2 on the root diameter, at the open length as the worst case", 1.5 * 10e3 * G / 1e3,
        math.pi**2 * 200e3 * I_root / 700**2 / 1e3, "kN", closed_by="This file (model: 330 mm swivel to crown closed, plus the 310 mm opening)")
c.order_of_magnitude("OC3", "Option C: about 43 turns cover the 300 mm opening", "Mathematics", "Orders of magnitude",
                     claimed=43, estimate=300 / lead, unit="turns", factor=1.1, law="Turns = travel / lead", closed_by="PPR-OPT-001")

state = c.write()
sys.exit(0 if state != "fail" else 1)
