"""PotPress product appearance model (build123d), TRL 3.

Finished-product look for photoreal renders: painted channel frame with hex-head joint bolts,
washers and nuts; a red 20 t bottle jack with a polished ram, serrated saddle, pump socket and
release valve knob; coiled return springs; a guided platen; rails with barrel hinges and a
carriage with a rubber-gripped pull handle; filleted cast aluminum female and male molds with an
ID plate; the teal male mold slide with a rounded SHS stem, a bright load pin with its lynch pin,
a bronze lead screw nut and a round-rim handwheel with a black grip knob; a nameplate and a load
rating label on the top crossbeam; the freshly pressed (green) pot between the molds. The QC
flow-test rack is an accessory: steel angle legs and edge frames, plywood shelves, fired test
pots, HDPE buckets, a printed T-gauge and water in one pot. Context is a compact patch of
workshop floor with an anti-fatigue mat at the operator side.
APPEARANCE MODEL ONLY: no tolerances, no fabrication detail. CONCEPT, NOT FOR FABRICATION.

Every main dimension, level and interface comes from PARAMS, SECTIONS, levels() and the helpers
in model.py. Axes as model.py: X across the press, Y front (-Y, operator side) to back, Z up
from the floor. The press is closed at the end of a pressing stroke with the rail extension
folded. Guarded version (decided by Amish 2026-09-26, PPR-DDR-003): fixed welded-mesh guards on
yellow powder-coated angle frames (group "guard"), the hinged front gate closed (group
"gate_closed") or swung open (group "gate_open"), a red guard-locking interlock on the right front
post with its link to the jack release T-handle, and a hazard label. The mesh is drawn wire by wire
at the specified 12.7 mm pitch as square wires, so it stays light to tessellate.

    from product_model import product_parts
    for p in product_parts(): print(p["name"], p["group"], p["material"])
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build123d import (Axis, Compound, Cylinder, Pos, RectangleRounded, RegularPolygon, Rot,
                       Torus, extrude, fillet)
from model import (PARAMS, SECTIONS, angle_frame, box, channel_upright, channel_x, cone, cyl, cyl_y,
                   guard_layout, levels, mesh_panel, pot, pot_outer)

TITLE = "PotPress: hand-pumped hydraulic press for ceramic pot water filters"

RENDER_VIEWS = [
    {"name": "hero", "groups": ["shell", "guard", "gate_closed", "internal", "context"], "explode": False,
     "el": 30, "az": -40,
     "note": "Product render from the front right and above (about 30 deg elevation); press closed at the end "
             "of a stroke behind welded-mesh guards with the interlocked front gate closed; bottle jack under "
             "the platen, molds on the slide-out carriage, handwheel on top"},
    {"name": "exploded", "groups": ["shell", "internal"], "explode": True, "el": 28, "az": -55,
     "note": "Exploded view from the front right and above (about 28 deg elevation): base beam and feet, "
             "uprights and joint bolts, bottle jack, springs, platen, rails and carriage, female mold, "
             "pressed pot, male mold, top crossbeam, male mold slide and handwheel; guards and gate not shown"},
    {"name": "lineup", "groups": ["shell", "guard", "gate_closed", "internal", "accessory", "context"],
     "explode": False, "el": 24, "az": -58,
     "note": "Lineup from the front right and above (about 24 deg elevation): the press at left and the "
             "2 x 2 QC flow-test rack at right with fired test pots, T-gauge and collection buckets"},
    {"name": "gate-open", "groups": ["shell", "guard", "gate_open", "internal", "context"], "explode": False,
     "el": 18, "az": -68,
     "note": "Front gate swung open (about 105 deg) on its left hinges, showing the molds and carriage; "
             "press parts drawn in the pressing position for comparison with the hero. In use the gate "
             "opens only after the jack release is open and the platen is down"},
]

# Colours (restrained product palette; kit accent)
C_FRAME = "#3A4048"      # painted steel channel
C_FRAME2 = "#4A515A"     # base and feet
C_PLATEN = "#7D858F"
C_ACCENT = "#0F766E"
C_JACK = "#A32020"
C_CHROME = "#D5D9DE"
C_ZINC = "#B8BEC6"
C_BRONZE = "#B08D57"
C_ALU = "#C9CED4"
C_ALU2 = "#B4BAC1"
C_RAIL = "#5B626B"
C_SPRING = "#C9A227"
C_BLACK = "#1C1F24"
C_RUBBER = "#26292E"
C_LABEL = "#F4F4F2"
C_INK = "#1F2937"
C_YELLOW = "#E8B517"
C_GREEN_POT = "#8A5A3C"   # freshly pressed (green) clay
C_FIRED_POT = "#C07A4F"   # fired terracotta
C_PLY = "#CFAE84"
C_BUCKET = "#E9EDF0"
C_WATER = "#BFE3F2"
C_FLOOR = "#D8D5CF"
C_GUARD = "#E2A90F"       # safety-yellow powder-coated guard frames
C_MESH = "#6F767F"        # galvanized welded mesh (shaded darker so the press reads through it)
C_INTERLOCK = "#C62828"   # guard-locking interlock housing


def _fillet_try(shape, edges, radii):
    """Fillet `edges` with the first radius that gives a valid solid; else return the input."""
    edges = list(edges)
    if not edges:
        return shape
    for r in radii:
        try:
            out = fillet(edges, r)
            if out.is_valid and out.volume > 0:
                return out
        except Exception:
            pass
    return shape


def _hex_y(x, y0, y1, z, af):
    """Hex prism along Y from y0 to y1, across flats `af`."""
    return Pos(x, (y0 + y1) / 2, z) * Rot(90, 30, 0) * extrude(RegularPolygon(af / 1.732, 6), amount=abs(y1 - y0) / 2,
                                                              both=True)


def _hex_z(x, y, z0, z1, af):
    return Pos(x, y, z0) * extrude(RegularPolygon(af / 1.732, 6), amount=z1 - z0)


def _circ_edges(s, r, tol=0.6):
    """Circular edges of radius about r."""
    out = []
    for e in s.edges():
        try:
            if e.geom_type.name == "CIRCLE" and abs(e.radius - r) < tol:
                out.append(e)
        except Exception:
            pass
    return out


def _comp(shapes):
    return Compound(children=list(shapes))


def product_parts(P=PARAMS):
    L = levels(P)
    b = SECTIONS[P["BEAM_SEC"]]; u = SECTIONS[P["UPRIGHT_SEC"]]; pl = SECTIONS[P["PLATEN_SEC"]]
    f = SECTIONS[P["FOOT_SEC"]]
    g2 = P["BEAM_GAP"] / 2; xs = P["SPAN"] / 2; bl = P["BEAM_L"] / 2
    out = []

    def add(name, shape, color, material, bom, group, explode):
        out.append({"name": name, "shape": shape, "color": color, "material": material,
                    "bom": bom, "group": group, "explode": tuple(float(v) for v in explode)})

    # ------------------------------------------------------------ 1 base beam, feet, jack plate
    EB = (0, 0, -260)
    base = channel_x(-bl, bl, g2, +1, L["base0"], P["BEAM_SEC"]) + channel_x(-bl, bl, -g2, -1, L["base0"], P["BEAM_SEC"])
    base += box(-100, 100, -90, 90, L["base1"], L["jack0"])
    add("Base beam and jack bearing plate", base, C_FRAME2, "painted", 1, "shell", EB)
    feet = None
    for sx in (-1, 1):
        xc = sx * (xs + 60)
        ft = box(xc - f["h"] / 2, xc + f["h"] / 2, -P["FOOT_L"] / 2, P["FOOT_L"] / 2, 0, f["tw"])
        for dx in (-1, 1):
            ft += box(xc + dx * f["h"] / 2 - (f["tf"] if dx > 0 else 0), xc + dx * f["h"] / 2 + (0 if dx > 0 else f["tf"]),
                      -P["FOOT_L"] / 2, P["FOOT_L"] / 2, 0, f["b"])
        # end caps close the channel ends (finished look)
        for sy in (-1, 1):
            y0 = sy * P["FOOT_L"] / 2
            ft += box(xc - f["h"] / 2, xc + f["h"] / 2, *sorted((y0, y0 - sy * 4)), 0, f["b"])
        feet = ft if feet is None else feet + ft
    add("Feet (UPN 100, end capped)", feet, C_FRAME2, "painted", 1, "shell", EB)

    # floor anchors and foot-to-beam bolts (BOM 18), hex nuts on washers
    anc = []
    nut = _hex_z(0, 0, f["tw"] + 2.5, f["tw"] + 12.5, 19.0)
    nut = _fillet_try(nut, nut.faces().sort_by(Axis.Z)[-1].edges(), [1.2, 0.6])
    wsh = cyl(12.0, f["tw"], f["tw"] + 2.5)
    stud = cyl(6.0, f["tw"] + 12.5, f["tw"] + 18.0)
    for sx in (-1, 1):
        for sy in (-1, 1):
            p_ = Pos(sx * (xs + 60), sy * (P["FOOT_L"] / 2 - 45), 0)
            anc += [p_ * nut, p_ * wsh, p_ * stud]
    add("Floor anchor nuts and washers", _comp(anc), C_ZINC, "metal", 18, "shell", EB)

    # ------------------------------------------------------------ 2 uprights and joint bolts
    upr = None
    for sx in (-1, 1):
        pair = channel_upright(sx * xs, -1, L["base0"], L["top1"], P["UPRIGHT_SEC"]) + \
            channel_upright(sx * xs, +1, L["base0"], L["top1"], P["UPRIGHT_SEC"])
        upr = pair if upr is None else upr + pair
    add("Uprights (back-to-back UPN 100)", upr, C_FRAME, "painted", 2, "shell", (0, 0, 0))

    rb_ = P["JOINT_BOLT_D"] / 2
    yb = g2 + b["tw"]
    head = _hex_y(0, -yb - 13, -yb - 3, 0, 30.0)
    head = _fillet_try(head, head.faces().sort_by(Axis.Y)[0].edges(), [1.5, 0.8])
    washer = cyl_y(18.5, -yb - 3, -yb, 0, 0)
    nutb = _hex_y(0, yb + 3, yb + 19, 0, 30.0)
    nutb = _fillet_try(nutb, nutb.faces().sort_by(Axis.Y)[-1].edges(), [1.5, 0.8])
    washer2 = cyl_y(18.5, yb, yb + 3, 0, 0)
    tail = cyl_y(rb_, yb + 19, yb + 25, 0, 0)
    tail = _fillet_try(tail, tail.faces().sort_by(Axis.Y)[-1].edges(), [1.5, 1.0])
    heads, nuts = [], []
    for sx in (-1, 1):
        for zc in ((L["base0"] + L["base1"]) / 2, (L["top0"] + L["top1"]) / 2):
            for dx in (-P["JOINT_BOLT_DX"], P["JOINT_BOLT_DX"]):
                for dz in (-P["JOINT_BOLT_DZ"], P["JOINT_BOLT_DZ"]):
                    p_ = Pos(sx * xs + dx, 0, zc + dz)
                    heads += [p_ * head, p_ * washer]
                    nuts += [p_ * nutb, p_ * washer2, p_ * tail]
    add("Joint bolt heads and washers (M20 8.8)", _comp(heads), C_ZINC, "metal", 2, "shell", (0, -160, 0))
    add("Joint nuts and washers", _comp(nuts), C_ZINC, "metal", 2, "shell", (0, 160, 0))

    # ------------------------------------------------------------ 3 top crossbeam
    ET = (0, 0, 560)
    top = channel_x(-bl, bl, g2, +1, L["top0"], P["BEAM_SEC"]) + channel_x(-bl, bl, -g2, -1, L["top0"], P["BEAM_SEC"])
    dl = P["DOUBLER_L"] / 2
    for sy in (-1, 1):
        y0 = g2 + b["tw"]; y1 = y0 + P["DOUBLER_T"]
        top += box(-dl, dl, *sorted((sy * y0, sy * y1)), L["top0"] + b["tf"], L["top1"] - b["tf"])
    top -= cyl_y(P["PIN_D"] / 2 + 1, -g2 - 40, g2 + 40, 0, L["pin"])
    add("Top crossbeam with pin doublers", top, C_FRAME, "painted", 3, "shell", ET)
    s2 = P["STEM"] / 2
    guides = box(-s2 - 30, -s2 - 1, -g2, g2, L["top0"], L["top1"]) + box(s2 + 1, s2 + 30, -g2, g2, L["top0"], L["top1"])
    add("Stem guide liners (UHMW-PE)", guides, "#F2F2EE", "plastic", 3, "shell", ET)

    # nameplate (teal, white print) and load rating label (yellow), on the front web, thin raised parts
    yf = -g2 - b["tw"]
    zc = L["pin"]
    npl = box(-250 + 12, -110, yf - 1.2, yf, zc - 32, zc + 32)
    npl = _fillet_try(npl, npl.edges().filter_by(Axis.Y), [4.0, 2.0])
    add("Nameplate", npl, C_ACCENT, "painted", 3, "shell", ET)
    ink = box(-222, -150, yf - 1.5, yf - 1.2, zc + 6, zc + 20) + box(-222, -175, yf - 1.5, yf - 1.2, zc - 6, zc) \
        + box(-222, -130, yf - 1.5, yf - 1.2, zc - 20, zc - 15)
    add("Nameplate print", ink, C_LABEL, "paper", 3, "shell", ET)
    rl = box(110, 238, yf - 0.6, yf, zc - 30, zc + 30)
    add("Load rating label (20 t max)", rl, C_YELLOW, "paper", 3, "shell", ET)
    rink = box(122, 170, yf - 0.9, yf - 0.6, zc + 4, zc + 20) + box(122, 226, yf - 0.9, yf - 0.6, zc - 8, zc - 3) \
        + box(122, 200, yf - 0.9, yf - 0.6, zc - 20, zc - 15)
    add("Load rating label print", rink, C_INK, "paper", 3, "shell", ET)

    # ------------------------------------------------------------ 4 bottle jack
    EJ = (0, -560, -120)
    jb = P["JACK_BASE"] / 2
    j0, jt = L["jack0"], L["platen0_low"] - 20
    jbase = box(-jb, jb, -jb, jb, j0, j0 + 25)
    jbase = _fillet_try(jbase, jbase.edges().filter_by(Axis.Z), [12.0, 8.0])
    jbase = _fillet_try(jbase, jbase.faces().sort_by(Axis.Z)[-1].edges(), [3.0, 1.5])
    rbody = P["JACK_BODY_D"] / 2
    body = cyl(rbody, j0 + 25, jt - 12) + cyl(rbody + 3, jt - 12, jt)
    body += cyl(rbody + 3, j0 + 25, j0 + 35)
    body = _fillet_try(body, _circ_edges(body, rbody + 3), [2.0, 1.0])
    # pump boss and handle socket (the model's pump envelope, x = jb - 10 to jb + 150)
    zp = j0 + 72
    boss = box(rbody - 20, jb + 10, -22, 22, j0 + 25, j0 + 95)
    boss = _fillet_try(boss, boss.edges().filter_by(Axis.Z), [8.0, 4.0])
    sock = Pos((jb + 10 + jb + 150) / 2, 0, zp) * Rot(0, 90, 0) * Cylinder(12, 140)
    sock -= Pos(jb + 150, 0, zp) * Rot(0, 90, 0) * Cylinder(8, 40)
    plunger = cyl(9, j0 + 95, j0 + 125, x=rbody - 5)
    add("20 t bottle jack body", jbase + body + boss, C_JACK, "painted", 4, "shell", EJ)
    add("Jack pump socket and plunger", sock + plunger, C_BLACK, "painted", 4, "shell", EJ)
    ram = cyl(P["RAM_D"] / 2, jt, L["platen0"] - 14)
    add("Jack ram (polished)", ram, C_CHROME, "metal", 4, "shell", EJ)
    sad = cyl(P["RAM_D"] / 2 - 4, L["platen0"] - 14, L["platen0"])
    for k in range(3):
        zk = L["platen0"] - 3 - 4 * k
        sad -= cyl(P["RAM_D"] / 2, zk - 1, zk) - cyl(P["RAM_D"] / 2 - 5.5, zk - 2, zk + 1)
    add("Jack screw saddle (serrated)", sad, C_ZINC, "metal", 4, "shell", EJ)
    rv = cyl_y(6, -jb - 16, -jb + 2, 30, j0 + 12)
    rv += cyl_y(10, -jb - 26, -jb - 16, 30, j0 + 12)
    rv = _fillet_try(rv, _circ_edges(rv, 10), [2.0, 1.0])
    add("Jack release valve knob", rv, C_BLACK, "plastic", 4, "shell", EJ)
    lab = cyl(rbody + 0.4, j0 + 70, j0 + 140) - cyl(rbody - 1, j0 + 60, j0 + 150)
    lab &= box(-90, 20, -rbody - 5, -10, j0 + 60, j0 + 150)
    add("Jack rating label", lab, C_LABEL, "paper", 4, "shell", EJ)
    link = cyl(rbody + 0.7, j0 + 108, j0 + 124) - cyl(rbody - 1, j0 + 100, j0 + 130)
    link &= box(-75, 0, -rbody - 5, -20, j0 + 100, j0 + 130)
    add("Jack rating label print", link, C_INK, "paper", 4, "shell", EJ)

    # ------------------------------------------------------------ 5 moving platen
    EP = (0, 0, -40)
    xin = xs - u["b"] - P["SLEEVE_T"] - P["SLEEVE_CLEAR"] / 2
    plat = channel_x(-xin, xin, g2, +1, L["platen0"], P["PLATEN_SEC"]) + channel_x(-xin, xin, -g2, -1, L["platen0"], P["PLATEN_SEC"])
    deck = box(-xin, xin, -220, 220, L["platen0"] + pl["h"], L["deck1"])
    deck = _fillet_try(deck, deck.edges().filter_by(Axis.Z), [10.0, 6.0])
    plat += deck
    plat += box(-100, 100, -g2, g2, L["platen0"], L["platen0"] + P["PLATEN_PAD_T"])
    for sx in (-1, 1):
        c = P["SLEEVE_CLEAR"] / 2; t = P["SLEEVE_T"]
        xo0, xo1 = sx * xs - u["b"] - c - t, sx * xs + u["b"] + c + t
        yo = u["h"] / 2 + c + t
        z0 = L["platen0"] - 20; z1 = z0 + P["SLEEVE_H"]
        sl = box(xo0, xo1, -yo, yo, z0, z1) - box(xo0 + t, xo1 - t, -yo + t, yo - t, z0 - 1, z1 + 1)
        plat += sl
    add("Moving platen with guide sleeves", plat, C_PLATEN, "painted", 5, "shell", EP)
    # grease nipples on the sleeves
    gn = []
    for sx in (-1, 1):
        gx = sx * xs
        gn.append(cyl_y(4, -u["h"] / 2 - 30, -u["h"] / 2 - 11, gx, L["platen0"] + 100))
        gn.append(Pos(gx, -u["h"] / 2 - 25, L["platen0"] + 100) * Rot(90, 0, 0) * Cylinder(6, 6))
    add("Sleeve grease nipples", _comp(gn), C_BRONZE, "metal", 5, "shell", EP)

    # ------------------------------------------------------------ 6 return springs (coils)
    # close-wound coils drawn as stacked annular turns (light to tessellate), hooks at both ends
    coils = []
    z_a, z_b = L["base1"] + 14, L["platen0"] - 14
    n = int((z_b - z_a) / 5.0)
    pitch = (z_b - z_a) / n
    turn = cyl(12.0, 0, pitch - 1.0) - cyl(7.4, -1, pitch)
    for sx in (-1, 1):
        x_ = sx * 190
        for k in range(n):
            coils.append(Pos(x_, 0, z_a + k * pitch) * turn)
        for zz, zh in ((z_a, L["base1"]), (z_b, L["platen0"])):     # hooks
            rr = abs(zz - zh) / 2 + 1
            hk = Pos(x_, 0, (zz + zh) / 2) * Rot(90, 0, 0) * (Cylinder(rr + 2.3, 4.6) - Cylinder(rr - 2.3, 6))
            coils.append(hk)
    add("Return springs", _comp(coils), C_SPRING, "metal", 6, "shell", (0, 460, -60))

    # ------------------------------------------------------------ 7 rails, hinged extension, carriage
    ER = (0, -520, 40)
    rw = P["RAIL_W"] / 2
    y_front = -P["RAIL_BACK"] - P["CARRIAGE_OUT"]
    y_h = -P["RAIL_HINGE"]
    ext_len = y_h - y_front
    rails = None
    hinges = []
    for xr in P["RAIL_X"]:
        for sx in (-1, 1):
            r = box(sx * xr - rw, sx * xr + rw, y_h, P["RAIL_BACK"], L["deck1"], L["rail1"])
            if P["EXT_FOLDED"]:
                r += box(sx * xr - rw, sx * xr + rw, y_h - P["RAIL_H"], y_h, L["rail1"] - ext_len, L["rail1"])
            else:
                r += box(sx * xr - rw, sx * xr + rw, y_front, y_h, L["deck1"], L["rail1"])
            rails = r if rails is None else rails + r
            hinges.append(Pos(sx * xr, y_h - P["RAIL_H"] - 5, L["deck1"] - 4) * Rot(0, 90, 0) * Cylinder(7, P["RAIL_W"] + 6))
    for sx in (-1, 1):
        xa, xb = sorted((sx * (P["RAIL_X"][0] - rw), sx * (P["RAIL_X"][1] + rw)))
        rails += box(xa, xb, y_h - 4, y_h + 12, L["deck1"] - 12, L["deck1"])
    rails += box(-200, 200, P["RAIL_BACK"], P["RAIL_BACK"] + 15, L["rail1"], L["rail1"] + 40)
    add("Rails with hinged extension (folded)", rails, C_RAIL, "metal", 7, "shell", ER)
    add("Rail extension barrel hinges", _comp(hinges), C_ZINC, "metal", 7, "shell", ER)
    fr = P["FM_BASE_D"] / 2 + 5
    car = box(-fr - 25, fr + 25, -fr - 25, fr + 25, L["rail1"], L["rail1"] + 12) - \
        box(-fr, fr, -fr, fr, L["rail1"] - 1, L["rail1"] + 13)
    car = _fillet_try(car, car.edges().filter_by(Axis.Z), [6.0, 3.0])
    hnd = box(-70, 70, -fr - 60, -fr - 25, L["rail1"], L["rail1"] + 12) + \
        box(-70, 70, -fr - 60, -fr - 45, L["rail1"] + 12, L["rail1"] + 110)
    hnd = _fillet_try(hnd, hnd.edges().filter_by(Axis.Y), [5.0, 3.0])
    for sx in (-1, 1):
        car += cyl_y(14, -20, 20, sx * (fr + 40), L["rail1"] + 25)
    add("Mold carriage frame with tilt pivots", car + hnd, C_FRAME, "painted", 7, "shell", ER)
    grip = Pos(0, -fr - 52.5, L["rail1"] + 96) * Rot(0, 90, 0) * Cylinder(11, 120)
    grip = _fillet_try(grip, grip.edges(), [3.0, 1.5])
    add("Carriage handle grip", grip, C_RUBBER, "rubber", 7, "shell", ER)

    # ------------------------------------------------------------ 8 female mold (cast aluminum)
    EF = (0, -520, 200)
    rbo, rto, h = pot_outer(P)
    sh = P["FM_SHELL"]
    fem = cyl(P["FM_BASE_D"] / 2, L["fm0"], L["pot0"]) + cone(rbo + sh, rto + sh, L["pot0"], L["fm1"]) + \
        cyl(P["FM_FLANGE_D"] / 2, L["fm1"] - P["FM_FLANGE_T"], L["fm1"])
    fem -= cone(rbo, rto, L["pot0"], L["fm1"] + 0.01)
    fem -= cyl(P["RIM_OD"] / 2, L["fm1"] - P["RIM_T"], L["fm1"] + 1)
    fem -= cyl(P["FLASH_R"], L["fm1"] - 3, L["fm1"] + 1) - cyl(P["RIM_OD"] / 2, L["fm1"] - 4, L["fm1"] + 2)
    r_fit = P["MM_FLANGE_D"] / 2 + P["LOC_CLEAR"] / 2
    if P["LOC_H"] > 0:      # the turned lip was replaced by locating pins (PPR-DDR-004)
        fem += cyl(P["FM_FLANGE_D"] / 2, L["fm1"], L["fm1"] + P["LOC_H"]) - \
            cone(r_fit, r_fit + P["LOC_TAPER"], L["fm1"] - 0.01, L["fm1"] + P["LOC_H"] + 0.01)
    fem = _fillet_try(fem, _circ_edges(fem, P["FM_FLANGE_D"] / 2), [3.0, 2.0, 1.0])
    fem = _fillet_try(fem, _circ_edges(fem, P["FM_BASE_D"] / 2), [3.0, 2.0, 1.0])
    add("Female mold (cast aluminum)", fem, C_ALU, "metal", 8, "shell", EF)
    rf = P["FM_FLANGE_D"] / 2
    idp = cyl(rf + 0.8, L["fm1"] - 30, L["fm1"] - 12) - cyl(rf - 1, L["fm1"] - 32, L["fm1"] - 10)
    idp &= box(-45, 45, -rf - 5, -rf + 30, L["fm1"] - 32, L["fm1"] - 10)
    add("Female mold ID plate", idp, "#E6E8EA", "metal", 8, "shell", EF)
    rv_ = []
    for xx in (-38, 38):
        rv_.append(Pos(xx, -((rf + 0.8) ** 2 - xx ** 2) ** 0.5, L["fm1"] - 21) * Rot(90, 0, 0) * Cylinder(2.2, 2.0))
    add("ID plate rivets", _comp(rv_), C_ZINC, "metal", 8, "shell", EF)

    # ------------------------------------------------------------ 9 male mold (cast aluminum)
    EM = (0, 0, 440)
    slope = (P["R_IN_RIM"] - P["R_IN_BOT"]) / P["D_IN"]
    z_tip = L["fm1"] - P["D_IN"]
    male = cone(P["R_IN_BOT"], P["R_IN_RIM"], z_tip, L["fm1"]) + cyl(P["MM_FLANGE_D"] / 2, L["fm1"], L["mm1"])
    z_in = z_tip + P["MM_TIP"]
    ti = P["MM_SHELL"]
    male -= cone(P["R_IN_BOT"] + slope * P["MM_TIP"] - ti, P["R_IN_RIM"] - ti, z_in, L["fm1"] + 0.01)
    male = _fillet_try(male, [e for e in _circ_edges(male, P["MM_FLANGE_D"] / 2) if e.center().Z > L["fm1"] + 1],
                       [3.0, 2.0, 1.0])
    male = _fillet_try(male, _circ_edges(male, P["R_IN_BOT"]), [6.0, 4.0, 2.0])
    add("Male mold (cast aluminum)", male, C_ALU2, "metal", 9, "shell", EM)

    # ------------------------------------------------------------ 10 male mold slide and crank
    ES = (0, 0, 680)
    t = P["STEM_T"]
    adp = box(-90, 90, -90, 90, L["mm1"], (L["mm1"] + P["ADAPTER_T"]))
    adp = _fillet_try(adp, adp.edges().filter_by(Axis.Z), [10.0, 6.0])
    screws = []
    for sx in (-1, 1):
        for sy in (-1, 1):
            hs = _hex_z(sx * 70, sy * 70, (L["mm1"] + P["ADAPTER_T"]), (L["mm1"] + P["ADAPTER_T"]) + 8, 18.0)
            screws.append(hs)
    ro = 2 * t                                           # SHS outer corner radius
    stem = Pos(0, 0, (L["mm1"] + P["ADAPTER_T"])) * extrude(RectangleRounded(P["STEM"], P["STEM"], ro), amount=L["stem1"] - (L["mm1"] + P["ADAPTER_T"]))
    stem -= Pos(0, 0, (L["mm1"] + P["ADAPTER_T"]) + 15) * extrude(RectangleRounded(P["STEM"] - 2 * t, P["STEM"] - 2 * t, ro - t),
                                                 amount=L["stem1"] - (L["mm1"] + P["ADAPTER_T"]))
    stem += box(-s2 + t, s2 - t, -s2 + t, s2 - t, L["pin"] - 60, L["pin"] + 60)
    stem -= cyl_y(P["PIN_D"] / 2 + 1, -s2 - 1, s2 + 1, 0, L["pin"])
    add("Male mold stem and adapter plate", adp + stem, C_ACCENT, "painted", 10, "shell", ES)
    add("Adapter plate screws", _comp(screws), C_ZINC, "metal", 10, "shell", ES)
    pin = cyl_y(P["PIN_D"] / 2, -P["PIN_L"] / 2, P["PIN_L"] / 2, 0, L["pin"])
    ph = cyl_y(P["PIN_D"] / 2 + 10, -P["PIN_L"] / 2 - 12, -P["PIN_L"] / 2, 0, L["pin"])
    ph = _fillet_try(ph, _circ_edges(ph, P["PIN_D"] / 2 + 10), [3.0, 1.5])
    pin = pin + ph
    pin = _fillet_try(pin, [e for e in _circ_edges(pin, P["PIN_D"] / 2) if e.center().Y > 0], [4.0, 2.0])
    for k in range(4):                                   # knurl grooves on the pin head
        yk = -P["PIN_L"] / 2 - 10 + 2.5 * k
        pin -= cyl_y(P["PIN_D"] / 2 + 12, yk, yk + 1.0, 0, L["pin"]) - cyl_y(P["PIN_D"] / 2 + 8.8, yk - 1, yk + 2, 0, L["pin"])
    add("Load pin (42CrMo4)", pin, C_CHROME, "metal", 10, "shell", (0, -300, 680))
    lynch = Pos(0, P["PIN_L"] / 2 - 10, L["pin"]) * Rot(90, 0, 0) * Torus(P["PIN_D"] / 2 + 4, 2.2)
    lynch &= box(-60, 60, P["PIN_L"] / 2 - 20, P["PIN_L"] / 2, L["pin"] - 5, L["pin"] + 60)
    add("Pin retaining ring", lynch, C_ZINC, "metal", 10, "shell", (0, -300, 680))

    brk = None
    for sx in (-1, 1):
        sp = box(sx * 80 - 5, sx * 80 + 5, -80, 80, L["top1"], L["bracket0"])
        sp = _fillet_try(sp, sp.edges().filter_by(Axis.X), [6.0, 3.0])
        # lightening window in each side plate shows the stem and lead screw
        win = Pos(sx * 80, 0, (L["top1"] + L["bracket0"]) / 2) * Rot(0, 90, 0) * \
            extrude(RectangleRounded(L["bracket0"] - L["top1"] - 70, 100, 20), amount=10, both=True)
        sp -= win
        brk = sp if brk is None else brk + sp
    tp = box(-100, 100, -80, 80, L["bracket0"], L["bracket1"])
    tp = _fillet_try(tp, tp.edges().filter_by(Axis.Z), [12.0, 8.0])
    brk += tp
    add("Crank bracket", brk, C_FRAME, "painted", 10, "shell", ES)
    lead = cyl(P["LEAD_D"] / 2, L["stem1"] - 40, L["wheel"] + 15)
    add("Tr24 lead screw", lead, C_ZINC, "metal", 10, "shell", ES)
    lnut = cyl(22, L["bracket1"], L["bracket1"] + 14) + _hex_z(0, 0, L["bracket1"] + 14, L["bracket1"] + 26, 36.0)
    lnut = _fillet_try(lnut, _circ_edges(lnut, 22), [2.0, 1.0])
    add("Lead screw nut (bronze)", lnut, C_BRONZE, "metal", 10, "shell", ES)

    hw = P["HANDWHEEL_D"] / 2
    zw = L["wheel"] + 6
    rim = Pos(0, 0, zw) * Torus(hw - 7, 7)
    spokes = [Pos(0, 0, zw) * Rot(0, 90, 0) * Cylinder(5.5, 2 * hw - 10), Pos(0, 0, zw) * Rot(90, 0, 0) * Cylinder(5.5, 2 * hw - 10)]
    hub = cyl(22, L["wheel"] - 4, L["wheel"] + 16)
    hub = _fillet_try(hub, hub.edges(), [3.0, 1.5])
    add("Handwheel rim and spokes", _comp([rim] + spokes), C_ACCENT, "painted", 10, "shell", ES)
    add("Handwheel hub", hub, C_ZINC, "metal", 10, "shell", ES)
    knob = cyl(10, L["wheel"] + 12, L["wheel"] + 70, x=hw - 7)
    knob = _fillet_try(knob, knob.faces().sort_by(Axis.Z)[-1].edges(), [4.0, 2.0])
    add("Handwheel grip knob", knob, C_BLACK, "plastic", 10, "shell", ES)

    # ------------------------------------------------------------ 11 freshly pressed pot, between the molds
    add("Pressed filter pot (green, unfired)", pot(L["pot0"], P=P), C_GREEN_POT, "clay", 11, "internal", (0, -520, 620))

    # ------------------------------------------------------------ 12 to 14 QC flow-test rack (accessory)
    x0 = P["QC_X0"]; pch = P["QC_PITCH"]; W = 2 * pch
    y0 = -pch
    lg = P["QC_LEG"]
    legs = []
    for i, xx in enumerate((x0, x0 + W - lg)):
        for j, yy in enumerate((y0, y0 + W - lg)):
            ang = box(xx, xx + lg, yy, yy + lg, 0, P["QC_SHELF_Z"])
            cx = xx + (4 if i == 0 else 0); cy = yy + (4 if j == 0 else 0)
            ang -= box(cx, cx + lg - 4, cy, cy + lg - 4, -1, P["QC_SHELF_Z"] + 1)
            legs.append(ang)
    frames = []
    for zt in (P["QC_SHELF_Z"], P["QC_BUCKET_Z"]):
        fr_ = box(x0, x0 + W, y0, y0 + W, zt - 40, zt - 18) - box(x0 + 4, x0 + W - 4, y0 + 4, y0 + W - 4, zt - 41, zt)
        frames.append(fr_)
    add("QC rack legs (steel angle)", _comp(legs), C_FRAME, "painted", 12, "accessory", (0, 0, 0))
    add("QC rack edge frames", _comp(frames), C_FRAME, "painted", 12, "accessory", (0, 0, 0))
    stations = [(x0 + pch / 2 + i * pch, y0 + pch / 2 + j * pch) for i in (0, 1) for j in (0, 1)]
    ply = box(x0 + 4, x0 + W - 4, y0 + 4, y0 + W - 4, P["QC_SHELF_Z"] - 18, P["QC_SHELF_Z"])
    for (sx_, sy_) in stations:
        ply -= cyl(rto + 3, P["QC_SHELF_Z"] - 19, P["QC_SHELF_Z"] + 1, x=sx_, y=sy_)
    ply2 = box(x0 + 4, x0 + W - 4, y0 + 4, y0 + W - 4, P["QC_BUCKET_Z"] - 18, P["QC_BUCKET_Z"])
    add("QC pot shelf (plywood)", ply, C_PLY, "wood", 12, "accessory", (0, 0, 0))
    add("QC bucket shelf (plywood)", ply2, C_PLY, "wood", 12, "accessory", (0, 0, 0))

    z_tp = P["QC_SHELF_Z"] + P["RIM_T"] - h
    tps = [pot(z_tp, sx_, sy_, P) for (sx_, sy_) in stations]
    add("Fired test pots", _comp(tps), C_FIRED_POT, "clay", None, "accessory", (0, 0, 300))

    gx, gy = stations[0]
    zr = P["QC_SHELF_Z"] + P["RIM_T"]
    gauge = box(gx - 6, gx + 6, gy - 170, gy + 170, zr, zr + 12) + box(gx - 4, gx + 4, gy - 4, gy + 4, zr - P["GAUGE_SCALE"], zr)
    gauge = _fillet_try(gauge, gauge.edges().filter_by(Axis.Y), [2.0, 1.0])
    add("Printed T-gauge (PETG)", gauge, C_ACCENT, "plastic", 13, "accessory", (0, 0, 520))
    marks = [box(gx - 4.6, gx - 4.0, gy - 3, gy + 3, zr - 10 - 16.7 * k, zr - 9 - 16.7 * k) for k in range(6)]
    add("T-gauge scale marks", _comp(marks), C_LABEL, "paper", 13, "accessory", (0, 0, 520))

    bk = []
    zb = P["QC_BUCKET_Z"]
    rbk = P["BUCKET_D"] / 2
    for (sx_, sy_) in stations:
        bu = cone(rbk - 12, rbk, zb, zb + P["BUCKET_H"], sx_, sy_) - \
            cone(rbk - 15, rbk - 3, zb + 3, zb + P["BUCKET_H"] + 0.01, sx_, sy_)
        bu += cyl(rbk + 3, zb + P["BUCKET_H"] - 14, zb + P["BUCKET_H"] - 2, sx_, sy_) - \
            cyl(rbk - 2, zb + P["BUCKET_H"] - 15, zb + P["BUCKET_H"] - 1, sx_, sy_)
        for zz in (zb + 110, zb + 220):
            rr = rbk - 12 + 12 * (zz - zb) / P["BUCKET_H"]
            bu += cyl(rr + 2, zz, zz + 6, sx_, sy_) - cyl(rr - 2, zz - 1, zz + 7, sx_, sy_)
        bk.append(bu)
    add("Collection buckets (20 L HDPE)", _comp(bk), C_BUCKET, "plastic", 14, "accessory", (0, 0, -150))

    wz0 = z_tp + P["WALL"] + 0.5
    wz1 = zr - 10
    rw1 = P["R_IN_BOT"] + (P["R_IN_RIM"] - P["R_IN_BOT"]) * (wz1 - wz0) / P["D_IN"]
    water = cone(P["R_IN_BOT"] - 0.5, rw1 - 0.5, wz0, wz1, gx, gy)
    add("Water in test pot", water, C_WATER, "clear", None, "accessory", (0, 0, 300))

    # ------------------------------------------------------------ 16, 20, 21 guarded version (PPR-DDR-003)
    pitch, wire = P["MESH_PITCH"], P["MESH_WIRE"]
    out_dir = {"Right side guard": (500, 0, 0), "Left side guard": (-500, 0, 0), "Rear guard": (0, 500, 0),
               "Front left strip": (0, -500, 0), "Front right strip": (0, -500, 0), "Lower front panel": (0, -500, 0),
               "Roof guard": (0, 0, 400)}
    for pnl in guard_layout(P):
        ex = out_dir[pnl["name"]]
        fr_ = angle_frame(pnl["plane"], pnl["a0"], pnl["a1"], pnl["b0"], pnl["b1"], pnl["c_out"], pnl["inward"],
                          P["GUARD_ANGLE"], P["GUARD_ANGLE_T"])
        add(f"{pnl['name']} frame (powder-coated angle)", fr_, C_GUARD, "painted", 16, "guard", ex)
        wires = mesh_panel(pnl["plane"], pnl["a0"], pnl["a1"], pnl["b0"], pnl["b1"], pnl["c_out"], pnl["inward"],
                           pitch, wire, pnl["holes"])
        add(f"{pnl['name']} mesh (12.7 mm welded)", _comp(wires), C_MESH, "metal", 16, "guard", ex)
    gx = P["GUARD_X"]
    sw, sz0, sz1 = P["PUMP_SLOT"]
    slot = box(gx - 6.2, gx - 3.2, -sw / 2 - 12, sw / 2 + 12, sz0 - 12, sz1 + 12) - box(gx - 7, gx - 2, -sw / 2, sw / 2, sz0, sz1)
    add("Pump handle slot frame", slot, C_GUARD, "painted", 16, "guard", (500, 0, 0))
    brush = box(gx - 5.5, gx - 3.5, -sw / 2, -1, sz0, sz1) + box(gx - 5.5, gx - 3.5, 1, sw / 2, sz0, sz1)
    add("Pump slot brush strip", brush, C_RUBBER, "rubber", 16, "guard", (500, 0, 0))
    stand = []
    for sx in (-1, 1):
        for zc in ((L["base0"] + L["base1"]) / 2, (L["top0"] + L["top1"]) / 2):
            for sy in (-1, 1):
                stand.append(box(*sorted((sx * bl, sx * (gx - 3.2 - P["GUARD_ANGLE"]))), sy * 80 - 20, sy * 80 + 20, zc - 3, zc + 3))
    add("Guard standoff brackets", _comp(stand), C_GUARD, "painted", 16, "guard", (0, 0, 0))

    # hazard label on the front right strip: yellow plate, black triangle and text lines
    gh, yf = P["GATE_HALF"], P["GUARD_Y_FRONT"]
    xl0, xl1, zl0, zl1 = gh + 38, gx - 22, 1150.0, 1250.0
    lab = box(xl0, xl1, yf - 1.2, yf, zl0, zl1)
    lab = _fillet_try(lab, lab.edges().filter_by(Axis.Y), [4.0, 2.0])
    add("Hazard label (crush, keep gate closed)", lab, C_YELLOW, "paper", 16, "guard", (0, -500, 0))
    xc_ = xl0 + 32; zc_ = (zl0 + zl1) / 2
    tri = Pos(xc_, yf - 1.35, zc_ - 4) * Rot(90, 0, 0) * extrude(RegularPolygon(26, 3, rotation=90), amount=0.3, both=True)
    tri -= Pos(xc_, yf - 1.35, zc_ - 4) * Rot(90, 0, 0) * extrude(RegularPolygon(17, 3, rotation=90), amount=1, both=True)
    tri += box(xc_ - 2.5, xc_ + 2.5, yf - 1.5, yf - 1.2, zc_ - 8, zc_ + 8)
    txt = box(xl0 + 68, xl1 - 8, yf - 1.5, yf - 1.2, zc_ + 14, zc_ + 24) + box(xl0 + 68, xl1 - 30, yf - 1.5, yf - 1.2, zc_ - 2, zc_ + 6) \
        + box(xl0 + 68, xl1 - 18, yf - 1.5, yf - 1.2, zc_ - 18, zc_ - 10) + box(xl0 + 8, xl1 - 8, yf - 1.5, yf - 1.2, zl0 + 6, zl0 + 12)
    add("Hazard label print", tri + txt, C_INK, "paper", 16, "guard", (0, -500, 0))

    # front gate, closed and open: 20 x 20 tube frame, mesh, lift-off hinges, pull handle, striker tongue
    tb = P["GATE_TUBE"]
    x0g, x1g = -gh + 4, gh - 4
    z0g, z1g = P["GATE_Z0"] + 4, L["top1"] - 4
    yin = yf + 3.2
    gfr = box(x0g, x1g, yin, yin + tb, z0g, z1g) - box(x0g + tb, x1g - tb, yin - 1, yin + tb + 1, z0g + tb, z1g - tb)
    gfr = _fillet_try(gfr, gfr.edges().filter_by(Axis.Y), [2.0, 1.0])
    zm = (z0g + z1g) / 2
    gfr += box(x0g + tb, x1g - tb, yin, yin + tb, zm - tb / 2, zm + tb / 2)
    gmesh = _comp(mesh_panel("xz", x0g, x1g, z0g, z1g, yf, +1, pitch, wire))
    hx, hy = -gh, yf - 12
    knuck, leaves = [], []
    for zh in (z0g + 120, z1g - 120):
        k_ = cyl(8, zh - 40, zh + 40, x=hx, y=hy)
        k_ = _fillet_try(k_, k_.edges(), [1.5, 0.8])
        knuck.append(k_)
        knuck.append(cyl(3, zh + 40, zh + 46, x=hx, y=hy))
        leaves.append(box(hx + 6, x0g + tb, hy - 3, yf, zh - 25, zh + 25))
    post_leaf = [box(-gh - 60, hx - 6, hy - 3, yf, zh - 25, zh + 25) for zh in (z0g + 120, z1g - 120)]
    zl = 900.0
    grip = box(x1g - 60, x1g - 45, yf - 25, yf - 13, zl - 70, zl + 70)
    grip = _fillet_try(grip, grip.edges().filter_by(Axis.Z), [4.0, 2.0])
    posts = box(x1g - 60, x1g - 45, yf - 13, yf, zl - 70, zl - 58) + box(x1g - 60, x1g - 45, yf - 13, yf, zl + 58, zl + 70)
    striker = box(x1g - 5, gh + 30, yf - 16, yf - 10, zl - 15, zl + 15)
    gate = [("Front gate frame (powder-coated tube)", gfr + _comp(leaves), C_GUARD, "painted"),
            ("Front gate mesh (12.7 mm welded)", gmesh, C_MESH, "metal"),
            ("Front gate hinge knuckles", _comp(knuck), C_ZINC, "metal"),
            ("Front gate pull handle", grip + posts, C_BLACK, "plastic"),
            ("Front gate striker tongue", striker, C_ZINC, "metal")]
    rot = Pos(hx, hy, 0) * Rot(0, 0, -105) * Pos(-hx, -hy, 0)
    for nm, sh_, col, mat_ in gate:
        add(nm, sh_, col, mat_, 20, "gate_closed", (0, -600, 0))
        add(nm + ", open", rot * sh_, col, mat_, 20, "gate_open", (0, -600, 0))
    add("Gate hinge leaves on the post", _comp(post_leaf), C_GUARD, "painted", 20, "guard", (0, -500, 0))

    # 21 guard-locking interlock on the right front post, link rod, lock bar, jack release extension
    jb_ = P["JACK_BASE"] / 2
    zr = L["jack0"] + 12
    yr = P["RELEASE_Y"]
    unit = box(gh + 5, gh + 65, yf - 25, yf, zl - 55, zl + 55)
    unit = _fillet_try(unit, unit.edges().filter_by(Axis.Y), [4.0, 2.0])
    add("Gate interlock housing (guard locking)", unit, C_INTERLOCK, "painted", 21, "guard", (0, -500, 0))
    cap = box(gh + 12, gh + 58, yf - 26.5, yf - 25, zl + 12, zl + 45) + cyl_y(6, yf - 30, yf - 25, gh + 35, zl - 30)
    add("Interlock cover plate and bolt cap", cap, C_BLACK, "plastic", 21, "guard", (0, -500, 0))
    rod = cyl(5, zr + 22, zl - 55, x=gh + 35, y=yf - 12) + box(10, gh + 40, yf - 18, yf - 6, zr + 16, zr + 28)
    add("Interlock link rod and lock bar", rod, C_ZINC, "metal", 21, "guard", (0, -500, 0))
    lblk = box(0, 60, yr - 6, yf - 6, zr + 10, zr + 30)
    lblk = _fillet_try(lblk, lblk.edges().filter_by(Axis.Y), [3.0, 1.5])
    add("Release valve lock block", lblk, C_INTERLOCK, "painted", 21, "guard", (0, -500, 0))
    ext = cyl_y(6, yr, -jb_ - 26, 30, zr)
    add("Jack release extension rod", ext, C_ZINC, "metal", 21, "guard", (0, -500, 0))
    th = Pos(30, yr, zr) * Rot(0, 90, 0) * Cylinder(7, 110)
    th = _fillet_try(th, th.edges(), [3.0, 1.5])
    add("Release valve T-handle", th, C_BLACK, "rubber", 21, "guard", (0, -500, 0))

    # ------------------------------------------------------------ context: workshop floor and mat
    slab = box(-560, 560, -560, 440, -20, 0)
    slab = _fillet_try(slab, slab.faces().sort_by(Axis.Z)[-1].edges(), [4.0, 2.0])
    add("Workshop floor (concrete)", slab, C_FLOOR, "paper", None, "context", (0, 0, 0))
    mat = box(-300, 300, -545, -365, 0, 12)
    mat = _fillet_try(mat, mat.faces().sort_by(Axis.Z)[-1].edges(), [5.0, 3.0])
    for k in range(9):
        yk = -525 + 20 * k
        mat -= box(-280, 280, yk, yk + 6, 9, 13)
    add("Anti-fatigue mat", mat, C_RUBBER, "rubber", None, "context", (0, 0, 0))
    return out


if __name__ == "__main__":
    for p in product_parts():
        s = p["shape"]
        print(f"{p['name']:42s} {p['group']:9s} {p['material']:8s} valid={s.is_valid} vol={s.volume / 1000:9.2f} cm3")
