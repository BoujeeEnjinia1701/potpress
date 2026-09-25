"""PotPress parametric model (build123d), TRL 3, massing-plus level of detail.

Run from the repo root:  python cad/src/model.py
Exports the assembly and the main parts to cad/step/*.step and cad/stl/*.stl.

Axes: X across the press between the uprights, Y front (-Y, operator side; the mold
carriage slides out this way) to back (+Y), Z up from the floor. Units mm. The press
is shown closed at the end of a pressing stroke, male mold pinned, with a formed pot
between the molds. The QC flow-test rack (2 x 2 stations) stands to the right (+X).

Correct interfaces and main dimensions only; not fabrication detail. Sizing is in
PPR-CAL-001 (docs/04-calcs/sizing.py), which reads PARAMS and levels() from here.
CONCEPT, NOT FOR FABRICATION.
"""
from __future__ import annotations

import math
from pathlib import Path

# ---------------------------------------------------------------------------
# Parameters (mm). Edit these, not the geometry below.
# ---------------------------------------------------------------------------
PARAMS = {
    # Reference filter (R1): inner surface is the male mold, outer is the female cavity
    "R_IN_BOT": 115.0,      # inner radius at the floor of the pot
    "R_IN_RIM": 140.0,      # inner radius at the rim (280 mm inner rim diameter)
    "D_IN": 240.0,          # inner depth
    "WALL": 15.0,           # wall and floor thickness, measured normal to the surface
    "RIM_OD": 345.0,        # flat rim outer diameter
    "RIM_T": 15.0,          # flat rim thickness
    # Female mold: cast aluminum shell on a solid base, with a rim counterbore and stop face
    "FM_SHELL": 20.0,       # shell thickness behind the cavity
    "FM_BASE": 30.0,        # solid floor under the cavity, bears on the rails
    "FM_BASE_D": 350.0,     # base disc diameter
    "FM_FLANGE_D": 410.0,   # top flange diameter (stop face ring)
    "FM_FLANGE_T": 40.0,    # top flange thickness
    "FLASH_R": 180.0,       # flash groove outer radius (stop face is outside this)
    "LOC_H": 10.0,          # locating lip on the female flange; the male flange centers in it
    "LOC_TAPER": 2.0,       # radial lead-in of the lip over its height
    "LOC_CLEAR": 0.1,       # diametral fit of the male flange in the lip, finished
    # Male mold: cast aluminum hollow plug with a rim-forming flange
    "MM_SHELL": 15.0,       # plug shell thickness
    "MM_TIP": 30.0,         # plug tip (floor-forming) plate thickness
    "MM_FLANGE_D": 390.0,   # flange diameter; outer ring lands on the female stop face
    "MM_FLANGE_T": 25.0,
    "ADAPTER_T": 15.0,      # steel stem adapter plate on the flange
    # Frame: channels are UPN sections (EN 10279); names index SECTIONS below
    "SPAN": 600.0,          # upright centerline spacing (beam span)
    "BEAM_SEC": "UPN160",   # top crossbeam and base beam, two channels each
    "BEAM_GAP": 100.0,      # clear gap between the channel webs (uprights and stem sit in it)
    "BEAM_L": 840.0,        # beam length
    "UPRIGHT_SEC": "UPN100",  # each upright is two channels back to back (100 x 100)
    "FOOT_SEC": "UPN100",   # feet, lying web down
    "FOOT_L": 640.0,
    "DOUBLER_T": 12.0,      # web doubler plates at the load pin
    "DOUBLER_L": 200.0,
    "BEARING_T": 20.0,      # jack bearing plate on the base beam
    # Jack and platen
    "JACK_CLOSED": 245.0,   # 20 t bottle jack, closed height including screw set
    "JACK_STROKE": 150.0,
    "JACK_BASE": 160.0,
    "JACK_BODY_D": 120.0,
    "RAM_D": 60.0,
    "PLATEN_SEC": "UPN140",  # two channels under a thin deck, with a jack pad
    "PLATEN_DECK_T": 6.0,
    "PLATEN_PAD_T": 20.0,
    "SLEEVE_T": 10.0,       # guide sleeve wall, around each upright
    "SLEEVE_H": 150.0,
    "SLEEVE_CLEAR": 1.0,    # diametral clearance on the upright
    # Carriage and rails
    "RAIL_X": (60.0, 170.0),  # rail centerlines, both sides of the axis
    "RAIL_W": 30.0,
    "RAIL_H": 15.0,
    "RAIL_BACK": 220.0,     # rail end stop, +Y
    "CARRIAGE_OUT": 430.0,  # slide-out travel toward -Y
    # Male mold slide
    "STEM": 90.0,           # SHS 90 x 90 x 8
    "STEM_T": 8.0,
    "PIN_D": 60.0,          # single load pin, 42CrMo4 quenched and tempered
    "PIN_L": 230.0,
    "LEAD_D": 24.0,         # Tr24 x 5 lead screw (lifts only)
    "LEAD_P": 5.0,
    "HANDWHEEL_D": 260.0,
    # Kinematics
    "PRESS_TRAVEL": 110.0,  # jack travel used from mold contact to closed
    "CRANK_LIFT": 200.0,    # male mold lift by crank
    "LIFT_CLEAR": 20.0,     # clearance under the top beam at full lift
    # QC rack, 2 x 2 stations
    "QC_X0": 760.0,         # rack left edge (X)
    "QC_PITCH": 390.0,      # station pitch in X and Y
    "QC_SHELF_Z": 550.0,    # pot shelf top (pot rims rest here)
    "QC_BUCKET_Z": 200.0,   # bucket shelf top
    "QC_SHELF_T": 20.0,
    "QC_LEG": 40.0,
    "BUCKET_D": 300.0,      # 20 L food-grade bucket
    "BUCKET_H": 325.0,
    "GAUGE_SCALE": 100.0,   # T-gauge stem length below the rim
}

