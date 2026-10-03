"""PotPress prototype build plan pictures (PPR-BLD-001, STANDARDS section 18).

Run from the repo root:
    python cad/src/build_plan_media.py                       everything (heavy: better one group per process)
    python cad/src/build_plan_media.py overview
    python cad/src/build_plan_media.py sheets [101 102 ...]
    python cad/src/build_plan_media.py joints [1 2 ...]
    python cad/src/build_plan_media.py steps [1 2 ...]
Every picture is drawn from cad/src/model.py (components(), moved()), so the pictures and the model never disagree:
    docs/05-build-plan/overview.png        every component pulled apart, numbered in build order
    cad/drawings/PPR-DWG-101 to 114        making sketches for the made components
    docs/05-build-plan/joint-NN.png        close-ups of the joints that need explaining
    docs/05-build-plan/step-NN.png         one picture per assembly step
Uses .kit/build_views.py. BUILD PLAN ILLUSTRATION, PLAN NOT YET BUILT.
"""
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / ".kit"), str(ROOT / "cad" / "src")]
import build_views as bv  # noqa: E402
from build_views import Part  # noqa: E402
import model as m  # noqa: E402
from model import PARAMS as P, levels, box  # noqa: E402

OUT = ROOT / "docs" / "05-build-plan"
DWG = ROOT / "cad" / "drawings"
DATE = "2026-10-02"                  # pictures redrawn for the pump slot shield
L = levels()
_C = None


def comps():
    global _C
    if _C is None:
        _C = {c.key: c for c in m.components()}
    return _C


def fuse(*keys, src=None):
    import build123d as b
    src = src or comps()
    return b.Compound(children=[src[k].shape for k in keys])


COL = {"foot": "#374151", "base": "#4B5563", "jplate": "#78716C", "jack": "#B91C1C", "upright": "#6B7280",
       "tube": "#0EA5E9", "shim": "#D97706", "bolt": "#111827", "platen": "#9CA3AF", "spring": "#CA8A04",
       "rails": "#1F2937", "ext": "#475569", "carriage": "#0F766E", "fm": "#CBD5E1", "fplate": "#64748B",
       "pin16": "#DC2626", "mm": "#94A3B8", "bush": "#B45309", "stem": "#0F766E", "pin": "#7C3AED",
       "top": "#4B5563", "liner": "#F5F5F4", "crank": "#0D9488", "screw": "#B45309", "nut": "#92400E",
       "guard": "#CA8A04", "gate": "#EAB308", "lock": "#1D4ED8", "rod": "#2563EB", "slider": "#DC2626",
       "qc": "#A16207", "shelf": "#D6B98C", "bucket": "#2563EB", "gauge": "#F59E0B", "pot": "#C8875A",
       "handle": "#7F1D1D"}


def part(name, shape, color, explode=(0, 0, 0), alpha=1.0):
    return Part(name, shape, color, None, tuple(explode), alpha)


def K(key, name, color, explode=(0, 0, 0)):
    return part(name, comps()[key].shape, color, explode)


def win(shape, x0, x1, y0, y1, z0, z1):
    """The part of a shape inside a box (for close-ups and cut-open views)."""
    import build123d as b
    w = box(x0, x1, y0, y1, z0, z1)
    try:
        sols = list(shape.solids()) or [shape]
    except Exception:
        sols = [shape]
    kept = []
    for s_ in sols:
        bb = s_.bounding_box()
        if bb.max.X < x0 or bb.min.X > x1 or bb.max.Y < y0 or bb.min.Y > y1 or bb.max.Z < z0 or bb.min.Z > z1:
            continue
        r = s_ & w
        if r is not None and r.volume > 1e-3:
            kept.append(r)
    return b.Compound(children=kept) if kept else None


def W(key, name, color, bx, src=None):
    src = src or comps()
    return part(name, win(src[key].shape, *bx), color)


# ----------------------------------------------------------------- named groups, in build order
def groups():
    return [
        ("feet", "Feet (2) and floor anchors", ("foot_left", "foot_right", "anchors"), COL["foot"]),
        ("base", "Base beam", ("base_beam",), COL["base"]),
        ("jplate", "Jack plate and bolts", ("jack_plate", "jack_plate_bolts"), COL["jplate"]),
        ("jack", "Bottle jack and pump handle", ("jack", "pump_handle"), COL["jack"]),
        ("uprights", "Uprights with tubes, shims, bolts", ("upright_left", "upright_right", "tubes_left", "tubes_right",
                                                           "shims_left", "shims_right", "bolts_left", "bolts_right"), COL["upright"]),
        ("platen", "Platen with rails and extension", ("platen", "rails", "extension"), COL["platen"]),
        ("springs", "Return springs (2)", ("springs",), COL["spring"]),
        ("stem", "Stem", ("stem", "nut"), COL["stem"]),
        ("top", "Top crossbeam with guides", ("top_beam", "liners"), COL["top"]),
        ("pin", "Load pin", ("pin",), COL["pin"]),
        ("crank", "Crank bracket, screw, handwheel", ("bracket", "bracket_bolts", "screw"), COL["crank"]),
        ("carriage", "Mold carriage", ("carriage", "retaining_pins"), COL["carriage"]),
        ("fm", "Female mold on its base plate", ("fm_cup", "fm_plate", "loc_pins", "fm_screws"), COL["fm"]),
        ("mm", "Male mold", ("mm", "bushes", "adapter_bolts"), COL["mm"]),
        ("guards", "Fixed mesh guards and pump slot shield", ("guards", "pump_shield"), COL["guard"]),
        ("gate", "Front gate", ("gate",), COL["gate"]),
        ("lock", "Interlock", ("release", "lock_post", "lock_rod", "sliders", "pin_sensor"), COL["lock"]),
        ("qc", "QC rack", ("qc_frame", "qc_shelves"), COL["qc"]),
        ("qcb", "Buckets and T-gauge", ("buckets", "gauge"), COL["bucket"]),
    ]


def G(key, explode=(0, 0, 0), color=None, name=None):
    for k, n, keys, c in groups():
        if k == key:
            return part(name or n, fuse(*keys), color or c, explode)
    raise KeyError(key)


