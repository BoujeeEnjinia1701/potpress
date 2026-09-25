"""PotPress sizing and first-principles checks (PPR-CAL-001).

Run from the repo root:  python docs/04-calcs/sizing.py
Prints every number quoted in docs/04-calcs/01-sizing.md. Geometry comes from
PARAMS, SECTIONS and levels() in cad/src/model.py; part masses come from the model
solids; the BOM total is read from bom/bom.csv. All values are estimates for a
paper design (TRL 3); nothing here is measured.
"""
from __future__ import annotations

import csv
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "cad/src"))
from model import PARAMS as P, SECTIONS as S, levels, pot_outer  # noqa: E402

G = 9.81
E_STEEL, G_STEEL = 200e3, 80e3          # MPa
FY_S275, ALLOW = 275.0, 165.0           # MPa; allowable at the jack rating = FY / about 1.67
FY_PIN = 650.0                          # 42CrMo4 quenched and tempered, 40 to 100 mm bar
FY_AL = 90.0                            # as-cast aluminum-silicon scrap alloy, conservative
WELD_ALLOW = 0.3 * 430.0                # E6013 fillet weld, allowable shear on the throat
RHO_ST, RHO_AL, RHO_PLY, RHO_UHMW = 7850.0, 2680.0, 600.0, 940.0   # kg/m3

# Forces (N)
T = 1000 * G                            # one tonne-force
F_WORK = (5 * T, 10 * T)                # assumed working range, not sourced
F_RATED = 20 * T                        # jack rating
F_DESIGN = 1.5 * F_RATED                # R3 design load

# Mix (Rayner 2009, RDI-C recipe) and process assumptions
MIX = {"clay": 0.59, "husk": 0.16, "water": 0.25}          # mass fractions
RHO_PART = {"clay": 2600.0, "husk": 1400.0, "water": 1000.0}  # particle densities, kg/m3
AIR = 0.03                              # entrapped air in the pressed wall
TRIM = 0.10                             # trim allowance, fraction of pressed mass (recycled)
LOOSE_RHO = 1.5                         # kg/L, loose charge as placed
RESID_WATER = 0.02                      # dried pot, water left as fraction of dry solids
CLAY_LOI = 0.10                         # clay loss on ignition (bound water, organics)
REJECT = 0.10                           # QC reject rate (estimate)

# Costs (USD, 2026, indicative, regional small-town suppliers)
STEEL_USD_KG = 1.30
AL_SCRAP_USD_KG = 2.00
POUR_FACTOR = 1.35                      # gates, risers and melt loss per kg of casting
FOUNDRY_USD_KG = 1.50                   # foundry fee per kg of finished casting
PLA_USD_KG = 20.0
PATTERN_FILL = 0.25                     # printed pattern mass fraction of a solid part
PLA_RHO = 1240.0
AL_SHRINK = 0.013                       # linear pattern shrink allowance
BED = 250.0                             # printer bed, mm (R7)


def frustum(r0, r1, h):
    return math.pi * h / 3 * (r0 * r0 + r0 * r1 + r1 * r1)


def geometry():
    g = {}
    rb, rt, h_out = pot_outer(P)
    g["r_out_bot"], g["r_out_top"], g["h_out"] = rb, rt, h_out
    slope = (P["R_IN_RIM"] - P["R_IN_BOT"]) / P["D_IN"]
    g["slope_deg"] = math.degrees(math.atan(slope))
    g["v_brim"] = frustum(P["R_IN_BOT"], P["R_IN_RIM"], P["D_IN"]) / 1e6
    h_w = P["D_IN"] - 40
    g["v_work"] = frustum(P["R_IN_BOT"], P["R_IN_BOT"] + slope * h_w, h_w) / 1e6
    v_outer = frustum(rb, rt, h_out)
    r_mid_rim = rt - slope * P["RIM_T"] / 2
    v_rim = math.pi * ((P["RIM_OD"] / 2) ** 2 - r_mid_rim ** 2) * P["RIM_T"]
    g["v_wall"] = (v_outer - frustum(P["R_IN_BOT"], P["R_IN_RIM"], P["D_IN"]) + v_rim) / 1e6
    g["a_proj"] = math.pi * (P["RIM_OD"] / 2) ** 2 / 1e6          # m2
    return g