# UPN channel properties (EN 10279 / DIN 1026 tables): h, b, tw, tf mm; A mm2; Ix mm4; Wx mm3; kg/m
SECTIONS = {
    "UPN100": dict(h=100, b=50, tw=6.0, tf=8.5, A=1350, Ix=206e4, Wx=41.2e3, m=10.6),
    "UPN120": dict(h=120, b=55, tw=7.0, tf=9.0, A=1700, Ix=364e4, Wx=60.7e3, m=13.4),
    "UPN140": dict(h=140, b=60, tw=7.0, tf=10.0, A=2040, Ix=605e4, Wx=86.4e3, m=16.0),
    "UPN160": dict(h=160, b=65, tw=7.5, tf=10.5, A=2400, Ix=925e4, Wx=116e3, m=18.8),
    "UPN180": dict(h=180, b=70, tw=8.0, tf=11.0, A=2800, Ix=1350e4, Wx=150e3, m=22.0),
}


def pot_outer(P=PARAMS):
    """Outer surface of the pot (female cavity): radii at the outer floor and at the rim top, and depth."""
    t = P["WALL"]
    slope = (P["R_IN_RIM"] - P["R_IN_BOT"]) / P["D_IN"]
    off = t / math.cos(math.atan(slope))           # horizontal offset of a normal wall
    r_bot = P["R_IN_BOT"] - t * slope + off          # at z = -t (outer floor)
    r_top = P["R_IN_RIM"] + off
    return r_bot, r_top, P["D_IN"] + t


