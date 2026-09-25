"""PotPress concept massing model and media (TRL 2).

Run from the repo root:  python cad/src/concept_media.py
Proportions and main parts only; not for fabrication.

Axes: X across the press between the uprights, Y front (-Y, operator side, the mold
carriage slides out this way) to back (+Y), Z up. Units mm. The press is shown closed,
at the end of a pressing stroke, with a formed pot between the molds. The QC flow-test
rack stands to the right (+X).

Filter geometry follows the common Potters for Peace flowerpot form, about 280 mm wide
by 250 mm deep (11 in by 10 in), with a 15 mm wall (estimate).
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / ".kit"))
from build123d import Align, Box, Cone, Cylinder, Pos
from concept import Part, render_all

MIN = (Align.CENTER, Align.CENTER, Align.MIN)


def box(x0, x1, y0, y1, z0, z1):
    """Axis-aligned box from min and max corners."""
    return Pos((x0 + x1) / 2, (y0 + y1) / 2, (z0 + z1) / 2) * Box(x1 - x0, y1 - y0, z1 - z0)


def cyl(r, z0, z1, x=0.0, y=0.0):
    return Pos(x, y, z0) * Cylinder(r, z1 - z0, align=MIN)


def cone(r0, r1, z0, z1, x=0.0, y=0.0):
    return Pos(x, y, z0) * Cone(r0, r1, z1 - z0, align=MIN)


# Filter (pot) geometry
WALL = 15.0
R_OUT_BOT, R_OUT_TOP, DEPTH = 130.0, 155.0, 255.0
R_IN_BOT, R_IN_TOP = R_OUT_BOT - WALL, R_OUT_TOP - WALL
RIM_R, RIM_T = 172.0, 15.0


def pot(z_bottom, x=0.0, y=0.0):
    """Pressed filter pot with a flat rim, outer bottom at z_bottom."""
    top = z_bottom + DEPTH
    outer = cone(R_OUT_BOT, R_OUT_TOP, z_bottom, top, x, y) + cyl(RIM_R, top - RIM_T, top, x, y)
    inner = cone(R_IN_BOT, R_IN_TOP, z_bottom + WALL, top + 1, x, y)
    return outer - inner


# Press frame
BASE_T = 100.0
UP_X0, UP_X1 = 265.0, 335.0           # upright inner and outer faces (each side)
TOP_Z0, TOP_Z1 = 1300.0, 1450.0       # top crossbeam

# 1 Base: crossbeam along X on two feet along Y
base = box(-460, 460, -80, 80, 40, BASE_T) + box(-460, -380, -320, 320, 0, 40) + box(380, 460, -320, 320, 0, 40)
# 2 Uprights, two channel pairs
uprights = box(-UP_X1, -UP_X0, -50, 50, BASE_T, TOP_Z0) + box(UP_X0, UP_X1, -50, 50, BASE_T, TOP_Z0)
# 3 Top crossbeam (double channel) with the male mold slide guide
top_beam = box(-420, 420, -80, 80, TOP_Z0, TOP_Z1) - box(-72, 72, -72, 72, TOP_Z0 - 1, TOP_Z1 + 1)
top_beam = top_beam + (box(-95, 95, -95, 95, TOP_Z1, TOP_Z1 + 40) - box(-72, 72, -72, 72, TOP_Z1 - 1, TOP_Z1 + 41))

# 4 20 t bottle jack on the base, ram raised about 80 mm into the pressing stroke
jack = box(-80, 80, -80, 80, BASE_T, BASE_T + 20) + cyl(60, BASE_T + 20, 340) + cyl(30, 340, 420)
jack = jack + box(55, 190, -12, 12, BASE_T + 60, BASE_T + 80)       # pump socket and handle stub

# 5 Moving platen with guide sleeves riding on the uprights
PL_Z0, PL_Z1 = 420.0, 460.0
platen = box(-UP_X0 + 5, UP_X0 - 5, -160, 160, PL_Z0, PL_Z1)
platen = platen + box(-UP_X1 - 12, -UP_X0 + 12, -62, 62, PL_Z0 - 20, PL_Z1 + 40) - box(-UP_X1 - 1, -UP_X0 + 1, -51, 51, 0, 2000)
platen = platen + box(UP_X0 - 12, UP_X1 + 12, -62, 62, PL_Z0 - 20, PL_Z1 + 40) - box(UP_X0 - 1, UP_X1 + 1, -51, 51, 0, 2000)

# 6 Return springs, platen to base
springs = cyl(14, BASE_T, PL_Z0, x=-200, y=110) + cyl(14, BASE_T, PL_Z0, x=200, y=110)

# 7 Mold carriage and slide rails (slides out toward -Y for loading and demolding)
RAIL_Z1 = PL_Z1 + 15
carriage = box(-190, -150, -330, 160, PL_Z1, RAIL_Z1) + box(150, 190, -330, 160, PL_Z1, RAIL_Z1)
carriage = carriage + box(-60, 60, -250, -215, RAIL_Z1, RAIL_Z1 + 120)   # pull handle

# 8 Female mold, cast aluminum, with the pot cavity
FM_Z0 = RAIL_Z1
FM_Z1 = FM_Z0 + 300.0
POT_Z0 = FM_Z1 - DEPTH                # outer bottom of the pot
female = cyl(205, FM_Z0, FM_Z1) - cone(R_OUT_BOT, R_OUT_TOP, POT_Z0, FM_Z1 + 1) - cyl(RIM_R, FM_Z1 - RIM_T, FM_Z1 + 1)

# 9 Male mold, cast aluminum, with a rim-forming flange
male = cone(R_IN_BOT, R_IN_TOP, POT_Z0 + WALL, FM_Z1) + cyl(RIM_R + 20, FM_Z1, FM_Z1 + 25)

# 10 Male mold slide: square stem through the top beam, load pins and hand-crank lift
stem_z0 = FM_Z1 + 25
slide = box(-70, 70, -70, 70, stem_z0, TOP_Z1 + 150)
slide = slide + Pos(0, 0, TOP_Z1 - 20) * Box(260, 30, 30)            # load pin through the stem (upper slot)
slide = slide + cyl(8, TOP_Z1 + 150, TOP_Z1 + 190) + (cyl(130, TOP_Z1 + 190, TOP_Z1 + 205) - cyl(115, TOP_Z1 + 189, TOP_Z1 + 206))
slide = slide + box(-10, 10, -130, 130, TOP_Z1 + 190, TOP_Z1 + 205)

# 11 Pressed filter pot (clay and burnout mix), shown in the closed mold
pressed = pot(POT_Z0)

# QC flow-test rack to the right of the press
QX0, QX1 = 700.0, 1500.0
QY0, QY1 = -220.0, 220.0
Q_TOP = 560.0
leg = lambda x, y: box(x - 20, x + 20, y - 20, y + 20, 0, Q_TOP)
rack = leg(QX0 + 20, QY0 + 20) + leg(QX1 - 20, QY0 + 20) + leg(QX0 + 20, QY1 - 20) + leg(QX1 - 20, QY1 - 20)
rack = rack + box(QX0, QX1, QY0, QY1, Q_TOP - 20, Q_TOP) + box(QX0, QX1, -15, 15, 120, 150)
ST = [QX0 + 200, QX1 - 200]           # two of the four stations modeled
for x in ST:
    rack = rack - cyl(R_OUT_TOP + 5, Q_TOP - 21, Q_TOP + 1, x=x)
test_pots = pot(Q_TOP - DEPTH + RIM_T, x=ST[0]) + pot(Q_TOP - DEPTH + RIM_T, x=ST[1])
buckets = (cyl(170, 0, 280, x=ST[0]) - cyl(162, 8, 281, x=ST[0])) + (cyl(170, 0, 280, x=ST[1]) - cyl(162, 8, 281, x=ST[1]))
water = cone(R_IN_BOT + 1, R_IN_TOP - 3, Q_TOP - DEPTH + RIM_T + WALL + 1, Q_TOP - 12, x=ST[0])
gauge = box(ST[0] - 6, ST[0] + 6, -150, 150, Q_TOP + 2, Q_TOP + 14) + box(ST[0] - 4, ST[0] + 4, -4, 4, Q_TOP - 180, Q_TOP + 2)

parts = [
    Part("Base and feet", base, "#4B5563", 1, (0, 0, -260)),
    Part("Uprights", uprights, "#6B7280", 2, (0, 760, 0)),
    Part("Top crossbeam", top_beam, "#4B5563", 3, (0, 0, 520)),
    Part("20 t bottle jack", jack, "#B91C1C", 4, (0, -520, -120)),
    Part("Moving platen with guide sleeves", platen, "#9CA3AF", 5, (0, 0, -40)),
    Part("Return springs", springs, "#D4A017", 6, (0, 420, -60)),
    Part("Mold carriage and slide rails", carriage, "#374151", 7, (0, -460, 60)),
    Part("Female mold (cast aluminum)", female, "#CBD5E1", 8, (0, -460, 180)),
    Part("Male mold (cast aluminum)", male, "#94A3B8", 9, (0, 0, 420)),
    Part("Male mold slide, load pins, crank", slide, "#0F766E", 10, (0, 0, 640)),
    Part("Pressed filter pot", pressed, "#C8875A", 11, (0, -460, 300)),
    Part("QC flow-test rack", rack, "#A16207", 12),
    Part("Test pots in the QC rack", test_pots, "#C8875A", None, (0, 0, 280)),
    Part("Printed T-gauge", gauge, "#F59E0B", 13, (0, 0, 520)),
    Part("Collection buckets", buckets, "#2563EB", 14, (0, 0, -120)),
    Part("Water in test pot", water, "#7DD3FC", None, (0, 0, 280)),
]

render_all(
    parts, project="PotPress", title="Filter press and QC rig concept", dwg_no="PPR-DWG-010",
    key_figures=["20 t bottle jack; working force about 5 to 10 t (est.)",
                 "About 0.5 to 1.1 MPa at 5 to 10 t on the pot (est.)",
                 "Filter about 280 mm x 250 mm, about 10 L working volume",
                 "About 8 kg mix per pot; about 4.2 kg fired (est.)",
                 "Cycle about 5 min; 50 or more pots per shift (est.)",
                 "QC: 1.0 to 2.5 L/h in the first hour (proposed)",
                 "Press about 920 x 640 x 1,655 mm, about 180 kg (est.)"],
    cut_exclude=("Return springs", "Printed T-gauge"),
    flow={"title": "material flow per filter, mixed charge to passed filter (all values are estimates)", "unit": "kg",
          "stages": [("Mixed charge", 8.0), ("Pressed pot", 7.3), ("Dried pot", 5.8), ("Fired pot", 4.2),
                     ("Passes QC", 3.8)],
          "losses": [(0, "Trim, recycled (est.)", 0.7), (1, "Drying water (est.)", 1.5),
                     (2, "Firing loss (est.)", 1.6), (3, "Rejects, 10 % (est.)", 0.4)]},
)
