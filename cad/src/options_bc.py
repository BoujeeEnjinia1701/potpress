"""PotPress concept options B and C at detail level D3 (kit 1.9, PPR-OPT-001, STANDARDS sections 21 and 24).

Imported by cad/src/model.py: components("B") and components("C"). Option A (the current design) is built in
model.py itself. B and C press the same reference filter between the same cast aluminium molds as A (the mold
parts, rails, carriage, pressed pot and QC rack are option A's parts moved to their place), on the same bolted
UPN channel frame practice; they differ in how the force is made:

    B  toggle (scissor) lever press: a 1.1 m hand lever turns the upper link of a toggle about its top pin; the
       knee straightens and pushes a guided crosshead, which carries the male mold, down onto the female mold
    C  power-screw press: a four-bar capstan turns a Tr40 x 7 screw through a bronze nut in the crown; the screw
       pushes the crosshead down through a thrust swivel

Both are drawn closed, molds on the stop, female mold fixed on a bed plate on the base beam. The fixed mesh guard
of option A applies to both (PPR-OPT-001) but is not drawn here, so the mechanism shows; the rail extension and
interlocks of A are also left out. Axes as model.py: X across the frame, Y front (-Y) to back, Z up from the floor.
CONCEPT, NOT FOR FABRICATION.
"""
from __future__ import annotations

import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parents[1] / ".kit")]

from build123d import Pos, Rot, SlotCenterToCenter, Plane, extrude, Sketch, Circle  # noqa: E402
import cad_parts as cp  # noqa: E402
from cad_parts import part, break_edges  # noqa: E402
import ppr_parts as pp  # noqa: E402

LEG = 5.0          # fillet weld leg, mm


def _m():
    import model
    return model


# ------------------------------------------------------------------------------------------- shared levels
def levels_bc(P=None):
    """Vertical stack for options B and C, closed (mm). Same feet, base beam and molds as A; the female mold sits
    on a 20 mm bed plate on the base beam instead of the moving platen."""
    M = _m(); P = P or M.PARAMS
    LA = M.levels(P)
    b = M.SECTIONS[P["BEAM_SEC"]]
    L = dict(base0=LA["base0"], base1=LA["base1"])
    L["bed1"] = L["base1"] + 20.0
    L["dz"] = L["bed1"] - LA["deck1"]                  # option A mold stack moved down by this
    for k in ("fm0", "fm1", "mm1", "adapter0", "stem0", "pot0"):
        L[k] = LA[k] + L["dz"]
    L["cs0"] = L["mm1"] + 40.0                         # crosshead underside (bottom plate)
    L["cs1"] = L["cs0"] + 20.0 + M.SECTIONS["UPN140"]["h"] + 15.0
    # option B toggle: links straight at the end of the stroke
    L["p1"] = L["cs1"] + 50.0                          # lower pin (crosshead clevis)
    L["p2"] = L["p1"] + 400.0                          # knee pin
    L["p3"] = L["p2"] + 400.0                          # top pin (head clevis)
    L["headB0"] = L["p3"] + 70.0                       # under the head beam's bottom flanges: 20 mm head plate below
    L["headB1"] = L["headB0"] + b["h"]
    # option C screw: crown above the swivel housing with the 310 mm opening stroke clear
    L["sw1"] = L["cs1"] + 60.0
    L["headC0"] = L["sw1"] + 330.0
    L["headC1"] = L["headC0"] + b["h"]
    L["hub0"] = L["headC1"] + 15.0 + 45.0
    return L


def _p(name, shape, mat, kind="made", group="frame", note=""):
    if kind in ("made", "bought") and _bare(shape):
        shape = break_edges(shape, 1.0)
    return part(name, shape, mat, kind=kind, group=group, note=note)


def _bare(shape):
    try:
        f = shape.faces()
        return len(f) == 3 or (len(f) == 6 and all(str(x.geom_type).endswith("PLANE") for x in f))
    except Exception:
        return False