# ----------------------------------------------------------------- overview
def overview():
    # three zones: the fixed frame in the middle, the moving parts pulled out to the front (left in the
    # picture), guards and the QC rack behind (right in the picture)
    F = -1000
    off = {"feet": (0, 0, -700), "base": (0, 0, -450), "jplate": (0, 0, -230), "uprights": (0, 0, 0),
           "top": (0, 0, 520), "crank": (0, 0, 950),
           "jack": (0, F, -420), "platen": (0, F, -120), "springs": (0, F - 450, -150), "carriage": (0, F, 250),
           "fm": (0, F, 420), "mm": (0, F, 700), "stem": (0, F, 900), "pin": (0, F + 300, 700),
           "guards": (0, 1300, 250), "gate": (0, 1300 + 450, 1650), "lock": (700, 1500, 300),
           "qc": (0, 1300, -900), "qcb": (0, 1300, -400)}
    parts = [G(k, off[k]) for k, *_ in groups()]
    return bv.overview(parts, OUT / "overview.png", "PotPress prototype: every component, pulled apart",
                       subtitle="Numbered in build order. Seen from the front right and above; mesh drawn at every 8th wire",
                       elev=14, azim=-35, size=(13, 9), dpi=150, key=True)


# ----------------------------------------------------------------- making sketches
# Sheets revised after their first issue on 2026-09-30: (rev, date, revision rows)
SHEET_REVS = {110: ("P2", "2026-10-02", [("P1", "First issue", "2026-09-30", "AC"),
                                        ("P2", "Pump slot lengthened; fixed inner shield added", "2026-10-02", "AC")])}


def sheet(n, key_or_shape, name, color, neighbours, title, material, notes, view_shape=None, inset=(24, -58)):
    shape = fuse(*key_or_shape) if isinstance(key_or_shape, tuple) else key_or_shape
    rev, date, revs = SHEET_REVS.get(n, ("P1", "2026-09-30", None))
    return bv.component_sheet(part(name, shape, color), neighbours, project="PotPress", dwg_no=f"PPR-DWG-{n}",
                              title=f"PotPress {title}: making sketch", material=material, notes=notes, date=date,
                              rev=rev, revisions=revs, view_shape=view_shape, inset_view=inset, out_dir=str(DWG))


