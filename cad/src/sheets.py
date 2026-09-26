"""PotPress general arrangement drawing PPR-DWG-001 (Rev P2).

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

parts = build_parts()
press = press_only(parts)
bb = press.bounding_box()
L = levels()

work = ROOT / "cad/drawings/_views"
views = project_views(press, work)

s = Sheet(project="PotPress", title="General arrangement, press closed", dwg_no="PPR-DWG-001",
          rev="P2", author="Amish Chadha", date="2026-09-25", concept=True, scale=None,
          material="S275 channel and plate; molds cast Al-Si (lead-free scrap); pin 42CrMo4 QT. See bom/bom.csv",
          revisions=[("P1", "Preliminary GA from the TRL 3 model (PPR-CAL-001)", "2026-09-25", "AC"),
                     ("P2", "Recommendations accepted (DDR-002): bolted joints, hinged rails", "2026-09-25", "AC")])
s.add_ortho(views, ["front", "top", "right"])
s.add_svg(views["iso"], 276, 30, 140, 84, label="Isometric view", sublabel="Not to scale; guards not shown")
s.add_notes("Key dimensions (mm) and data", [
    f"Frame {P['BEAM_L']:.0f} x {P['FOOT_L']:.0f} on feet; {P['BEAM_L']:.0f} x {P['RAIL_HINGE'] + P['RAIL_H'] + P['FOOT_L'] / 2:.0f} rails folded",
    f"Rail hinge {P['RAIL_HINGE']:.0f} in front of axis; deployed to {P['RAIL_BACK'] + P['CARRIAGE_OUT']:.0f}",
    f"Height {L['overall']:.0f} to handwheel; loading rim height {L['fm1'] - P['PRESS_TRAVEL']:.0f}",
    f"Uprights at {P['SPAN']:.0f} centers; beams 2 x {P['BEAM_SEC']}, gap {P['BEAM_GAP']:.0f}",
    f"Upright joints bolted, 4 x M{P['JOINT_BOLT_D']:.0f} 8.8 each (16 total)",
    f"Top beam {L['top0']:.0f} to {L['top1']:.0f}; load pin {P['PIN_D']:.0f} dia at {L['pin']:.0f}",
    f"20 t jack, stroke {P['JACK_STROKE']:.0f}; pressing travel {P['PRESS_TRAVEL']:.0f}",
    f"Crank lift {P['CRANK_LIFT']:.0f} (Tr24 x 5, {P['CRANK_LIFT'] / P['LEAD_P']:.0f} turns); open gap {L['open_gap']:.0f}",
    f"Pot: inner rim {2 * P['R_IN_RIM']:.0f}, depth {P['D_IN']:.0f}, wall {P['WALL']:.0f}, rim {P['RIM_OD']:.0f}",
    f"Female mold {P['FM_FLANGE_D']:.0f} dia; male flange {P['MM_FLANGE_D']:.0f} in lip, fit {P['LOC_CLEAR']:.1f}",
    "Frame 190 MPa, pin 258 MPa, bolts 75 MPa at 294 kN",
    "Mold gap deflection 0.6 mm at 10 t, 1.8 mm at 30 t",
    "Press about 298 kg plus bolts; heaviest part 39 kg",
    "Not met at TRL 3: R10 cost ($984 vs $930)",
    "Pin-presence interlock; guards required",
    "PRELIMINARY, NOT FOR FABRICATION",
], x=276, y=130, width=140)
s.save(ROOT / "cad/drawings/PPR-DWG-001")
shutil.rmtree(work, ignore_errors=True)
print("wrote cad/drawings/PPR-DWG-001.svg, .pdf, .png")