def _pcs(pieces, mat="zinc_plated", kind="fastener", group="frame"):
    return [part(n, s, mat, kind=kind, group=group) for n, s in pieces]


# ------------------------------------------------------------------------------------------- shared frame
def frame(P, top0, label):
    """Feet with studs and anchors, base beam with bed plate, two upright pairs with M16 joints and shims, and the
    head beam (two UPN 160) whose underside is at top0. Returns parts."""
    M = _m()
    box, cyl, cyl_y = M.box, M.cyl, M.cyl_y
    L = levels_bc(P)
    b = M.SECTIONS[P["BEAM_SEC"]]; u = M.SECTIONS[P["UPRIGHT_SEC"]]; f = M.SECTIONS[P["FOOT_SEC"]]
    g2, xs, bl = P["BEAM_GAP"] / 2, P["SPAN"] / 2, P["BEAM_L"] / 2
    yw = g2 + b["tw"]
    top1 = top0 + b["h"]
    out = []
    # feet: UPN 100 web up, anchor tubes, holes for the studs
    xf = xs + 60
    for sx, side in ((-1, "left"), (1, "right")):
        xc = sx * xf; w = f["h"] / 2
        foot = box(xc - w, xc + w, -P["FOOT_L"] / 2, P["FOOT_L"] / 2, f["b"] - f["tw"], f["b"])
        for dx in (-1, 1):
            x_a, x_b = sorted((xc + dx * w, xc + dx * (w - f["tf"])))
            foot += box(x_a, x_b, -P["FOOT_L"] / 2, P["FOOT_L"] / 2, 0, f["b"])
        for sy in (-1, 1):
            foot += cyl(13.45, 0, f["b"] - f["tw"], xc, sy * P["ANCHOR_Y"]) - cyl(10.25, -1, f["b"], xc, sy * P["ANCHOR_Y"])
            foot -= cyl(7, f["b"] - f["tw"] - 1, f["b"] + 1, xc, sy * P["ANCHOR_Y"])
        studs = [(xc + dx, sy * 88.0) for dx in (-25, 25) for sy in (-1, 1)]
        for x_, y_ in studs:
            foot -= cyl(6.5, f["b"] - f["tw"] - 1, f["b"] + 1, x_, y_)
        out.append(_p(f"Foot, {side}, UPN 100 web up", foot, "painted_steel"))
        for x_, y_ in studs:
            out += _pcs(pp.bolt_set(12, f["tw"] + b["tf"], (x_, y_, f["b"] - f["tw"]), "+z"))
        for sy in (-1, 1):
            out += _pcs(pp.stud_anchor(12, -80.0, f["b"], xc, sy * P["ANCHOR_Y"]))
    # joint bolt positions on both beams
    zcb, zct = (L["base0"] + L["base1"]) / 2, (top0 + top1) / 2
    pts = [(sx * xs + dx, zc + dz) for sx in (-1, 1) for zc in (zcb, zct)
           for dx in (-P["JOINT_BOLT_DX"], P["JOINT_BOLT_DX"]) for dz in (-P["JOINT_BOLT_DZ"], P["JOINT_BOLT_DZ"])]
    rh = (P["JOINT_BOLT_D"] + 2) / 2
    bed_bolts = [(sx * 105.0, sy * 90.0) for sx in (-1, 1) for sy in (-1, 1)]

    def beam(z0, nm, extra_holes=()):
        sh = M.channel_x(-bl, bl, g2, +1, z0, P["BEAM_SEC"]) + M.channel_x(-bl, bl, -g2, -1, z0, P["BEAM_SEC"])
        for sx in (-1, 1):
            sh += box(*sorted((sx * bl, sx * (bl - P["END_BLOCK_L"]))), -g2, g2, z0 + b["tf"], z0 + b["h"] - b["tf"])
        for x_, z_ in pts:
            if z0 <= z_ <= z0 + b["h"]:
                sh -= cyl_y(rh, -yw - 1, yw + 1, x_, z_)
        for x_, y_, za, zb_, r in extra_holes:
            sh -= cyl(r, za, zb_, x_, y_)
        out.append(_p(nm, sh, "painted_steel"))
        for sx in (-1, 1):                                    # end blocks welded to both webs
            for sy in (-1, 1):
                out.append(part(f"Weld, {nm.split(',')[0].lower()} end block {'right' if sx > 0 else 'left'} {'back' if sy > 0 else 'front'}",
                                pp.weld((sx * (bl - P["END_BLOCK_L"]), sy * g2, z0 + b["tf"]), (0, 0, 1), b["h"] - 2 * b["tf"], LEG,
                                        (-sx, 0, 0), (0, -sy, 0)), "mild_steel", kind="weld"))
    studs_all = [(sx * xf + dx, sy * 88.0) for sx in (-1, 1) for dx in (-25, 25) for sy in (-1, 1)]
    beam(L["base0"], "Base beam, 2 x UPN 160 with end blocks",
         [(x_, y_, L["base1"] - b["tf"] - 1, L["base1"] + 1, 7.0) for x_, y_ in bed_bolts] +
         [(x_, y_, L["base0"] - 1, L["base0"] + b["tf"] + 1, 7.0) for x_, y_ in studs_all])
    beam(top0, f"Head beam ({label}), 2 x UPN 160 with end blocks")
    # bed plate on the base beam, bolted with 4 x M12
    bed = box(-235, 235, -270, 230, L["base1"], L["bed1"])
    for x_, y_ in bed_bolts:
        bed -= cyl(7, L["base1"] - 1, L["bed1"] + 1, x_, y_)
    out.append(_p("Bed plate 470 x 500 x 20, S275", break_edges(bed, 1.5), "mild_steel", group="mold"))
    for x_, y_ in bed_bolts:
        out += _pcs(pp.bolt_set(12, 20 + b["tf"], (x_, y_, L["bed1"]), "-z"))
    # upright pairs, spacer tubes, shims, M16 10.9 joint bolts
    ys = u["h"] / 2
    for sx, side in ((-1, "left"), (1, "right")):
        pair = M.channel_upright(sx * xs, -1, L["base0"], top1, P["UPRIGHT_SEC"]) + \
            M.channel_upright(sx * xs, +1, L["base0"], top1, P["UPRIGHT_SEC"])
        mine = [q for q in pts if (q[0] > 0) == (sx > 0)]
        for x_, z_ in mine:
            pair -= cyl_y(rh, -ys - 1, ys + 1, x_, z_)
        out.append(_p(f"Upright pair, {side}, 2 x UPN 100 back to back", pair, "painted_steel"))
        for x_, z_ in mine:
            t_ = cyl_y(P["SPACER_OD"] / 2, -ys + u["tf"], ys - u["tf"], x_, z_) - cyl_y(9.5, -ys, ys, x_, z_)
            out.append(_p(f"Spacer tube 25 x 3, {side}", t_, "mild_steel"))
            out += _pcs(pp.bolt_set(16, 2 * yw, (x_, -yw, z_), "+y", grade="10.9"))
        for zc in (zcb, zct):
            for sy in (-1, 1):
                sh = box(sx * xs - ys, sx * xs + ys, *sorted((sy * ys, sy * g2)), zc - 60, zc + 60)
                for x_, z_ in mine:
                    if abs(z_ - zc) < 50:
                        sh -= cyl_y(rh, -g2 - 1, g2 + 1, x_, z_)
                out.append(_p(f"Shim pack 2 mm, {side}", sh, "galvanised"))
    return out


