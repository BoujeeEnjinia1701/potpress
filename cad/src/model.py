"""PotPress parametric model (build123d), TRL 3, constructable design (PPR-DDR-004).

Run from the repo root:  python cad/src/model.py
Exports the assembly and the main parts to cad/step/*.step and cad/stl/*.stl, and runs the
fit checks (parts that must not touch, faces that must touch) with --check.

Axes: X across the press between the uprights, Y front (-Y, operator side; the mold
carriage slides out this way) to back (+Y), Z up from the floor. Units mm. The press
is shown closed at the end of a pressing stroke, load pin home, jack release closed,
with a formed pot between the molds, guarded: fixed welded-mesh guards and the hinged
front gate closed (PPR-DDR-003). The QC flow-test rack (2 x 2 stations) stands to the
right (+X). Guard mesh is drawn at every 8th wire (101.6 mm); the specified mesh is 12.7 mm.

components() returns every made or bought component on its own (for the build plan);
build_parts() groups them by BOM line (for the concept media, the drawing and the masses).
Design for construction changes (2026-09-30) are recorded in PPR-DDR-004. Sizing is in
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
    # Female mold (DDR-004): cast aluminum cup drawn from the flange side, bolted to a steel base plate
    "FM_SHELL": 20.0,       # shell thickness behind the cavity
    "FM_BASE": 30.0,        # everything under the cavity: steel base plate plus aluminum floor
    "FM_PLATE_T": 15.0,     # steel base plate (bears on the rails, sits in the carriage)
    "FM_PLATE_W": 350.0,    # base plate, square
    "FM_BASE_D": 350.0,     # kept for the appearance model (was the cast base disc)
    "FM_FLANGE_D": 450.0,   # top flange (stop face ring 360 to 450 mm)
    "FM_FLANGE_T": 40.0,
    "FLASH_R": 180.0,       # flash groove outer radius (stop face is outside this)
    # Mold location (DDR-004): two hardened pins in the female flange, steel bushes in the male flange,
    # drilled and reamed with the molds clamped together; replaces the turned 390 mm lip
    "LOC_PIN_D": 16.0,
    "LOC_PIN_R": 202.0,     # pin circle radius; pins on the X axis
    "LOC_PIN_PROUD": 20.0,  # pin height above the female stop face
    "LOC_PIN_DEPTH": 30.0,  # pressed into the female flange
    "BUSH_OD": 22.0,
    "LOC_CLEAR": 0.05,      # pin in bush, diametral (reamed)
    "LOC_H": 0.0,           # no turned lip any more (kept for the appearance model)
    "LOC_TAPER": 0.0,
    # Male mold (DDR-004): cast aluminum plug, open at the back (drafted core space), 45 mm flange
    "MM_SHELL": 15.0,       # plug shell thickness
    "MM_TIP": 30.0,         # plug tip (floor-forming) plate thickness
    "MM_FLANGE_D": 450.0,   # flange diameter; outer ring lands on the female stop face
    "MM_FLANGE_T": 45.0,
    "ADAPTER_T": 20.0,      # steel adapter disc at the stem foot, seated on the plug tip inside the core space
    "ADAPTER_D": 190.0,
    # Frame: channels are UPN sections (EN 10279); names index SECTIONS below
    "SPAN": 600.0,          # upright centerline spacing (beam span)
    "BEAM_SEC": "UPN160",   # top crossbeam and base beam, two channels each
    "BEAM_GAP": 104.0,      # clear gap between the channel webs: 100 mm uprights plus 2 mm shims each side (DDR-004)
    "SHIM_T": 2.0,
    "BEAM_L": 840.0,        # beam length
    "END_BLOCK_L": 10.0,    # end plates welded between the channel webs at each beam end
    "UPRIGHT_SEC": "UPN100",  # each upright is two channels back to back (100 x 100)
    "FOOT_SEC": "UPN100",   # feet, lying web up (DDR-004) so the base beam sits on the flat web
    "FOOT_L": 640.0,
    "ANCHOR_Y": 260.0,      # floor anchors through each foot, both ends
    "JOINT_BOLT_D": 16.0,   # M16 10.9 bolts, 4 per upright-to-beam joint (DDR-004; was M20 8.8)
    "JOINT_BOLT_DX": 28.0,  # bolt offset either side of the upright web plane (X): 22 mm from the flange tip
    "JOINT_BOLT_DZ": 30.0,  # bolt offset above and below the beam mid-height (Z)
    "SPACER_OD": 25.0,      # spacer tube inside the upright between its flanges (25 x 3 tube, 19 mm bore)
    "DOUBLER_T": 12.0,      # web doubler plates at the load pin
    "DOUBLER_L": 200.0,
    "BEARING_T": 20.0,      # jack bearing plate on the base beam
    "BEARING_W": 240.0,     # jack bearing plate, X; it spans the beam flanges in Y and is bolted on (DDR-004)
    # Jack and platen
    "JACK_CLOSED": 245.0,   # 20 t bottle jack, closed height including screw set
    "JACK_STROKE": 150.0,
    "JACK_BASE": 160.0,
    "JACK_BODY_D": 120.0,
    "RAM_D": 60.0,
    "JACK_TURN": -25.0,     # jack turned so its pump socket and release valve point 25 deg in front of +X (DDR-004)
    "PLATEN_SEC": "UPN140",  # two channels under a thin deck, with a jack pad
    "PLATEN_DECK_T": 6.0,
    "PLATEN_PAD_T": 20.0,
    "SLEEVE_T": 10.0,       # guide sleeve wall, around each upright
    "SLEEVE_H": 150.0,
    "SLEEVE_CLEAR": 1.0,    # diametral clearance on the upright
    "SPRING_X": 190.0,      # return springs, both sides of the jack, on anchor lugs
    "SPRING_LUG_T": 8.0,
    # Carriage and rails
    "RAIL_X": (60.0, 170.0),  # rail centerlines, both sides of the axis
    "RAIL_W": 30.0,
    "RAIL_H": 15.0,
    "RAIL_BACK": 205.0,     # back end stop face, +Y (carriage back edge touches it when the mold is centered)
    "CARRIAGE_OUT": 430.0,  # slide-out travel toward -Y
    "RAIL_HINGE": 290.0,    # hinge line of the folding rail extension, in front of the axis (DDR-004: was 320; the folded
                            # extension now clears the gate and the lower front panel with the platen down)
    "EXT_FOLDED": True,     # show the rail extension folded down (pressing); False = deployed for demolding
    "PIVOT_DY": 190.0,      # carriage tipping pins, this far in front of the carriage center
    "PIVOT_D": 12.0,
    # Male mold slide
    "STEM": 90.0,           # SHS 90 x 90 x 8
    "STEM_T": 8.0,
    "PIN_D": 60.0,          # single load pin, 42CrMo4 quenched and tempered
    "PIN_L": 173.0,         # shank under the head: through both webs and doublers, plus 30 for the R-clip
    "PIN_HEAD_T": 12.0,
    "LEAD_D": 24.0,         # Tr24 x 5 lead screw (lifts only)
    "LEAD_P": 5.0,
    "NUT_FLOAT": 8.0,
    "SCREW_HOLE": 28.0,     # hole down the middle of the pin block and the nut box floor: the fixed screw passes as the stem rises       # free space under the lead screw nut in its box, so press force bypasses the screw
    "HANDWHEEL_D": 260.0,
    # Kinematics
    "PRESS_TRAVEL": 110.0,  # jack travel used from mold contact to closed
    "CRANK_LIFT": 200.0,    # male mold lift by crank
    "LIFT_CLEAR": 15.0,     # clearance between the male flange and the top beam at full lift
    # QC rack, 2 x 2 stations (DDR-004: pot shelf raised so the hanging pots clear the buckets)
    "QC_X0": 760.0,         # rack left edge (X)
    "QC_PITCH": 390.0,      # station pitch in X and Y
    "QC_SHELF_Z": 720.0,    # pot shelf top (pot rims rest here)
    "QC_BUCKET_Z": 120.0,   # bucket shelf top
    "QC_SHELF_T": 18.0,     # plywood
    "QC_LEG": 40.0,         # 40 x 40 x 4 angle
    "QC_ANGLE_T": 4.0,
    "BUCKET_D": 300.0,      # 20 L food-grade bucket
    "BUCKET_H": 325.0,
    "GAUGE_SCALE": 100.0,   # T-gauge stem length below the rim
    # Guarding (guarded version, decided by Amish 2026-09-26, PPR-DDR-003). Mesh planes are outer faces.
    "MESH_PITCH": 12.7,     # welded mesh, 12.7 mm (1/2 in) square wire centers, about 11 mm clear opening
    "MESH_WIRE": 1.6,       # wire diameter (drawn square)
    "MESH_SHOW_EVERY": 8,   # model.py draws every 8th wire (101.6 mm) so views stay readable
    "GUARD_X": 470.0,       # side guard mesh plane, both sides of the axis
    "GUARD_Y_FRONT": -350.0,  # front mesh plane (gate and fixed front strips)
    "GUARD_Y_BACK": 325.0,  # rear guard mesh plane
    "GUARD_Z0": 60.0,       # bottom edge of the guards, above the feet
    "GUARD_ANGLE": 25.0,    # 25 x 25 x 3 angle frames on the fixed panels
    "GUARD_ANGLE_T": 3.0,
    "GATE_HALF": 290.0,     # gate opening from -290 to +290 in X (DDR-004: widened so the folded tipping blocks clear it)
    "GATE_Z0": 380.0,       # gate bottom; the lower front panel is fixed below it
    "GATE_TUBE": 20.0,      # 20 x 20 x 2 square tube gate frame
    "GATE_OPEN_DEG": 0.0,   # 0 = closed (pressing); about 105 = swung open to the left
    "PUMP_SLOT": (30.0, 174.0, 446.0),  # jack pump handle slot in the right side guard: width, z from, z to (DDR-004: 30 wide
                            # so the 20 mm handle passes the 6 mm guard at 25 deg; still in the 20 to 30 mm slot band).
                            # 2026-10-02: each end 25 mm beyond the handle at its stroke ends (ISO 13854 finger gap)
    "HANDLE_D": 20.0,       # jack pump handle, bought with the jack (or 20 mm tube), about 700 mm long
    "HANDLE_STROKE": (211.0, 409.0),  # handle centre line height where it crosses the guard, at the bottom and top of a stroke
    # Fixed inner shield (tunnel) behind the pump slot (decided by Amish 2026-10-02, PPR-DEC-001): 2 mm folded sheet
    # round the handle's path from the guard to the jack body, so through the slot only the handle and the jack's
    # pump socket can be reached; the platen, molds, springs and ram stay behind steel
    "SHIELD_T": 2.0,        # sheet thickness
    "SHIELD_W": 30.0,       # clear width across the handle (5 mm each side of the 20 mm handle)
    "SHIELD_GAP": 25.0,     # roof and floor stand this far beyond the handle at its stroke ends (ISO 13854 finger gap)
    "SHIELD_JACK_GAP": 3.0,  # inner end follows the jack body this far off it
    "SHIELD_STAY_R": 235.0,  # flat-bar stay from the tunnel floor to the base beam, this far out along the handle line
    # Interlock (DDR-004): lock rod on a post in front of the right front strip
    "STRIP_Y": -310.0,      # front right guard strip, set back 40 mm to make a pocket for the interlock (DDR-004)
    "LOCK_X": 330.0,        # lock rod and release shaft line, X
    "LOCK_Y": -360.0,       # lock rod, Y
    "LOCK_LIFT": 15.0,      # lock rod travel: the depth of the slot in the lock disc
    "LATCH_Z": 905.0,       # underside of the gate tongue
    "RELEASE_Y": -371.0,    # release knob, Y (front face at -375, the same depth as before)
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
    L["foot_top"] = f["b"]                           # channel lying web up: height = flange width
    L["base0"] = L["foot_top"]; L["base1"] = L["base0"] + b["h"]
    L["jack0"] = L["base1"] + P["BEARING_T"]
    L["platen0_low"] = L["jack0"] + P["JACK_CLOSED"]
    L["platen0"] = L["platen0_low"] + P["PRESS_TRAVEL"]            # closed
    L["deck1"] = L["platen0"] + pl["h"] + P["PLATEN_DECK_T"]
    L["rail1"] = L["deck1"] + P["RAIL_H"]
    L["fm0"] = L["rail1"]                                          # female base plate underside
    _, _, h_out = pot_outer(P)
    L["pot0"] = L["fm0"] + P["FM_BASE"]                            # pot outer floor
    L["fm1"] = L["pot0"] + h_out                                   # female top = pot rim top = stop face
    L["mm1"] = L["fm1"] + P["MM_FLANGE_T"]                         # male flange top
    L["tip"] = L["fm1"] - P["D_IN"]                                # male plug tip
    L["adapter0"] = L["tip"] + P["MM_TIP"]                         # core floor inside the plug
    L["stem0"] = L["adapter0"] + P["ADAPTER_T"]                    # stem foot on the adapter disc
    L["top0"] = L["mm1"] + P["CRANK_LIFT"] + P["LIFT_CLEAR"]
    L["top1"] = L["top0"] + b["h"]
    L["pin"] = (L["top0"] + L["top1"]) / 2
    L["stem1"] = L["top1"] + 60.0                                  # stem top, under its 10 mm cap plate
    L["bracket0"] = L["stem1"] + 10.0 + P["CRANK_LIFT"] + 10.0
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


def _minus(lo, hi, cuts):
    """Interval [lo, hi] minus a list of (a, b) intervals."""
    out = [(lo, hi)]
    for a, b in sorted(cuts):
        nxt = []
        for s, e in out:
            if b <= s or a >= e:
                nxt.append((s, e))
                continue
            if a > s:
                nxt.append((s, a))
            if b < e:
                nxt.append((b, e))
        out = nxt
    return [(s, e) for s, e in out if e - s > 1.0]


def mesh_panel(plane, a0, a1, b0, b1, c_out, inward, pitch, wire, holes=()):
    """Welded wire mesh as square wires, returned as a list of solids (not fused, so it stays light).

    plane 'xz' (normal Y: a = x, b = z, c = y), 'yz' (normal X: a = y, b = z, c = x) or 'xy' (normal Z).
    c_out is the outer face; inward (+1 or -1) points into the guarded space. The outer layer runs along a,
    the inner layer along b, welded where they cross. holes: (a0, a1, b0, b1) rectangles with no wire."""
    def place(a_lo, a_hi, b_lo, b_hi, c_lo, c_hi):
        c_lo, c_hi = sorted((c_lo, c_hi))
        if plane == "xz":
            return box(a_lo, a_hi, c_lo, c_hi, b_lo, b_hi)
        if plane == "yz":
            return box(c_lo, c_hi, a_lo, a_hi, b_lo, b_hi)
        return box(a_lo, a_hi, b_lo, b_hi, c_lo, c_hi)

    def positions(lo, hi):
        n = int((hi - lo) // pitch)
        start = lo + (hi - lo - n * pitch) / 2
        return [start + k * pitch for k in range(n + 1) if lo + wire / 2 <= start + k * pitch <= hi - wire / 2]

    w = wire / 2
    out = []
    c1, c2, c3 = c_out, c_out + inward * wire, c_out + 2 * inward * wire
    for bb in positions(b0, b1):             # outer layer, wires along a
        cuts = [(h[0], h[1]) for h in holes if h[2] - w < bb < h[3] + w]
        for s, e in _minus(a0, a1, cuts):
            out.append(place(s, e, bb - w, bb + w, c1, c2))
    for aa in positions(a0, a1):             # inner layer, wires along b
        cuts = [(h[2], h[3]) for h in holes if h[0] - w < aa < h[1] + w]
        for s, e in _minus(b0, b1, cuts):
            out.append(place(aa - w, aa + w, s, e, c2, c3))
    return out


def angle_frame(plane, a0, a1, b0, b1, c_out, inward, leg, t):
    """Rectangular frame of equal angle behind a mesh panel: one leg flat behind the mesh, one pointing inward."""
    c_back = c_out + inward * 3.2                       # behind the two wire layers
    flat_lo, flat_hi = sorted((c_back, c_back + inward * t))
    out_lo, out_hi = sorted((c_back, c_back + inward * leg))
    if plane == "xz":
        ring = box(a0, a1, flat_lo, flat_hi, b0, b1) - box(a0 + leg, a1 - leg, flat_lo - 1, flat_hi + 1, b0 + leg, b1 - leg)
        ring += box(a0, a1, out_lo, out_hi, b0, b1) - box(a0 + t, a1 - t, out_lo - 1, out_hi + 1, b0 + t, b1 - t)
    elif plane == "yz":
        ring = box(flat_lo, flat_hi, a0, a1, b0, b1) - box(flat_lo - 1, flat_hi + 1, a0 + leg, a1 - leg, b0 + leg, b1 - leg)
        ring += box(out_lo, out_hi, a0, a1, b0, b1) - box(out_lo - 1, out_hi + 1, a0 + t, a1 - t, b0 + t, b1 - t)
    else:
        ring = box(a0, a1, b0, b1, flat_lo, flat_hi) - box(a0 + leg, a1 - leg, b0 + leg, b1 - leg, flat_lo - 1, flat_hi + 1)
        ring += box(a0, a1, b0, b1, out_lo, out_hi) - box(a0 + t, a1 - t, b0 + t, b1 - t, out_lo - 1, out_hi + 1)
    return ring


def cyl_between(p0, p1, r):
    """Cylinder of radius r from point p0 to point p1."""
    bd = _b()
    v = bd.Vector(*p1) - bd.Vector(*p0)
    return bd.Solid.make_cylinder(r, v.length, bd.Plane(origin=bd.Vector(*p0), z_dir=v))


def rot_z(shape, deg, x=0.0, y=0.0):
    bd = _b()
    return bd.Pos(x, y, 0) * bd.Rot(0, 0, deg) * bd.Pos(-x, -y, 0) * shape


def ring_hole(r, z0, z1, x=0.0, y=0.0):
    return cyl(r, z0 - 1, z1 + 1, x, y)


def pump_slot_y(P=PARAMS):
    """Y of the pump handle slot in the right side guard: on the line of the turned jack's pump socket."""
    return (P["GUARD_X"] - 3.1) * math.tan(math.radians(P["JACK_TURN"]))   # centred on the guard's thickness