def sheets(which=None):
    import build123d as b
    c = comps()
    out = []
    grey = lambda *ks: [G(k) for k in ks]  # noqa: E731
    S = {}
    S[101] = lambda: sheet(101, c["foot_right"].shape, "Foot", COL["foot"], grey("base", "uprights"),
        "foot (make 2)", "UPN 100 channel, S275; 26.9 x 3.2 mm tube; M12 bolts",
        ["Make two. Cut UPN 100 channel 640 mm long. It lies web up: the flat",
         "  6 mm web on top, the two 50 mm flanges standing on the floor.",
         "Anchor tubes: 14 mm hole through the web 260 mm each side of the middle;",
         "  weld a 26.9 x 3.2 mm tube, 44 mm long, under each hole, floor to web.",
         "Studs: four 13 mm holes in the web, 25 mm each side of the centre line",
         "  (lengthwise) and 88 mm each side of the middle. Put an M12 x 40 bolt",
         "  up through each from below and weld its head under the web.",
         "Fit: the base beam's bottom flanges sit flat on the web; the studs go",
         "  through them, nut and washer on top. The upright stands on the web.",
         "Floor: M12 anchors, 80 mm into concrete, down through the tubes.",
         "Check: the web is flat and the four studs stand square and at",
         "  50 mm and 176 mm spacing."], inset=(20, -60))
    S[102] = lambda: sheet(102, ("base_beam", "jack_plate"), "Base beam and jack plate", COL["base"], grey("feet", "uprights", "jack"),
        "base beam and jack plate", "Two UPN 160 channels 840 mm; plate 20 mm; flat bar 8 mm; S275",
        ["Two UPN 160 channels 840 mm long, webs 104 mm apart (inside faces),",
         "  flanges pointing out. Weld a 10 x 104 x 139 mm block between the webs",
         "  at each end, flush with the ends. The gap takes the uprights plus shims.",
         "Joint holes, 18 mm, through both webs: at 272, 328 (right) and -272, -328",
         "  (left) mm from the middle; 50 and 110 mm up from the beam bottom.",
         "  Drill the two channels clamped together so the holes line up.",
         "Stud holes, 14 mm, in the bottom flanges: 335 and 385 mm each side of",
         "  the middle, 88 mm each side of the centre line.",
         "Spring lugs: 30 x 150 x 8 mm flat bar across the top flanges, 190 mm",
         "  each side of the middle, 12 mm hole in the centre; weld both sides.",
         "Jack plate: 240 x 234 x 20 mm, four 14 mm holes at 105 and 90 mm from",
         "  its middle; bolted across the top flanges with 4 x M12 (matching holes).",
         "  Weld three 10 x 40 x 15 mm blocks round the jack base, 82 mm out, at",
         "  90 degrees; leave the right front open for the release valve.",
         "Check: webs parallel within 1 mm; the uprights slide in with shims."], inset=(28, -55))
    S[103] = lambda: sheet(103, ("upright_right", "tubes_right", "shims_right"), "Upright pair", COL["upright"],
        grey("base", "top", "platen"), "upright pair (make 2)", "Two UPN 100 channels 1,401 mm; 25 x 3 tube; 2 mm sheet; S275",
        ["Make two (drawn lying down). Two UPN 100 channels 1,401 mm, square ends,",
         "  webs back to back, flanges pointing sideways. Stitch weld the two",
         "  web seams, 50 mm welds every 300 mm. The pair is 100 x 100 mm.",
         "Holes, 18 mm, through all four flanges, 28 mm each side of the web",
         "  seam, at 50, 110, 1,291 and 1,351 mm up from the bottom end.",
         "Spacer tubes: 25 x 3 mm tube cut 83 mm long (flange to flange inside),",
         "  eight per pair, slid in from the open side of each channel.",
         "Shims: 2 mm steel, 100 x 120 mm, two 18 mm holes 56 mm apart;",
         "  one each side of each joint (eight per pair); add or thin to suit.",
         "Bolts: M16 x 150 grade 10.9, hardened washer under head and nut.",
         "Fit: the bottom end stands on the foot; the pair sits between the",
         "  beam webs with a shim each side; four bolts per joint through web,",
         "  shim, flange, tube, flange, shim, web.",
         "Check: straight within 1 mm; mass about 29 kg (two people)."], inset=(22, -60),
        view_shape=b.Rot(0, 90, 0) * b.Pos(-300, 0, -750) * fuse("upright_right", "tubes_right", "shims_right"))
    S[104] = lambda: sheet(104, ("top_beam", "liners"), "Top crossbeam", COL["top"], grey("uprights", "stem", "crank"),
        "top crossbeam with doublers and guides", "Two UPN 160 channels 840 mm; 12 mm plate; UHMW-PE; S275",
        ["As the base beam: two UPN 160 channels 840 mm, webs 104 mm apart,",
         "  10 mm end blocks, joint holes 18 mm at 272 and 328 mm each side,",
         "  50 and 110 mm up from the beam bottom.",
         "Doublers: 12 x 200 x 139 mm plate, one on the outside of each web, in",
         "  the middle, 6 mm fillet weld all round.",
         "Pin bore: 62 mm through both webs and doublers, 80 mm up (mid-height).",
         "  Clamp the channels together and cut both with a 62 mm annular cutter",
         "  (hired magnetic drill); weld the end blocks with a 60 mm bar through.",
         "Bracket holes: four 14 mm in the top flanges, 40 mm each side of the",
         "  middle, 100 mm each side of the centre line.",
         "Guides (UHMW-PE): two blocks 29 x 104 x 160 mm, 46 to 75 mm each side",
         "  of the middle; two 6 x 92 x 139 mm strips on the webs with 62 mm",
         "  holes on the pin. Two M6 countersunk screws each, through the web.",
         "Fit: the stem slides between the guides with 1 mm each side.",
         "Check: a 60 mm bar slides through both bores by hand."], inset=(28, -55))
    S[105] = lambda: sheet(105, b.Compound(children=[c["platen"].shape, c["rails"].shape, _ext_deployed()]),
        "Platen with rails", COL["platen"], grey("uprights", "jack", "base"), "moving platen, rails and hinged extension",
        "Two UPN 140 channels 479 mm; 6, 10 and 20 mm plate; 30 x 15 flat bar; S275",
        ["Two UPN 140 channels 479 mm, webs 104 mm apart, flanges out. Deck",
         "  479 x 440 x 6 mm welded on top; jack pad 200 x 104 x 20 mm between",
         "  the webs at the bottom, in the middle (the ram pushes here).",
         "Sleeves: four 10 mm plates each, 121 x 121 mm outside, 150 mm tall,",
         "  welded round a real upright wrapped in 0.5 mm shim, then slid off.",
         "  Weld to the channel ends with the uprights 600 mm apart in a jig,",
         "  sleeve bottom 20 mm below the channels.",
         "Spring lugs: 30 x 160 x 8 mm under the bottom flanges at 190 mm each",
         "  side, 12 mm hole. Rails: four 30 x 15 mm bars 510 mm long, at 60 and",
         "  170 mm each side of the middle, from 290 mm in front of the middle to",
         "  220 mm behind; end stop 400 x 15 x 40 mm across the back.",
         "Extension: four 30 x 15 bars 335 mm on two weld-on barrel hinges under",
         "  the rail ends, with 20 x 30 mm stop lugs; a 12 mm bright steel",
         "  tipping pin sticks out 67 mm at the far end of each outer bar.",
         "Check: slides the full 110 mm on two uprights in a jig; the",
         "  extension, swung out, is level with the rails within 1 mm."], inset=(24, -58))
    S[106] = lambda: sheet(106, ("carriage", "retaining_pins"), "Carriage", COL["carriage"], grey("platen", "fm"),
        "mold carriage", "25 x 12 and 20 x 10 flat bar, 12 mm plate, 10 mm round bar; S275",
        ["Ring: 25 x 12 mm flat bar, 410 mm square outside, 360 mm inside;",
         "  it lies flat on the rails round the female mold's base plate.",
         "Pull handle: 140 x 35 x 12 mm tab at the front, with a 140 x 15 mm",
         "  upright 98 mm tall.",
         "Side lips: 6 x 12 mm bar under the ring, 186 to 192 mm out, along",
         "  the back half; they run 1 mm outside the outer rails.",
         "Tipping hooks: a 12 mm arm from the ring out to 252 mm each side,",
         "  190 mm in front of the middle, and a 40 x 27 x 12 mm plate hanging",
         "  down with a 14 mm tall slot, 23 mm deep, open to the front.",
         "Lift handles: 20 x 10 mm bar bent to a loop 70 mm tall, on the",
         "  ring's outer edge 110 to 180 mm behind the middle.",
         "Retaining pins: 12 mm hole across each side at the middle; a 10 mm",
         "  pin with a T handle goes through into the base plate edge.",
         "Check: slides the full rail length without catching at the hinge."], inset=(30, -55))
    S[107] = lambda: sheet(107, ("fm_cup", "fm_plate", "loc_pins", "fm_screws"), "Female mold", COL["fm"], grey("carriage", "platen"),
        "female mold", "Sand-cast aluminium (lead-free scrap); 15 mm S275 plate; 16 mm dowels",
        ["Cast cup: flange 450 mm dia x 40, cavity the pot's outside (257 mm",
         "  at the floor, 310 mm at the rim, 255 deep), 20 mm shell, 15 mm floor,",
         "  rim counterbore 345 x 15, flash groove to 360 x 3 deep.",
         "Pattern: printed in PLA, flat-back, flange face down on the board;",
         "  the cavity forms its own sand core. Add 1.3 % shrink, 3 mm to",
         "  lap off the flange face and the base, 2 degree draft on the rim.",
         "Finish: lap the flange face (stop ring 360 to 450) flat on abrasive",
         "  paper on float glass; finish the cavity to printed templates.",
         "Base plate: 350 x 350 x 15 mm, four 9 mm countersunk holes on the",
         "  diagonals, 137 mm from the middle; 14 mm holes 20 deep in two edges.",
         "  Bed the cup on steel epoxy putty and hold it with 4 x M8 screws.",
         "Dowels: 16 mm hardened, 50 long, pressed 30 deep at 202 mm each",
         "  side; drilled with the male mold clamped on (see the joint picture).",
         "Check: templates within 0.3 mm; lead-free note from the foundry."], inset=(30, -55))
    S[108] = lambda: sheet(108, ("mm", "bushes"), "Male mold", COL["mm"], grey("fm", "stem"),
        "male mold and its casting pattern", "Sand-cast aluminium (lead-free scrap); 22 mm steel bushes",
        ["Cast plug: 230 mm dia at the tip to 280 at the flange, 240 long; 15",
         "  mm shell, 30 mm tip; flange 450 dia x 45. Open at the top: the",
         "  inside is a cone 206 dia at the floor to 259 at the top (draft 6 deg).",
         "Pattern: printed PLA, flat-back, flange top face down on the board,",
         "  plug pointing up; the inside forms its own sand core, so no core",
         "  box. Add 1.3 % shrink, 3 mm to lap off the flange underside,",
         "  2 degree draft on the flange rim. Print in 8 segments, glue, seal.",
         "Finish: lap the flange underside flat; plug to printed templates.",
         "Bushes: 22 mm holes through the flange at 202 mm each side, steel",
         "  bushes 22 x 16 x 45 set in retaining compound; 16 mm bore reamed.",
         "Floor: four M12 holes (drill 10.2, tap 20 deep) at 75 mm from the",
         "  middle, square to the axes, for the stem's adapter disc.",
         "Check: plug to templates within 0.3 mm; bushes slide on the dowels."], inset=(28, -50))
    S[109] = lambda: sheet(109, ("stem", "nut", "pin", "bracket", "screw"), "Stem, pin and crank", COL["stem"], grey("top", "mm"),
        "male mold slide: stem, load pin and crank", "SHS 90 x 90 x 8; 42CrMo4 bar; 10 and 15 mm plate; Tr24 x 5 screw",
        ["Stem: SHS 90 x 90 x 8, 670 mm, welded square on a 190 x 20 mm disc with",
         "  four 13 mm holes at 75 mm. Pin block 74 x 74 x 120 mm inside, centre",
         "  530 mm up; bore 62 mm across it, then a 28 mm hole down its middle.",
         "Nut box: captive Tr24 nut (60 x 60 x 40) under a 10 mm cap plate",
         "  (26 mm hole), a 10 mm floor with a 28 mm hole 8 mm below the nut.",
         "  The nut lifts the stem by the cap; the 8 mm gap is the float.",
         "Load pin: 60 mm 42CrMo4, quenched and tempered, 173 mm shank, 80 x 12",
         "  mm head turned on, pull knob, 6 mm hole for the R-clip. Do not weld it.",
         "Bracket: 200 x 240 x 10 mm base with a 100 mm square hole and four",
         "  14 mm holes; two 10 mm side plates 270 tall at 80 mm each side; a",
         "  200 x 160 x 15 top with a 26 mm hole. Bolted to the top beam, 4 x M12.",
         "Screw: Tr24 x 5, about 360 mm, held by two collars at the top plate,",
         "  260 mm handwheel with a crank knob. 40 turns lift the mold 200 mm.",
         "Check: the pin slides through beam and stem together by hand."], inset=(20, -55))
    S[110] = lambda: sheet(110, _right_guard(), "Right side guard", COL["guard"], grey("uprights", "base", "top", "jack"),
        "fixed mesh guards (right side guard drawn)", "Galvanised welded mesh 12.7 x 12.7 x 1.6 mm; 25 x 25 x 3 angle; 2 mm steel sheet (shield)",
        ["Seven panels, each mesh on a welded frame of 25 x 25 x 3 angle:",
         "  sides 635 (right) and 675 (left) x 1,391 mm; rear 940 x 1,391;",
         "  front strips 180 x 1,391; lower front 580 x 320; roof 940 x 675",
         "  with a cut-out round the top beam. Mesh drawn at every 8th wire.",
         "Pump slot (right side): 30 x 272 mm, 174 to 446 mm up, centred 218 mm",
         "  in front of the middle; frame it with 3 mm strip. No brush strip.",
         "Shield behind the slot: 2 mm sheet folded into a tunnel 30 mm wide",
         "  inside, along the pump handle's line to 3 mm off the jack body; roof",
         "  and floor 25 mm clear of the handle at both ends of its stroke. A",
         "  3 mm flange bolts through the slot frame (4 x M8); a 30 x 6 mm stay",
         "  bolts to the base beam. The handle goes in through slot and tunnel.",
         "Interlock holes (front right strip): 44 mm square at the release",
         "  shaft and a 40 mm square for the pin cable.",
         "Fixing mesh: clamp it under bolted flat strips, or grind the zinc",
         "  off before welding (fume: see safety stops).",
         "Standoffs: eight 40 x 6 mm flat bars bolted to the beam webs; the",
         "  side panels bolt to them. Panels bolt to each other with M8.",
         "Right front strip sits 40 mm back to leave a pocket for the interlock.",
         "Check: flat within 3 mm; no panel over about 10 kg."], inset=(18, -40))
    S[111] = lambda: sheet(111, ("gate",), "Front gate", COL["gate"], grey("guards", "lock"),
        "front gate", "20 x 20 x 2 square tube; welded mesh; lift-off hinges",
        ["Frame: 20 x 20 x 2 square tube, 572 wide x 1,063 tall outside, with a",
         "  mid rail. Weld square; diagonals equal within 2 mm.",
         "Mesh: the same welded mesh, clamped or welded on the front face.",
         "Hinges: two weld-on lift-off hinges on the left, 120 mm in from the",
         "  top and bottom; the fixed leaves weld to the left front strip frame.",
         "Handle: bent 15 x 12 mm bar, 140 mm grip, near the right edge at",
         "  905 mm up.",
         "Tongue: an arm off the right-hand post and a 6 mm plate reaching",
         "  over the lock rod, with a 14 mm hole centred on the rod.",
         "Fit: the gate closes in the opening between 380 and 1,451 mm up;",
         "  the lower 320 mm is the fixed lower front panel.",
         "Opens outward to the left, about 105 degrees.",
         "Check: swings without touching the folded rail extension; the",
         "  tongue hole drops over the rod top without forcing."], inset=(18, -65))
    S[112] = lambda: sheet(112, ("release", "lock_post", "lock_rod", "sliders"), "Interlock", COL["lock"], grey("jack", "gate"),
        "gate and pin interlock round the jack release", "12 mm bar, 20 x 8 flat bar, 6 mm plate, bought universal joints",
        ["Release shaft: a coupling that fits the jack's release screw, a 12 mm",
         "  shaft out to the right front with two universal joints, then",
         "  straight forward through the guard to a 60 mm knob outside.",
         "Lock disc: 80 mm dia x 6 mm on the shaft just behind the knob, with",
         "  one notch 12.5 wide x 15.5 deep, 120 degrees round from the top",
         "  (check the angle against the jack you buy: open about 1/3 turn).",
         "Post: 20 x 8 mm flat bar from 60 to 1,451 mm up, bolted to the right",
         "  front strip frame, 330 mm right of the middle, with guide tabs.",
         "Lock rod: 12 mm bar standing on the disc rim, a lift handle at 680 mm",
         "  and a 24 mm collar. Valve open: the rod drops 15 mm into the notch.",
         "Gate slider: rides over the rod top when the gate is open; the",
         "  closing gate tongue pushes it back. Pin slider: blocks the collar",
         "  until the pin-presence plunger pulls it aside by its cable.",
         "Result: the valve closes only with the gate shut and the pin home;",
         "  with the valve closed the rod stands through the gate tongue.",
         "Views: the lower end only; the upper end is in the gate joint picture."], inset=(15, -40),
        view_shape=win(fuse("release", "lock_post", "lock_rod"), 90, 420, -400, -30, 190, 345))
    S[113] = lambda: sheet(113, ("qc_frame", "qc_shelves"), "QC rack", COL["qc"], [G("qcb")] + [part("Test pots", c["test_pots"].shape, "#9CA3AF")],
        "QC flow-test rack (2 x 2)", "40 x 40 x 4 steel angle; 18 mm exterior plywood",
        ["Legs: four 40 x 40 x 4 angle, 702 mm, one at each corner.",
         "Frames: two squares of 40 x 40 x 4 angle, 780 x 780 mm outside, one",
         "  under each shelf, horizontal leg flat under the plywood; weld the",
         "  legs inside the corners.",
         "Pot shelf: 18 mm plywood 780 x 780 mm, top 720 mm up; four 316 mm",
         "  holes at 390 mm pitch (195 mm in from each edge). The pot rims",
         "  (345 mm) rest on it; the pots hang through.",
         "Bucket shelf: 18 mm plywood, top 120 mm up, notched round the legs.",
         "Buckets: 20 L, 300 mm dia, no more than 330 mm tall, so they clear the",
         "  hanging pots by 35 mm.",
         "Seal the plywood; stand the rack level on a drained floor.",
         "Check: a 345 mm rim bears at least 14 mm all round each hole."], inset=(28, -55))
    S[114] = lambda: sheet(114, ("gauge",), "T-gauge", COL["gauge"], [part("Test pot", win(c["test_pots"].shape, 780, 1130, -370, -20, 400, 800), "#9CA3AF")],
        "printed T-gauge (make 4)", "PETG, 3D printed",
        ["Crossbar 340 x 12 x 12 mm; it rests across the pot rim.",
         "Stem 8 x 8 mm, 100 mm long below the rim, with the scale in liters",
         "  generated from the filter shape: 0.1 L about every 1.7 mm,",
         "  1.0 L at 16.7 mm, 2.5 L at 42.6 mm below the rim.",
         "Print the crossbar on the diagonal of a 250 mm bed, or in two",
         "  halves glued; print the scale in a second colour.",
         "Check: pour 1.0 L of water from a full, soaked pot; the level",
         "  reads 16.7 mm within 1 mm."], inset=(30, -50))
    for n in sorted(S):
        if which and n not in which:
            continue
        out.append(S[n]())
        print("sheet", n, "->", out[-1], flush=True)
    return out