def crosshead(P):
    """Guided crosshead carrying the male mold: two UPN 140 between a 20 mm bottom plate and a 15 mm top plate,
    guide sleeves round the uprights; under it a 20 mm stem flange bolted with 4 x M16 and a SHS 90 x 8 stem down
    to the adapter disc in the male mold. Returns parts."""
    M = _m()
    box, cyl = M.box, M.cyl
    L = levels_bc(P)
    u = M.SECTIONS[P["UPRIGHT_SEC"]]; pl = M.SECTIONS["UPN140"]
    g2, xs = P["BEAM_GAP"] / 2, P["SPAN"] / 2
    xin = xs - u["b"] - P["SLEEVE_T"] - P["SLEEVE_CLEAR"] / 2
    z0, z1 = L["cs0"], L["cs1"]
    out = []
    bolts = [(sx * 70.0, sy * 30.0) for sx in (-1, 1) for sy in (-1, 1)]
    bot = box(-xin, xin, -150, 150, z0, z0 + 20)
    for x_, y_ in bolts:
        bot -= cyl(9, z0 - 1, z0 + 21, x_, y_)
    out.append(_p("Crosshead bottom plate 20 mm", break_edges(bot, 1.5), "painted_steel", group="slide"))
    ch = M.channel_x(-xin, xin, g2, +1, z0 + 20, "UPN140") + M.channel_x(-xin, xin, -g2, -1, z0 + 20, "UPN140")
    out.append(_p("Crosshead channels, 2 x UPN 140", ch, "painted_steel", group="slide"))
    out.append(_p("Crosshead top plate 15 mm", break_edges(box(-xin, xin, -150, 150, z0 + 20 + pl["h"], z1), 1.5),
                  "painted_steel", group="slide"))
    c = P["SLEEVE_CLEAR"] / 2; t = P["SLEEVE_T"]
    for sx in (-1, 1):
        xo0, xo1 = sorted((sx * (xs - u["b"] - c - t), sx * (xs + u["b"] + c + t)))
        yo = u["h"] / 2 + c + t
        sl = box(xo0, xo1, -yo, yo, z0, z0 + P["SLEEVE_H"]) - box(xo0 + t, xo1 - t, -yo + t, yo - t, z0 - 1, z0 + P["SLEEVE_H"] + 1)
        out.append(_p(f"Crosshead guide sleeve, {'right' if sx > 0 else 'left'}, 10 mm plate", sl, "painted_steel", group="slide"))
        out.append(part(f"Weld, sleeve to crosshead bottom plate, {'right' if sx > 0 else 'left'}",       # between the webs
                        pp.weld((sx * xin, -g2 + LEG, z0 + 20), (0, 1, 0), 2 * g2 - 2 * LEG, LEG, (-sx, 0, 0), (0, 0, 1)),
                        "mild_steel", kind="weld", group="slide"))
    # stem flange, SHS stem and adapter disc
    s2, ts = P["STEM"] / 2, P["STEM_T"]
    fl = box(-90, 90, -90, 90, z0 - 20, z0)
    for x_, y_ in bolts:
        fl -= cyl(9, z0 - 21, z0 + 1, x_, y_)
    out.append(_p("Stem flange plate 180 x 180 x 20", break_edges(fl, 1.0), "painted_steel", group="slide"))
    for x_, y_ in bolts:
        out += _pcs(pp.bolt_set(16, 40, (x_, y_, z0 - 20), "+z"), group="slide")
    stem = cp.shs(P["STEM"], ts, z0 - 20 - L["stem0"])
    out.append(_p("Stem SHS 90 x 90 x 8", Pos(0, 0, L["stem0"]) * stem, "painted_steel", group="slide"))
    ad = cyl(P["ADAPTER_D"] / 2, L["adapter0"], L["stem0"])
    ad_bolts = [(75.0, 0.0), (-75.0, 0.0), (0.0, 75.0), (0.0, -75.0)]
    for x_, y_ in ad_bolts:
        ad -= cyl(6.5, L["adapter0"] - 1, L["stem0"] + 1, x_, y_)
    out.append(_p("Adapter disc 190 x 20", break_edges(ad, 1.0), "mild_steel", group="slide"))
    for x_, y_ in ad_bolts:
        out += _pcs(pp.tapped(12, 40, (x_, y_, L["stem0"]), "-z"), group="slide")
    for sx, sy, nm in ((1, 0, "right"), (-1, 0, "left"), (0, 1, "back"), (0, -1, "front")):   # stem welds
        if sx:
            org, along, uu = (sx * s2, -s2 + LEG, None), (0, 1, 0), (sx, 0, 0)
        else:
            org, along, uu = (-s2 + LEG, sy * s2, None), (1, 0, 0), (0, sy, 0)
        for zz, vv, lv in ((L["stem0"], (0, 0, 1), "disc"), (z0 - 20, (0, 0, -1), "flange")):
            o = (org[0], org[1], zz)
            out.append(part(f"Weld, stem to {lv}, {nm}", pp.weld(o, along, P["STEM"] - 2 * LEG, LEG, uu, vv), "mild_steel",
                            kind="weld", group="slide"))
    return out