def pump_handle(P=PARAMS, z_slot=None):
    """Jack pump handle from the end of the pump socket out through the guard slot, 170 mm beyond the guard.
    z_slot: height of the handle's centre line where it passes the slot (default: the middle of the slot)."""
    L = levels(P)
    a = math.radians(P["JACK_TURN"])
    sw, sz0, sz1 = P["PUMP_SLOT"]
    z_slot = (sz0 + sz1) / 2 if z_slot is None else z_slot
    bd = _b()
    r_s, r0, z0 = 150.0, 170.0, L["jack0"] + 72.0          # socket end face; handle straight in the socket to 170
    rs = P["GUARD_X"] / math.cos(a)                         # where the handle line crosses the side guard
    r1 = rs + 170.0
    z1 = z0 + (z_slot - z0) * (r1 - r0) / (rs - r0)
    pt = lambda r, z: (r * math.cos(a), r * math.sin(a), z)  # noqa: E731
    h = cyl_between(pt(r_s, z0), pt(r0, z0), P["HANDLE_D"] / 2) + bd.Pos(*pt(r0, z0)) * bd.Sphere(P["HANDLE_D"] / 2)
    return h + cyl_between(pt(r0, z0), pt(r1, z1), P["HANDLE_D"] / 2)


def pump_shield(P=PARAMS, core_only=False, interior=False):
    """Fixed inner shield behind the pump slot (2026-10-02): a tunnel of 2 mm folded sheet that follows the
    handle's path from the slot to the jack body, with a flange bolted behind the slot frame and a flat-bar stay
    down to the base beam. Built along the handle line, then turned with the jack.
    core_only: only the roof and floor (the part between the side walls), to measure the stroke-end gaps.
    interior: the space inside the tunnel, from the guard's outer face to the jack body (for the desk check)."""
    bd = _b()
    L = levels(P)
    a = math.radians(P["JACK_TURN"])
    t, w, gap = P["SHIELD_T"], P["SHIELD_W"] / 2, P["SHIELD_GAP"]
    rh = P["HANDLE_D"] / 2
    z0, r0 = L["jack0"] + 72.0, 170.0                     # handle pivot, as in pump_handle()
    rs = P["GUARD_X"] / math.cos(a)
    zlo, zhi = P["HANDLE_STROKE"]
    k_lo, k_hi = (zlo - z0) / (rs - r0), (zhi - z0) / (rs - r0)
    roof = lambda r: z0 + k_hi * (max(r, r0) - r0) + (rh + gap) / math.cos(math.atan(k_hi))   # noqa: E731
    floor = lambda r: z0 + k_lo * (max(r, r0) - r0) - (rh + gap) / math.cos(math.atan(k_lo))  # noqa: E731
    r_a, r_b = 30.0, rs + 40.0

    def prism(dz, s0, s1, ra=r_a, rb=r_b):
        pts = [(ra, floor(ra) - dz), (r0, floor(r0) - dz), (rb, floor(rb) - dz),
               (rb, roof(rb) + dz), (r0, roof(r0) + dz), (ra, roof(ra) + dz)]
        face = bd.Plane.XZ * bd.Polygon(*pts, align=None)
        return bd.Pos(0, s1, 0) * bd.extrude(face, amount=s1 - s0)   # Plane.XZ extrudes toward -Y

    inner = prism(0.0, -w, w, r_a - 10, r_b + 10)
    if interior:
        sp = (bd.Rot(0, 0, P["JACK_TURN"]) * inner) & box(-1000, P["GUARD_X"], -1000, 1000, 0, 2000)
        return sp - cyl(P["JACK_BODY_D"] / 2 + P["SHIELD_JACK_GAP"], L["jack0"], L["platen0_low"])
    body = (prism(t, -w, w) if core_only else prism(t, -w - t, w + t)) - inner
    # stay: 30 x 6 flat bar from the base beam's top flange up to the floor, with a 26 x 20 foot plate
    rst = P["SHIELD_STAY_R"]
    if not core_only:
        body += box(rst - 15, rst + 15, -3, 3, L["base1"], floor(rst - 15) - t + 1) - inner
        body += box(rst - 13, rst + 13, -10, 10, L["base1"], L["base1"] + 6)
    body = bd.Rot(0, 0, P["JACK_TURN"]) * body
    gx = P["GUARD_X"]
    sw, sz0, sz1 = P["PUMP_SLOT"]
    py = pump_slot_y(P)
    body &= box(-1000, gx - 6.2, -1000, 1000, 0, 2000)        # trimmed square to the slot frame
    body -= cyl(P["JACK_BODY_D"] / 2 + P["SHIELD_JACK_GAP"], L["jack0"], L["platen0_low"])   # follows the jack body
    if not core_only:                                       # flange behind the slot frame, bolted through it
        fl = box(gx - 9.2, gx - 6.2, py - sw / 2 - 12, py + sw / 2 + 12, sz0 - 12, sz1 + 12)
        body += fl - bd.Rot(0, 0, P["JACK_TURN"]) * inner
    return body


def release_z(P=PARAMS):
    return levels(P)["jack0"] + 12.0


def guard_layout(P=PARAMS):
    """Fixed guard panels as dicts: name, plane, a0, a1, b0, b1, c_out, inward, holes. Pure arithmetic."""
    L = levels(P)
    gx, yf, yb, z0, z1 = P["GUARD_X"], P["GUARD_Y_FRONT"], P["GUARD_Y_BACK"], P["GUARD_Z0"], L["top1"]
    gh = P["GATE_HALF"]
    b = SECTIONS[P["BEAM_SEC"]]
    y_beam = P["BEAM_GAP"] / 2 + b["b"]                  # beam flange tips, front and back
    sw, sz0, sz1 = P["PUMP_SLOT"]
    py = pump_slot_y(P)
    zr = release_z(P)
    lx = P["LOCK_X"]
    return [
        dict(name="Right side guard", plane="yz", a0=P["STRIP_Y"], a1=yb, b0=z0, b1=z1, c_out=gx, inward=-1,
             holes=[(py - sw / 2, py + sw / 2, sz0, sz1)]),
        dict(name="Left side guard", plane="yz", a0=yf, a1=yb, b0=z0, b1=z1, c_out=-gx, inward=+1, holes=[]),
        dict(name="Rear guard", plane="xz", a0=-gx, a1=gx, b0=z0, b1=z1, c_out=yb, inward=-1, holes=[]),
        dict(name="Front left strip", plane="xz", a0=-gx, a1=-gh, b0=z0, b1=z1, c_out=yf, inward=+1, holes=[]),
        dict(name="Front right strip", plane="xz", a0=gh, a1=gx, b0=z0, b1=z1, c_out=P["STRIP_Y"], inward=+1,
             holes=[(lx - 22, lx + 22, zr - 22, zr + 22), (lx + 50, lx + 90, 731, 771)]),
        dict(name="Lower front panel", plane="xz", a0=-gh, a1=gh, b0=z0, b1=P["GATE_Z0"], c_out=yf, inward=+1, holes=[]),
        dict(name="Roof guard", plane="xy", a0=-gx, a1=gx, b0=yf, b1=yb, c_out=z1 + 3.2 + P["GUARD_ANGLE"], inward=-1,
             holes=[(-P["BEAM_L"] / 2 - 5, P["BEAM_L"] / 2 + 5, -y_beam - 5, y_beam + 5)]),
    ]


