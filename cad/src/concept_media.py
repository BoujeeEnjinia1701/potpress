"""PotPress concept media from the TRL 3 parametric model.

Run from the repo root:  python cad/src/concept_media.py
Geometry comes from cad/src/model.py; the material flow values come from
PPR-CAL-001 (docs/04-calcs/sizing.py). Massing-plus detail; not for fabrication.

Axes: X across the press, Y front (-Y, operator side) to back, Z up. The press is shown
closed at the end of a pressing stroke inside its mesh guards with the front gate closed
(guard mesh drawn at every 8th wire); the 2 x 2 QC flow-test rack stands to the right.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / ".kit"))
sys.path.insert(0, str(ROOT / "cad/src"))
sys.path.insert(0, str(ROOT / "docs/04-calcs"))
from concept import Part, render_all  # noqa: E402
from model import build_parts  # noqa: E402
import sizing  # noqa: E402

g = sizing.geometry()
m = sizing.mix(g)
k = sizing.kinematics(g, m)
c = sizing.cycle(k)

parts = [Part(name, shape, color, bom, explode) for name, shape, color, bom, explode in build_parts()]

render_all(
    parts, project="PotPress", title="Filter press and QC rig concept", dwg_no="PPR-DWG-010",
    date="2026-09-26",
    key_figures=["20 t bottle jack; working force 5 to 10 t (assumed)",
                 "0.5 to 1.05 MPa mean on the pot at 5 to 10 t",
                 f"Filter 280 mm inner rim, 240 mm deep, {g['v_work']:.1f} L working",
                 f"About {m['charge']:.1f} kg mix per pot; about {m['fired']:.1f} kg fired (est.)",
                 f"Cycle about {c['total_min']:.1f} min; about {c['pots_6h']:.0f} pots per 6 h (est.)",
                 "QC: 1.0 to 2.5 L/h in the first hour, at 25 C",
                 "Press 940 x 700 x 1,806 mm guarded, rails folded; about 350 kg (est.)",
                 "Mesh guards; front gate interlocked with the jack release"],
    cut_exclude=("Return springs", "Printed T-gauge"),
    flow={"title": "material flow per filter, mixed charge to passed filter (all values are estimates)", "unit": "kg",
          "stages": [("Mixed charge", round(m["charge"], 1)), ("Pressed pot", round(m["pressed"], 1)),
                     ("Dried pot", round(m["dried"], 1)), ("Fired pot", round(m["fired"], 1)),
                     ("Passes QC", round(m["passed"], 1))],
          "losses": [(0, "Trim, recycled (est.)", round(m["trim"], 1)),
                     (1, "Drying water (est.)", round(m["drying_loss"], 1)),
                     (2, "Firing loss (est.)", round(m["firing_loss"], 1)),
                     (3, "Rejects, 10 % (est.)", round(m["reject"], 1))]},
)