def mix(g):
    m = {}
    vol_per_kg = sum(MIX[k] / RHO_PART[k] for k in MIX)          # m3/kg
    m["rho_solid"] = 1 / vol_per_kg / 1000                        # kg/L, no air
    m["rho_pressed"] = m["rho_solid"] * (1 - AIR)
    m["pressed"] = g["v_wall"] * m["rho_pressed"]
    m["charge"] = m["pressed"] * (1 + TRIM)
    m["trim"] = m["charge"] - m["pressed"]
    solids = m["pressed"] * (MIX["clay"] + MIX["husk"])
    m["dried"] = solids * (1 + RESID_WATER)
    m["drying_loss"] = m["pressed"] - m["dried"]
    clay = m["pressed"] * MIX["clay"]
    m["fired"] = clay * (1 - CLAY_LOI)
    m["firing_loss"] = m["dried"] - m["fired"]
    m["passed"] = m["fired"] * (1 - REJECT)
    m["reject"] = m["fired"] - m["passed"]
    m["husk_vol_frac"] = (MIX["husk"] / RHO_PART["husk"]) / vol_per_kg
    return m


def frame():
    f = {}
    b = S[P["BEAM_SEC"]]; u = S[P["UPRIGHT_SEC"]]; pl = S[P["PLATEN_SEC"]]
    L = levels()
    span = P["SPAN"]
    I2, W2 = 2 * b["Ix"], 2 * b["Wx"]
    Aw = 2 * b["h"] * b["tw"]
    f["beam_W_cm3"] = W2 / 1e3
    for tag, F in (("work", F_WORK[1]), ("rated", F_RATED), ("design", F_DESIGN)):
        M = F * span / 4                                         # N mm, center load
        f[f"beam_M_{tag}"] = M / 1e6                              # kN m
        f[f"beam_sig_{tag}"] = M / W2
        f[f"beam_tau_{tag}"] = (F / 2) / Aw
        f[f"upr_sig_{tag}"] = (F / 2) / (2 * u["A"])
    # Load pin: one pin through both webs (with doublers) and the stem pin block
    d = P["PIN_D"]; a = b["tw"] + P["DOUBLER_T"]; blk = P["STEM"]; gap = (P["BEAM_GAP"] - P["STEM"]) / 2
    Z = math.pi * d ** 3 / 32; A = math.pi * d * d / 4
    f["pin_arm"] = blk / 4 + gap + a / 2
    for tag, F in (("rated", F_RATED), ("design", F_DESIGN)):
        f[f"pin_M_{tag}"] = F / 2 * f["pin_arm"] / 1e6
        f[f"pin_sig_{tag}"] = F / 2 * f["pin_arm"] / Z
        f[f"pin_tau_{tag}"] = F / (2 * A)
        f[f"pin_brg_web_{tag}"] = (F / 2) / (d * a)
        f[f"pin_brg_web_nodbl_{tag}"] = (F / 2) / (d * b["tw"])
        f[f"pin_brg_blk_{tag}"] = F / (d * blk)
        lig = (b["h"] / 2 - d / 2 - 1 - b["tf"])
        f["pin_ligament"] = lig
        f[f"pin_tear_{tag}"] = (F / 2) / (2 * lig * a)
    # Old TRL 2 pin arrangement for comparison: two 30 mm pins, same geometry
    d0 = 30.0; Z0 = math.pi * d0 ** 3 / 32
    f["pin30_tau_design"] = F_DESIGN / (4 * math.pi * d0 * d0 / 4)
    f["pin30_sig_design"] = (F_DESIGN / 4) * f["pin_arm"] / Z0
    # Stem
    As = P["STEM"] ** 2 - (P["STEM"] - 2 * P["STEM_T"]) ** 2
    f["stem_A"] = As
    f["stem_sig_design"] = F_DESIGN / As
    # Upright to beam joints: fillet welds, 4 vertical runs over the clear web height, 6 mm leg
    run = b["h"] - 2 * b["tf"]
    f["weld_len"] = 4 * run
    f["weld_tau_design"] = (F_DESIGN / 2) / (f["weld_len"] * 6 * 0.707)
    # Bolted option: 4 x M20 8.8 in double shear per joint (thread in the shear plane)
    f["bolt_tau_design"] = (F_DESIGN / 2) / (4 * 2 * 245)
    # Platen: rails at +-60 and +-170 mm, F/4 each, support at the jack
    xr = P["RAIL_X"]
    Wp = 2 * pl["Wx"]; Ip = 2 * pl["Ix"]
    for tag, F in (("rated", F_RATED), ("design", F_DESIGN)):
        M = F / 4 * (xr[0] + xr[1])
        f[f"platen_sig_{tag}"] = M / Wp
    # Mold floors and shells at the mean pressure
    rb, rt, _ = pot_outer(P)
    for tag, F in (("work", F_WORK[1]), ("rated", F_RATED), ("design", F_DESIGN)):
        p = F / (math.pi * (P["RIM_OD"] / 2) ** 2)             # MPa
        f[f"p_{tag}"] = p
        s = max(2 * xr[0], xr[1] - xr[0])
        f[f"fm_floor_sig_{tag}"] = 0.75 * p * (s / P["FM_BASE"]) ** 2
        r_tip = P["R_IN_BOT"] - P["MM_SHELL"]
        f[f"mm_tip_sig_{tag}"] = 3 * (3 + 0.33) / 8 * p * (r_tip / P["MM_TIP"]) ** 2
        f[f"fm_hoop_{tag}"] = p * rt / P["FM_SHELL"]
        f[f"mm_hoop_{tag}"] = p * P["R_IN_RIM"] / P["MM_SHELL"]
    # Axial deflection chain between the molds
    Lu = L["pin"] - (L["base0"] + L["base1"]) / 2
    Ls = L["pin"] - L["stem0"]
    for tag, F in (("work", F_WORK[1]), ("rated", F_RATED), ("design", F_DESIGN)):
        bend = F * span ** 3 / (48 * E_STEEL * I2)
        shear = F * span / (4 * G_STEEL * Aw)
        upr = (F / 2) * Lu / (E_STEEL * 2 * u["A"])
        stem = F * Ls / (E_STEEL * As)
        a_ = xr[1]; P4 = F / 4
        plat = P4 * xr[0] ** 2 * (3 * a_ - xr[0]) / (6 * E_STEEL * Ip) + P4 * a_ ** 3 / (3 * E_STEEL * Ip)
        pin = 0.05 * F / F_DESIGN * 2                             # allowance for pin bending and bearing
        tot = 2 * (bend + shear) + upr + stem + plat + pin
        f[f"defl_{tag}"] = dict(beam=bend + shear, beam_bend=bend, beam_shear=shear, upr=upr, stem=stem,
                                platen=plat, pin=pin, total=tot)
    return f