def guard_solids(P=PARAMS, pitch=None):
    """Fixed guards as a list of solids: angle frames, mesh (every 8th wire by default; pitch=MESH_PITCH draws every
    wire, for the appearance model), pump slot frame, standoffs, fixed hinge leaves and the strip's return plate."""
    L = levels(P)
    pitch = pitch or P["MESH_PITCH"] * P["MESH_SHOW_EVERY"]
    b = SECTIONS[P["BEAM_SEC"]]
    yw = P["BEAM_GAP"] / 2 + b["tw"]; bl = P["BEAM_L"] / 2
    zc_base = (L["base0"] + L["base1"]) / 2; zc_top = (L["top0"] + L["top1"]) / 2
    g = []
    for pnl in guard_layout(P):
        g.append(angle_frame(pnl["plane"], pnl["a0"], pnl["a1"], pnl["b0"], pnl["b1"], pnl["c_out"], pnl["inward"],
                             P["GUARD_ANGLE"], P["GUARD_ANGLE_T"]))
        g += mesh_panel(pnl["plane"], pnl["a0"], pnl["a1"], pnl["b0"], pnl["b1"], pnl["c_out"], pnl["inward"],
                        pitch, P["MESH_WIRE"], pnl["holes"])
    sw, sz0, sz1 = P["PUMP_SLOT"]; py = pump_slot_y(P)
    gx = P["GUARD_X"]
    g.append(box(gx - 6.2, gx - 3.2, py - sw / 2 - 12, py + sw / 2 + 12, sz0 - 12, sz1 + 12) -
             box(gx - 7, gx - 2, py - sw / 2, py + sw / 2, sz0, sz1))                          # pump slot frame
    for sx in (-1, 1):                                                                          # side standoffs on the beam webs
        for zc in (zc_base, zc_top):
            for sy in (-1, 1):
                g.append(box(*sorted((sx * (bl - 40), sx * (gx - 3.2 - P["GUARD_ANGLE"]))), *sorted((sy * yw, sy * (yw + 6))), zc - 20, zc + 20))
    hx, hy = -P["GATE_HALF"], P["GUARD_Y_FRONT"] - 12
    for zh in (P["GATE_Z0"] + 124, L["top1"] - 124):                                           # fixed hinge leaves
        g.append(box(hx - 30, hx - 8, hy - 3, P["GUARD_Y_FRONT"], zh - 25, zh + 25))
    g.append(box(P["GATE_HALF"], P["GATE_HALF"] + 3, P["GUARD_Y_FRONT"], P["STRIP_Y"], P["GUARD_Z0"], L["top1"]))   # return plate of the set-back strip
    return g


def gate_geometry(P=PARAMS, pitch=None, open_deg=None):
    """Hinged front gate (closed or swung open) as a list of solids: tube frame, mesh, hinges, handle, tongue."""
    bd = _b()
    L = levels(P)
    pitch = pitch or P["MESH_PITCH"] * P["MESH_SHOW_EVERY"]
    open_deg = P["GATE_OPEN_DEG"] if open_deg is None else open_deg
    gh, yf, tb = P["GATE_HALF"], P["GUARD_Y_FRONT"], P["GATE_TUBE"]
    x0, x1 = -gh + 4, gh - 4
    z0, z1 = P["GATE_Z0"] + 4, L["top1"] - 4
    yin = yf + 3.2                                          # frame sits behind the mesh
    fr = box(x0, x1, yin, yin + tb, z0, z1) - box(x0 + tb, x1 - tb, yin - 1, yin + tb + 1, z0 + tb, z1 - tb)
    zm = (z0 + z1) / 2
    fr += box(x0 + tb, x1 - tb, yin, yin + tb, zm - tb / 2, zm + tb / 2)            # mid rail
    solids = [fr] + mesh_panel("xz", x0, x1, z0, z1, yf, +1, pitch, P["MESH_WIRE"])
    hx, hy = -gh, yf - 12                                   # hinge axis, just ahead of the mesh
    for zh in (z0 + 120, z1 - 120):
        solids.append(cyl(8, zh - 40, zh + 40, x=hx, y=hy))                          # hinge knuckle
        solids.append(box(hx + 8, x0 + tb, hy - 3, yf, zh - 25, zh + 25))            # hinge leaf on the gate
    zl = P["LATCH_Z"]
    solids.append(box(x1 - 60, x1 - 45, yf - 25, yf - 13, zl - 70, zl + 70))        # pull handle, grip
    solids.append(box(x1 - 60, x1 - 45, yf - 13, yf, zl - 70, zl - 58) + box(x1 - 60, x1 - 45, yf - 13, yf, zl + 58, zl + 70))
    # Tongue: an arm off the right-hand gate post, then a plate with a 14 mm hole over the lock rod
    ly, lx = P["LOCK_Y"], P["LOCK_X"]
    tongue = box(x1 - 16, x1, ly - 10, yin, zl, zl + 6) + box(x1, lx + 15, ly - 10, yf, zl, zl + 6)
    tongue -= cyl(7, zl - 1, zl + 7, lx, ly)
    solids.append(tongue)
    if open_deg:
        rot = bd.Pos(hx, hy, 0) * bd.Rot(0, 0, -open_deg) * bd.Pos(-hx, -hy, 0)
        solids = [rot * s for s in solids]
    return solids


def pot(z_floor, x=0.0, y=0.0, P=PARAMS):
    """Pressed filter pot, outer floor at z_floor."""
    rb, rt, h = pot_outer(P)
    top = z_floor + h
    outer = cone(rb, rt, z_floor, top, x, y) + cyl(P["RIM_OD"] / 2, top - P["RIM_T"], top, x, y)
    inner = cone(P["R_IN_BOT"], P["R_IN_RIM"] + (P["R_IN_RIM"] - P["R_IN_BOT"]) / P["D_IN"],
                 z_floor + P["WALL"], top + 1, x, y)
    return outer - inner


def angle_ring(x0, x1, y0, y1, ztop, leg, t):
    """Frame of equal angle under a shelf: horizontal leg flat under the shelf, vertical leg down on the outside."""
    hor = box(x0, x1, y0, y1, ztop - t, ztop) - box(x0 + leg, x1 - leg, y0 + leg, y1 - leg, ztop - t - 1, ztop + 1)
    ver = box(x0, x1, y0, y1, ztop - leg, ztop) - box(x0 + t, x1 - t, y0 + t, y1 - t, ztop - leg - 1, ztop + 1)
    return hor + ver


class C:
    """One component: what it is called, its shape, how it is made, and its BOM line."""
    def __init__(self, key, name, shape, color, bom, how, group, explode=(0, 0, 0)):
        self.key, self.name, self.shape, self.color = key, name, shape, color
        self.bom, self.how, self.group, self.explode = bom, how, group, explode


