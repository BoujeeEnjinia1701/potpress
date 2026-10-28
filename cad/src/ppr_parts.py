"""PotPress repo-specific CAD helpers beside .kit/cad_parts.py (kit 1.9).

    bolt_set()    cad_parts.hex_bolt_set placed on any axis: head face at a point, the joint along a direction
    tapped()      ISO 4017 screw and ISO 7089 washer into a tapped hole (no nut), on any axis
    stud_anchor() M12 stud anchor for the feet: stud from below the floor, washer and nut on top of the foot
    weld()        a fillet weld bead along any axis with its two legs on two faces
    countersunk() ISO 10642 style countersunk screw, head flush with a face

All sizes in millimetres. Directions are "+x", "-x", "+y", "-y", "+z", "-z". Each helper returns a list of
(name, shape) pairs, so the model can make one cad_parts.part() per bolt, washer and nut.
"""
from __future__ import annotations

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / ".kit"))
from build123d import Cone, Cylinder, Plane, Polygon, Pos, Rot, extrude  # noqa: E402
import cad_parts as cp  # noqa: E402

# rotation that takes the library's "into the joint" direction (-Z) to the direction asked for
_TURN = {"-z": Rot(0, 0, 0), "+z": Rot(180, 0, 0), "+y": Rot(90, 0, 0), "-y": Rot(-90, 0, 0),
         "+x": Rot(0, -90, 0), "-x": Rot(0, 90, 0)}
_VEC = {"+x": (1, 0, 0), "-x": (-1, 0, 0), "+y": (0, 1, 0), "-y": (0, -1, 0), "+z": (0, 0, 1), "-z": (0, 0, -1)}


def _place(shape, at, into):
    return Pos(*at) * _TURN[into] * shape


def bolt_set(d, grip, at, into, grade="8.8"):
    """Hex bolt, two washers and a nut clamping a joint 'grip' thick. 'at' is the point on the face under the
    head; 'into' is the direction from that face through the joint. Returns [(name, shape), ...]."""
    out = []
    for nm, shp in cp.hex_bolt_set(int(d), grip):
        if "bolt" in nm:
            nm = nm.replace("hex bolt", f"hex bolt {grade}")
        out.append((nm, _place(shp, at, into)))
    return out


def tapped(d, length, at, into, washer=True, grade="8.8"):
    """Hex head screw (ISO 4017) of the given length under the head into a tapped hole, with a washer."""
    h = cp.ISO[int(d)][4] if washer else 0.0
    out = [(f"M{d}x{length:.0f} hex screw {grade} (ISO 4017), into tapped hole", _place(Pos(0, 0, h) * cp.hex_bolt(int(d), length), at, into))]
    if washer:
        out.append((f"M{d} washer (ISO 7089)", _place(cp.washer(int(d)), at, into)))
    return out


def stud_anchor(d, z_floor_depth, z_top, x, y):
    """Stud anchor: a threaded stud from z_floor_depth (below the floor) up through the foot, with a washer and
    nut on the foot's top face at z_top."""
    s, k, m, d2, h, p = cp.ISO[int(d)]
    top = z_top + h + m + 2 * p
    stud = Pos(x, y, z_floor_depth) * cp.round_bar(d, top - z_floor_depth, chamfer_ends=1.0)
    return [(f"M{d} stud anchor, zinc plated, {top - z_floor_depth:.0f} mm", stud),
            (f"M{d} washer (ISO 7089)", Pos(x, y, z_top) * cp.washer(int(d))),
            (f"M{d} hex nut (ISO 4032)", Pos(x, y, z_top + h) * cp.hex_nut(int(d)))]


def countersunk(d, length, at, into):
    """Countersunk screw: 90 degree head (head diameter 2d) flush with the face at 'at', shank 'length' into
    the joint along 'into'."""
    head = _cs_head(d)
    shank = Pos(0, 0, -length / 2) * Cylinder(d / 2, length)
    return [(f"M{d}x{length:.0f} countersunk screw (ISO 10642)", _place(head + shank, at, into))]


def _cs_head(d):
    """Countersunk head from z 0 (flush face, diameter 2d) down to z -d/2 (diameter d)."""
    from build123d import Align
    return Pos(0, 0, -d / 2) * Cone(d / 2, d, d / 2, align=(Align.CENTER, Align.CENTER, Align.MIN))


def weld(origin, along, length, leg, u, v):
    """Fillet weld bead from 'origin' for 'length' along direction 'along' (a vector), its two legs 'leg' long
    lying along u and v (unit vectors pointing away from the corner over the two welded faces)."""
    import numpy as np
    a = np.array(along, float); a /= np.linalg.norm(a)
    uu = np.array(u, float); uu /= np.linalg.norm(uu)
    vv = np.array(v, float); vv /= np.linalg.norm(vv)
    y = np.cross(a, uu)
    sgn = 1.0 if float(np.dot(y, vv)) > 0 else -1.0
    pl = Plane(origin=tuple(float(c) for c in origin), x_dir=tuple(float(c) for c in uu), z_dir=tuple(float(c) for c in a))
    pts = [(0, 0), (leg, 0), (0, leg)] if sgn > 0 else [(0, 0), (0, -leg), (leg, 0)]   # counter-clockwise: extrudes along +normal
    tri = Polygon(*pts, align=None)
    return extrude(pl * tri, amount=length)