def kinematics(g, m):
    k = {}
    L = levels()
    rb, rt, _ = pot_outer(P)
    so = (rt - rb) / g["h_out"]
    v = m["charge"] / LOOSE_RHO * 1e6                            # mm3
    h = 0.0
    while frustum(rb, rb + so * h, h) < v:
        h += 0.5
    k["slug_h"] = h
    k["press_travel_need"] = h - P["WALL"] + 10.0                # plus 10 mm approach
    k["press_travel"] = P["PRESS_TRAVEL"]
    k["jack_margin"] = P["JACK_STROKE"] - P["PRESS_TRAVEL"]
    k["open_need"] = P["D_IN"] + 30.0
    k["open_have"] = P["PRESS_TRAVEL"] + P["CRANK_LIFT"]
    k["open_gap"] = L["open_gap"]
    k["load_height"] = L["fm1"] - P["PRESS_TRAVEL"]
    k["crank_turns"] = P["CRANK_LIFT"] / P["LEAD_P"]
    k["wheel_height"] = L["wheel"]
    # Jack pumping (typical 20 t bottle jack; assumed, not from a data sheet)
    ram_A = math.pi * P["RAM_D"] ** 2 / 4
    pump_d, pump_s, lever = 16.0, 22.0, 30.0
    k["jack_p_rated"] = F_RATED / ram_A
    k["lift_per_stroke"] = math.pi * pump_d ** 2 / 4 * pump_s / ram_A
    k["pump_strokes"] = P["PRESS_TRAVEL"] / k["lift_per_stroke"]
    for tag, F in (("work", F_WORK[1]), ("rated", F_RATED)):
        k[f"handle_N_{tag}"] = F / ram_A * math.pi * pump_d ** 2 / 4 / lever
    # Lead screw: Tr24 x 5, lifts the male mold and slide only
    return k