def _ext_deployed():
    import build123d as b
    y_h = -P["RAIL_HINGE"]
    return b.Pos(0, y_h, L["deck1"]) * b.Rot(-90, 0, 0) * b.Pos(0, -y_h, -L["deck1"]) * comps()["extension"].shape


def _right_guard():
    """The right side guard panel on its own (mesh, angle frame and slot frame), from the guard compound."""
    import build123d as b
    g = comps()["guards"].shape
    kept = [s for s in g.solids() if s.bounding_box().min.X > P["GUARD_X"] - 40 and s.bounding_box().min.Y > P["STRIP_Y"] - 5]
    return b.Compound(children=kept + [comps()["pump_shield"].shape])


# ----------------------------------------------------------------- joints
def joints(which=None):
    import build123d as b
    c = comps()
    out = []
    J = {}
    zb = (L["base0"] + L["base1"]) / 2
    # 1 upright bolted into the base beam, cut through the outer bolt line
    bx = (236, 328, -130, 130, zb - 75, zb + 75)
    J[1] = lambda bx=bx: bv.joint([W("base_beam", "Base beam (two channels)", COL["base"], bx),
                             W("upright_right", "Upright pair", COL["upright"], bx),
                             W("tubes_right", "Spacer tube, inside the upright", COL["tube"], bx),
                             W("shims_right", "2 mm shims, both sides", COL["shim"], bx),
                             W("bolts_right", "M16 10.9 bolts, washers, nuts", COL["bolt"], bx),
                             W("foot_right", "Foot", COL["foot"], bx)],
                            OUT / "joint-01.png", "Joint 1: upright bolted into the base beam (right side, cut open on a bolt line)",
                            subtitle="Four M16 bolts pass web, shim, flange, spacer tube, flange, shim, web. The top joint is the same",
                            elev=18, azim=-25, size=(8.5, 6))
    # 2 load pin through the doublers, webs, guides and stem, cut on the pin axis
    bx = (-120, 0, -240, 140, L["top0"] - 30, L["top1"] + 60)
    J[2] = lambda bx=bx: bv.joint([W("top_beam", "Top beam web and doubler", COL["top"], bx),
                             W("liners", "Plastic guides", COL["liner"], bx),
                             W("stem", "Stem with pin block", COL["stem"], bx),
                             W("pin", "Load pin, 60 mm", COL["pin"], bx),
                             W("pin_sensor", "Pin-presence plunger", COL["slider"], bx)],
                            OUT / "joint-02.png", "Joint 2: the load pin through the top beam and the stem (cut on the pin's axis)",
                            subtitle="Seen from the right. The pin passes doubler, web, guide strip, stem wall, pin block and out the other side",
                            elev=12, azim=-10, size=(8.5, 6))
    # 3 mold location: dowel in the female flange, bush in the male flange
    bx = (135, 245, 0, 60, L["fm1"] - 70, L["mm1"] + 25)
    J[3] = lambda bx=bx: bv.joint([W("fm_cup", "Female mold flange", COL["fm"], bx),
                             W("loc_pins", "16 mm dowel, pressed in", COL["pin16"], bx),
                             W("mm", "Male mold flange", COL["mm"], bx),
                             W("bushes", "Steel bush, reamed 16 mm", COL["bush"], bx),
                             W("pot", "Pot rim", COL["pot"], bx)],
                            OUT / "joint-03.png", "Joint 3: how the molds locate (right dowel, cut through its centre)",
                            subtitle="Seen from the front. The flanges meet on the lapped stop ring; the dowel in its bush keeps the wall even",
                            elev=12, azim=-80, size=(8.5, 6))
    # 4 jack seat
    bx = (-140, 140, -130, 130, L["base1"] - 30, L["jack0"] + 90)
    J[4] = lambda bx=bx: bv.joint([W("base_beam", "Base beam top flanges", COL["base"], bx),
                             W("jack_plate", "Jack plate with three locating blocks", COL["jplate"], bx),
                             W("jack_plate_bolts", "M12 bolts (4)", COL["bolt"], bx),
                             W("jack", "Jack base", COL["jack"], bx)],
                            OUT / "joint-04.png", "Joint 4: the jack seat",
                            subtitle="The plate bridges the beam's two top flanges; the blocks stop the jack turning; the right front is open",
                            elev=40, azim=-60, size=(8.5, 6))
    # 5 interlock, lower: release shaft, lock disc and rod
    zr = m.release_z()
    bx = (270, 400, -366, -340, zr - 60, zr + 100)
    J[5] = lambda bx=bx: bv.joint([W("release", "Release shaft, lock disc, knob", COL["lock"], bx),
                             W("lock_rod", "Lock rod, resting on the disc", COL["rod"], bx),
                             W("lock_post", "Guide tab on the post", "#1E3A8A", bx)],
                            OUT / "joint-05.png", "Joint 5: interlock at the release valve (valve closed; seen from behind the disc)",
                            subtitle="Turn the knob a third of a turn to open: the notch comes to the top and the rod drops into it, locking the valve open",
                            elev=8, azim=95, size=(8.5, 6))
    # 6 interlock, upper: gate tongue, sliders, collar
    bx = (250, 420, -392, -300, 720, 935)
    J[6] = lambda bx=bx: bv.joint([W("lock_rod", "Lock rod and collar", COL["rod"], bx),
                             W("sliders", "Gate slider and pin slider", COL["slider"], bx),
                             W("gate", "Gate tongue", COL["gate"], bx),
                             W("lock_post", "Post with guide tabs", "#1E3A8A", bx),
                             W("pin_sensor", "Cable from the pin plunger", "#7F1D1D", bx)],
                            OUT / "joint-06.png", "Joint 6: interlock at the gate (gate shut, valve closed, rod up)",
                            subtitle="The rod stands through the tongue, so the gate stays shut until the valve is opened",
                            elev=22, azim=-55, size=(8.5, 6))
    # 7 foot and base beam
    bx = (300, 425, -330, -40, -20, 95)
    J[7] = lambda bx=bx: bv.joint([W("foot_right", "Foot, web up", COL["foot"], bx),
                             W("base_beam", "Base beam bottom flange", COL["base"], bx),
                             W("anchors", "M12 floor anchor", COL["bolt"], bx)],
                            OUT / "joint-07.png", "Joint 7: base beam on a foot (right front corner)",
                            subtitle="Studs welded under the foot's web pass up through the beam flange; the anchor goes down its tube",
                            elev=25, azim=-60, size=(8.5, 6))
    # 8 carriage hook on the tipping pin, set for demolding
    J[8] = lambda: _joint_hook()
    # 9 lead screw nut and float, cut on the axis
    bx = (-80, 0, -60, 60, L["stem1"] - 75, L["stem1"] + 25)
    J[9] = lambda bx=bx: bv.joint([W("stem", "Stem top: nut box floor and cap plate", COL["stem"], bx),
                             W("nut", "Captive nut", COL["nut"], bx),
                             W("screw", "Lead screw", COL["screw"], bx)],
                            OUT / "joint-09.png", "Joint 9: lead screw nut and its 8 mm float (cut on the axis)",
                            subtitle="Cranking up, the nut lifts the cap plate. Pressing, the stem rides up on the pin and the nut stays free",
                            elev=10, azim=-10, size=(8.5, 6))
    # 10 male mold on the stem adapter disc, cut on the axis
    bx = (0, 150, 0, 150, L["tip"] - 10, L["stem0"] + 60)
    J[10] = lambda bx=bx: bv.joint([W("mm", "Male mold floor", COL["mm"], bx),
                              W("stem", "Adapter disc and stem", COL["stem"], bx),
                              W("adapter_bolts", "M12 bolts into the floor", COL["bolt"], bx)],
                             OUT / "joint-10.png", "Joint 10: stem to male mold (cut on the axis)",
                             subtitle="The disc is bedded on steel epoxy putty on the mold floor and held by four M12 bolts",
                             elev=15, azim=-125, size=(8.5, 6))
    # 11 pump handle through the guard slot
    J[11] = lambda: _joint_shield()
    for n in sorted(J):
        if which and n not in which:
            continue
        out.append(J[n]())
        print("joint", n, "->", out[-1], flush=True)
    return out