def levels(P=PARAMS):
    """Vertical stack (z, mm) with the press closed. Pure arithmetic; no CAD needed."""
    b = SECTIONS[P["BEAM_SEC"]]; f = SECTIONS[P["FOOT_SEC"]]; pl = SECTIONS[P["PLATEN_SEC"]]
    L = {}
    L["foot_top"] = f["b"]                           # channel lying web down: height = flange width
    L["base0"] = L["foot_top"]; L["base1"] = L["base0"] + b["h"]
    L["jack0"] = L["base1"] + P["BEARING_T"]
    L["platen0_low"] = L["jack0"] + P["JACK_CLOSED"]
    L["platen0"] = L["platen0_low"] + P["PRESS_TRAVEL"]            # closed
    L["deck1"] = L["platen0"] + pl["h"] + P["PLATEN_DECK_T"]
    L["rail1"] = L["deck1"] + P["RAIL_H"]
    L["fm0"] = L["rail1"]
    _, _, h_out = pot_outer(P)
    L["pot0"] = L["fm0"] + P["FM_BASE"]                            # pot outer floor
    L["fm1"] = L["pot0"] + h_out                                   # female top = pot rim top
    L["mm1"] = L["fm1"] + P["MM_FLANGE_T"]
    L["stem0"] = L["mm1"] + P["ADAPTER_T"]
    L["top0"] = L["stem0"] + P["CRANK_LIFT"] + P["LIFT_CLEAR"]
    L["top1"] = L["top0"] + b["h"]
    L["pin"] = (L["top0"] + L["top1"]) / 2
    L["stem1"] = L["top1"] + 60.0
    L["bracket0"] = L["stem1"] + P["CRANK_LIFT"] + 20.0
    L["bracket1"] = L["bracket0"] + 15.0
    L["wheel"] = L["bracket1"] + 45.0
    L["overall"] = L["wheel"] + 15.0
    # Opening: jack fully retracted and male mold cranked up
    L["open_gap"] = P["PRESS_TRAVEL"] + P["CRANK_LIFT"] - P["D_IN"]  # male tip above female rim
    return L


# ---------------------------------------------------------------------------
# Geometry helpers
# ---------------------------------------------------------------------------
def _b():
    import build123d as bd
    return bd


def box(x0, x1, y0, y1, z0, z1):
    bd = _b()
    return bd.Pos((x0 + x1) / 2, (y0 + y1) / 2, (z0 + z1) / 2) * bd.Box(x1 - x0, y1 - y0, z1 - z0)


def cyl(r, z0, z1, x=0.0, y=0.0):
    bd = _b()
    return bd.Pos(x, y, z0) * bd.Cylinder(r, z1 - z0, align=(bd.Align.CENTER, bd.Align.CENTER, bd.Align.MIN))


def cone(r0, r1, z0, z1, x=0.0, y=0.0):
    bd = _b()
    return bd.Pos(x, y, z0) * bd.Cone(r0, r1, z1 - z0, align=(bd.Align.CENTER, bd.Align.CENTER, bd.Align.MIN))


def cyl_y(r, y0, y1, x, z):
    """Cylinder along Y."""
    bd = _b()
    return bd.Pos(x, (y0 + y1) / 2, z) * bd.Rot(90, 0, 0) * bd.Cylinder(r, y1 - y0)


def channel_x(x0, x1, y_web, side, z0, sec):
    """UPN channel running along X, web vertical at y_web, flanges pointing to side (+1 or -1)."""
    s = SECTIONS[sec]
    y_a, y_b = sorted((y_web, y_web + side * s["tw"]))
    web = box(x0, x1, y_a, y_b, z0, z0 + s["h"])
    y_c, y_d = sorted((y_web, y_web + side * s["b"]))
    fl = box(x0, x1, y_c, y_d, z0, z0 + s["tf"]) + box(x0, x1, y_c, y_d, z0 + s["h"] - s["tf"], z0 + s["h"])
    return web + fl


def channel_upright(x_back, side, z0, z1, sec):
    """UPN channel standing along Z, web in the plane x = x_back, flanges pointing to side in X, depth in Y."""
    s = SECTIONS[sec]; h = s["h"]
    x_a, x_b = sorted((x_back, x_back + side * s["tw"]))
    web = box(x_a, x_b, -h / 2, h / 2, z0, z1)
    x_c, x_d = sorted((x_back, x_back + side * s["b"]))
    fl = box(x_c, x_d, -h / 2, -h / 2 + s["tf"], z0, z1) + box(x_c, x_d, h / 2 - s["tf"], h / 2, z0, z1)
    return web + fl


def pot(z_floor, x=0.0, y=0.0, P=PARAMS):
    """Pressed filter pot, outer floor at z_floor."""
    rb, rt, h = pot_outer(P)
    top = z_floor + h
    outer = cone(rb, rt, z_floor, top, x, y) + cyl(P["RIM_OD"] / 2, top - P["RIM_T"], top, x, y)
    inner = cone(P["R_IN_BOT"], P["R_IN_RIM"] + (P["R_IN_RIM"] - P["R_IN_BOT"]) / P["D_IN"],
                 z_floor + P["WALL"], top + 1, x, y)
    return outer - inner


