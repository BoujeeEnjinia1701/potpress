"""PotPress concept media from the TRL 3 parametric model (constructable design, PPR-DDR-004).

Run from the repo root:  python cad/src/concept_media.py [hero|cutaway|exploded|flow|web|blueprint ...]
With no argument it draws everything, but on a small machine run one picture per process (each
one rebuilds the model and frees its memory when the process ends). Geometry comes from
cad/src/model.py; the material flow values come from PPR-CAL-001 (docs/04-calcs/sizing.py).
The pictures are made with the pieces of .kit/concept.py render_all, one at a time.

Axes: X across the press, Y front (-Y, operator side) to back, Z up. The press is shown
closed at the end of a pressing stroke inside its mesh guards with the front gate closed
(guard mesh drawn at every 8th wire); the 2 x 2 QC flow-test rack stands to the right. The
cutaway leaves the guards and gate out so the frame, molds and slide can be seen.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / ".kit"))
sys.path.insert(0, str(ROOT / "cad/src"))
sys.path.insert(0, str(ROOT / "docs/04-calcs"))
import concept as K  # noqa: E402
from concept import Part  # noqa: E402
from model import build_parts, components  # noqa: E402

PROJECT, TITLE, DWG, DATE = "PotPress", "Filter press and QC rig concept", "PPR-DWG-010", "2026-09-30"
MD = ROOT / "media"
NO_CUT = ("Return springs", "Printed T-gauge", "Fixed mesh guards (sides, back, front strips, roof)",
          "Front gate, mesh in a tube frame, with hinges and tongue")


def parts():
    # Floor anchors go into the concrete; they are left out so the press stands on the floor line
    return [Part(name, shape, color, bom, explode)
            for name, shape, color, bom, explode in build_parts(comps=[c for c in components() if c.key != "anchors"])]


def hero():
    ps = parts()
    return K._render(K.with_scale_figure(ps), MD / "hero.png", title=PROJECT,
                     note="Seen from the front right and above, 24 deg elevation. Grey figure: 1.75 m person for scale")


def cutaway():
    ps = [p for p in parts() if p.name not in NO_CUT]
    return K._render(K.cutaway_parts(ps), MD / "cutaway.png", azim=-90, elev=18, title=f"{PROJECT}: cutaway",
                     note="Front half removed, guards and gate left out; seen from the front and above, 18 deg elevation")


def exploded():
    return K._render(parts(), MD / "exploded.png", offsets=True, labels=True, title=f"{PROJECT}: exploded view",
                     note="Seen from the front right and above, 24 deg elevation; numbers match bom/bom.csv")


def web():
    return K.export_web_model(parts(), "media", title=f"{PROJECT}: {TITLE}")


def flow():
    import sizing
    g = sizing.geometry(); m = sizing.mix(g)
    return K.flow_diagram(
        [("Mixed charge", round(m["charge"], 1)), ("Pressed pot", round(m["pressed"], 1)), ("Dried pot", round(m["dried"], 1)),
         ("Fired pot", round(m["fired"], 1)), ("Passes QC", round(m["passed"], 1))],
        MD / "flow.png", f"{PROJECT}: material flow per filter, mixed charge to passed filter (all values are estimates)", "kg",
        [(0, "Trim, recycled (est.)", round(m["trim"], 1)), (1, "Drying water (est.)", round(m["drying_loss"], 1)),
         (2, "Firing loss (est.)", round(m["firing_loss"], 1)), (3, "Rejects, 10 % (est.)", round(m["reject"], 1))])


def blueprint():
    import sizing
    from build123d import Compound
    from drawing import Sheet, project_views
    g = sizing.geometry(); m = sizing.mix(g); k = sizing.kinematics(g, m); c = sizing.cycle(k)
    ps = parts()
    shown = K.with_scale_figure(ps)
    views = project_views(Compound(children=[p.shape for p in ps]), MD / "_views")
    views["iso"] = project_views(Compound(children=[p.shape for p in shown]), MD / "_views_fig")["iso"]
    s = Sheet(project=PROJECT, title=TITLE, dwg_no=DWG, rev="P1", author="Amish Chadha", date=DATE, theme="blueprint",
              material="Massing model for concept communication", revisions=[("P1", "Concept sheet", DATE, "AC")])
    s.add_ortho(views)
    s.add_svg(views["iso"], 276, 32, 140, 118, label="Isometric view", sublabel="Not to scale; figure is a 1.75 m person")
    s.add_notes("Key figures", [
        "20 t bottle jack; working force 5 to 10 t (assumed)",
        "0.5 to 1.05 MPa mean on the pot at 5 to 10 t",
        f"Filter 280 mm inner rim, 240 mm deep, {g['v_work']:.1f} L working",
        f"About {m['charge']:.1f} kg mix per pot; about {m['fired']:.1f} kg fired (est.)",
        f"Cycle about {c['total_min']:.1f} min; about {c['pots_6h']:.0f} pots per 6 h (est.)",
        "QC: 1.0 to 2.5 L/h in the first hour, at 25 C",
        "Press 940 x 700 x 1,806 mm guarded, rails folded; about 390 kg (est.)",
        "Mesh guards; front gate interlocked with the jack release"], x=276, y=168, width=140)
    s.save(MD / "concept-blueprint")
    import shutil
    shutil.rmtree(MD / "_views", ignore_errors=True); shutil.rmtree(MD / "_views_fig", ignore_errors=True)
    return MD / "concept-blueprint.png"


if __name__ == "__main__":
    fns = {"hero": hero, "cutaway": cutaway, "exploded": exploded, "flow": flow, "web": web, "blueprint": blueprint}
    for w in sys.argv[1:] or list(fns):
        print(w, "->", fns[w]())