def cycle(k):
    c = {"load": 60.0, "crank_down": k["crank_turns"] / 1.5, "press": k["pump_strokes"] * 1.2,
         "dwell": 15.0, "release": 10.0, "crank_up": k["crank_turns"] / 1.5, "demold_trim": 90.0}
    c["total_s"] = sum(c.values())
    c["total_min"] = c["total_s"] / 60
    c["pots_6h"] = 6 * 3600 / c["total_s"]
    return c


def alignment():
    a = {}
    fit = P["LOC_CLEAR"] / 2
    cast = math.hypot(0.8, 0.3, 0.5)          # CT10 radius share, pattern print error, core shift
    fin = 0.3                                 # hand finished to a printed template
    a["cast_each"] = cast
    a["wall_cast"] = math.sqrt(2 * cast ** 2 + fit ** 2)
    a["wall_fin"] = math.sqrt(2 * fin ** 2 + fit ** 2)
    a["coax_fin"] = math.sqrt(fin ** 2 + fin ** 2 + fit ** 2)
    return a


def patterns():
    out = {}
    for key, d, h in (("female", P["FM_FLANGE_D"], None), ("male", P["MM_FLANGE_D"], P["D_IN"] + P["MM_FLANGE_T"])):
        if h is None:
            L = levels(); h = L["fm1"] - L["fm0"] + P["LOC_H"]
        dd, hh = d * (1 + AL_SHRINK), h * (1 + AL_SHRINK)
        n_plan = 1 if dd <= BED else (4 if dd / 2 <= BED else 8)   # whole, quadrants or octants
        tiers = math.ceil(hh / BED)
        out[key] = dict(d=dd, h=hh, plan=n_plan, tiers=tiers, n=n_plan * tiers)
    return out


def qc(g):
    q = {}
    slope = (P["R_IN_RIM"] - P["R_IN_BOT"]) / P["D_IN"]
    h0 = P["D_IN"] - 10.0

    def vol(h):
        return frustum(P["R_IN_BOT"], P["R_IN_BOT"] + slope * h, h) / 1e6

    def drop(Q):
        lo, hi = 0.0, h0
        for _ in range(60):
            mid = (lo + hi) / 2
            if vol(h0) - vol(h0 - mid) < Q:
                lo = mid
            else:
                hi = mid
        return lo
    q["fill"] = vol(h0)
    q["area_top"] = math.pi * (P["R_IN_BOT"] + slope * h0) ** 2 / 1e6
    for Q in (0.1, 1.0, 2.5, 3.0):
        q[f"drop_{Q}"] = drop(Q)
    q["res_0.1_at_1"] = drop(1.1) - drop(1.0)
    q["res_0.1_at_2.5"] = drop(2.6) - drop(2.5)
    q["read_err_L"] = q["area_top"] * 1.0                        # m2 x 1 mm = L

    def mu(Tc):                                                  # Vogel equation, Pa s
        return 2.414e-5 * 10 ** (247.8 / (Tc + 273.15 - 140))
    q["mu20"], q["mu25"], q["mu30"] = mu(20), mu(25), mu(30)
    q["per_C"] = (mu(24.5) / mu(25.5) - 1) * 100
    q["ratio_30_20"] = mu(20) / mu(30)
    q["corr_20"] = mu(20) / mu(25)
    q["corr_30"] = mu(30) / mu(25)
    return q


def masses():
    """Per-item masses from the model solids."""
    from model import build_parts
    parts = build_parts()
    vol = {p[3]: 0.0 for p in parts if p[3] is not None}
    ctr = {}
    for name, shape, col, bom, exp in parts:
        if bom is None:
            continue
        vol[bom] += shape.volume / 1e9                          # m3
        ctr[bom] = shape.center()
    b = S[P["BEAM_SEC"]]
    v_guides = 2 * 29 * P["BEAM_GAP"] * b["h"] / 1e9            # UHMW guide blocks in item 3
    ms = {}
    for bom, v in vol.items():
        rho = {8: RHO_AL, 9: RHO_AL, 11: 1640.0, 12: RHO_PLY, 13: 1270.0, 14: 950.0}.get(bom, RHO_ST)
        ms[bom] = v * rho
    ms[3] -= v_guides * (RHO_ST - RHO_UHMW)
    # QC rack: legs are steel angle 40 x 40 x 4 (2.42 kg/m), shelves plywood; recompute legs as angle
    leg_len = 4 * P["QC_SHELF_Z"] / 1000
    leg_vol = 4 * P["QC_LEG"] ** 2 * P["QC_SHELF_Z"] / 1e9
    ms[12] = (vol[12] - leg_vol) * RHO_PLY + leg_len * 2.42 + 4 * 2 * 0.78 * 2.42   # plus shelf edge angles
    ms[4] = 13.0                                                # typical 20 t bottle jack (massing solid overstates it)
    ms[6] = 2 * 0.3                                             # two tension springs
    ms[14] = 4 * 0.9                                            # 20 L HDPE bucket, about 0.9 kg each
    ms[11] = None
    return ms, ctr


