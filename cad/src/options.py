"""PotPress concept options as massing models (PPR-OPT-001, STANDARDS section 21).

Run from the repo root:  python .kit/options.py   -> media/options.png
All three options press the same reference filter between the same cast aluminium molds; they differ
in how the force is made. Sizes are first-order massing, not design geometry (option A's design
geometry is cad/src/model.py).
"""
import sys
from pathlib import Path
from build123d import Box, Cylinder, Pos, Rot

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / ".kit"))
from concept import Part  # noqa: E402

TITLE = "PotPress"
STEEL, JACK, ALU, HANDLE, CLAY = "#4B5563", "#B91C1C", "#9CA3AF", "#1F2937", "#C2410C"


def molds(z_female, z_male):
    """Female cup (450 mm flange) and male plug, in the closed position."""
    female = Pos(0, 0, z_female + 150) * Cylinder(225, 300)
    plug = Pos(0, 0, z_male + 130) * Cylinder(175, 260)
    return [Part("Female mold", female, ALU), Part("Male mold", plug, "#D1D5DB")]


def option_a():
    """Hydraulic: 20 t bottle jack under a guided platen in a bolted channel frame (current design)."""
    up = [Pos(x, 0, 900) * Box(100, 100, 1800) for x in (-370, 370)]
    beams = [Pos(0, 0, 60) * Box(840, 160, 120), Pos(0, 0, 1740) * Box(840, 160, 120)]
    jack = Pos(0, 0, 260) * Cylinder(60, 280)
    platen = Pos(0, 0, 440) * Box(480, 440, 60)
    stem = Pos(0, 0, 1460) * Cylinder(45, 400)
    return ([Part("Frame", s, STEEL) for s in up + beams] + [Part("Bottle jack", jack, JACK), Part("Platen", platen, STEEL),
            Part("Male slide", stem, STEEL)] + molds(470, 1000))


def option_b():
    """Mechanical toggle: a long hand lever drives a scissor (toggle) linkage that closes the molds."""
    base = Pos(0, 0, 40) * Box(900, 600, 80)
    posts = [Pos(x, 0, 700) * Box(80, 80, 1300) for x in (-380, 380)]
    head = Pos(0, 0, 1380) * Box(840, 160, 100)
    links = [Pos(0, 0, 1180) * Rot(0, 30, 0) * Box(60, 120, 400), Pos(0, 0, 1180) * Rot(0, -30, 0) * Box(60, 120, 400)]
    lever = Pos(500, 0, 1250) * Rot(0, -20, 0) * Box(1100, 40, 40)
    return ([Part("Frame", s, STEEL) for s in [base, head] + posts] + [Part("Toggle links", l, JACK) for l in links]
            + [Part("Hand lever", lever, HANDLE)] + molds(80, 600))


def option_c():
    """Power screw: a hand-turned capstan drives a square-thread screw down through a nut in the crown."""
    base = Pos(0, 0, 40) * Box(840, 560, 80)
    posts = [Pos(x, 0, 820) * Box(90, 90, 1560) for x in (-370, 370)]
    crown = Pos(0, 0, 1620) * Box(840, 180, 140)
    screw = Pos(0, 0, 1350) * Cylinder(40, 900)
    capstan = Pos(0, 0, 1830) * Cylinder(450, 30)
    return ([Part("Frame", s, STEEL) for s in [base, crown] + posts] + [Part("Power screw", screw, JACK),
            Part("Capstan wheel", capstan, HANDLE)] + molds(80, 600))


OPTIONS = [
    {"key": "A", "name": "Hydraulic bottle-jack press", "parts": option_a(), "scale": "person", "chosen": True,
     "principle": "20 t hand-pumped bottle jack lifts the female mold onto a fixed male mold in a bolted steel channel frame (current design)."},
    {"key": "B", "name": "Toggle (scissor) lever press", "parts": option_b(), "scale": "person",
     "principle": "A long hand lever drives a toggle linkage; force rises steeply as the links straighten at the bottom of the stroke."},
    {"key": "C", "name": "Power-screw press", "parts": option_c(), "scale": "person",
     "principle": "A capstan turns a square-thread screw through a nut in the crown, driving the male mold down; self-locking at any height."},
]