# ---------------------------------------------------------------------------
# Parts
# ---------------------------------------------------------------------------
def build_parts(P=PARAMS):
    """Return a list of (name, shape, color, bom_no, explode_offset). Press closed."""
    L = levels(P)
    b = SECTIONS[P["BEAM_SEC"]]; u = SECTIONS[P["UPRIGHT_SEC"]]; pl = SECTIONS[P["PLATEN_SEC"]]
    g2 = P["BEAM_GAP"] / 2; xs = P["SPAN"] / 2; bl = P["BEAM_L"] / 2
    parts = []

    # 1 Base beam (two channels) on two feet, with the jack bearing plate
    base = channel_x(-bl, bl, g2, +1, L["base0"], P["BEAM_SEC"]) + channel_x(-bl, bl, -g2, -1, L["base0"], P["BEAM_SEC"])
    f = SECTIONS[P["FOOT_SEC"]]
    for sx in (-1, 1):
        xc = sx * (xs + 60)
        base += box(xc - f["h"] / 2, xc + f["h"] / 2, -P["FOOT_L"] / 2, P["FOOT_L"] / 2, 0, f["tw"])
        for dx in (-1, 1):
            base += box(xc + dx * f["h"] / 2 - (f["tf"] if dx > 0 else 0), xc + dx * f["h"] / 2 + (0 if dx > 0 else f["tf"]),
                        -P["FOOT_L"] / 2, P["FOOT_L"] / 2, 0, f["b"])
    base += box(-100, 100, -90, 90, L["base1"], L["jack0"])
    parts.append(("Base beam, feet and jack plate", base, "#4B5563", 1, (0, 0, -260)))

    # 2 Uprights: two back-to-back channels each side, sandwiched between the beam channels
    upr = None
    for sx in (-1, 1):
        pair = channel_upright(sx * xs, -1, L["base0"], L["top1"], P["UPRIGHT_SEC"]) + \
            channel_upright(sx * xs, +1, L["base0"], L["top1"], P["UPRIGHT_SEC"])
        upr = pair if upr is None else upr + pair
    parts.append(("Uprights", upr, "#6B7280", 2, (0, 0, 0)))

    # 3 Top crossbeam: two channels, web doublers at the pin, stem guide liners
    top = channel_x(-bl, bl, g2, +1, L["top0"], P["BEAM_SEC"]) + channel_x(-bl, bl, -g2, -1, L["top0"], P["BEAM_SEC"])
    dl = P["DOUBLER_L"] / 2
    for sy in (-1, 1):
        y0 = g2 + b["tw"]; y1 = y0 + P["DOUBLER_T"]
        top += box(-dl, dl, *sorted((sy * y0, sy * y1)), L["top0"] + b["tf"], L["top1"] - b["tf"])
    s2 = P["STEM"] / 2
    guides = box(-s2 - 30, -s2 - 1, -g2, g2, L["top0"], L["top1"]) + box(s2 + 1, s2 + 30, -g2, g2, L["top0"], L["top1"])
    top += guides
    top -= cyl_y(P["PIN_D"] / 2 + 1, -g2 - 40, g2 + 40, 0, L["pin"])
    parts.append(("Top crossbeam with pin doublers", top, "#4B5563", 3, (0, 0, 560)))

    # 4 20 t bottle jack, ram extended by PRESS_TRAVEL
    jb = P["JACK_BASE"] / 2
    jack = box(-jb, jb, -jb, jb, L["jack0"], L["jack0"] + 25) + \
        cyl(P["JACK_BODY_D"] / 2, L["jack0"] + 25, L["platen0_low"] - 20) + \
        cyl(P["RAM_D"] / 2, L["platen0_low"] - 20, L["platen0"])
    jack += box(jb - 10, jb + 150, -12, 12, L["jack0"] + 60, L["jack0"] + 84)
    parts.append(("20 t bottle jack", jack, "#B91C1C", 4, (0, -560, -120)))

    # 5 Moving platen: two channels, deck, jack pad, guide sleeves on the uprights
    xin = xs - u["b"] - P["SLEEVE_T"] - P["SLEEVE_CLEAR"] / 2
    plat = channel_x(-xin, xin, g2, +1, L["platen0"], P["PLATEN_SEC"]) + channel_x(-xin, xin, -g2, -1, L["platen0"], P["PLATEN_SEC"])
    plat += box(-xin, xin, -220, 220, L["platen0"] + pl["h"], L["deck1"])
    plat += box(-100, 100, -g2, g2, L["platen0"], L["platen0"] + P["PLATEN_PAD_T"])
    for sx in (-1, 1):
        c = P["SLEEVE_CLEAR"] / 2; t = P["SLEEVE_T"]
        xo0, xo1 = sx * xs - u["b"] - c - t, sx * xs + u["b"] + c + t
        yo = u["h"] / 2 + c + t
        z0 = L["platen0"] - 20; z1 = z0 + P["SLEEVE_H"]
        sl = box(xo0, xo1, -yo, yo, z0, z1) - box(xo0 + t, xo1 - t, -yo + t, yo - t, z0 - 1, z1 + 1)
        plat += sl
    parts.append(("Moving platen with guide sleeves", plat, "#9CA3AF", 5, (0, 0, -40)))

    # 6 Return springs, base to platen
    springs = cyl(12, L["base1"], L["platen0"], x=-190) + cyl(12, L["base1"], L["platen0"], x=190)
    parts.append(("Return springs", springs, "#D4A017", 6, (0, 460, -60)))

    # 7 Rails (with front extension) and mold carriage frame with pull handle
    rails = None
    rw = P["RAIL_W"] / 2
    y_front = -P["RAIL_BACK"] - P["CARRIAGE_OUT"]
    for xr in P["RAIL_X"]:
        for sx in (-1, 1):
            r = box(sx * xr - rw, sx * xr + rw, y_front, P["RAIL_BACK"], L["deck1"], L["rail1"])
            rails = r if rails is None else rails + r
    rails += box(-200, 200, P["RAIL_BACK"], P["RAIL_BACK"] + 15, L["rail1"], L["rail1"] + 40)    # end stop
    fr = P["FM_BASE_D"] / 2 + 5
    car = box(-fr - 25, fr + 25, -fr - 25, fr + 25, L["rail1"], L["rail1"] + 12) - \
        box(-fr, fr, -fr, fr, L["rail1"] - 1, L["rail1"] + 13)
    car += box(-70, 70, -fr - 60, -fr - 25, L["rail1"], L["rail1"] + 12) + \
        box(-70, 70, -fr - 60, -fr - 45, L["rail1"] + 12, L["rail1"] + 110)
    for sx in (-1, 1):   # tilt pivot bosses
        car += cyl_y(14, -20, 20, sx * (fr + 40), L["rail1"] + 25)
    parts.append(("Rails and mold carriage", rails + car, "#374151", 7, (0, -520, 40)))

    # 8 Female mold: base disc, conical shell, top flange; cavity, rim counterbore, flash groove
    rb, rt, h = pot_outer(P)
    sh = P["FM_SHELL"]
    fem = cyl(P["FM_BASE_D"] / 2, L["fm0"], L["pot0"]) + cone(rb + sh, rt + sh, L["pot0"], L["fm1"]) + \
        cyl(P["FM_FLANGE_D"] / 2, L["fm1"] - P["FM_FLANGE_T"], L["fm1"])
    fem -= cone(rb, rt, L["pot0"], L["fm1"] + 0.01)
    fem -= cyl(P["RIM_OD"] / 2, L["fm1"] - P["RIM_T"], L["fm1"] + 1)
    fem -= cyl(P["FLASH_R"], L["fm1"] - 3, L["fm1"] + 1) - cyl(P["RIM_OD"] / 2, L["fm1"] - 4, L["fm1"] + 2)
    r_fit = P["MM_FLANGE_D"] / 2 + P["LOC_CLEAR"] / 2
    fem += cyl(P["FM_FLANGE_D"] / 2, L["fm1"], L["fm1"] + P["LOC_H"]) - \
        cone(r_fit, r_fit + P["LOC_TAPER"], L["fm1"] - 0.01, L["fm1"] + P["LOC_H"] + 0.01)
    parts.append(("Female mold (cast aluminum)", fem, "#CBD5E1", 8, (0, -520, 200)))

    # 9 Male mold: hollow plug with tip plate and rim-forming flange
    slope = (P["R_IN_RIM"] - P["R_IN_BOT"]) / P["D_IN"]
    z_tip = L["fm1"] - P["D_IN"]
    male = cone(P["R_IN_BOT"], P["R_IN_RIM"], z_tip, L["fm1"]) + cyl(P["MM_FLANGE_D"] / 2, L["fm1"], L["mm1"])
    z_in = z_tip + P["MM_TIP"]
    ti = P["MM_SHELL"]
    male -= cone(P["R_IN_BOT"] + slope * P["MM_TIP"] - ti, P["R_IN_RIM"] - ti, z_in, L["fm1"] + 0.01)
    parts.append(("Male mold (cast aluminum)", male, "#94A3B8", 9, (0, 0, 440)))

    # 10 Male mold slide: adapter, SHS stem, load pin, crank bracket, lead screw, handwheel
    t = P["STEM_T"]
    slide = box(-90, 90, -90, 90, L["mm1"], L["stem0"])
    slide += box(-s2, s2, -s2, s2, L["stem0"], L["stem1"]) - box(-s2 + t, s2 - t, -s2 + t, s2 - t, L["stem0"] + 15, L["stem1"] + 1)
    slide += box(-s2 + t, s2 - t, -s2 + t, s2 - t, L["pin"] - 60, L["pin"] + 60)            # pin block
    slide -= cyl_y(P["PIN_D"] / 2 + 1, -s2 - 1, s2 + 1, 0, L["pin"])
    slide += cyl_y(P["PIN_D"] / 2, -P["PIN_L"] / 2, P["PIN_L"] / 2, 0, L["pin"])            # the pin
    slide += cyl_y(P["PIN_D"] / 2 + 10, -P["PIN_L"] / 2 - 12, -P["PIN_L"] / 2, 0, L["pin"])  # pin head
    for sx in (-1, 1):
        slide += box(sx * 80 - 5, sx * 80 + 5, -80, 80, L["top1"], L["bracket0"])
    slide += box(-100, 100, -80, 80, L["bracket0"], L["bracket1"])
    slide += cyl(P["LEAD_D"] / 2, L["stem1"] - 40, L["wheel"] + 15)
    hw = P["HANDWHEEL_D"] / 2
    slide += cyl(hw, L["wheel"], L["wheel"] + 12) - cyl(hw - 14, L["wheel"] - 1, L["wheel"] + 13)
    slide += box(-hw + 5, hw - 5, -8, 8, L["wheel"], L["wheel"] + 12) + box(-8, 8, -hw + 5, hw - 5, L["wheel"], L["wheel"] + 12)
    slide += cyl(10, L["wheel"] + 12, L["wheel"] + 70, x=hw - 7)
    parts.append(("Male mold slide, load pin, crank", slide, "#0F766E", 10, (0, 0, 680)))

    # 11 Pressed filter pot
    parts.append(("Pressed filter pot", pot(L["pot0"], P=P), "#C8875A", 11, (0, -520, 620)))

    # 12 QC rack, 2 x 2 stations: legs, bucket shelf, pot shelf with holes
    x0 = P["QC_X0"]; pch = P["QC_PITCH"]; W = 2 * pch
    y0 = -pch
    lg = P["QC_LEG"]
    rack = None
    for xx in (x0, x0 + W - lg):
        for yy in (y0, y0 + W - lg):
            leg = box(xx, xx + lg, yy, yy + lg, 0, P["QC_SHELF_Z"])
            rack = leg if rack is None else rack + leg
    rack += box(x0, x0 + W, y0, y0 + W, P["QC_SHELF_Z"] - P["QC_SHELF_T"], P["QC_SHELF_Z"])
    rack += box(x0, x0 + W, y0, y0 + W, P["QC_BUCKET_Z"] - P["QC_SHELF_T"], P["QC_BUCKET_Z"])
    stations = [(x0 + pch / 2 + i * pch, y0 + pch / 2 + j * pch) for i in (0, 1) for j in (0, 1)]
    for (sx_, sy_) in stations:
        rack -= cyl(rt + 3, P["QC_SHELF_Z"] - P["QC_SHELF_T"] - 1, P["QC_SHELF_Z"] + 1, x=sx_, y=sy_)
    parts.append(("QC flow-test rack (2 x 2)", rack, "#A16207", 12, (0, 0, 0)))

    # Test pots hang by their rims on the shelf
    z_tp = P["QC_SHELF_Z"] + P["RIM_T"] - h
    tp = None
    for (sx_, sy_) in stations:
        p_ = pot(z_tp, sx_, sy_, P)
        tp = p_ if tp is None else tp + p_
    parts.append(("Test pots in the QC rack", tp, "#C8875A", None, (0, 0, 300)))

    # 13 Printed T-gauge on one station
    gx, gy = stations[0]
    zr = P["QC_SHELF_Z"] + P["RIM_T"]
    gauge = box(gx - 6, gx + 6, gy - 170, gy + 170, zr, zr + 12) + \
        box(gx - 4, gx + 4, gy - 4, gy + 4, zr - P["GAUGE_SCALE"], zr)
    parts.append(("Printed T-gauge", gauge, "#F59E0B", 13, (0, 0, 520)))

    # 14 Collection buckets on the lower shelf
    bk = None
    zb = P["QC_BUCKET_Z"]
    for (sx_, sy_) in stations:
        b_ = cyl(P["BUCKET_D"] / 2, zb, zb + P["BUCKET_H"], sx_, sy_) - cyl(P["BUCKET_D"] / 2 - 3, zb + 3, zb + P["BUCKET_H"] + 1, sx_, sy_)
        bk = b_ if bk is None else bk + b_
    parts.append(("Collection buckets", bk, "#2563EB", 14, (0, 0, -150)))

    # Water in one test pot, filled to 10 mm below the rim
    wz0 = z_tp + P["WALL"] + 0.5
    wz1 = zr - 10
    rw1 = P["R_IN_BOT"] + (P["R_IN_RIM"] - P["R_IN_BOT"]) * (wz1 - wz0) / P["D_IN"]
    water = cone(P["R_IN_BOT"] - 0.5, rw1 - 0.5, wz0, wz1, gx, gy)
    parts.append(("Water in test pot", water, "#7DD3FC", None, (0, 0, 300)))
    return parts


