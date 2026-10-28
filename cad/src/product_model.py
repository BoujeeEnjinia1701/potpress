"""PotPress product appearance model for photoreal renders (STANDARDS sections 12 and 24), TRL 3.

Every product part is components(CHOSEN) from cad/src/model.py as it is (kit 1.9, detail level D3): frame, feet
with their M12 studs and floor anchors, every M16 10.9 joint bolt, washer and nut, jack plate and bolts, the bottle
jack turned 25 degrees with its pump handle, platen, rails with the folding extension and tipping pins, carriage,
female mold on its steel base plate with dowels and countersunk screws, the open-topped male mold with bushes,
stem on its adapter disc, load pin, captive nut, crank bracket and handwheel, the mechanical interlock, the pump
slot shield, small-hole plates, cover plates and their screws, every weld bead, and the QC rack. Only the look is
added: the guard and gate mesh drawn wire by wire at the specified pitch (model.py draws every 8th wire, decided
by Amish 2026-10-03), close-wound coils in place of the return spring envelopes, a polished jack ram, a nameplate
and load rating label on the top crossbeam and a hazard label on the front right strip. The site is added as
context parts: the concrete floor slab of a filter workshop, a blockwork back wall and two steel posts of the
open-sided shed, a pallet of clay mix, an anti-fatigue mat and a 1.75 m mannequin standing on the floor.
Ground level is model z = 0 (photoreal --ground-z=0); every site part reaches below it.
APPEARANCE MODEL ONLY: no tolerances, no fabrication detail. CONCEPT, NOT FOR FABRICATION.

Axes as model.py: X across the press, Y front (-Y, operator side) to back, Z up from the floor. The press is
closed at the end of a pressing stroke with the rail extension folded. Groups: "shell" (the press), "internal"
(the pressed pot), "guard" (fixed guards, shield, plates, covers, interlock, labels on the guards), "gate_closed"
and "gate_open" (the front gate shut or swung open 105 degrees), "accessory" (QC rack) and "context" (site and
mannequin).

    from product_model import product_parts
    for p in product_parts(): print(p["name"], p["group"], p["material"])
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parents[1] / ".kit")]

from build123d import Axis, Compound, Pos, RegularPolygon, Rot, extrude, fillet  # noqa: E402
import model as M  # noqa: E402
from model import BOM_NAMES, PARAMS, SECTIONS, box, cyl, gate_geometry, guard_pieces, levels  # noqa: E402
from cad_parts import part as kpart, break_edges  # noqa: E402

TITLE = "PotPress: hand-pumped hydraulic press for ceramic pot water filters"

_SITE = ["--scene=outdoor", "--ground=concrete", "--ground-z=0", "--sun=42,-20", "--lens=45"]
RENDER_VIEWS = [
    {"name": "hero", "groups": ["shell", "guard", "gate_closed", "internal", "accessory", "context"], "explode": False,
     "el": 18, "az": -40, "args": _SITE,
     "note": "Site render in a filter workshop, from the front right and a little above (about 18 deg elevation): "
             "press closed at the end of a stroke behind welded-mesh guards with the interlocked front gate shut, "
             "pump handle out through the shielded slot in the right guard, QC flow-test rack at the right, on the "
             "concrete floor of an open-sided shed; 1.75 m person standing at the front left for scale"},
    {"name": "studio", "groups": ["shell", "guard", "gate_closed", "internal"], "explode": False, "el": 26, "az": -38,
     "note": "Studio render from the front right and above (about 26 deg elevation): bolted UPN channel frame with "
             "its M16 joints, bottle jack under the platen, mesh guards and interlocked front gate"},
    {"name": "exploded", "groups": ["shell", "internal"], "explode": True, "el": 28, "az": -55,
     "note": "Exploded view from the front right and above (about 28 deg elevation): base beam and feet, "
             "uprights and joint bolts, bottle jack, springs, platen, rails and carriage, female mold on its "
             "steel base plate, pressed pot, male mold, top crossbeam, male mold slide and handwheel; guards "
             "and gate not shown"},
    {"name": "lineup", "groups": ["shell", "guard", "gate_closed", "internal", "accessory"],
     "explode": False, "el": 24, "az": -58,
     "note": "Lineup from the front right and above (about 24 deg elevation): the press at left and the "
             "2 x 2 QC flow-test rack at right with fired test pots, T-gauge and collection buckets"},
    {"name": "gate-open", "groups": ["shell", "guard", "gate_open", "internal"], "explode": False,
     "el": 18, "az": -68,
     "note": "Front gate swung open (about 105 deg) on its left hinges, showing the molds and carriage; "
             "press parts drawn in the pressing position for comparison with the hero. In use the gate "
             "opens only after the jack release is open and the platen is down"},
]

C_CHROME, C_SPRING, C_LABEL, C_INK, C_YELLOW, C_ACCENT = "#D5D9DE", "#C9A227", "#F4F4F2", "#1F2937", "#E8B517", "#0F766E"
C_GUARD, C_MESH = "#E2A90F", "#6F767F"
GUARD_KEYS = ("pump_shield", "opening_plates", "beam_covers", "bracket_covers", "cover_screws", "release", "lock_post",
              "lock_rod", "sliders", "pin_sensor")


def _fillet_try(shape, edges, radii):
    """Fillet `edges` with the first radius that gives a valid solid; else return the input."""
    edges = list(edges)
    for r in radii:
        try:
            out = fillet(edges, r)
            if out.is_valid and out.volume > 0:
                return out
        except Exception:
            pass
    return shape


def _comp(shapes):
    return Compound(children=list(shapes))


def product_parts(P=PARAMS):
    L = levels(P)
    b = SECTIONS[P["BEAM_SEC"]]
    g2 = P["BEAM_GAP"] / 2
    out = []

    def add(name, shape, material, group, bom=None, kind="made", color=None, explode=None):
        q = kpart(name, shape, material, kind=kind, bom=bom, group=group, color=color)
        if explode is None:
            explode = BOM_NAMES[bom][2] if bom in BOM_NAMES else (0, 0, 0)
        q["explode"] = tuple(float(v) for v in explode)
        out.append(q)
        return q

    # ------------------------------------------------------------ the chosen option as modelled (kit 1.9 parts)
    for p in M.components(M.CHOSEN):
        k = p.get("key_src")
        if k in ("guards", "gate", "springs", "jack"):
            continue                                            # redrawn for the look below
        grp = ("internal" if k == "pot" else "accessory" if k in M.QC_KEYS else "guard" if k in GUARD_KEYS or p["bom"] == 16
               else "shell")
        exp = (0, 0, 300) if k in ("test_pots", "water") else None
        add(p["name"], p["shape"], p["material_name"], grp, p["bom"], p["kind"], p["color"], exp)

    # ------------------------------------------------------------ jack: red body, polished ram
    comps = {c.key: c for c in M.press_components(P, detail=True) if c.key in ("jack",)}
    jack = comps["jack"].shape
    ram_zone = cyl(P["RAM_D"] / 2 + 0.5, L["platen0_low"] - 20, L["platen0"] + 1)
    add("20 t bottle jack body", jack - ram_zone, "safety_red", "shell", 4, "bought")
    add("Jack ram (polished)", jack & ram_zone, "stainless", "shell", 4, "bought")

    # ------------------------------------------------------------ return springs as close-wound coils with hooks
    coils = []
    z_a, z_b = L["base1"] + P["SPRING_LUG_T"] + 12, L["platen0"] - P["SPRING_LUG_T"] - 12
    n = int((z_b - z_a) / 5.0)
    pitch = (z_b - z_a) / n
    turn = cyl(12.0, 0, pitch - 1.0) - cyl(7.4, -1, pitch)
    for sx in (-1, 1):
        x_ = sx * P["SPRING_X"]
        for k in range(n):
            coils.append(Pos(x_, 0, z_a + k * pitch) * turn)
        coils.append(cyl(2.5, L["base1"] + P["SPRING_LUG_T"] / 2, z_a, x_ + 3.5))
        coils.append(cyl(2.5, z_b, L["platen0"] - P["SPRING_LUG_T"] / 2, x_ + 3.5))
    add("Return springs", _comp(coils), "zinc_plated", "shell", 6, "bought", C_SPRING)

    # ------------------------------------------------------------ nameplate and load rating label on the top beam
    yf = -g2 - b["tw"]
    zc = L["pin"]
    npl = box(-238, -110, yf - 1.2, yf, zc - 32, zc + 32)
    npl = _fillet_try(npl, npl.edges().filter_by(Axis.Y), [4.0, 2.0])
    add("Nameplate", npl, "painted_steel", "shell", 3, color=C_ACCENT)
    ink = box(-222, -150, yf - 1.5, yf - 1.2, zc + 6, zc + 20) + box(-222, -175, yf - 1.5, yf - 1.2, zc - 6, zc) \
        + box(-222, -130, yf - 1.5, yf - 1.2, zc - 20, zc - 15)
    add("Nameplate print", ink, "label", "shell", 3)
    rl = box(110, 238, yf - 0.6, yf, zc - 30, zc + 30)
    add("Load rating label (20 t max)", rl, "label", "shell", 3, color=C_YELLOW)
    rink = box(122, 170, yf - 0.9, yf - 0.6, zc + 4, zc + 20) + box(122, 226, yf - 0.9, yf - 0.6, zc - 8, zc - 3) \
        + box(122, 200, yf - 0.9, yf - 0.6, zc - 20, zc - 15)
    add("Load rating label print", rink, "label", "shell", 3, color=C_INK)

    # ------------------------------------------------------------ guards with every wire, and the gate shut and open
    for nm, kind, sols in guard_pieces(P, every_wire=True):
        if kind == "mesh":
            add(nm + " (every wire)", _comp(sols), "galvanised", "guard", 16, color=C_MESH)
        else:
            add(nm, sols[0] if len(sols) == 1 else _comp(sols), "safety_yellow", "guard", 16, color=C_GUARD)
    for state, deg in (("gate_closed", 0.0), ("gate_open", 105.0)):
        tag = "" if deg == 0 else ", open"
        for nm, kind, sols in gate_geometry(P, every_wire=True, open_deg=deg, pieces=True):
            sh = sols[0] if len(sols) == 1 else _comp(sols)
            if kind == "mesh":
                add(nm + tag, sh, "galvanised", state, 20, color=C_MESH)
            else:
                add(nm + tag, sh, "zinc_plated" if kind == "hinge" else "safety_yellow", state, 20,
                    color=None if kind == "hinge" else C_GUARD)

    # hazard label on the front right strip (set back for the interlock), clear of the interlock post
    ys, gx = P["STRIP_Y"], P["GUARD_X"]
    xl0, xl1, zl0, zl1 = P["LOCK_X"] + 16, gx - 22, 1150.0, 1250.0
    lab = box(xl0, xl1, ys - 1.2, ys, zl0, zl1)
    lab = _fillet_try(lab, lab.edges().filter_by(Axis.Y), [4.0, 2.0])
    add("Hazard label (crush, keep gate closed)", lab, "label", "guard", 16, color=C_YELLOW)
    xc_ = xl0 + 26; zc_ = (zl0 + zl1) / 2
    tri = Pos(xc_, ys - 1.35, zc_ - 4) * Rot(90, 0, 0) * extrude(RegularPolygon(22, 3, rotation=90), amount=0.3, both=True)
    tri -= Pos(xc_, ys - 1.35, zc_ - 4) * Rot(90, 0, 0) * extrude(RegularPolygon(14, 3, rotation=90), amount=1, both=True)
    tri += box(xc_ - 2.5, xc_ + 2.5, ys - 1.5, ys - 1.2, zc_ - 8, zc_ + 8)
    txt = box(xl0 + 56, xl1 - 8, ys - 1.5, ys - 1.2, zc_ + 14, zc_ + 24) + box(xl0 + 56, xl1 - 20, ys - 1.5, ys - 1.2, zc_ - 2, zc_ + 6) \
        + box(xl0 + 56, xl1 - 14, ys - 1.5, ys - 1.2, zc_ - 18, zc_ - 10) + box(xl0 + 8, xl1 - 8, ys - 1.5, ys - 1.2, zl0 + 6, zl0 + 12)
    add("Hazard label print", tri + txt, "label", "guard", 16, color=C_INK)
    return out + site()


def site():
    """A filter workshop: the concrete floor slab of an open-sided shed (top at z = 0, 150 mm thick, so it reaches
    below ground), a blockwork back wall 2.6 m behind the press, two steel shed posts on pad footings, a pallet with
    bagged clay mix, an anti-fatigue mat at the press front and a 1.75 m mannequin standing on the floor."""
    out = []
    ctx = lambda n, sh, mat, color=None: out.append(kpart(f"{n} (site)", sh, mat, kind="context", group="context", color=color))  # noqa: E731
    ctx("Workshop floor slab, concrete", box(-3500, 4000, -3500, 3200, -150, 0), "concrete")
    wall = box(-3500, 4000, 2600, 2790, -150, 2400)
    for k in range(1, 12):                                       # block coursing: shallow joints every 200 mm
        wall -= box(-3600, 4100, 2595, 2602, 200 * k - 5, 200 * k + 5)
    ctx("Blockwork back wall", wall, "concrete", "#A8A49C")
    for x_ in (-2600, 3100):
        ctx(f"Shed post at {x_:.0f} mm, SHS 100", Pos(x_, 2450, -400) * __import__("cad_parts").shs(100, 4, 3200), "painted_steel", "#3D4651")
        ctx(f"Post footing at {x_:.0f} mm", box(x_ - 250, x_ + 250, 2200, 2700, -500, -150), "concrete")
    ctx("Pallet, hardwood", break_edges(box(-2100, -1300, 1100, 2300, 0, 100) - box(-2090, -1310, 1110, 2290, 22, 101), 2.0), "hardwood")
    for i in range(2):
        for j in range(3):
            bag = box(-2080 + 390 * i, -1700 + 380 * i - 10, 1130 + 380 * j, 1480 + 380 * j, 100, 260)
            ctx(f"Bag of clay mix {i * 3 + j + 1}", break_edges(bag, 30.0), "canvas")
    mat = box(-300, 300, -560, -385, 0, 12)
    mat = _fillet_try(mat, mat.faces().sort_by(Axis.Z)[-1].edges(), [5.0, 3.0])
    for k in range(8):
        yk = -545 + 20 * k
        mat -= box(-280, 280, yk, yk + 6, 9, 13)
    ctx("Anti-fatigue mat", Pos(0, 0, -5) * mat, "epdm")
    from context_parts import mannequin
    person = Pos(-900, -600, 0) * Rot(0, 0, 90) * mannequin(1750, "stand")    # front left, facing the press
    out.append(kpart("Person 1.75 m (scale)", person, "skin", kind="context", group="context"))
    return out


if __name__ == "__main__":
    ps = product_parts()
    from collections import Counter
    print(len(ps), "parts;", dict(Counter(p["group"] for p in ps)))