# ---------------------------------------------------------------------------
# Components
# ---------------------------------------------------------------------------
def components(P=PARAMS):
    """Every component on its own, press closed and guarded. how: make, cast, print or buy."""
    bd = _b()
    L = levels(P)
    b = SECTIONS[P["BEAM_SEC"]]; u = SECTIONS[P["UPRIGHT_SEC"]]; pl = SECTIONS[P["PLATEN_SEC"]]; f = SECTIONS[P["FOOT_SEC"]]
    g2 = P["BEAM_GAP"] / 2; xs = P["SPAN"] / 2; bl = P["BEAM_L"] / 2
    yw = g2 + b["tw"]                                   # outer face of the beam webs
    out = []
    add = lambda *a, **k: out.append(C(*a, **k))

    # Joint bolt positions (both beams, both uprights)
    zc_base = (L["base0"] + L["base1"]) / 2; zc_top = (L["top0"] + L["top1"]) / 2
    bolt_pts = [(sx * xs + dx, zc + dz) for sx in (-1, 1) for zc in (zc_base, zc_top)
                for dx in (-P["JOINT_BOLT_DX"], P["JOINT_BOLT_DX"]) for dz in (-P["JOINT_BOLT_DZ"], P["JOINT_BOLT_DZ"])]
    rh = (P["JOINT_BOLT_D"] + 2) / 2                    # 18 mm clearance holes
    holes_y = lambda y0, y1, pts: [cyl_y(rh, y0, y1, x_, z_) for x_, z_ in pts]

    # ---- Feet: UPN 100 lying web up, with welded-in anchor tubes and four studs for the base beam
    xf = xs + 60
    stud_pts = lambda sx: [(sx * xf + dx, sy * 88.0) for dx in (-25, 25) for sy in (-1, 1)]
    for sx, side in ((-1, "left"), (1, "right")):
        xc = sx * xf; w = f["h"] / 2
        foot = box(xc - w, xc + w, -P["FOOT_L"] / 2, P["FOOT_L"] / 2, f["b"] - f["tw"], f["b"])
        for dx in (-1, 1):
            x_a, x_b = sorted((xc + dx * w, xc + dx * (w - f["tf"])))
            foot += box(x_a, x_b, -P["FOOT_L"] / 2, P["FOOT_L"] / 2, 0, f["b"])
        for sy in (-1, 1):
            foot += cyl(13.45, 0, f["b"] - f["tw"], xc, sy * P["ANCHOR_Y"]) - cyl(10.25, -1, f["b"], xc, sy * P["ANCHOR_Y"])
            foot -= cyl(7, f["b"] - f["tw"] - 1, f["b"] + 1, xc, sy * P["ANCHOR_Y"])
        for (x_, y_) in stud_pts(sx):                                     # M12 bolts, heads welded under the web
            foot += cyl(9, f["b"] - f["tw"] - 8, f["b"] - f["tw"], x_, y_) + cyl(6, f["b"] - f["tw"], L["base0"] + b["tf"] + 16, x_, y_)
            foot += cyl(10, L["base0"] + b["tf"], L["base0"] + b["tf"] + 10, x_, y_)       # nut and washer on the beam flange
        add(f"foot_{side}", f"Foot, {side}", foot, "#4B5563", 1, "make", "frame", (0, 0, -200))
    anchors = None
    for sx in (-1, 1):
        for sy in (-1, 1):
            a = cyl(6, -80, f["b"] + 12, sx * xf, sy * P["ANCHOR_Y"]) + cyl(10, f["b"], f["b"] + 10, sx * xf, sy * P["ANCHOR_Y"])
            anchors = a if anchors is None else anchors + a
    add("anchors", "Floor anchors, 4 x M12", anchors, "#111827", 1, "buy", "frame", (0, 0, -300))

    # ---- Base beam: two UPN 160 with end blocks, jack plate, jack locating blocks and spring anchor lugs
    base = channel_x(-bl, bl, g2, +1, L["base0"], P["BEAM_SEC"]) + channel_x(-bl, bl, -g2, -1, L["base0"], P["BEAM_SEC"])
    for sx in (-1, 1):
        base += box(*sorted((sx * bl, sx * (bl - P["END_BLOCK_L"]))), -g2, g2, L["base0"] + b["tf"], L["base1"] - b["tf"])
    bw = P["BEARING_W"] / 2; yfl = g2 + b["b"]
    jplate = box(-bw, bw, -yfl, yfl, L["base1"], L["jack0"])
    jb = P["JACK_BASE"] / 2
    for k in (1, 2, 3):                                 # locating blocks round the jack base (not on the valve side)
        blk = box(jb + 2, jb + 12, -20, 20, L["jack0"], L["jack0"] + 15)
        jplate += bd.Rot(0, 0, P["JACK_TURN"] + 90 * k) * blk
    jp_bolts = [(sx * (bw - 15), sy * 90.0) for sx in (-1, 1) for sy in (-1, 1)]
    jbolts = None
    for (x_, y_) in jp_bolts:
        jplate -= cyl(7, L["base1"] - 1, L["jack0"] + 1, x_, y_)
        base -= cyl(7, L["base1"] - b["tf"] - 1, L["base1"] + 1, x_, y_)
        q = cyl(6, L["base1"] - b["tf"] - 14, L["jack0"] + 8, x_, y_) + cyl(10, L["jack0"], L["jack0"] + 8, x_, y_) + \
            cyl(10, L["base1"] - b["tf"] - 10, L["base1"] - b["tf"], x_, y_)
        jbolts = q if jbolts is None else jbolts + q
    for sx in (-1, 1):                                  # spring anchor lugs across the top flanges
        base += box(sx * P["SPRING_X"] - 15, sx * P["SPRING_X"] + 15, -75, 75, L["base1"], L["base1"] + P["SPRING_LUG_T"]) - \
            ring_hole(6, L["base1"], L["base1"] + P["SPRING_LUG_T"], sx * P["SPRING_X"])
    for p_ in holes_y(-yw - 1, yw + 1, [q for q in bolt_pts if q[1] < L["base1"]]):
        base -= p_
    for sx in (-1, 1):
        for (x_, y_) in stud_pts(sx):
            base -= cyl(7, L["base0"] - 1, L["base0"] + b["tf"] + 1, x_, y_)
    add("base_beam", "Base beam", base, "#4B5563", 1, "make", "frame", (0, 0, -120))
    add("jack_plate", "Jack plate", jplate, "#6B7280", 1, "make", "frame", (0, 0, 0))
    add("jack_plate_bolts", "Jack plate bolts, 4 x M12", jbolts, "#111827", 1, "buy", "frame", (0, 0, 0))

    # ---- Upright pairs: two UPN 100 back to back, with spacer tubes, shims and M16 bolts at each joint
    ys = u["h"] / 2
    for sx, side in ((-1, "left"), (1, "right")):
        pair = channel_upright(sx * xs, -1, L["base0"], L["top1"], P["UPRIGHT_SEC"]) + \
            channel_upright(sx * xs, +1, L["base0"], L["top1"], P["UPRIGHT_SEC"])
        pts = [q for q in bolt_pts if (q[0] > 0) == (sx > 0)]
        for p_ in holes_y(-ys - 1, ys + 1, pts):
            pair -= p_
        add(f"upright_{side}", f"Upright pair, {side}", pair, "#6B7280", 2, "make", "frame", (0, 0, 0))
        tubes = None; shims = None; bolts = None
        for (x_, z_) in pts:
            t_ = cyl_y(P["SPACER_OD"] / 2, -ys + u["tf"], ys - u["tf"], x_, z_) - cyl_y(9.5, -ys, ys, x_, z_)
            tubes = t_ if tubes is None else tubes + t_
            bt = cyl_y(P["JOINT_BOLT_D"] / 2, -yw - 13, yw + 21, x_, z_) + cyl_y(12, -yw - 13, -yw - 3, x_, z_) + \
                cyl_y(15, -yw - 3, -yw, x_, z_) + cyl_y(15, yw, yw + 3, x_, z_) + cyl_y(13, yw + 3, yw + 16, x_, z_)
            bolts = bt if bolts is None else bolts + bt
        for zc in (zc_base, zc_top):
            for sy in (-1, 1):
                sh = box(sx * xs - ys, sx * xs + ys, *sorted((sy * ys, sy * g2)), zc - 60, zc + 60)
                for (x_, z_) in pts:
                    if abs(z_ - zc) < 50:
                        sh -= cyl_y(rh, -g2 - 1, g2 + 1, x_, z_)
                shims = sh if shims is None else shims + sh
        add(f"tubes_{side}", f"Spacer tubes, {side} upright", tubes, "#9CA3AF", 2, "make", "frame", (0, 0, 0))
        add(f"shims_{side}", f"Shim packs, {side} upright", shims, "#D97706", 2, "make", "frame", (0, 0, 0))
        add(f"bolts_{side}", f"Joint bolts M16, {side} upright", bolts, "#111827", 2, "buy", "frame", (0, 0, 0))

    # ---- Top crossbeam: two UPN 160 with end blocks, pin doublers, 62 mm pin bore, stem guide liners
    top = channel_x(-bl, bl, g2, +1, L["top0"], P["BEAM_SEC"]) + channel_x(-bl, bl, -g2, -1, L["top0"], P["BEAM_SEC"])
    for sx in (-1, 1):
        top += box(*sorted((sx * bl, sx * (bl - P["END_BLOCK_L"]))), -g2, g2, L["top0"] + b["tf"], L["top1"] - b["tf"])
    dl = P["DOUBLER_L"] / 2
    for sy in (-1, 1):
        top += box(-dl, dl, *sorted((sy * yw, sy * (yw + P["DOUBLER_T"]))), L["top0"] + b["tf"], L["top1"] - b["tf"])
    top -= cyl_y(P["PIN_D"] / 2 + 1, -yw - P["DOUBLER_T"] - 1, yw + P["DOUBLER_T"] + 1, 0, L["pin"])
    for p_ in holes_y(-yw - 1, yw + 1, [q for q in bolt_pts if q[1] > L["base1"]]):
        top -= p_
    for x_ in (-40, 40):                                # crank bracket bolts through the top flanges
        for sy in (-1, 1):
            top -= cyl(7, L["top1"] - b["tf"] - 1, L["top1"] + 1, x_, sy * 100)
    add("top_beam", "Top crossbeam", top, "#4B5563", 3, "make", "frame", (0, 0, 300))
    s2 = P["STEM"] / 2
    liners = box(-s2 - 30, -s2 - 1, -g2, g2, L["top0"], L["top1"]) + box(s2 + 1, s2 + 30, -g2, g2, L["top0"], L["top1"])
    for sy in (-1, 1):                                  # front and back strips on the webs (DDR-004): 1 mm to the stem
        liners += box(-s2 - 1, s2 + 1, *sorted((sy * (s2 + 1), sy * g2)), L["top0"] + b["tf"], L["top1"] - b["tf"])
    liners -= cyl_y(P["PIN_D"] / 2 + 1, -g2 - 1, g2 + 1, 0, L["pin"])
    add("liners", "Stem guide liners (UHMW-PE)", liners, "#F3F4F6", 3, "make", "frame", (0, 0, 300))

    # ---- 20 t bottle jack (bought), turned so its pump socket and release valve face the right front
    jack = box(-jb, jb, -jb, jb, L["jack0"], L["jack0"] + 25) + \
        cyl(P["JACK_BODY_D"] / 2, L["jack0"] + 25, L["platen0_low"] - 20) + \
        cyl(P["RAM_D"] / 2, L["platen0_low"] - 20, L["platen0"])
    jack += box(50, 150, -12, 12, L["jack0"] + 60, L["jack0"] + 84)                      # pump socket
    zr = release_z(P)
    jack += bd.Pos(jb, 0, zr) * bd.Rot(0, 90, 0) * bd.Cylinder(7, 30, align=(bd.Align.CENTER, bd.Align.CENTER, bd.Align.MIN))  # release valve
    jack = bd.Rot(0, 0, P["JACK_TURN"]) * jack
    add("jack", "20 t bottle jack", jack, "#B91C1C", 4, "buy", "press", (0, 0, 0))
    add("pump_handle", "Jack pump handle", pump_handle(P), "#7F1D1D", 4, "buy", "press", (0, 0, 0))

    # ---- Moving platen: two UPN 140, deck, jack pad, guide sleeves, spring anchor lugs
    xin = xs - u["b"] - P["SLEEVE_T"] - P["SLEEVE_CLEAR"] / 2
    plat = channel_x(-xin, xin, g2, +1, L["platen0"], P["PLATEN_SEC"]) + channel_x(-xin, xin, -g2, -1, L["platen0"], P["PLATEN_SEC"])
    plat += box(-xin, xin, -220, 220, L["platen0"] + pl["h"], L["deck1"])
    plat += box(-100, 100, -g2, g2, L["platen0"], L["platen0"] + P["PLATEN_PAD_T"])
    for sx in (-1, 1):
        c = P["SLEEVE_CLEAR"] / 2; t = P["SLEEVE_T"]
        xo0, xo1 = sx * xs - u["b"] - c - t, sx * xs + u["b"] + c + t
        yo = u["h"] / 2 + c + t
        z0 = L["platen0"] - 20; z1 = z0 + P["SLEEVE_H"]
        plat += box(xo0, xo1, -yo, yo, z0, z1) - box(xo0 + t, xo1 - t, -yo + t, yo - t, z0 - 1, z1 + 1)
        plat += box(sx * P["SPRING_X"] - 15, sx * P["SPRING_X"] + 15, -80, 80, L["platen0"] - P["SPRING_LUG_T"], L["platen0"]) - \
            ring_hole(6, L["platen0"] - P["SPRING_LUG_T"], L["platen0"], sx * P["SPRING_X"])
    add("platen", "Moving platen", plat, "#9CA3AF", 5, "make", "press", (0, 0, 0))

    # ---- Return springs (bought) hooked on the lugs
    springs = None
    z_lo = L["base1"] + P["SPRING_LUG_T"]; z_hi = L["platen0"] - P["SPRING_LUG_T"]
    for sx in (-1, 1):
        x_ = sx * P["SPRING_X"]
        s_ = cyl(12, z_lo + 12, z_hi - 12, x_) + cyl(2.5, z_lo - P["SPRING_LUG_T"] / 2, z_lo + 12, x_ + 3.5) + \
            cyl(2.5, z_hi - 12, z_hi + P["SPRING_LUG_T"] / 2, x_ + 3.5)                  # hooks bear on the hole edge
        springs = s_ if springs is None else springs + s_
    add("springs", "Return springs", springs, "#D4A017", 6, "buy", "press", (0, 0, 0))

    # ---- Rails with the folding extension and its tipping pins
    rw = P["RAIL_W"] / 2
    y_h = -P["RAIL_HINGE"]
    y_piv = -(P["CARRIAGE_OUT"] + P["PIVOT_DY"])        # tipping axis with the carriage fully out
    y_end = y_piv - 5
    rails = None; ext = None
    for xr in P["RAIL_X"]:
        for sx in (-1, 1):
            r = box(sx * xr - rw, sx * xr + rw, y_h, P["RAIL_BACK"] + 15, L["deck1"], L["rail1"])
            rails = r if rails is None else rails + r
            e = box(sx * xr - rw, sx * xr + rw, y_end, y_h, L["deck1"], L["rail1"])
            ext = e if ext is None else ext + e
    for sx in (-1, 1):
        xa, xb = sorted((sx * (P["RAIL_X"][0] - rw), sx * (P["RAIL_X"][1] + rw)))
        rails += box(xa, xb, y_h, y_h + 16, L["deck1"] - 12, L["deck1"])                  # hinge bar with stop lugs
        ext += box(xa, xb, y_h - 170, y_h - 150, L["deck1"] - 12, L["deck1"])             # extension cross tie
        xo = sx * (P["RAIL_X"][1] + rw)
        ext += bd.Pos(0, 0, 0) * cyl_between((xo, y_piv, L["deck1"] + 7), (sx * 252, y_piv, L["deck1"] + 7), P["PIVOT_D"] / 2)
    rails += box(-200, 200, P["RAIL_BACK"], P["RAIL_BACK"] + 15, L["rail1"], L["rail1"] + 40)    # end stop
    if P["EXT_FOLDED"]:
        ext = bd.Pos(0, y_h, L["deck1"]) * bd.Rot(90, 0, 0) * bd.Pos(0, -y_h, -L["deck1"]) * ext
    add("rails", "Rails with end stop", rails, "#374151", 7, "make", "press", (0, 0, 0))
    add("extension", "Folding rail extension with tipping pins", ext, "#374151", 7, "make", "press", (0, 0, 0))

    # ---- Carriage: square ring round the female base plate, handle, side lips, tipping hooks, retaining pins
    fr = P["FM_PLATE_W"] / 2 + 5
    zc0 = L["rail1"]
    car = box(-fr - 25, fr + 25, -fr - 25, fr + 25, zc0, zc0 + 12) - box(-fr, fr, -fr, fr, zc0 - 1, zc0 + 13)
    car += box(-70, 70, -fr - 60, -fr - 25, zc0, zc0 + 12) + box(-70, 70, -fr - 60, -fr - 45, zc0 + 12, zc0 + 110)
    xo = P["RAIL_X"][1] + rw
    for sx in (-1, 1):
        car += box(*sorted((sx * (xo + 1), sx * (xo + 7))), 0, fr + 25, L["deck1"] + 3, zc0)   # side lip outside the outer rail
        # tipping hook: arm out to 252 mm, plate hanging down with a slot open to the front for the tipping pin
        hook = box(*sorted((sx * (fr + 25), sx * 252)), -P["PIVOT_DY"] - 15, -P["PIVOT_DY"] + 25, zc0, zc0 + 12)
        hook += box(*sorted((sx * 240, sx * 252)), -P["PIVOT_DY"] - 15, -P["PIVOT_DY"] + 25, L["deck1"] - 12, zc0)
        hook -= box(*sorted((sx * 239, sx * 253)), -P["PIVOT_DY"] - 16, -P["PIVOT_DY"] + 7, L["deck1"], L["deck1"] + 14)
        car += hook
        car -= cyl_between((sx * (fr - 1), 0, zc0 + 6), (sx * (fr + 26), 0, zc0 + 6), 6)
        # lift handle near the back of each side (DDR-004): lifted to tip the mold forward over the tipping pins
        xa_, xb_ = sorted((sx * (fr + 25), sx * (fr + 45)))
        car += box(xa_, xb_, 110, 120, zc0, zc0 + 70) + box(xa_, xb_, 170, 180, zc0, zc0 + 70) + box(xa_, xb_, 110, 180, zc0 + 70, zc0 + 80)
    add("carriage", "Mold carriage", car, "#1F2937", 7, "make", "press", (0, 0, 0))
    rpins = None
    for sx in (-1, 1):
        rp = cyl_between((sx * (fr - 18), 0, zc0 + 6), (sx * (fr + 40), 0, zc0 + 6), 5) + \
            cyl_between((sx * (fr + 40), 0, zc0 + 6 - 12), (sx * (fr + 40), 0, zc0 + 6 + 12), 3)
        rpins = rp if rpins is None else rpins + rp
    add("retaining_pins", "Mold retaining pins", rpins, "#111827", 7, "make", "press", (0, 0, 0))

    # ---- Female mold: steel base plate, cast aluminum cup, two locating pins
    rb, rt, h = pot_outer(P)
    sh = P["FM_SHELL"]; slope = (rt - rb) / h
    zp1 = L["fm0"] + P["FM_PLATE_T"]
    pw = P["FM_PLATE_W"] / 2
    plate = box(-pw, pw, -pw, pw, L["fm0"], zp1)
    for sx in (-1, 1):
        plate -= cyl_between((sx * (pw + 1), 0, zc0 + 6), (sx * (pw - 20), 0, zc0 + 6), 7)
    cup_bolts = [(137 * math.cos(math.radians(a)), 137 * math.sin(math.radians(a))) for a in (45, 135, 225, 315)]
    for (x_, y_) in cup_bolts:
        plate -= cyl(4.5, L["fm0"] - 1, zp1 + 1, x_, y_) + cone(8.5, 4.5, L["fm0"] - 0.01, L["fm0"] + 4, x_, y_)
    add("fm_plate", "Female mold base plate", plate, "#6B7280", 8, "make", "mold", (0, 0, 0))
    r_out0 = rb + sh - slope * (L["pot0"] - zp1)
    z_fl0 = L["fm1"] - P["FM_FLANGE_T"]
    cup = cone(r_out0, rt + sh, zp1, L["fm1"]) + cyl(P["FM_FLANGE_D"] / 2, z_fl0, L["fm1"])
    cup -= cone(rb, rt, L["pot0"], L["fm1"] + 0.01)
    cup -= cyl(P["RIM_OD"] / 2, L["fm1"] - P["RIM_T"], L["fm1"] + 1)
    cup -= cyl(P["FLASH_R"], L["fm1"] - 3, L["fm1"] + 1) - cyl(P["RIM_OD"] / 2, L["fm1"] - 4, L["fm1"] + 2)
    for sx in (-1, 1):
        cup -= cyl(P["LOC_PIN_D"] / 2, L["fm1"] - P["LOC_PIN_DEPTH"], L["fm1"] + 1, sx * P["LOC_PIN_R"])
    for (x_, y_) in cup_bolts:
        cup -= cyl(4, zp1 - 1, zp1 + 16, x_, y_)
    add("fm_cup", "Female mold (cast aluminum)", cup, "#CBD5E1", 8, "cast", "mold", (0, 0, 0))
    screws = None
    for (x_, y_) in cup_bolts:
        s_ = cyl(4, L["fm0"] + 2, zp1 + 14, x_, y_) + cone(8, 4, L["fm0"], L["fm0"] + 4, x_, y_)
        screws = s_ if screws is None else screws + s_
    locp = None
    for sx in (-1, 1):
        p_ = cyl(P["LOC_PIN_D"] / 2, L["fm1"] - P["LOC_PIN_DEPTH"], L["fm1"] + P["LOC_PIN_PROUD"] - 3, sx * P["LOC_PIN_R"]) + \
            cone(P["LOC_PIN_D"] / 2, P["LOC_PIN_D"] / 2 - 3, L["fm1"] + P["LOC_PIN_PROUD"] - 3, L["fm1"] + P["LOC_PIN_PROUD"], sx * P["LOC_PIN_R"])
        locp = p_ if locp is None else locp + p_
    add("loc_pins", "Locating pins, 2 x 16 mm", locp, "#111827", 8, "buy", "mold", (0, 0, 0))
    add("fm_screws", "Base plate screws, 4 x M8", screws, "#111827", 8, "buy", "mold", (0, 0, 0))

    # ---- Male mold: plug open at the back (drafted core space), 45 mm flange with two steel bushes
    sl = (P["R_IN_RIM"] - P["R_IN_BOT"]) / P["D_IN"]
    z_tip = L["tip"]
    male = cone(P["R_IN_BOT"], P["R_IN_RIM"], z_tip, L["fm1"]) + cyl(P["MM_FLANGE_D"] / 2, L["fm1"], L["mm1"])
    hoff = P["MM_SHELL"] / math.cos(math.atan(sl))
    r_c0 = P["R_IN_BOT"] + sl * P["MM_TIP"] - hoff
    r_c1 = r_c0 + sl * (L["mm1"] - L["adapter0"])
    male -= cone(r_c0, r_c1, L["adapter0"], L["mm1"] + 0.01)
    for sx in (-1, 1):
        male -= cyl(P["BUSH_OD"] / 2, L["fm1"] - 1, L["mm1"] + 1, sx * P["LOC_PIN_R"])
    ad_bolts = [(75.0, 0.0), (-75.0, 0.0), (0.0, 75.0), (0.0, -75.0)]
    for (x_, y_) in ad_bolts:
        male -= cyl(5, L["adapter0"] - 20, L["adapter0"] + 1, x_, y_)
    add("mm", "Male mold (cast aluminum)", male, "#94A3B8", 9, "cast", "mold", (0, 0, 0))
    bushes = None
    for sx in (-1, 1):
        b_ = cyl(P["BUSH_OD"] / 2, L["fm1"], L["mm1"], sx * P["LOC_PIN_R"]) - \
            cone(P["LOC_PIN_D"] / 2 + P["LOC_CLEAR"] / 2 + 2, P["LOC_PIN_D"] / 2 + P["LOC_CLEAR"] / 2, L["fm1"] - 0.1, L["fm1"] + 2, sx * P["LOC_PIN_R"]) - \
            cyl(P["LOC_PIN_D"] / 2 + P["LOC_CLEAR"] / 2, L["fm1"] - 1, L["mm1"] + 1, sx * P["LOC_PIN_R"])
        bushes = b_ if bushes is None else bushes + b_
    add("bushes", "Locating bushes, 2 x 16 mm", bushes, "#111827", 9, "buy", "mold", (0, 0, 0))

    # ---- Stem: SHS 90 x 8 on a steel adapter disc, pin block, lead screw nut box with free space under the nut
    t = P["STEM_T"]
    stem = cyl(P["ADAPTER_D"] / 2, L["adapter0"], L["stem0"])
    for (x_, y_) in ad_bolts:
        stem -= cyl(6.5, L["adapter0"] - 1, L["stem0"] + 1, x_, y_)
    stem += box(-s2, s2, -s2, s2, L["stem0"], L["stem1"]) - box(-s2 + t, s2 - t, -s2 + t, s2 - t, L["stem0"] + 1, L["stem1"] + 1)
    stem += box(-s2 + t, s2 - t, -s2 + t, s2 - t, L["pin"] - 60, L["pin"] + 60)            # pin block
    stem -= cyl_y(P["PIN_D"] / 2 + 1, -s2 - 1, s2 + 1, 0, L["pin"])
    stem -= cyl(P["SCREW_HOLE"] / 2, L["pin"] - 61, L["pin"] + 61)                          # lead screw passes when cranked up (DDR-004)
    nut0 = L["stem1"] - 40
    floor0 = nut0 - P["NUT_FLOAT"] - 10
    stem += box(-s2 + t, s2 - t, -s2 + t, s2 - t, floor0, floor0 + 10) - ring_hole(P["SCREW_HOLE"] / 2, floor0, floor0 + 10)   # nut box floor
    stem += box(-s2, s2, -s2, s2, L["stem1"], L["stem1"] + 10) - ring_hole(13, L["stem1"], L["stem1"] + 10)   # cap plate
    add("stem", "Stem with adapter disc and nut box", stem, "#0F766E", 10, "make", "slide", (0, 0, 0))
    abolts = None
    for (x_, y_) in ad_bolts:
        a_ = cyl(6, L["adapter0"] - 18, L["stem0"] + 12, x_, y_) - cyl(6.1, L["adapter0"] - 20, L["adapter0"], x_, y_) + \
            cyl(5, L["adapter0"] - 18, L["adapter0"], x_, y_) + cyl(9, L["stem0"], L["stem0"] + 12, x_, y_)
        abolts = a_ if abolts is None else abolts + a_
    add("adapter_bolts", "Adapter bolts, 4 x M12", abolts, "#111827", 10, "buy", "slide", (0, 0, 0))
    ph = P["PIN_HEAD_T"]; y_face = -(yw + P["DOUBLER_T"])
    pin = cyl_y(P["PIN_D"] / 2, y_face, y_face + P["PIN_L"], 0, L["pin"]) + cyl_y(P["PIN_D"] / 2 + 10, y_face - ph, y_face, 0, L["pin"])
    pin -= cyl(3, L["pin"] - 40, L["pin"] + 40, 0, -y_face + 20)
    pin += cyl(2.5, L["pin"] - 38, L["pin"] + 38, 0, -y_face + 20)                           # R-clip through the tail
    pin += cyl_y(8, y_face - ph - 40, y_face - ph, 0, L["pin"]) + cyl_y(20, y_face - ph - 52, y_face - ph - 40, 0, L["pin"])  # pull knob
    add("pin", "Load pin", pin, "#E5E7EB", 10, "make", "slide", (0, 0, 0))
    nut = box(-30, 30, -30, 30, nut0, L["stem1"]) - ring_hole(12, nut0, L["stem1"])
    add("nut", "Lead screw nut (captive in the stem)", nut, "#92400E", 10, "buy", "slide", (0, 0, 0))
    screw = cyl(P["LEAD_D"] / 2 - 0.5, floor0 + 2, L["wheel"] + 15)
    hw = P["HANDWHEEL_D"] / 2
    wheel = cyl(hw, L["wheel"], L["wheel"] + 12) - cyl(hw - 14, L["wheel"] - 1, L["wheel"] + 13)
    wheel += box(-hw + 5, hw - 5, -8, 8, L["wheel"], L["wheel"] + 12) + box(-8, 8, -hw + 5, hw - 5, L["wheel"], L["wheel"] + 12)
    wheel += cyl(10, L["wheel"] + 12, L["wheel"] + 70, x=hw - 7)
    wheel += cyl(20, L["bracket1"], L["wheel"]) - ring_hole(12, L["bracket1"], L["wheel"])     # hub and upper thrust collar
    wheel += cyl(20, L["bracket0"] - 10, L["bracket0"]) - ring_hole(12, L["bracket0"] - 10, L["bracket0"])  # lower thrust collar
    wheel -= cyl(P["LEAD_D"] / 2 - 0.5, L["bracket0"] - 20, L["wheel"] + 20)
    add("screw", "Lead screw, collars and handwheel", screw + wheel, "#B45309", 10, "buy", "slide", (0, 0, 0))
    brk = box(-100, 100, -120, 120, L["top1"], L["top1"] + 10) - box(-50, 50, -50, 50, L["top1"] - 1, L["top1"] + 11)
    for sx in (-1, 1):
        brk += box(sx * 80 - 5, sx * 80 + 5, -80, 80, L["top1"] + 10, L["bracket0"])
    brk += box(-100, 100, -80, 80, L["bracket0"], L["bracket1"]) - ring_hole(13, L["bracket0"], L["bracket1"])
    for x_ in (-40, 40):
        for sy in (-1, 1):
            brk -= cyl(7, L["top1"] - 1, L["top1"] + 11, x_, sy * 100)
    add("bracket", "Crank bracket", brk, "#0F766E", 10, "make", "slide", (0, 0, 0))
    bb_ = None
    for x_ in (-40, 40):
        for sy in (-1, 1):
            q = cyl(6, L["top1"] - b["tf"] - 12, L["top1"] + 18, x_, sy * 100) + cyl(10, L["top1"] + 10, L["top1"] + 18, x_, sy * 100) + \
                cyl(10, L["top1"] - b["tf"] - 10, L["top1"] - b["tf"], x_, sy * 100)
            bb_ = q if bb_ is None else bb_ + q
    add("bracket_bolts", "Bracket bolts, 4 x M12", bb_, "#111827", 10, "buy", "slide", (0, 0, 0))

    # ---- Pressed filter pot
    add("pot", "Pressed filter pot", pot(L["pot0"], P=P), "#C8875A", 11, "product", "mold", (0, 0, 0))

    # ---- QC rack, 2 x 2 stations: angle legs and shelf frames, plywood shelves
    x0 = P["QC_X0"]; pch = P["QC_PITCH"]; W = 2 * pch; y0 = -pch
    lg, at = P["QC_LEG"], P["QC_ANGLE_T"]
    zs, zbk, st = P["QC_SHELF_Z"], P["QC_BUCKET_Z"], P["QC_SHELF_T"]
    rack = angle_ring(x0, x0 + W, y0, y0 + W, zs - st, lg, at) + angle_ring(x0, x0 + W, y0, y0 + W, zbk - st, lg, at)
    for (xx, sx_) in ((x0, 1), (x0 + W, -1)):
        for (yy, sy_) in ((y0, 1), (y0 + W, -1)):
            leg = box(*sorted((xx, xx + sx_ * lg)), *sorted((yy, yy + sy_ * at)), 0, zs - st) + \
                box(*sorted((xx, xx + sx_ * at)), *sorted((yy, yy + sy_ * lg)), 0, zs - st)
            rack += leg
    add("qc_frame", "QC rack frame", rack, "#A16207", 12, "make", "qc", (0, 0, 0))
    stations = [(x0 + pch / 2 + i * pch, y0 + pch / 2 + j * pch) for i in (0, 1) for j in (0, 1)]
    shelves = box(x0, x0 + W, y0, y0 + W, zs - st, zs) + box(x0, x0 + W, y0, y0 + W, zbk - st, zbk)
    for (sx_, sy_) in stations:
        shelves -= cyl(rt + 3, zs - st - 1, zs + 1, x=sx_, y=sy_)
    for xx in (x0, x0 + W - lg - 1):                     # lower shelf notched round the four legs
        for yy in (y0, y0 + W - lg - 1):
            shelves -= box(xx, xx + lg + 1, yy, yy + lg + 1, zbk - st - 1, zbk + 1)
    add("qc_shelves", "QC rack shelves (plywood)", shelves, "#D6B98C", 12, "make", "qc", (0, 0, 0))
    z_tp = zs + P["RIM_T"] - h
    tp = None
    for (sx_, sy_) in stations:
        p_ = pot(z_tp, sx_, sy_, P)
        tp = p_ if tp is None else tp + p_
    add("test_pots", "Test pots in the QC rack", tp, "#C8875A", None, "product", "qc", (0, 0, 0))
    gx_, gy_ = stations[0]
    zrim = zs + P["RIM_T"]
    gauge = box(gx_ - 6, gx_ + 6, gy_ - 170, gy_ + 170, zrim, zrim + 12) + \
        box(gx_ - 4, gx_ + 4, gy_ - 4, gy_ + 4, zrim - P["GAUGE_SCALE"], zrim)
    add("gauge", "Printed T-gauge", gauge, "#F59E0B", 13, "print", "qc", (0, 0, 0))
    bk = None
    for (sx_, sy_) in stations:
        b_ = cyl(P["BUCKET_D"] / 2, zbk, zbk + P["BUCKET_H"], sx_, sy_) - cyl(P["BUCKET_D"] / 2 - 3, zbk + 3, zbk + P["BUCKET_H"] + 1, sx_, sy_)
        bk = b_ if bk is None else bk + b_
    add("buckets", "Collection buckets", bk, "#2563EB", 14, "buy", "qc", (0, 0, 0))
    wz0 = z_tp + P["WALL"] + 0.5
    wz1 = zrim - 10
    rw1 = P["R_IN_BOT"] + (P["R_IN_RIM"] - P["R_IN_BOT"]) * (wz1 - wz0) / P["D_IN"]
    add("water", "Water in test pot", cone(P["R_IN_BOT"] - 0.5, rw1 - 0.5, wz0, wz1, gx_, gy_), "#7DD3FC", None, "product", "qc", (0, 0, 0))

    # ---- Fixed guards: welded mesh on 25 x 25 x 3 angle frames; standoffs bolted to the beam webs
    g = guard_solids(P)
    add("guards", "Fixed mesh guards", bd_comp(g), "#CA8A04", 16, "make", "guard", (0, 0, 0))
    add("pump_shield", "Pump slot inner shield", pump_shield(P), "#A16207", 16, "make", "guard", (0, 0, 0))
    add("gate", "Front gate", bd_comp(gate_geometry(P)), "#EAB308", 20, "make", "guard", (0, 0, 0))

    # ---- Interlock (BOM 21): release shaft with two universal joints, lock disc and knob; lock rod on a post
    # in the pocket in front of the set-back right guard strip; two sliders stop the rod lifting
    lx, ly, lift = P["LOCK_X"], P["LOCK_Y"], P["LOCK_LIFT"]
    yf, ysr = P["GUARD_Y_FRONT"], P["STRIP_Y"]
    a_ = math.radians(P["JACK_TURN"])
    A = (122 * math.cos(a_), 122 * math.sin(a_), zr)
    B = (lx, ysr + 20, zr)
    shaft = cyl_between((110 * math.cos(a_), 110 * math.sin(a_), zr), A, 5)
    shaft += bd.Pos(*A) * bd.Sphere(11) + cyl_between(A, B, 6) + bd.Pos(*B) * bd.Sphere(11)
    shaft += cyl_between(B, (lx, P["RELEASE_Y"], zr), 6)
    shaft += cyl_y(30, P["RELEASE_Y"] - 4, P["RELEASE_Y"] + 4, lx, zr)
    disc = cyl_y(40, ly - 3, ly + 3, lx, zr) - bd.Pos(lx, ly, zr) * bd.Rot(0, 120, 0) * bd.Pos(0, 0, 40 - 7.5) * bd.Box(12.5, 8, 15.5)
    add("release", "Release shaft, lock disc and knob", shaft + disc, "#1D4ED8", 21, "make", "lock", (0, 0, 0))
    post = box(lx - 10, lx + 10, ysr - 8, ysr, P["GUARD_Z0"], L["top1"]) - cyl_y(7, ysr - 9, ysr + 1, lx, zr)
    tab = lambda z_, x1_=lx + 10, r_=6.5: box(lx - 10, x1_, ly - 12, ysr - 8, z_, z_ + 6) - cyl(r_, z_ - 1, z_ + 7, lx, ly)
    for zt in (330, 600):
        post += tab(zt)
    t1 = P["LATCH_Z"] - 6
    post += tab(t1)                                                                                  # under slider 1 and the tongue
    t2 = 742.0
    post += tab(t2, lx + 62, 13)                                                                     # under slider 2; the collar passes
    add("lock_post", "Interlock post with guides", post, "#1E3A8A", 21, "make", "lock", (0, 0, 0))
    z_rb = zr + 40                                        # rod bottom resting on the disc rim (valve closed, rod up)
    rod = cyl(6, z_rb, P["LATCH_Z"] + lift, lx, ly)
    rod += cyl(12, t2 - 2 + lift, t2 + 4 + lift, lx, ly)                                            # collar for slider 2
    rod += box(lx + 6, lx + 60, ly - 4, ly + 4, 680, 688) + cyl(8, 676, 692, lx + 60, ly)          # lift handle
    add("lock_rod", "Lock rod", rod, "#1D4ED8", 21, "make", "lock", (0, 0, 0))
    sl1 = box(lx - 10, lx + 10, ly + 10, ly + 30, P["LATCH_Z"], P["LATCH_Z"] + 6)                   # pushed back by the tongue
    sl2 = box(lx + 14, lx + 56, ly - 14, ly + 14, t2 + 6, t2 + 12) - box(lx + 13, lx + 29, ly - 7, ly + 7, t2 + 5, t2 + 13)  # pulled aside by the cable
    add("sliders", "Interlock sliders", sl1 + sl2, "#DC2626", 21, "make", "lock", (0, 0, 0))
    yd = -(yw + P["DOUBLER_T"])
    plunger = box(-20, 20, yd - 25, yd, L["pin"] + 54, L["pin"] + 62) + cyl(5, L["pin"] + 40, L["pin"] + 69, 0, yd - ph / 2)
    zc_ = t2 + 9
    pts = [(0, yd - ph / 2, L["pin"] + 66), (0, -125, L["pin"] + 66), (400, -125, L["pin"] + 66), (400, -125, zc_),
           (400, ly, zc_), (lx + 56, ly, zc_)]
    cable = None
    for p0, p1 in zip(pts[:-1], pts[1:]):
        seg = cyl_between(p0, p1, 3)
        cable = seg if cable is None else cable + seg
    for c_ in pts[1:-1]:
        cable += bd.Pos(*c_) * bd.Sphere(3)
    add("pin_sensor", "Pin-presence plunger and cable", plunger + cable, "#DC2626", 21, "make", "lock", (0, 0, 0))
    return out