def _joint_shield():
    """Joint 11: the pump handle through the slot and the fixed inner shield, cut along the handle's line."""
    import build123d as b
    c = comps()
    py = m.pump_slot_y()
    half = b.Rot(0, 0, P["JACK_TURN"]) * box(-1000, 1000, 0, 1000, 0, 1000)      # keep the back half of the tunnel
    shield = c["pump_shield"].shape & half
    gw = win(c["guards"].shape, 440, 480, py - 90, py + 90, 120, 500)
    jw = win(c["jack"].shape, -100, 200, -150, 100, L["jack0"], L["jack0"] + 150)
    return bv.joint([part("Right side guard and slot frame", gw, COL["guard"]),
                     part("Shield, cut along the handle", shield, "#64748B"),
                     part("Pump handle, 20 mm", c["pump_handle"].shape, COL["handle"]),
                     part("Jack, pump socket end", jw, COL["jack"])],
                    OUT / "joint-11.png", "Joint 11: pump handle, slot and the fixed shield behind it (shield cut along the handle)",
                    subtitle="30 x 272 mm slot; a 2 mm steel tunnel round the handle to 3 mm off the jack body: 5 mm each side, 25 mm above and below at the stroke ends",
                    elev=20, azim=-75, size=(8.5, 6))


def _joint_hook():
    mc = {c.key: c for c in m.moved(list(comps().values()), "demold")}
    zp = L["deck1"] + 7 - P["PRESS_TRAVEL"]; yp = -(P["CARRIAGE_OUT"] + P["PIVOT_DY"])
    bx = (150, 262, yp - 60, yp + 60, zp - 40, zp + 50)
    return bv.joint([W("extension", "Rail extension (swung out) and tipping pin", COL["ext"], bx, src=mc),
                     W("carriage", "Carriage hook", COL["carriage"], bx, src=mc)],
                    OUT / "joint-08.png", "Joint 8: carriage hook on the tipping pin (carriage pulled out, right side)",
                    subtitle="The slot slides onto the pin; lifting the handles tips the mold forward about the pin",
                    elev=15, azim=-30, size=(8.5, 6))


