#!/usr/bin/env python3
"""Redesigned Figure 1 - clean conceptual overview of delay-encrypted sequencing."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

import os
OUT_DIR = os.environ.get("OUT_DIR", "figures")
os.makedirs(OUT_DIR, exist_ok=True)
OUT = os.path.join(OUT_DIR, "fig_overview.png")

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times', 'Times New Roman', 'DejaVu Serif'],
})

fig, ax = plt.subplots(figsize=(7.2, 4.2))
ax.set_xlim(0, 12); ax.set_ylim(0, 7.2)
ax.axis('off')

# Palette
C_BLUE = '#1f4e79'; C_TEAL = '#2e75b6'; C_GREEN = '#548235'
C_RED = '#c00000'; C_ORANGE = '#ed7d31'
F_BLUE = '#dce6f1'; F_TEAL = '#e8f0fe'; F_GREEN = '#e2efda'
F_RED = '#fce4e4'; F_ORANGE = '#fff3e0'

def box(x, y, w, h, text, edge, fill, fs=8.5, bold=True):
    b = FancyBboxPatch((x, y), w, h,
                       boxstyle="round,pad=0.10,rounding_size=0.12",
                       facecolor=fill, edgecolor=edge, linewidth=1.3)
    ax.add_patch(b)
    weight = 'bold' if bold else 'normal'
    ax.text(x + w/2, y + h/2, text, ha='center', va='center',
            fontsize=fs, color=edge, fontweight=weight)

def harrow(x1, x2, y, color='#555555'):
    a = FancyArrowPatch((x1, y), (x2, y),
                        arrowstyle='-|>', mutation_scale=14,
                        color=color, lw=1.3)
    ax.add_patch(a)

def small_label(xc, y, text, color):
    ax.text(xc, y, text, ha='center', va='center',
            fontsize=7, color=color, style='italic')

# ── Pipeline (single row) ────────────────────────────────────────────
y0 = 3.8       # row bottom
h  = 1.5       # box height

# Box widths and positions
specs = [
    (0.2,  2.0, 'Users', C_BLUE,   F_BLUE),
    (2.7,  2.2, 'Encrypted\nMempool', C_TEAL, F_TEAL),
    (5.6,  2.2, 'Delay $\\delta$\n(time-lock)', C_ORANGE, F_ORANGE),
    (8.5,  2.2, 'Sequencer\norders batch', C_RED, F_RED),
    (11.0, 0.9, 'L1', C_GREEN, F_GREEN),
]

# Reposition to fit 0..12
x_positions = [0.15, 2.55, 5.25, 7.95, 10.75]
widths      = [2.20, 2.40, 2.40, 2.40, 1.10]
labels      = ['Users', 'Encrypted\nMempool', 'Delay $\\delta$\n(time-lock)',
               'Sequencer\norders batch', 'L1']
edges       = [C_BLUE, C_TEAL, C_ORANGE, C_RED, C_GREEN]
fills       = [F_BLUE, F_TEAL, F_ORANGE, F_RED, F_GREEN]

for x, w, t, ec, fc in zip(x_positions, widths, labels, edges, fills):
    box(x, y0, w, h, t, ec, fc, fs=9)

# Arrows between boxes (at mid-height of row)
ym = y0 + h/2
gaps = []
for i in range(4):
    x_end_i = x_positions[i] + widths[i]
    x_start_ii = x_positions[i+1]
    gaps.append((x_end_i + 0.05, x_start_ii - 0.05))

for (xa, xb) in gaps:
    harrow(xa, xb, ym)

# Labels above arrows
gap_labels = ['encrypt', 'wait $\\delta$', 'decrypt', 'settle']
gap_colors = [C_BLUE,    C_ORANGE,      C_RED,     C_GREEN]
for (xa, xb), lab, col in zip(gaps, gap_labels, gap_colors):
    small_label((xa+xb)/2, ym + h/2 + 0.20, lab, col)

# ── Result ribbon (below pipeline) ──────────────────────────────────
ribbon = FancyBboxPatch((0.15, 1.20), 11.70, 1.75,
                        boxstyle="round,pad=0.08,rounding_size=0.10",
                        facecolor='#f5f9ff', edgecolor=C_BLUE, linewidth=1.1)
ax.add_patch(ribbon)

ax.text(6.0, 2.55,
        'Three evaluation lenses',
        ha='center', va='center', fontsize=9.5,
        color=C_BLUE, fontweight='bold')
ax.text(6.0, 1.80,
        r'best-response $\alpha^{*}$    $\cdot$    risk-averse welfare    $\cdot$    365-day backtest',
        ha='center', va='center', fontsize=8.8, color='#333333')

# ── Headline row (topmost) ──────────────────────────────────────────
ax.text(6.0, 6.75,
        'Delay-encrypted sequencing',
        ha='center', va='center',
        fontsize=12.0, color=C_BLUE, fontweight='bold')

ax.text(6.0, 6.10,
        r'conceal transaction contents for a short, verifiable delay $\delta$',
        ha='center', va='center',
        fontsize=8.8, color='#444444', style='italic')

# ── Footer numbers ──────────────────────────────────────────────────
ax.text(6.0, 0.55,
        r'500 ms delay $\rightarrow$ 80% MEV reduction    $\cdot$    '
        r'$\alpha^{*}\!\approx\!0.026$    $\cdot$    '
        r'$\sim$34 k ETH/yr prevented',
        ha='center', va='center', fontsize=8.5, color=C_BLUE)

fig.savefig(OUT, dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("fig_overview.png saved:", OUT)