def bd_comp(shapes):
    bd = _b()
    return bd.Compound(children=list(shapes))


BOM_NAMES = {
    1: ("Base beam, feet and jack plate", "#4B5563", (0, 0, -260)),
    2: ("Uprights with bolted joints", "#6B7280", (0, 0, 0)),
    3: ("Top crossbeam with pin doublers", "#4B5563", (0, 0, 560)),
    4: ("20 t bottle jack", "#B91C1C", (0, -560, -120)),
    5: ("Moving platen with guide sleeves", "#9CA3AF", (0, 0, -40)),
    6: ("Return springs", "#D4A017", (0, 460, -60)),
    7: ("Rails, folding extension and carriage", "#374151", (0, -520, 40)),
    8: ("Female mold (cast aluminum on a steel base plate)", "#CBD5E1", (0, -520, 200)),
    9: ("Male mold (cast aluminum)", "#94A3B8", (0, 0, 440)),
    10: ("Male mold slide, load pin, crank", "#0F766E", (0, 0, 680)),
    11: ("Pressed filter pot", "#C8875A", (0, -520, 620)),
    12: ("QC flow-test rack (2 x 2)", "#A16207", (0, 0, 0)),
    13: ("Printed T-gauge", "#F59E0B", (0, 0, 520)),
    14: ("Collection buckets", "#2563EB", (0, 0, -150)),
    16: ("Fixed mesh guards and pump slot shield", "#CA8A04", (0, 900, 250)),
    20: ("Front gate, mesh in a tube frame, with hinges and tongue", "#EAB308", (0, -650, 250)),
    21: ("Gate and pin interlock, release shaft", "#1D4ED8", (250, -700, -150)),
}
LOOSE = {"test_pots": ("Test pots in the QC rack", (0, 0, 300)), "water": ("Water in test pot", (0, 0, 300))}