# ----------------------------------------------------------------- assembly steps
def steps(which=None):
    out = []
    ctx = []
    E = {}

    def st(n, done, new, title, sub, **kw):
        out.append(bv.step(done, new, OUT / f"step-{n:02d}.png", f"Step {n}: {title}", subtitle=sub, **kw))
        print("step", n, "->", out[-1], flush=True)

    c = comps()
    feet, base, jpl = G("feet"), G("base"), G("jplate")
    jack = K("jack", "Jack", COL["jack"])
    upr = G("uprights")
    plat, spr = G("platen"), G("springs")
    stem, top, pin, crank = G("stem"), G("top"), G("pin"), G("crank")
    car, fm, mm = G("carriage"), G("fm"), G("mm")
    guards, gate, lock = G("guards"), G("gate"), G("lock")
    handle = K("pump_handle", "Pump handle", COL["handle"])

    def mv(p, e, name=None):
        return part(name or p.name, p.shape, p.color, e)

    import build123d as b
    dz = P["PRESS_TRAVEL"]
    down = lambda p_, name=None: part(name or p_.name, b.Pos(0, 0, -dz) * p_.shape, p_.color)  # noqa: E731
    jack_low = part("Jack (ram down)", c["jack"].shape - box(-200, 200, -200, 200, L["platen0_low"], L["platen0"] + 10), COL["jack"])
    spr_low = part("Return springs (2)", win(c["springs"].shape, -300, 300, -50, 50, 0, L["platen0_low"]), COL["spring"])
    plat_low, car_low, fm_low, mm_low = down(plat), down(car), down(fm), down(mm)
    frame1 = [feet, base, jpl, jack_low, upr]
    E[3] = lambda: st(3, [feet, base], [mv(jpl, (0, 0, 120)), mv(jack_low, (0, -300, 200), "Jack")], "jack plate and jack",
                      "Plate on with four M12 bolts; stand the jack in the blocks, pump socket and release valve to the right front",
                      elev=30, azim=-55)
    E[4] = lambda: st(4, [feet, base, jpl, jack_low],
                      [mv(K("upright_left", "Left upright", COL["upright"]), (0, 0, 350)),
                       mv(K("upright_right", "Right upright", COL["upright"]), (0, 0, 350)),
                       mv(part("Shims, tubes and M16 bolts", fuse("shims_left", "shims_right", "tubes_left", "tubes_right",
                                                                  "bolts_left", "bolts_right"), COL["shim"]), (0, -250, 0))],
                      "uprights into the base beam",
                      "Drop each pair between the webs onto its foot; shims both sides; tubes inside; four bolts, snug. Prop plumb",
                      elev=22, azim=-55, label_done=False)
    E[5] = lambda: st(5, frame1, [mv(plat_low, (0, 0, 800))], "platen over the uprights",
                      "Lift with a hoist; lower the sleeves over the upright tops until the jack pad rests on the ram",
                      elev=22, azim=-55, label_done=False)
    E[6] = lambda: st(6, frame1 + [plat_low], [mv(spr_low, (0, -250, 0))], "return springs",
                      "Hook each spring into the lug on the base beam and the lug under the platen",
                      elev=15, azim=-40, label_done=False)
    stem_low = part("Stem, standing on the rails", b.Pos(0, 0, L["rail1"] - dz - L["adapter0"]) * stem.shape, COL["stem"])
    E[7] = lambda: st(7, frame1 + [plat_low, spr_low], [mv(stem_low, (0, 0, 300))], "stand the stem on the rails",
                      "Platen down on the jack; stand the stem upright in the middle of the rails, disc down; tie it to an upright",
                      elev=22, azim=-55, label_done=False)
    E[8] = lambda: st(8, frame1 + [plat_low, spr_low, stem_low], [mv(top, (0, 0, 450))], "top crossbeam onto the uprights",
                      "Hoist it level and lower it over the upright tops and the stem top; shims, tubes and four M16 bolts each side",
                      elev=22, azim=-55, label_done=False)
    frame2 = frame1 + [plat_low, spr_low, top]
    lifted = L["adapter0"] - (L["rail1"] - dz)
    E[9] = lambda: st(9, frame2, [mv(stem, (0, 0, -lifted)), mv(pin, (0, -260, 0)), mv(crank, (0, 0, 300))],
                      "lift the stem, pin it, fit the crank",
                      f"Lift the stem {lifted:.0f} mm, push the pin through, bolt on the bracket, wind the screw into the nut. Then park the pin and crank to the top",
                      elev=22, azim=-55, label_done=False)
    frame3 = frame2 + [stem, pin, crank]
    yo = -P["CARRIAGE_OUT"]
    shift = lambda p_, name=None: part(name or p_.name, b.Pos(0, yo, -dz) * p_.shape, p_.color)  # noqa: E731
    stem_up = part("Stem, cranked up", b.Pos(0, 0, P["CRANK_LIFT"]) * stem.shape, COL["stem"])
    pin_park = part("Load pin, parked", b.Pos(0, -m.PIN_PARK, 0) * pin.shape, COL["pin"])
    plat_out = part("Platen, extension swung out", b.Pos(0, 0, -dz) * b.Compound(children=[c["platen"].shape, c["rails"].shape, _ext_deployed()]), COL["platen"])
    frame3o = [feet, base, jpl, jack_low, upr, plat_out, spr_low, top, stem_up, pin_park, crank]
    car_out, fm_out, mm_out = shift(car), shift(fm), shift(mm)
    E[10] = lambda: st(10, frame3o, [mv(car_out, (0, -150, 150)), mv(fm_out, (0, 0, 350))], "carriage and female mold, out on the extension",
                       "Swing the extension out; slide the carriage onto it against the tipping pins; lift the mold in; retaining pins in",
                       elev=22, azim=-55, label_done=False)
    E[11] = lambda: st(11, frame3o + [car_out, fm_out], [mv(mm_out, (0, 0, 350))], "male mold onto the female mold",
                       "Two people, 23 kg: lower it onto the dowels until the flanges meet. No pot, no clay",
                       elev=22, azim=-55, label_done=False)
    E[12] = lambda: st(12, frame3o, [part("Carriage with both molds", b.Pos(0, 0, -dz) * b.Compound(children=[car.shape, fm.shape, mm.shape]),
                                          COL["mm"], (0, yo, 0))],
                       "slide the molds in, crank down, pin",
                       "Push the pair in to the end stop and fold the extension; crank the stem down 200 mm and push the pin home",
                       elev=22, azim=-55, label_done=False)
    up = lambda p_: part(p_.name, p_.shape, p_.color, (0, 0, -dz))  # noqa: E731
    E[13] = lambda: st(13, [feet, base, jpl, upr, top, stem, pin, crank],
                       [up(part("Platen, carriage and both molds", b.Compound(children=[plat.shape, car.shape, fm.shape, mm.shape]), COL["mm"])),
                        part("Jack, ram rising", c["jack"].shape, COL["jack"]), spr],
                       "jack up and bolt the male mold to the stem",
                       "Putty on the mold floor; pump slowly until the floor meets the disc; four M12 bolts from above. Hold point",
                       elev=22, azim=-55, label_done=False)
    frame4 = [feet, base, jpl, jack, upr, plat, spr, top, stem, pin, crank, car, fm, mm]
    E[14] = lambda: st(14, frame4, [part("Fixed mesh guards", fuse("guards"), COL["guard"]),
                                    K("pump_shield", "Pump slot shield", "#64748B", (420, 0, 0))], "fixed guards and pump slot shield",
                       "Standoffs on the beam webs; side, rear, front strips, lower panel and roof; M8 bolts at every corner; shield bolted behind the slot",
                       elev=22, azim=-55, label_done=False)
    E[15] = lambda: st(15, frame4 + [guards], [mv(gate, (0, -350, 0))], "front gate",
                       "Weld the fixed hinge leaves on the left front strip; lift the gate onto its hinges; check it swings clear",
                       elev=22, azim=-55, label_done=False)
    E[16] = lambda: st(16, frame4 + [guards, gate], [mv(lock, (250, -300, 0)), mv(handle, (300, -150, 0))],
                       "interlock and pump handle",
                       "Coupling on the release screw, shaft, disc and knob; post, rod, sliders; plunger and cable; handle in through the slot and shield",
                       elev=22, azim=-55, label_done=False)
    qc = G("qc"); qcb = G("qcb")
    E[17] = lambda: st(17, [], [mv(part("QC rack frame", c["qc_frame"].shape, COL["qc"]), (0, 0, 0)),
                                mv(part("Plywood shelves", c["qc_shelves"].shape, COL["shelf"]), (0, 0, 250))],
                       "QC rack", "Weld the angle frame; drop in the shelves; seal the plywood; level on a drained floor",
                       elev=25, azim=-55)
    E[18] = lambda: st(18, [qc], [mv(part("Buckets (4)", c["buckets"].shape, COL["bucket"]), (0, -700, 0)),
                                  mv(part("Test pots", c["test_pots"].shape, COL["pot"]), (0, 0, 500)),
                                  mv(part("T-gauge", c["gauge"].shape, COL["gauge"]), (0, 0, 900))],
                       "buckets, pots and gauge",
                       "Buckets on the lower shelf under each hole; pots hang by their rims; the gauge rests across a rim",
                       elev=25, azim=-55)
    for n in sorted(E):
        if which and n not in which:
            continue
        E[n]()
    return out


if __name__ == "__main__":
    args = sys.argv[1:] or ["overview", "sheets", "joints", "steps"]
    what, nums = args[0], [int(a) for a in args[1:]]
    if what == "overview":
        print("overview ->", overview())
    elif what == "sheets":
        sheets(nums or None)
    elif what == "joints":
        joints(nums or None)
    elif what == "steps":
        steps(nums or None)
    else:
        for w in args:
            {"overview": overview, "sheets": sheets, "joints": joints, "steps": steps}[w]()