def assembly(parts=None):
    bd = _b()
    parts = parts or build_parts()
    return bd.Compound(children=[p[1] for p in parts])


def press_only(parts=None):
    bd = _b()
    parts = parts or build_parts()
    return bd.Compound(children=[p[1] for p in parts if p[3] is not None and p[3] <= 11])


if __name__ == "__main__":
    from build123d import Compound, export_step, export_stl
    root = Path(__file__).resolve().parents[1]
    (root / "step").mkdir(exist_ok=True); (root / "stl").mkdir(exist_ok=True)
    parts = build_parts()
    by = {p[0]: p[1] for p in parts}
    export_step(assembly(parts), str(root / "step" / "potpress-assembly.step"))
    export_step(press_only(parts), str(root / "step" / "potpress-press.step"))
    for key, stem in [("Female mold (cast aluminum)", "female-mold"), ("Male mold (cast aluminum)", "male-mold"),
                      ("Pressed filter pot", "filter-pot"), ("Printed T-gauge", "t-gauge")]:
        export_step(Compound(children=[by[key]]), str(root / "step" / f"{stem}.step"))
        export_stl(by[key], str(root / "stl" / f"{stem}.stl"))
    export_stl(press_only(parts), str(root / "stl" / "potpress-press.stl"))
    L = levels()
    bb = press_only(parts).bounding_box()
    print(f"press envelope {bb.size.X:.0f} x {bb.size.Y:.0f} x {bb.size.Z:.0f} mm (carriage rails extended to the front)")
    print(f"overall height {L['overall']:.0f} mm; male tip above female rim when open {L['open_gap']:.0f} mm")
    print("wrote cad/step/*.step and cad/stl/*.stl")