def build_parts(P=PARAMS, comps=None):
    """Components grouped by BOM line: a list of (name, shape, color, bom_no, explode_offset). Press closed."""
    bd = _b()
    comps = comps or components(P)
    parts = []
    for bom, (name, color, exp) in BOM_NAMES.items():
        kids = [c.shape for c in comps if c.bom == bom]
        if kids:
            parts.append((name, bd.Compound(children=kids), color, bom, exp))
        if bom == 12:
            for c in comps:
                if c.key in LOOSE:
                    parts.append((LOOSE[c.key][0], c.shape, c.color, None, LOOSE[c.key][1]))
    order = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, None, 13, 14, 16, 20, 21]
    return parts


GUARD_BOM = (16, 20, 21)


def assembly(parts=None):
    bd = _b()
    parts = parts or build_parts()
    return bd.Compound(children=[p[1] for p in parts])


def press_only(parts=None):
    bd = _b()
    parts = parts or build_parts()
    return bd.Compound(children=[p[1] for p in parts if p[3] is not None and (p[3] <= 11 or p[3] in GUARD_BOM)])


# Faces that must touch (the joint is made there), checked by --check
CONTACTS = [
    ("foot_left", "base_beam"), ("foot_right", "base_beam"), ("foot_right", "upright_right"),
    ("anchors", "foot_left"), ("shims_left", "upright_left"), ("shims_left", "base_beam"), ("shims_right", "top_beam"),
    ("tubes_right", "upright_right"), ("bolts_right", "base_beam"), ("bolts_right", "top_beam"),
    ("liners", "top_beam"), ("pump_handle", "jack"), ("jack", "jack_plate"), ("jack_plate", "base_beam"), ("jack_plate_bolts", "jack_plate"), ("jack", "platen"), ("springs", "base_beam"), ("springs", "platen"),
    ("rails", "platen"), ("carriage", "rails"), ("fm_plate", "rails"), ("fm_cup", "fm_plate"), ("loc_pins", "fm_cup"),
    ("mm", "fm_cup"), ("bushes", "mm"), ("stem", "mm"), ("adapter_bolts", "stem"), ("pin", "top_beam"),
    ("nut", "stem"), ("screw", "bracket"), ("bracket", "top_beam"), ("bracket_bolts", "bracket"),
    ("pot", "fm_cup"), ("pot", "mm"), ("guards", "base_beam"), ("guards", "top_beam"), ("gate", "guards"),
    ("release", "jack"), ("lock_rod", "release"), ("gate", "sliders"), ("lock_post", "guards"),
    ("pin_sensor", "pin"), ("pin_sensor", "top_beam"), ("pump_shield", "guards"), ("pump_shield", "base_beam"), ("qc_shelves", "qc_frame"), ("test_pots", "qc_shelves"),
    ("buckets", "qc_shelves"), ("gauge", "test_pots"),
]