def tipping(ms, ctr):
    t = {}
    press = [i for i in range(1, 11)]
    M = sum(ms[i] for i in press)
    cy = sum(ms[i] * ctr[i].Y for i in press) / M
    cz = sum(ms[i] * ctr[i].Z for i in press) / M
    t["mass"], t["cg_y"], t["cg_z"] = M, cy, cz
    moving = ms[8] + 7.4 + 8.0                                   # female mold, charge, carriage frame
    cy_out = (M * cy - moving * P["CARRIAGE_OUT"]) / M
    edge = -P["FOOT_L"] / 2
    t["cg_y_out"] = cy_out
    t["restoring_Nm"] = M * G * (cy_out - edge) / 1000
    t["push_N_at_1m"] = t["restoring_Nm"] / 1.0
    return t


def costs(ms, pat):
    c = {}
    steel = lambda i: ms[i] * STEEL_USD_KG
    c[1] = steel(1); c[2] = steel(2); c[3] = steel(3) + 8.0   # UHMW guide liners
    c[4] = 60.0
    c[5] = steel(5)
    c[6] = 2 * 5.0
    c[7] = steel(7) + 8.0                                       # UHMW slide strips
    for i in (8, 9):
        c[i] = ms[i] * POUR_FACTOR * AL_SCRAP_USD_KG + ms[i] * FOUNDRY_USD_KG
    pin_kg = math.pi * (P["PIN_D"] / 2) ** 2 * P["PIN_L"] / 1e9 * RHO_ST
    c[10] = (ms[10] - pin_kg) * STEEL_USD_KG + 15.0 + 25.0 + 12.0   # pin bar, Tr24 screw and nut, handwheel
    c[12] = 45.0; c[13] = 4 * 2.0; c[14] = 4 * 4.0
    pla = (ms[8] + ms[9]) / RHO_AL * (1 + AL_SHRINK) ** 3 * PATTERN_FILL * PLA_RHO
    c["pla_kg"] = pla
    c[15] = pla * PLA_USD_KG + 10.0
    c[16] = 55.0; c[17] = 10.0; c[18] = 45.0; c[19] = 12.0
    c["total"] = sum(v for k, v in c.items() if isinstance(k, int))
    c["press"] = sum(c[i] for i in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 16, 17, 18))
    c["qc"] = sum(c[i] for i in (12, 13, 14, 19))
    c["pin_kg"] = pin_kg
    return c


def bom_total():
    rows = list(csv.DictReader((ROOT / "bom/bom.csv").open()))
    tot = sum(float(r["qty"]) * float(r["unit_cost_usd"]) for r in rows)
    press = sum(float(r["qty"]) * float(r["unit_cost_usd"]) for r in rows
                if int(r["item"].split()[0]) in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 16, 17, 18))
    return tot, press, len(rows)


def budget():
    for line in (ROOT / "project.yaml").read_text().splitlines():
        if line.startswith("budget_usd:"):
            return float(line.split(":")[1].split("#")[0])
    return float("nan")