def shared_molds_and_qc(P):
    """Option A's mold set, rails, carriage, pressed pot and QC rack, the mold stack moved down onto the bed plate."""
    M = _m()
    L = levels_bc(P)
    dz = L["dz"]
    out = []
    for p in M.option_a_parts(P):
        k = p.get("key_src")
        if k in M.MOLD_KEYS:
            q = dict(p); q["shape"] = Pos(0, 0, dz) * p["shape"]; q["bom"] = None
            out.append(q)
        elif k in M.QC_KEYS:
            q = dict(p); q["bom"] = None
            out.append(q)
    return out


# ------------------------------------------------------------------------------------------- option B
def option_b(P=None):
    M = _m(); P = P or M.PARAMS
    box, cyl, cyl_y = M.box, M.cyl, M.cyl_y
    L = levels_bc(P)
    b = M.SECTIONS[P["BEAM_SEC"]]
    out = frame(P, L["headB0"], "toggle reaction") + crosshead(P) + shared_molds_and_qc(P)
    pd, hole = 40.0, 25.0                               # 40 mm pins in 50 x 40 bronze bushes (holes 50 mm); 30 mm until the independent review (bending)
    # head plate under the head beam with the upper clevis plates
    hp = box(-200, 200, -117, 117, L["headB0"] - 20, L["headB0"])
    out.append(_p("Head plate 400 x 234 x 20, welded under the head beam", break_edges(hp, 1.5), "painted_steel"))
    for sy in (-1, 1):
        cl = box(-60, 60, *sorted((sy * 38, sy * 50)), L["p3"] - 50, L["headB0"] - 20) - cyl_y(pd / 2 + 0.5, -60, 60, 0, L["p3"])
        cl = break_edges(cl, 1.0)
        out.append(_p(f"Upper clevis plate 12 mm, {'back' if sy > 0 else 'front'}", cl, "painted_steel"))
        for sx in (-1, 1):
            out.append(part(f"Weld, upper clevis to head plate {'back' if sy > 0 else 'front'} {'right' if sx > 0 else 'left'}",
                            pp.weld((-55, sy * (50 if sx > 0 else 38), L["headB0"] - 20), (1, 0, 0), 110, LEG,
                                    (0, sy if sx > 0 else -sy, 0), (0, 0, -1)), "mild_steel", kind="weld"))
        lc = box(-60, 60, *sorted((sy * 21, sy * 33)), L["cs1"], L["p1"] + 50) - cyl_y(pd / 2 + 0.5, -60, 60, 0, L["p1"])
        out.append(_p(f"Lower clevis plate 12 mm, {'back' if sy > 0 else 'front'}", break_edges(lc, 1.0), "painted_steel", group="slide"))
        for sx in (-1, 1):
            out.append(part(f"Weld, lower clevis to crosshead {'back' if sy > 0 else 'front'} {'outer' if sx > 0 else 'inner'}",
                            pp.weld((-55, sy * (33 if sx > 0 else 21), L["cs1"]), (1, 0, 0), 110, LEG,
                                    (0, sy if sx > 0 else -sy, 0), (0, 0, 1)), "mild_steel", kind="weld", group="slide"))

    def link(z_a, z_b, y0, y1, nm):
        """Flat link 80 wide with round eyes, from pin z_a to pin z_b, between y0 and y1, with 50 mm eye holes for the bushes."""
        sk = SlotCenterToCenter(z_b - z_a, 80) - Pos(-(z_b - z_a) / 2, 0) * Circle(hole) - Pos((z_b - z_a) / 2, 0) * Circle(hole)
        pl_ = Plane(origin=(0, y0, (z_a + z_b) / 2), x_dir=(0, 0, 1), z_dir=(0, 1, 0))
        sh = extrude(pl_ * sk, amount=y1 - y0)
        return _p(nm, break_edges(sh, 1.0), "painted_steel", group="toggle")
    for sy in (-1, 1):                                  # upper link: two 16 mm bars outside the lower link
        out.append(link(L["p2"], L["p3"], *sorted((sy * 21, sy * 37)), f"Upper link bar 80 x 16, {'back' if sy > 0 else 'front'}"))
    out.append(link(L["p1"], L["p2"], -20, 20, "Lower link 80 x 40"))
    # bronze bushes in every link eye
    for zz, spans in ((L["p3"], [(-37, -21), (21, 37)]), (L["p2"], [(-36, -21), (21, 37), (-20, 20)]), (L["p1"], [(-20, 20)])):
        for ya, yb_ in spans:
            bu = Pos(0, ya, zz) * Rot(-90, 0, 0) * cp.bush(2 * hole, pd + 0.5, yb_ - ya)
            out.append(_p(f"Bronze bush 50 x 40 x {yb_ - ya:.0f} at {zz:.0f} mm", bu, "brass", kind="bought", group="toggle"))
    for zz, grip, nm in ((L["p3"], 100.0, "top"), (L["p2"], 74.0, "knee"), (L["p1"], 66.0, "lower")):
        pin = Pos(0, -grip / 2 - 2.5, zz) * Rot(90, 0, 0) * cp.clevis_pin(pd, grip)     # 2.5 mm clear of the face: head fillet
        out.append(part(f"Clevis pin 40 mm (ISO 2341 B), {nm}", pin, "zinc_plated", kind="fastener", group="toggle"))
        sp = Pos(0, grip / 2 + pd - 2.5, zz) * cp.split_pin(pd)
        out.append(part(f"Split pin (ISO 1234), {nm}", sp, "zinc_plated", kind="fastener", group="toggle"))
    # hand lever: socket welded to the front upper link bar, 42.4 x 3.2 tube 1.1 m along +X, grip
    zs, ysk = L["p3"] - 110, -75.0
    xbolt = 60.0
    boltcut = cyl(5.5, zs - 40, zs + 40, xbolt, ysk)
    sock = Pos(0, ysk, zs) * Rot(0, 90, 0) * cp.round_tube(60.3, 5.0, 120)
    out.append(_p("Lever socket 60.3 x 5 tube, welded to the front upper link bar", sock - boltcut, "painted_steel", group="toggle"))
    web = box(-0, 120, -46, -37, zs - 25, zs + 25) - (Pos(0, ysk, zs) * Rot(0, 90, 0) * Pos(0, 0, -40) * extrude(Circle(30.15), 200))
    out.append(_p("Socket web plate 9 mm", break_edges(web, 1.0), "painted_steel", group="toggle"))
    tube, grip_ = cp.lever_handle(1100.0, d=42.4, grip_len=150)
    tube -= Pos(550, 0, 0) * Rot(0, 90, 0) * extrude(Circle(21.2 - 3.2), 600, both=True)
    grip_ -= Pos(1025, 0, 0) * Rot(0, 90, 0) * extrude(Circle(21.2), 100, both=True)
    out.append(_p("Hand lever 42.4 x 3.2 tube, 1.1 m", Pos(0, ysk, zs) * tube - boltcut, "mild_steel", group="toggle"))
    out.append(_p("Lever grip, rubber", Pos(0, ysk, zs) * grip_, "epdm", kind="bought", group="toggle"))
    out += _pcs(pp.bolt_set(10, 60.3, (xbolt, ysk, zs + 30.15), "-z"), group="toggle")
    # return springs from the crosshead top plate to the head plate
    for sx in (-1, 1):
        x_ = sx * 170.0
        for zz, top in ((L["cs1"], False), (L["headB0"] - 20, True)):
            lug = box(x_ - 15, x_ + 15, -40, 40, *((zz - 8, zz) if top else (zz, zz + 8))) - cyl(5, zz - 9, zz + 9, x_)
            out.append(_p(f"Spring lug {'head' if top else 'crosshead'} {'right' if sx > 0 else 'left'}", lug, "painted_steel"))
        z_lo, z_hi = L["cs1"] + 8, L["headB0"] - 28
        spr = cyl(14, z_lo + 25, z_hi - 25, x_) - cyl(11, z_lo + 24, z_hi - 24, x_)
        spr += cyl(2.5, z_lo - 4, z_lo + 26, x_ + 0) + cyl(2.5, z_hi - 26, z_hi + 4, x_)
        out.append(_p(f"Return spring, about 200 N, {'right' if sx > 0 else 'left'}", spr, "zinc_plated", kind="bought", group="slide"))
    return out