# Pairs that share volume on purpose: the pressed pot fills the molds; the gauge stem stands in the test water
ALLOWED = {frozenset(("pot", "fm_cup")), frozenset(("pot", "mm")), frozenset(("gauge", "water")),
           frozenset(("water", "test_pots"))}


def _solids(shape):
    return list(shape.solids()) or [shape]


def _bb_apart(A, B, pad=0.0):
    return (A.min.X > B.max.X + pad or B.min.X > A.max.X + pad or A.min.Y > B.max.Y + pad or B.min.Y > A.max.Y + pad
            or A.min.Z > B.max.Z + pad or B.min.Z > A.max.Z + pad)


def check_fits(comps=None, tol=1.0, verbose=True, contacts=None):
    """No two components may overlap (intersection volume under tol mm3), and every CONTACTS pair must touch.
    Compounds are split into solids so the mesh guards check quickly. Returns (overlaps, gaps)."""
    comps = comps or components()
    by = {c.key: c for c in comps}
    sol = {c.key: [(s_, s_.bounding_box()) for s_ in _solids(c.shape)] for c in comps}
    bbs = {c.key: c.shape.bounding_box() for c in comps}
    overlaps = []
    for i, a in enumerate(comps):
        for b_ in comps[i + 1:]:
            if frozenset((a.key, b_.key)) in ALLOWED or _bb_apart(bbs[a.key], bbs[b_.key]):
                continue
            v = 0.0
            for sa, ba in sol[a.key]:
                if _bb_apart(ba, bbs[b_.key]):
                    continue
                for sb, bb_ in sol[b_.key]:
                    if _bb_apart(ba, bb_):
                        continue
                    r = sa & sb
                    v += r.volume if r is not None else 0.0
            if v >= tol:
                overlaps.append((a.key, b_.key, v))
    gaps = []
    for ka, kb in (CONTACTS if contacts is None else contacts):
        if ka not in sol or kb not in sol:
            continue
        d = min(sa.distance_to(sb) for sa, ba in sol[ka] for sb, bb_ in sol[kb] if not _bb_apart(ba, bb_, 1.0)) \
            if any(not _bb_apart(ba, bb_, 1.0) for sa, ba in sol[ka] for sb, bb_ in sol[kb]) else 99.0
        if d > 0.05:
            gaps.append((ka, kb, d))
    if verbose:
        print(f"fit check: {len(comps)} components; {len(overlaps)} overlaps; {len(gaps)} missing contacts")
        for o in overlaps:
            print(f"  OVERLAP {o[0]} / {o[1]}: {o[2]:.1f} mm3")
        for g_ in gaps:
            print(f"  NO CONTACT {g_[0]} / {g_[1]}: {g_[2]:.2f} mm apart")
    return overlaps, gaps


# ---------------------------------------------------------------------------
# The press in its other positions (DDR-004). The model is drawn closed; these move the parts that move and
# check again, so nothing collides anywhere in the cycle.
# ---------------------------------------------------------------------------
WITH_PLATEN = ("platen", "rails", "extension", "carriage", "retaining_pins", "fm_plate", "fm_cup", "loc_pins", "fm_screws")
WITH_SLIDE = ("mm", "bushes", "stem", "adapter_bolts", "nut")
WITH_CARRIAGE = ("carriage", "retaining_pins", "fm_plate", "fm_cup", "loc_pins", "fm_screws")
PIN_PARK = 150.0                                           # load pin pulled out this far to crank; it stays in the front bores


def moved(comps, state, P=PARAMS):
    """Components in another position: 'open' (release open, platen down, pin pulled, male mold cranked up, pot
    out) or 'demold' (open, rail extension swung out, carriage pulled out onto the tipping pins, gate open).
    Springs stretch and are left out; the jack ram is drawn retracted."""
    bd = _b()
    L = levels(P)
    out = []
    for c in comps:
        if c.key in ("pot", "springs"):
            continue
        sh = c.shape
        if c.key == "jack":
            sh = sh - box(-200, 200, -200, 200, L["platen0_low"], L["platen0"] + 10)
        if c.key in WITH_PLATEN:
            if c.key == "extension" and state == "demold" and P["EXT_FOLDED"]:
                y_h = -P["RAIL_HINGE"]
                sh = bd.Pos(0, y_h, L["deck1"]) * bd.Rot(-90, 0, 0) * bd.Pos(0, -y_h, -L["deck1"]) * sh
            if c.key in WITH_CARRIAGE and state == "demold":
                sh = bd.Pos(0, -P["CARRIAGE_OUT"], 0) * sh
            sh = bd.Pos(0, 0, -P["PRESS_TRAVEL"]) * sh
        if c.key in WITH_SLIDE:
            sh = bd.Pos(0, 0, P["CRANK_LIFT"]) * sh
        if c.key == "pin":                                 # R-clip out, then the pin pulled to its parked position
            b_ = SECTIONS[P["BEAM_SEC"]]
            y_tail = P["BEAM_GAP"] / 2 + b_["tw"] + P["DOUBLER_T"] + 20
            sh = bd.Pos(0, -PIN_PARK, 0) * (sh - cyl(3.2, L["pin"] - 41, L["pin"] + 41, 0, y_tail))
        if c.key == "pin_sensor":                           # plunger drops 10 mm when the pin head leaves it
            continue
        if c.key == "lock_rod":                            # valve open: rod down in the disc notch
            sh = bd.Pos(0, 0, -P["LOCK_LIFT"]) * sh
        if c.key == "gate" and state == "demold":
            sh = bd_comp(gate_geometry(P, open_deg=105.0))
        out.append(C(c.key, c.name, sh, c.color, c.bom, c.how, c.group, c.explode))
    return out


def check_states(comps=None, verbose=True):
    """Overlap checks with the press open and set for demolding, the pump handle over its whole stroke, the
    carriage hooks on the tipping pins and the lock rod in the disc notch. Returns a list of failures."""
    bd = _b()
    P = PARAMS
    L = levels(P)
    comps = comps or components()
    fails = []
    skip = {frozenset(("lock_rod", "release"))}             # checked on their own below
    for state in ("open", "demold"):
        mc = moved(comps, state)
        ov, _ = check_fits(mc, verbose=False, contacts=())
        ov = [o for o in ov if frozenset(o[:2]) not in skip]
        fails += [(state, "overlap", o) for o in ov]
        if verbose:
            print(f"state {state}: {len(mc)} components; {len(ov)} overlaps")
            for o in ov:
                print(f"  OVERLAP {o[0]} / {o[1]}: {o[2]:.1f} mm3")
        if state == "demold":
            by = {c.key: c.shape for c in mc}
            zp = L["deck1"] + 7 - P["PRESS_TRAVEL"]; yp = -(P["CARRIAGE_OUT"] + P["PIVOT_DY"])
            pins = by["extension"] & (box(186, 260, yp - 8, yp + 8, zp - 8, zp + 8) + box(-260, -186, yp - 8, yp + 8, zp - 8, zp + 8))
            d = by["carriage"].distance_to(pins)
            if verbose:
                print(f"  carriage hooks to tipping pins: {d:.2f} mm (sliding fit, must be 1.5 or less)")
            if d > 1.5:
                fails.append((state, "hooks", d))
    # pump handle over its stroke: lowest and highest position where it crosses the guard
    sw, sz0, sz1 = P["PUMP_SLOT"]
    others = [c for c in comps if c.key not in ("jack", "pump_handle", "pot")]
    shield = next(c.shape for c in comps if c.key == "pump_shield")
    core = pump_shield(P, core_only=True)
    for zz in P["HANDLE_STROKE"]:
        h = C("pump_handle", "handle", pump_handle(P, zz), "", 4, "buy", "press")
        ov, _ = check_fits([h] + others, verbose=False, contacts=())
        ov = [o for o in ov if "pump_handle" in o[:2]]
        clear = min(h.shape.distance_to(c.shape) for c in others if not _bb_apart(h.shape.bounding_box(), c.shape.bounding_box(), 30))
        d_wall = h.shape.distance_to(shield)
        z0_, r0_ = L["jack0"] + 72.0, 170.0                     # the slot end, measured square to the handle
        cos_ = math.cos(math.atan((zz - z0_) / (P["GUARD_X"] / math.cos(math.radians(P["JACK_TURN"])) - r0_)))
        d_end = min(h.shape.distance_to(core), (sz1 - zz if zz > (sz0 + sz1) / 2 else zz - sz0) * cos_ - P["HANDLE_D"] / 2)
        if verbose:
            print(f"pump handle at {zz:.0f} mm at the guard: {len(ov)} overlaps; nearest part {clear:.1f} mm; "
                  f"shield side walls {d_wall:.1f} mm; shield roof or floor and slot end {d_end:.1f} mm (finger gap, 25 or more)")
        fails += [("handle", "overlap", o) for o in ov]
        if d_end < P["SHIELD_GAP"] - 0.6:
            fails.append(("handle", "finger gap", d_end))
    # lock rod dropped into the disc notch with the valve turned open (the notch comes to the top)
    rel = next(c.shape for c in comps if c.key == "release")
    rod = next(c.shape for c in comps if c.key == "lock_rod")
    zr = release_z(P)
    disc = rel & box(P["LOCK_X"] - 45, P["LOCK_X"] + 45, P["LOCK_Y"] - 3.5, P["LOCK_Y"] + 3.5, zr - 45, zr + 45)
    turned = bd.Pos(P["LOCK_X"], 0, zr) * bd.Rot(0, -120, 0) * bd.Pos(-P["LOCK_X"], 0, -zr) * disc
    dropped = bd.Pos(0, 0, -P["LOCK_LIFT"]) * rod
    vol = lambda x: 0.0 if x is None else x.volume  # noqa: E731
    v = vol(turned & dropped)
    d_ = turned.distance_to(dropped)
    v_closed = vol(disc & rod)
    if verbose:
        print(f"lock rod: resting on the disc rim with the valve closed {v_closed:.1f} mm3 overlap; dropped into the notch "
              f"with the valve turned 120 deg open {v:.1f} mm3 overlap, {d_:.2f} mm from the notch floor")
    if v > 1.0 or v_closed > 1.0 or d_ > 0.5:
        fails.append(("lock", "notch", (v, d_)))
    if verbose:
        print(f"state checks: {len(fails)} failures")
    return fails


