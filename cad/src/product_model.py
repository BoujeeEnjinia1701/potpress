"""PotPress product appearance model (build123d), TRL 3, constructable design (PPR-DDR-004).

Finished-product look for photoreal renders, built from the constructable model: every component of
cad/src/model.py components() is used as it is (frame, feet with studs and floor-anchor tubes, M16 joint
bolts, jack plate, the bottle jack turned 25 degrees with its pump handle, platen, rails with the folding
extension and tipping pins, carriage with hooks and lift handles, female mold on its steel base plate with
dowels, the open-topped male mold with bushes, stem, load pin, captive nut, crank bracket and handwheel,
the mechanical interlock, the fixed inner shield behind the pump slot, and the QC rack). Only the look is
added: the guard mesh drawn wire by wire at the specified 12.7 mm pitch (model.py draws every 8th wire),
coiled return springs in place of the model's spring envelopes, a polished jack ram, a nameplate and a load
rating label on the top crossbeam, a hazard label on the front right strip, a workshop floor, an
anti-fatigue mat and a 1.75 m mannequin for scale standing beside the press.
APPEARANCE MODEL ONLY: no tolerances, no fabrication detail. CONCEPT, NOT FOR FABRICATION.

Axes as model.py: X across the press, Y front (-Y, operator side) to back, Z up from the floor. The press
is closed at the end of a pressing stroke with the rail extension folded. Groups: "shell" (the press),
"internal" (the pressed pot), "guard" (fixed guards, pump slot shield, interlock, labels on the guards),
"gate_closed" and "gate_open" (the front gate shut or swung open 105 degrees), "accessory" (QC rack) and
"context" (floor, mat, mannequin).

    from product_model import product_parts
    for p in product_parts(): print(p["name"], p["group"], p["material"])
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parents[1] / ".kit")]

from build123d import Axis, Compound, Cylinder, Pos, RegularPolygon, Rot, extrude, fillet  # noqa: E402
from model import (BOM_NAMES, PARAMS, SECTIONS, box, components, cyl, gate_geometry, guard_solids,  # noqa: E402
                   levels)

TITLE = "PotPress: hand-pumped hydraulic press for ceramic pot water filters"

RENDER_VIEWS = [
    {"name": "hero", "groups": ["shell", "guard", "gate_closed", "internal", "context"], "explode": False,
     "el": 30, "az": -40,
     "note": "Product render from the front right and above (about 30 deg elevation); press closed at the end "
             "of a stroke behind welded-mesh guards with the interlocked front gate closed; bottle jack under "
             "the platen with its pump handle out through the shielded slot in the right guard; 1.75 m person "
             "at the front left for scale"},
    {"name": "exploded", "groups": ["shell", "internal"], "explode": True, "el": 28, "az": -55,
     "note": "Exploded view from the front right and above (about 28 deg elevation): base beam and feet, "
             "uprights and joint bolts, bottle jack, springs, platen, rails and carriage, female mold on its "
             "steel base plate, pressed pot, male mold, top crossbeam, male mold slide and handwheel; guards "
             "and gate not shown"},
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
C_MESH = "#6F767F"        # galvanized welded mesh
C_SHIELD = "#8A9099"      # galvanized sheet of the pump slot shield
C_INTERLOCK = "#C62828"
C_UHMW = "#F2F2EE"
C_CLAY = "#B9B4AC"        # mannequin

# Each model component: (display name, colour, material, group). Explode offsets come from BOM_NAMES in model.py.
LOOK = {
    "foot_left": ("Foot, left (UPN 100, web up)", C_FRAME2, "painted", "shell"),
    "foot_right": ("Foot, right (UPN 100, web up)", C_FRAME2, "painted", "shell"),
    "base_beam": ("Base beam (two UPN 160)", C_FRAME2, "painted", "shell"),
    "jack_plate": ("Jack plate with locating blocks", C_FRAME2, "painted", "shell"),
    "jack_plate_bolts": ("Jack plate bolts", C_ZINC, "metal", "shell"),
    "upright_left": ("Upright pair, left", C_FRAME, "painted", "shell"),
    "upright_right": ("Upright pair, right", C_FRAME, "painted", "shell"),
    "tubes_left": ("Spacer tubes, left", C_ZINC, "metal", "shell"),
    "tubes_right": ("Spacer tubes, right", C_ZINC, "metal", "shell"),
    "shims_left": ("Shim packs, left", C_ZINC, "metal", "shell"),
    "shims_right": ("Shim packs, right", C_ZINC, "metal", "shell"),
    "bolts_left": ("Joint bolts M16 10.9, left", C_ZINC, "metal", "shell"),
    "bolts_right": ("Joint bolts M16 10.9, right", C_ZINC, "metal", "shell"),
    "top_beam": ("Top crossbeam with pin doublers", C_FRAME, "painted", "shell"),
    "liners": ("Stem guide liners (UHMW-PE)", C_UHMW, "plastic", "shell"),
    "pump_handle": ("Jack pump handle", C_BLACK, "painted", "shell"),
    "platen": ("Moving platen with guide sleeves", C_PLATEN, "painted", "shell"),
    "rails": ("Rails with end stop", C_RAIL, "metal", "shell"),
    "extension": ("Folding rail extension with tipping pins", C_RAIL, "metal", "shell"),
    "carriage": ("Mold carriage with hooks and lift handles", C_FRAME, "painted", "shell"),
    "retaining_pins": ("Mold retaining pins", C_ZINC, "metal", "shell"),
    "fm_plate": ("Female mold steel base plate", C_FRAME2, "painted", "shell"),
    "fm_cup": ("Female mold (cast aluminum)", C_ALU, "metal", "shell"),
    "loc_pins": ("Locating dowels", C_CHROME, "metal", "shell"),
    "fm_screws": ("Base plate screws", C_ZINC, "metal", "shell"),
    "mm": ("Male mold (cast aluminum, open topped)", C_ALU2, "metal", "shell"),
    "bushes": ("Locating bushes", C_ZINC, "metal", "shell"),
    "stem": ("Male mold stem with adapter disc", C_ACCENT, "painted", "shell"),
    "adapter_bolts": ("Adapter disc bolts", C_ZINC, "metal", "shell"),
    "pin": ("Load pin (42CrMo4)", C_CHROME, "metal", "shell"),
    "nut": ("Lead screw nut (bronze)", C_BRONZE, "metal", "shell"),
    "screw": ("Lead screw, collars and handwheel", C_ACCENT, "painted", "shell"),
    "bracket": ("Crank bracket", C_FRAME, "painted", "shell"),
    "bracket_bolts": ("Crank bracket bolts", C_ZINC, "metal", "shell"),
    "pot": ("Pressed filter pot (green, unfired)", C_GREEN_POT, "clay", "internal"),
    "qc_frame": ("QC rack frame (steel angle)", C_FRAME, "painted", "accessory"),
    "qc_shelves": ("QC rack shelves (plywood)", C_PLY, "wood", "accessory"),
    "test_pots": ("Fired test pots", C_FIRED_POT, "clay", "accessory"),
    "gauge": ("Printed T-gauge (PETG)", C_ACCENT, "plastic", "accessory"),
    "buckets": ("Collection buckets (20 L HDPE)", C_BUCKET, "plastic", "accessory"),
    "water": ("Water in test pot", C_WATER, "clear", "accessory"),
    "pump_shield": ("Pump slot inner shield (galvanized sheet)", C_SHIELD, "metal", "guard"),
    "release": ("Release shaft, lock disc and knob", C_BLACK, "metal", "guard"),
    "lock_post": ("Interlock post with guides", C_INTERLOCK, "painted", "guard"),
    "lock_rod": ("Lock rod", C_ZINC, "metal", "guard"),
    "sliders": ("Interlock sliders", C_INTERLOCK, "painted", "guard"),
    "pin_sensor": ("Pin-presence plunger and cable", C_BLACK, "plastic", "guard"),
}
SKIP = {"anchors", "springs", "jack", "guards", "gate"}      # below the floor, or redrawn for the look below


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


def _comp(shapes):
    return Compound(children=list(shapes))


def product_parts(P=PARAMS):
    L = levels(P)
    b = SECTIONS[P["BEAM_SEC"]]
    g2 = P["BEAM_GAP"] / 2
    comps = {c.key: c for c in components(P)}
    out = []

    def add(name, shape, color, material, bom, group, explode=None):
        if explode is None:
            explode = BOM_NAMES[bom][2] if bom in BOM_NAMES else (0, 0, 0)
        out.append({"name": name, "shape": shape, "color": color, "material": material,
                    "bom": bom, "group": group, "explode": tuple(float(v) for v in explode)})

    # ------------------------------------------------------------ the constructable components as modelled
    for key, c in comps.items():
        if key in SKIP or key not in LOOK:
            continue
        name, col, mat, grp = LOOK[key]
        exp = (0, 0, 300) if key in ("test_pots", "water") else None
        add(name, c.shape, col, mat, c.bom, grp, exp)

    # ------------------------------------------------------------ jack: red body, polished ram
    jack = comps["jack"].shape
    ram_zone = cyl(P["RAM_D"] / 2 + 0.5, L["platen0_low"] - 20, L["platen0"] + 1)
    add("20 t bottle jack body", jack - ram_zone, C_JACK, "painted", 4, "shell")
    add("Jack ram (polished)", jack & ram_zone, C_CHROME, "metal", 4, "shell")

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
    add("Return springs", _comp(coils), C_SPRING, "metal", 6, "shell")

    # ------------------------------------------------------------ nameplate and load rating label on the top beam
    yf = -g2 - b["tw"]
    zc = L["pin"]
    npl = box(-238, -110, yf - 1.2, yf, zc - 32, zc + 32)
    npl = _fillet_try(npl, npl.edges().filter_by(Axis.Y), [4.0, 2.0])
    add("Nameplate", npl, C_ACCENT, "painted", 3, "shell")
    ink = box(-222, -150, yf - 1.5, yf - 1.2, zc + 6, zc + 20) + box(-222, -175, yf - 1.5, yf - 1.2, zc - 6, zc) \
        + box(-222, -130, yf - 1.5, yf - 1.2, zc - 20, zc - 15)
    add("Nameplate print", ink, C_LABEL, "paper", 3, "shell")
    rl = box(110, 238, yf - 0.6, yf, zc - 30, zc + 30)
    add("Load rating label (20 t max)", rl, C_YELLOW, "paper", 3, "shell")
    rink = box(122, 170, yf - 0.9, yf - 0.6, zc + 4, zc + 20) + box(122, 226, yf - 0.9, yf - 0.6, zc - 8, zc - 3) \
        + box(122, 200, yf - 0.9, yf - 0.6, zc - 20, zc - 15)
    add("Load rating label print", rink, C_INK, "paper", 3, "shell")

    # ------------------------------------------------------------ guards with every wire, and the gate shut and open
    gs = guard_solids(P, pitch=P["MESH_PITCH"])
    wire = P["MESH_WIRE"] + 0.01
    thin = lambda s_: min(s_.bounding_box().size.X, s_.bounding_box().size.Y, s_.bounding_box().size.Z) <= wire   # noqa: E731
    mesh = [s_ for s_ in gs if thin(s_) and max(s_.bounding_box().size.X, s_.bounding_box().size.Y,
                                                 s_.bounding_box().size.Z) > 30]
    frames = [s_ for s_ in gs if s_ not in mesh]
    add("Guard frames, standoffs and slot frame (powder-coated)", _comp(frames), C_GUARD, "painted", 16, "guard")
    add("Guard mesh (12.7 mm welded, galvanized)", _comp(mesh), C_MESH, "metal", 16, "guard")
    for state, deg in (("gate_closed", 0.0), ("gate_open", 105.0)):
        gg = gate_geometry(P, pitch=P["MESH_PITCH"], open_deg=deg)
        gmesh = [s_ for s_ in gg if thin(s_)]
        grest = [s_ for s_ in gg if not thin(s_)]
        tag = "" if deg == 0 else ", open"
        add("Front gate frame, hinges, handle and tongue" + tag, _comp(grest), C_GUARD, "painted", 20, state)
        add("Front gate mesh" + tag, _comp(gmesh), C_MESH, "metal", 20, state)

    # hazard label on the front right strip (set back for the interlock), clear of the interlock post
    ys, gx = P["STRIP_Y"], P["GUARD_X"]
    xl0, xl1, zl0, zl1 = P["LOCK_X"] + 16, gx - 22, 1150.0, 1250.0
    lab = box(xl0, xl1, ys - 1.2, ys, zl0, zl1)
    lab = _fillet_try(lab, lab.edges().filter_by(Axis.Y), [4.0, 2.0])
    add("Hazard label (crush, keep gate closed)", lab, C_YELLOW, "paper", 16, "guard")
    xc_ = xl0 + 26; zc_ = (zl0 + zl1) / 2
    tri = Pos(xc_, ys - 1.35, zc_ - 4) * Rot(90, 0, 0) * extrude(RegularPolygon(22, 3, rotation=90), amount=0.3, both=True)
    tri -= Pos(xc_, ys - 1.35, zc_ - 4) * Rot(90, 0, 0) * extrude(RegularPolygon(14, 3, rotation=90), amount=1, both=True)
    tri += box(xc_ - 2.5, xc_ + 2.5, ys - 1.5, ys - 1.2, zc_ - 8, zc_ + 8)
    txt = box(xl0 + 56, xl1 - 8, ys - 1.5, ys - 1.2, zc_ + 14, zc_ + 24) + box(xl0 + 56, xl1 - 20, ys - 1.5, ys - 1.2, zc_ - 2, zc_ + 6) \
        + box(xl0 + 56, xl1 - 14, ys - 1.5, ys - 1.2, zc_ - 18, zc_ - 10) + box(xl0 + 8, xl1 - 8, ys - 1.5, ys - 1.2, zl0 + 6, zl0 + 12)
    add("Hazard label print", tri + txt, C_INK, "paper", 16, "guard")

    # ------------------------------------------------------------ context: floor, mat, 1.75 m person for scale
    slab = box(-1350, 1650, -1000, 500, -20, 0)
    add("Workshop floor (concrete)", slab, C_FLOOR, "paper", None, "context", (0, 0, 0))
    mat = box(-300, 300, -560, -385, 0, 12)
    mat = _fillet_try(mat, mat.faces().sort_by(Axis.Z)[-1].edges(), [5.0, 3.0])
    for k in range(8):
        yk = -545 + 20 * k
        mat -= box(-280, 280, yk, yk + 6, 9, 13)
    add("Anti-fatigue mat", mat, C_RUBBER, "rubber", None, "context", (0, 0, 0))
    from context_parts import mannequin
    # front left of the press, facing it, so the figure does not hide the press or the pump handle
    person = Pos(-900, -600, 0) * Rot(0, 0, 90) * mannequin(1750, "stand")
    add("Person, 1.75 m mannequin (scale)", person, C_CLAY, "clay", None, "context", (0, 0, 0))
    return out


if __name__ == "__main__":
    for p in product_parts():
        s = p["shape"]
        print(f"{p['name']:52s} {p['group']:11s} {p['material']:8s} valid={s.is_valid} vol={s.volume / 1000:9.2f} cm3")