def main():
    g = geometry(); m = mix(g); f = frame(); k = kinematics(g, m); c = cycle(k)
    a = alignment(); pat = patterns(); q = qc(g)
    ms, ctr = masses(); t = tipping(ms, ctr); cost = costs(ms, pat)
    L = levels()
    bt, bp, nrows = bom_total(); bud = budget()

    print("PPR-CAL-001 PotPress sizing (all values estimates)\n")
    print("1 Filter geometry")
    print(f"  outer floor radius {g['r_out_bot']:.1f} mm, outer rim radius {g['r_out_top']:.1f} mm, outer depth {g['h_out']:.0f} mm, wall slope {g['slope_deg']:.1f} deg")
    print(f"  volume to brim {g['v_brim']:.2f} L; working volume (40 mm below rim) {g['v_work']:.2f} L")
    print(f"  wall and rim volume {g['v_wall']:.2f} L; projected area {g['a_proj']:.4f} m2")
    print("2 Mix and masses")
    print(f"  mix density, no air {m['rho_solid']:.2f} kg/L; pressed at {AIR*100:.0f} % air {m['rho_pressed']:.2f} kg/L; husk {m['husk_vol_frac']*100:.0f} % by volume")
    print(f"  pressed pot {m['pressed']:.2f} kg; charge {m['charge']:.2f} kg (trim {m['trim']:.2f} kg)")
    print(f"  dried {m['dried']:.2f} kg (drying loss {m['drying_loss']:.2f}); fired {m['fired']:.2f} kg (firing loss {m['firing_loss']:.2f})")
    print(f"  passes QC {m['passed']:.2f} kg per pot made (rejects {m['reject']:.2f} kg at {REJECT*100:.0f} %)")
    print("3 Force and pressure")
    for tag, F in (("5 t", F_WORK[0]), ("10 t", F_WORK[1]), ("20 t", F_RATED), ("30 t (1.5 x)", F_DESIGN)):
        print(f"  {tag:13s} {F/1000:6.1f} kN  mean pressure {F/g['a_proj']/1e6:5.2f} MPa")
    print("4 Frame and load path (two channels per beam, span %.0f mm)" % P["SPAN"])
    print(f"  beam {P['BEAM_SEC']} pair W = {f['beam_W_cm3']:.0f} cm3")
    for tag, lab in (("work", "10 t"), ("rated", "20 t"), ("design", "30 t")):
        print(f"  {lab}: beam M {f['beam_M_'+tag]:.1f} kN m, bending {f['beam_sig_'+tag]:.0f} MPa, web shear {f['beam_tau_'+tag]:.0f} MPa; uprights {f['upr_sig_'+tag]:.0f} MPa")
    print(f"  pin {P['PIN_D']:.0f} mm, lever arm {f['pin_arm']:.2f} mm: rated M {f['pin_M_rated']:.2f} kN m, bending {f['pin_sig_rated']:.0f} MPa; design bending {f['pin_sig_design']:.0f} MPa, shear {f['pin_tau_design']:.0f} MPa (yield {FY_PIN:.0f})")
    print(f"  pin bearing on web plus doubler {f['pin_brg_web_design']:.0f} MPa (web alone {f['pin_brg_web_nodbl_design']:.0f}); on pin block {f['pin_brg_blk_design']:.0f} MPa; tear-out, ligament {f['pin_ligament']:.1f} mm, {f['pin_tear_design']:.0f} MPa")
    print(f"  TRL 2 pins (2 x 30 mm) at 30 t: shear {f['pin30_tau_design']:.0f} MPa, bending {f['pin30_sig_design']:.0f} MPa")
    print(f"  stem SHS {P['STEM']:.0f} x {P['STEM_T']:.0f}: A {f['stem_A']:.0f} mm2, {f['stem_sig_design']:.0f} MPa at 30 t")
    print(f"  upright joint welds {f['weld_len']:.0f} mm of 6 mm fillet: {f['weld_tau_design']:.0f} MPa at 30 t (allow {WELD_ALLOW:.0f}); bolted option 4 x M20 8.8 double shear {f['bolt_tau_design']:.0f} MPa")
    print(f"  platen {P['PLATEN_SEC']} pair: {f['platen_sig_rated']:.0f} MPa at 20 t, {f['platen_sig_design']:.0f} MPa at 30 t")
    for tag, lab in (("work", "10 t"), ("rated", "20 t"), ("design", "30 t")):
        print(f"  {lab}: p {f['p_'+tag]:.2f} MPa; female floor {f['fm_floor_sig_'+tag]:.0f} MPa, male tip {f['mm_tip_sig_'+tag]:.0f} MPa, hoop female {f['fm_hoop_'+tag]:.0f} / male {f['mm_hoop_'+tag]:.0f} MPa (cast Al yield about {FY_AL:.0f})")
    for tag, lab in (("work", "10 t"), ("rated", "20 t"), ("design", "30 t")):
        d = f["defl_" + tag]
        print(f"  deflection at {lab}: each beam {d['beam']:.2f} (bending {d['beam_bend']:.2f}, shear {d['beam_shear']:.2f}), uprights {d['upr']:.2f}, stem {d['stem']:.2f}, platen {d['platen']:.2f}, pin {d['pin']:.2f}; total {d['total']:.2f} mm")
    u100 = S["UPN100"]; u200 = dict(Ix=1910e4, h=200, tw=8.5)
    print(f"  TRL 2 base beam, one UPN 100: {F_DESIGN * P['SPAN'] / 4 / u100['Wx']:.0f} MPa at 30 t")
    d200 = 2 * (F_DESIGN * P['SPAN'] ** 3 / (48 * E_STEEL * 2 * u200['Ix']) + F_DESIGN * P['SPAN'] / (4 * G_STEEL * 2 * u200['h'] * u200['tw']))
    dd = f["defl_design"]
    print(f"  with 2 x UPN 200 beams: total {d200 + dd['total'] - 2 * dd['beam']:.2f} mm at 30 t; extra steel {2 * 2 * P['BEAM_L'] / 1000 * (25.3 - 18.8):.1f} kg")
    rb, rt, h_out = pot_outer(P)
    Lv = levels()
    v_fs = math.pi * (P["FM_FLANGE_D"] / 2) ** 2 * (Lv["fm1"] - Lv["fm0"]) - frustum(rb, rt, h_out) - math.pi * ((P["RIM_OD"] / 2) ** 2 - rt ** 2) * P["RIM_T"]
    v_ms = frustum(P["R_IN_BOT"], P["R_IN_RIM"], P["D_IN"]) + math.pi * (P["MM_FLANGE_D"] / 2) ** 2 * P["MM_FLANGE_T"]
    print(f"  solid (not shelled) molds would weigh: female {v_fs / 1e9 * RHO_AL:.0f} kg, male {v_ms / 1e9 * RHO_AL:.0f} kg")
    print("5 Travel and jack")
    print(f"  loose charge slug height {k['slug_h']:.0f} mm; pressing travel needed {k['press_travel_need']:.0f} mm; used {k['press_travel']:.0f} of {P['JACK_STROKE']:.0f} mm stroke (margin {k['jack_margin']:.0f})")
    print(f"  opening: need {k['open_need']:.0f} mm, have {k['open_have']:.0f} mm; male tip {k['open_gap']:.0f} mm above female rim when open")
    print(f"  loading height (female rim, platen down) {k['load_height']:.0f} mm; crank {k['crank_turns']:.0f} turns each way; handwheel at {k['wheel_height']:.0f} mm")
    dm = P["LEAD_D"] - P["LEAD_P"] / 2
    print(f"  lead screw Tr{P['LEAD_D']:.0f} x {P['LEAD_P']:.0f}: lead angle {math.degrees(math.atan(P['LEAD_P'] / (math.pi * dm))):.1f} deg, friction angle {math.degrees(math.atan(0.15)):.1f} deg at mu 0.15")
    print(f"  jack pressure at 20 t {k['jack_p_rated']:.0f} MPa; lift per pump stroke {k['lift_per_stroke']:.2f} mm; {k['pump_strokes']:.0f} strokes to close")
    print(f"  handle force {k['handle_N_work']:.0f} N at 10 t, {k['handle_N_rated']:.0f} N at 20 t")
    print("6 Cycle")
    print("  " + ", ".join(f"{kk} {v:.0f} s" for kk, v in c.items() if kk not in ("total_s", "total_min", "pots_6h")))
    print(f"  total {c['total_s']:.0f} s = {c['total_min']:.1f} min; {c['pots_6h']:.0f} pots per 6 h of pressing")
    print("7 Alignment and wall evenness (radial, RSS)")
    print(f"  as-cast error per mold +-{a['cast_each']:.2f} mm; wall variation as cast +-{a['wall_cast']:.2f} mm; finished to templates +-{a['wall_fin']:.2f} mm")
    print(f"  mold coaxiality with finished locating lip +-{a['coax_fin']:.2f} mm (fit {P['LOC_CLEAR']:.1f} mm diametral)")
    print("8 Casting patterns (bed %.0f mm, shrink %.1f %%)" % (BED, AL_SHRINK * 100))
    for kk, v in pat.items():
        print(f"  {kk}: {v['d']:.0f} dia x {v['h']:.0f} mm; {v['plan']} sectors x {v['tiers']} tiers = {v['n']} segments")
    print(f"  PLA at {PATTERN_FILL*100:.0f} % of solid mass: {cost['pla_kg']:.1f} kg")
    print("9 QC flow test")
    print(f"  fill to 10 mm below rim {q['fill']:.2f} L; surface area {q['area_top']:.4f} m2")
    print(f"  level drop: 0.1 L {q['drop_0.1']:.1f} mm, 1.0 L {q['drop_1.0']:.1f} mm, 2.5 L {q['drop_2.5']:.1f} mm, 3.0 L {q['drop_3.0']:.1f} mm")
    print(f"  0.1 L step at 1.0 L/h {q['res_0.1_at_1']:.2f} mm, at 2.5 L/h {q['res_0.1_at_2.5']:.2f} mm; 1 mm reading error = {q['read_err_L']:.3f} L")
    print(f"  viscosity 20/25/30 C: {q['mu20']*1e3:.3f}/{q['mu25']*1e3:.3f}/{q['mu30']*1e3:.3f} mPa s; {q['per_C']:.1f} % per C at 25 C")
    print(f"  flow at 30 C / flow at 20 C = {q['ratio_30_20']:.2f}; correction to 25 C: x{q['corr_20']:.3f} at 20 C, x{q['corr_30']:.3f} at 30 C")
    print("10 Masses from the model (kg)")
    print("  " + ", ".join(f"{i}: {v:.1f}" for i, v in sorted(ms.items()) if v is not None))
    frame_weld = ms[1] + ms[2] + ms[3]
    print(f"  press items 1 to 10 {t['mass']:.0f} kg; welded frame (1 to 3) {frame_weld:.0f} kg; heaviest part as handled {max(ms[1] - 2 * 0.64 * 10.6, ms[2] / 2, ms[3], ms[5], ms[8], ms[9], ms[10]):.1f} kg")
    print(f"  parts as handled (feet bolted): base beam {ms[1] - 2 * 0.64 * 10.6:.1f} kg, each foot {0.64 * 10.6:.1f} kg, each upright pair {ms[2] / 2:.1f} kg, top beam {ms[3]:.1f} kg, platen {ms[5]:.1f} kg, slide {ms[10]:.1f} kg")
    print(f"  load pin {cost['pin_kg']:.1f} kg")
    print("11 Tipping")
    print(f"  press CG y {t['cg_y']:.0f} mm, z {t['cg_z']:.0f} mm; carriage out: CG y {t['cg_y_out']:.0f} mm vs front foot edge {-P['FOOT_L']/2:.0f} mm")
    print(f"  restoring moment {t['restoring_Nm']:.0f} N m; horizontal push at 1 m height to tip forward {t['push_N_at_1m']:.0f} N")
    print("12 Envelope")
    print(f"  frame {P['BEAM_L']:.0f} x {P['FOOT_L']:.0f} mm; with the carriage rails {P['BEAM_L']:.0f} x {P['RAIL_BACK'] + P['CARRIAGE_OUT'] + P['FOOT_L'] / 2:.0f} mm; height {L['overall']:.0f} mm")
    qw = 2 * P["QC_PITCH"]
    print(f"  QC rack {qw:.0f} x {qw:.0f} x {P['QC_SHELF_Z']:.0f} mm; minimum for 4 rims in one row {4*(P['RIM_OD']+20):.0f} mm")
    print("13 Cost (USD)")
    print("  " + ", ".join(f"{i}: {v:.0f}" for i, v in cost.items() if isinstance(i, int)))
    print(f"  estimate: press {cost['press']:.0f}, QC {cost['qc']:.0f}, total {cost['total']:.0f}")
    print(f"  bom.csv: {nrows} lines, total {bt:.2f}, press {bp:.2f}, QC {bt-bp:.2f}; budget_usd {bud:.0f}; over by {bt-bud:.0f} ({(bt/bud-1)*100:.0f} %)")


if __name__ == "__main__":
    main()