# ---------------------------------------------------------------------------
# ISO 13857 desk check (decided by Amish 2026-10-02: done now, signed by a competent person, a hold point
# before any force above hand pressure). Distances are straight lines from the outer face of each opening to
# the nearest moving part, with the press closed and open; a real reach round an obstacle is longer.
# ---------------------------------------------------------------------------
# Moving parts and what moves them. The load pin is left out: it is moved only by hand, with the press open.
HAZARD = {**{k: "jack" for k in WITH_PLATEN + ("springs", "pot")}, **{k: "crank" for k in WITH_SLIDE}}

# ISO 13857:2019 Table 4 (persons 14 years and older), upper limbs through regular openings, as read for this
# desk check: (e up to, slot, square, round) in mm. The competent person confirms against the published table.
ISO13857_T4 = [(4, 2, 2, 2), (6, 10, 5, 5), (8, 20, 15, 5), (10, 80, 25, 20), (12, 100, 80, 80),
               (20, 120, 120, 120), (30, 850, 120, 120), (40, 850, 200, 120), (120, 850, 850, 850)]


def iso_sr(e, kind):
    """Safety distance sr (mm) for an opening e (mm) of kind 'slot', 'square' or 'round' (Table 4)."""
    col = {"slot": 1, "square": 2, "round": 3}[kind]
    for row in ISO13857_T4:
        if e <= row[0]:
            return row[col]
    return None


def iso_openings(P=PARAMS):
    """Every guard opening as (name, kind, e, slab), slab a thin box on the opening's outer face."""
    L = levels(P)
    gx = P["GUARD_X"]; sw, sz0, sz1 = P["PUMP_SLOT"]; py = pump_slot_y(P)
    lx, ys, zr = P["LOCK_X"], P["STRIP_Y"], release_z(P)
    g2, top1 = P["BEAM_GAP"] / 2, L["top1"]
    s2 = P["STEM"] / 2
    xs, ub, bl = P["SPAN"] / 2, SECTIONS[P["UPRIGHT_SEC"]]["b"], P["BEAM_L"] / 2
    out = [("Pump slot, right side guard", "slot", sw, box(gx - 0.5, gx, py - sw / 2, py + sw / 2, sz0, sz1)),
           ("Release shaft opening, front right strip (16 mm round the 12 mm shaft)", "slot", 22 - 6,
            box(lx - 22, lx + 22, ys - 0.5, ys, zr - 22, zr + 22)),
           ("Pin cable opening, front right strip", "square", 40, box(lx + 50, lx + 90, ys - 0.5, ys, 731, 771))]
    for sx in (-1, 1):                                        # top beam gap, open from above between the parts in it
        side = "right" if sx > 0 else "left"
        for x0_, x1_ in ((100.0, xs - ub), (xs + ub, bl - P["END_BLOCK_L"])):
            out.append((f"Top beam gap, {side}, {x0_:.0f} to {x1_:.0f} mm from the middle", "square", min(x1_ - x0_, 2 * g2),
                        box(*sorted((sx * x0_, sx * x1_)), -g2, g2, top1 - 0.5, top1)))
    return out


def iso13857_check(comps=None, verbose=True):
    """Desk check of the guard openings against ISO 13857 Table 4 from the model's distances. Returns rows
    (item, kind, e, sr needed, distance found, verdict) and prints them."""
    bd = _b()
    P = PARAMS
    L = levels(P)
    comps = comps or components()
    states = {"closed": comps, "open": moved(comps, "open")}
    haz = {k: [c for c in v if c.key in HAZARD] for k, v in states.items()}

    def nearest(slab):
        best = (1e9, "", "")
        for st, cs in haz.items():
            for c in cs:
                if _bb_apart(slab.bounding_box(), c.shape.bounding_box(), best[0]):
                    continue
                d = slab.distance_to(c.shape)
                if d < best[0]:
                    best = (d, f"{c.name}, moved by the {HAZARD[c.key]}", st)
        return best
    rows = []
    e_mesh = P["MESH_PITCH"] - P["MESH_WIRE"]
    for pnl in guard_layout(P):
        a0, a1, b0, b1, c = pnl["a0"], pnl["a1"], pnl["b0"], pnl["b1"], pnl["c_out"]
        if pnl["plane"] == "yz":
            slab = box(*sorted((c, c - 0.5 * pnl["inward"])), a0, a1, b0, b1)
            holes = [box(c - 1, c + 1, h[0], h[1], h[2], h[3]) for h in pnl["holes"]]
        elif pnl["plane"] == "xz":
            slab = box(a0, a1, *sorted((c, c - 0.5 * pnl["inward"])), b0, b1)
            holes = [box(h[0], h[1], c - 1, c + 1, h[2], h[3]) for h in pnl["holes"]]
        else:
            slab = box(a0, a1, b0, b1, *sorted((c, c - 0.5 * pnl["inward"])))
            holes = [box(h[0], h[1], h[2], h[3], c - 1, c + 1) for h in pnl["holes"]]
        for h in holes:
            slab -= h
        d, who, st = nearest(slab)
        rows.append((f"Mesh, {pnl['name'].lower()}", "square", e_mesh, iso_sr(e_mesh, "square"), d, who, st))
    gh, yf, z1 = P["GATE_HALF"], P["GUARD_Y_FRONT"], L["top1"]
    gate_slab = box(-gh + 4, gh - 4, yf, yf + 0.5, P["GATE_Z0"] + 4, z1 - 4)
    d, who, st = nearest(gate_slab)
    rows.append(("Mesh, front gate", "square", e_mesh, iso_sr(e_mesh, "square"), d, who, st))
    for name, kind, e, slab in iso_openings(P):
        d, who, st = nearest(slab)
        rows.append((name, kind, e, iso_sr(e, kind), d, who, st))
    # the pump slot opens only into the shield: no moving part may enter the space inside it in any position
    space = pump_shield(P, interior=True)
    inside = [c.name for st, cs in haz.items() for c in cs
              if not _bb_apart(space.bounding_box(), c.shape.bounding_box()) and ((space & c.shape) is not None)
              and (space & c.shape).volume > 1.0]
    out = []
    for name, kind, e, sr, d, who, st in rows:
        ok = d >= sr
        if name.startswith("Pump slot"):
            ok = not inside
            who = "none inside the shield" if ok else ", ".join(sorted(set(inside)))
        out.append(dict(item=name, kind=kind, e=e, sr=sr, d=d, part=who, state=st, ok=ok))
    # the pump slot: what can be reached through it is inside the shield
    shield = next(c.shape for c in comps if c.key == "pump_shield")
    jack = next(c.shape for c in comps if c.key == "jack")
    a = math.radians(P["JACK_TURN"])
    zj = L["jack0"] + 150
    d_jack = shield.distance_to(jack & cyl(P["JACK_BODY_D"] / 2 + 1, zj - 60, zj + 60))
    sh_d = min(shield.distance_to(c.shape) for st, cs in haz.items() for c in cs
               if not _bb_apart(shield.bounding_box(), c.shape.bounding_box(), 200))
    extra = dict(shield_jack_gap=d_jack, shield_to_hazard=sh_d)
    # pump handle passing the slot frame (sideways), at both stroke ends
    guards = next(c.shape for c in comps if c.key == "guards")
    extra["handle_pass"] = min(pump_handle(P, z).distance_to(guards) for z in P["HANDLE_STROKE"])
    # crank: the stem's cap plate under the bracket top plate at full lift (moved by the handwheel, not the jack)
    extra["cap_to_bracket"] = L["bracket0"] - (L["stem1"] + 10 + P["CRANK_LIFT"])
    extra["flange_to_beam"] = P["LIFT_CLEAR"]
    if verbose:
        print("ISO 13857 desk check (Table 4, as read; straight-line distance from the opening to the nearest moving part)")
        for r in out:
            if r["item"].startswith("Pump slot"):
                print(f"  {r['item']}: {r['kind']} e {r['e']:.1f} mm, sr needed {r['sr']} mm; the slot opens only into the fixed "
                      f"inner shield; moving parts inside it: {r['part']} (only the pump handle and the jack's pump socket): "
                      f"{'meets' if r['ok'] else 'DOES NOT MEET'}")
                continue
            print(f"  {r['item']}: {r['kind']} e {r['e']:.1f} mm, sr needed {r['sr']} mm; nearest moving part "
                  f"{r['d']:.0f} mm ({r['part']}, press {r['state']}): {'meets' if r['ok'] else 'DOES NOT MEET'}")
        print(f"  pump slot shield: inner end {extra['shield_jack_gap']:.1f} mm off the jack body; nearest moving part outside "
              f"the shield {extra['shield_to_hazard']:.0f} mm from it")
        print(f"  pump handle passing the slot frame: {extra['handle_pass']:.1f} mm at the stroke ends")
        print(f"  crank: stem cap plate {extra['cap_to_bracket']:.0f} mm under the bracket top at full lift; male flange "
              f"{extra['flange_to_beam']:.0f} mm under the top beam at full lift")
    return out, extra


if __name__ == "__main__":
    import sys
    from build123d import Compound, export_step, export_stl
    comps = components()
    if "--iso" in sys.argv:
        iso13857_check(comps)
        sys.exit(0)
    if "--check" in sys.argv:
        ov, gp = check_fits(comps)
        fl = check_states(comps)
        print("constructability checks:", "PASS" if not (ov or gp or fl) else "FAIL")
        sys.exit(1 if (ov or gp or fl) else 0)
    root = Path(__file__).resolve().parents[1]
    (root / "step").mkdir(exist_ok=True); (root / "stl").mkdir(exist_ok=True)
    parts = build_parts(comps=comps)
    by = {c.key: c.shape for c in comps}
    export_step(assembly(parts), str(root / "step" / "potpress-assembly.step"))
    export_step(press_only(parts), str(root / "step" / "potpress-press.step"))
    for key, stem in [("fm_cup", "female-mold"), ("mm", "male-mold"), ("pot", "filter-pot"), ("gauge", "t-gauge")]:
        export_step(Compound(children=[by[key]]), str(root / "step" / f"{stem}.step"))
        export_stl(by[key], str(root / "stl" / f"{stem}.stl"))
    export_stl(press_only(parts), str(root / "stl" / "potpress-press.stl"))
    L = levels()
    P_ = PARAMS
    bb = press_only(parts).bounding_box()
    print(f"press envelope {bb.size.X:.0f} x {bb.size.Y:.0f} x {bb.max.Z:.0f} mm from the floor, guarded (rail extension folded; "
          f"crank knob included; floor anchors go {-bb.min.Z:.0f} mm into the floor)")
    nh = bd_comp([c.shape for c in comps if c.key != "pump_handle" and c.bom is not None and (c.bom <= 11 or c.bom in GUARD_BOM)]).bounding_box()
    print(f"without the pump handle {nh.size.X:.0f} x {nh.size.Y:.0f} mm; the handle stands {bb.max.X - nh.max.X:.0f} mm outside the right guard while pumping")
    print(f"guard mesh planes {2 * P_['GUARD_X']:.0f} x {P_['GUARD_Y_BACK'] - P_['GUARD_Y_FRONT']:.0f} mm; y from {bb.min.Y:.0f} to {bb.max.Y:.0f}")
    print(f"overall height {L['overall']:.0f} mm; male tip above female rim when open {L['open_gap']:.0f} mm")
    print("wrote cad/step/*.step and cad/stl/*.stl")
