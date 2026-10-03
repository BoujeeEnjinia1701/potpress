"""PotPress general arrangement drawing PPR-DWG-001 (Rev P6).

Run from the repo root:  python cad/src/sheets.py
Builds cad/drawings/PPR-DWG-001.svg, .pdf and .png from the parametric model.
The concept sheet in media/ uses PPR-DWG-010. Figures in the notes come from
PPR-CAL-001 (python docs/04-calcs/sizing.py).
"""
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / ".kit"))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from drawing import Sheet, project_views  # noqa: E402
from model import PARAMS as P, build_parts, levels, press_only  # noqa: E402

from model import components, pump_handle, box  # noqa: E402
from build123d import Compound  # noqa: E402

# Drawn from the floor up: the floor anchors, which go 80 mm into the concrete, are left out of the views
comps = [c for c in components() if c.key != "anchors"]
parts = build_parts(comps=comps)
press = press_only(parts)
bb = press.bounding_box()
L = levels()

# Floor layout (decided by Amish 2026-10-02): the pump handle's operating space outside the right guard, like a
# door swing, outlined on the floor (2 mm strips at floor level, so it shows in the top view)
hb = Compound(children=[pump_handle(P, z) & box(P["GUARD_X"], 2000, -2000, 2000, 0, 2000)
                        for z in P["HANDLE_STROKE"]]).bounding_box()
ox0, ox1 = P["GUARD_X"], hb.max.X
oy0, oy1 = hb.min.Y - 15, hb.max.Y + 15                         # the handle's plan footprint, 15 mm round it
op_space = Compound(children=[box(ox0, ox1, oy0, oy0 + 2, 0, 2), box(ox0, ox1, oy1 - 2, oy1, 0, 2),
                              box(ox1 - 2, ox1, oy0, oy1, 0, 2)])
op_out = ox1 - P["GUARD_X"]

work = ROOT / "cad/drawings/_views"
views = project_views(Compound(children=[press, op_space]), work)

s = Sheet(project="PotPress", title="General arrangement, press closed, guarded", dwg_no="PPR-DWG-001",
          rev="P6", author="Amish Chadha", date="2026-10-02", concept=True, scale=None,
          material="S275 channel and plate; molds cast Al-Si (lead-free scrap); pin 42CrMo4 QT. See bom/bom.csv",
          revisions=[("P1", "Preliminary GA from the TRL 3 model (PPR-CAL-001)", "2026-09-25", "AC"),
                     ("P2", "Recommendations accepted (DDR-002): bolted joints, hinged rails", "2026-09-25", "AC"),
                     ("P3", "Guards and interlocked front gate added", "2026-09-26", "AC"),
                     ("P4", "Budget raised to $1,060 (DDR-003); R10 met; note only", "2026-09-27", "AC"),
                     ("P5", "Design for construction (DDR-004); cost note removed", "2026-09-30", "AC"),
                     ("P6", "Pump slot shield; handle operating space on the floor", "2026-10-02", "AC")])
s.add_ortho(views, ["front", "top", "right"])
s.add_svg(views["iso"], 276, 50, 140, 68, label="Isometric view", sublabel="Not to scale; mesh drawn at every 8th wire")
s.add_notes("Key dimensions (mm) and data", [
    f"Frame {P['BEAM_L']:.0f} x {P['FOOT_L']:.0f} on feet; guarded 940 x {bb.size.Y:.0f}",
    f"Floor: outline right of guard = pump handle space, {op_out:.0f} x {oy1 - oy0:.0f}",
    f"Pump slot {P['PUMP_SLOT'][0]:.0f} x {P['PUMP_SLOT'][2] - P['PUMP_SLOT'][1]:.0f}; fixed 2 mm sheet tunnel behind it",
    f"Rail hinge {P['RAIL_HINGE']:.0f} in front of axis; deployed to {P['CARRIAGE_OUT'] + P['PIVOT_DY'] + 5:.0f}",
    f"Height {L['overall']:.0f} to handwheel; loading rim height {L['fm1'] - P['PRESS_TRAVEL']:.0f}",
    f"Uprights at {P['SPAN']:.0f} centers, 16 x M{P['JOINT_BOLT_D']:.0f} 10.9, shims; beams 2 x {P['BEAM_SEC']}",
    f"Top beam {L['top0']:.0f} to {L['top1']:.0f}; load pin {P['PIN_D']:.0f} dia at {L['pin']:.0f}",
    f"20 t jack, stroke {P['JACK_STROKE']:.0f}, travel {P['PRESS_TRAVEL']:.0f}; crank lift {P['CRANK_LIFT']:.0f}, open gap {L['open_gap']:.0f}",
    f"Pot: inner rim {2 * P['R_IN_RIM']:.0f}, depth {P['D_IN']:.0f}, wall {P['WALL']:.0f}, rim {P['RIM_OD']:.0f}",
    f"Molds {P['FM_FLANGE_D']:.0f} dia flanges, located by 2 x {P['LOC_PIN_D']:.0f} mm pins",
    f"At 294 kN: frame 190, pin 272, bolts 117, {P['MM_FLANGE_T']:.0f} mm male flange 62 MPa",
    "Press about 344 kg plus about 48 kg of guards; heaviest part 40 kg",
    f"Guards: welded mesh {P['MESH_PITCH']:.1f} x {P['MESH_PITCH']:.1f} x {P['MESH_WIRE']:.1f}, planes {2 * P['GUARD_X']:.0f} x {P['GUARD_Y_BACK'] - P['GUARD_Y_FRONT']:.0f}",
    f"Gate {2 * P['GATE_HALF']:.0f} wide, hinged left; lock rod holds jack release open",
    "PRELIMINARY, NOT FOR FABRICATION",
], x=276, y=130, width=140)
s.save(ROOT / "cad/drawings/PPR-DWG-001")
shutil.rmtree(work, ignore_errors=True)
print("wrote cad/drawings/PPR-DWG-001.svg, .pdf, .png")