# ------------------------------------------------------------------------------------------- option C
def option_c(P=None):
    M = _m(); P = P or M.PARAMS
    box, cyl = M.box, M.cyl
    L = levels_bc(P)
    b = M.SECTIONS[P["BEAM_SEC"]]
    out = frame(P, L["headC0"], "crown") + crosshead(P) + shared_molds_and_qc(P)
    # swivel housing on the crosshead: cast block with a thrust bearing seat, bolted with 4 x M12
    hb = [(sx * 45.0, sy * 45.0) for sx in (-1, 1) for sy in (-1, 1)]
    hs = box(-60, 60, -60, 60, L["cs1"], L["sw1"]) - cyl(32, L["cs1"] + 15, L["sw1"] + 1) - cyl(21, L["sw1"] - 16, L["sw1"] + 1)
    for x_, y_ in hb:
        hs -= cyl(7, L["cs1"] - 1, L["cs1"] + 21, x_, y_) + cyl(15, L["cs1"] + 20, L["sw1"] + 1, x_, y_)   # spot-faced pockets
    for q in out:                                       # tapped M12 holes in the crosshead top plate (major diameter)
        if q["name"].startswith("Crosshead top plate"):
            for x_, y_ in hb:
                q["shape"] = q["shape"] - cyl(6, L["cs1"] - 16, L["cs1"] + 1, x_, y_)
    out.append(_p("Swivel housing 120 x 120 x 60 with thrust bearing seat", break_edges(hs, 1.5), "mild_steel", group="slide"))
    for x_, y_ in hb:
        out += _pcs(pp.tapped(12, 30, (x_, y_, L["cs1"] + 20), "-z"), group="slide")
    out.append(_p("Thrust ball bearing 51108 (40 x 60 x 13)", Pos(0, 0, L["cs1"] + 15) *
                  (cp.bush(60, 40.5, 13)), "stainless", kind="bought", group="slide"))
    # screw: Tr40 x 7, drawn at the major diameter, collar under the bearing, through the nut, capstan hub on top
    z_s0, z_s1 = L["cs1"] + 30, L["hub0"] + 80
    scr = Pos(0, 0, z_s0) * cp.round_bar(40, z_s1 - z_s0, chamfer_ends=2.0)
    scr -= Pos(0, 0, L["hub0"] + 15) * Rot(90, 0, 0) * extrude(Circle(5.25), 60, both=True)
    out.append(_p("Power screw Tr40 x 7, 1045 steel, thread drawn as its major diameter", scr, "mild_steel", kind="bought", group="screw"))
    out.append(_p("Screw thrust collar 58 x 2 on the bearing", cyl(29, L["cs1"] + 28, L["cs1"] + 30) - cyl(8, L["cs1"] + 27, L["cs1"] + 31),
                  "mild_steel", group="screw"))
    # crown nut: bronze flanged nut between the crown channels, flange plate bolted to the top flanges
    nut = cyl(40, L["headC0"] + 10, L["headC1"]) + cyl(60, L["headC1"], L["headC1"] + 15) - cyl(20, L["headC0"], L["headC1"] + 16)
    nut -= cyl(20, L["headC0"], L["headC1"] + 16)
    for a in (45, 135, 225, 315):
        nut -= cyl(5.5, L["headC1"] - 1, L["headC1"] + 16, 48 * math.cos(math.radians(a)), 48 * math.sin(math.radians(a)))
    out.append(_p("Crown nut Tr40 x 7, cast bronze, flanged", break_edges(nut, 0.8), "brass", kind="bought", group="screw"))
    for a in (45, 135, 225, 315):
        out += _pcs(pp.tapped(10, 25, (48 * math.cos(math.radians(a)), 48 * math.sin(math.radians(a)), L["headC1"] + 15), "-z"), group="screw")
    # nut seat plates welded across the crown channels: the nut flange bolts into them
    seat = box(-75, 75, -52, 52, L["headC1"] - 20, L["headC1"]) - cyl(40.5, L["headC1"] - 21, L["headC1"] + 1)
    for a in (45, 135, 225, 315):
        seat -= cyl(5, L["headC1"] - 21, L["headC1"] + 1, 48 * math.cos(math.radians(a)), 48 * math.sin(math.radians(a)))
    out.append(_p("Nut seat plate 150 x 104 x 20, welded between the crown webs", break_edges(seat, 1.0), "painted_steel"))
    for sx in (-1, 1):
        for sy in (-1, 1):
            out.append(part(f"Weld, nut seat to crown web {'right' if sx > 0 else 'left'} {'back' if sy > 0 else 'front'}",
                            pp.weld((sx * 75, sy * 52, L["headC1"] - 20), (0, 0, 1), 20 - 0.5, LEG, (sx, 0, 0), (0, -sy, 0)),
                            "mild_steel", kind="weld"))
    # capstan: hub pinned to the screw, four 25 mm bars to a 450 mm radius with rubber grips
    hub = cyl(55, L["hub0"], L["hub0"] + 80) - cyl(20, L["hub0"] - 1, L["hub0"] + 81)
    for a in (0, 90):
        hub -= Pos(0, 0, L["hub0"] + 40) * Rot(0, 0, a) * Rot(0, 90, 0) * extrude(Circle(12.75), 120, both=True)
    hub -= Pos(0, 0, L["hub0"] + 15) * Rot(90, 0, 0) * extrude(Circle(5.25), 60, both=True)
    out.append(_p("Capstan hub 110 x 80, steel", break_edges(hub, 1.0), "painted_steel", group="screw"))
    out.append(part("Cross pin 10 mm through hub and screw", Pos(0, 0, L["hub0"] + 15) * Rot(90, 0, 0) * Pos(0, 0, -58) *
                    cp.round_bar(10, 116), "zinc_plated", kind="fastener", group="screw"))
    for a in (0, 90, 180, 270):
        bar = Pos(0, 0, L["hub0"] + 40) * Rot(0, 0, a) * Rot(0, 90, 0) * Pos(0, 0, 22) * cp.round_bar(25, 428)
        out.append(_p(f"Capstan bar 25 mm at {a} deg", bar, "mild_steel", group="screw"))
        gr = Pos(0, 0, L["hub0"] + 40) * Rot(0, 0, a) * Rot(0, 90, 0) * Pos(0, 0, 330) * (cp.round_tube(33, 4, 120))
        out.append(_p(f"Capstan grip, rubber, at {a} deg", break_edges(gr, 1.0), "epdm", kind="bought", group="screw"))
    return out
