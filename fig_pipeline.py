#!/usr/bin/env python3
"""Figure: Pipeline comparison -- No protection vs Delay-encrypted."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

OUT = "/sessions/kind-sweet-hopper/mnt/Delay-Encrypted_Sequencing_for_Layer-2_Rollups_IEEEAccess_(Pro)/png2.png"

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times', 'Times New Roman', 'DejaVu Serif'],
})

fig, ax = plt.subplots(figsize=(8.0, 3.2))
ax.set_xlim(0, 16); ax.set_ylim(0, 6)
ax.axis('off')

C_BLUE = '#2f5b8d'
C_ORANGE = '#e08a38'
TEXT_WHITE = 'white'

def box(x, y, w, h, text, color):
    b = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.05",
                       facecolor=color, edgecolor='#333333', linewidth=1.0)
    ax.add_patch(b)
    ax.text(x+w/2, y+h/2, text, ha='center', va='center',
            fontsize=10.5, color=TEXT_WHITE, fontweight='bold')

def harrow(x1, x2, y):
    a = FancyArrowPatch((x1, y), (x2, y),
                        arrowstyle='-|>', mutation_scale=12,
                        color='#333', lw=1.0)
    ax.add_patch(a)

# Layout: labels on the left, 5 boxes spaced evenly
LEFT_X = 0.3          # row label start
BOX_W = 1.9
BOX_H = 1.3
GAP = 0.55
ROW1_Y = 4.1           # top row (No protection)
ROW2_Y = 0.8           # bottom row (Delay-encrypted)

# Row label column width
LABEL_COL_END = 3.4
FIRST_BOX_X = LABEL_COL_END + 0.15

# Row 1: No protection
ax.text(LABEL_COL_END - 0.15, ROW1_Y + BOX_H/2,
        'No protection', ha='right', va='center',
        fontsize=10.5, fontweight='bold', color='#222')

labels1 = ['Submit', 'Visible', 'Order', 'Execute', 'Confirm']
x = FIRST_BOX_X
xs_row1 = []
for t in labels1:
    box(x, ROW1_Y, BOX_W, BOX_H, t, C_BLUE)
    xs_row1.append((x, x+BOX_W))
    x += BOX_W + GAP
for i in range(len(xs_row1)-1):
    harrow(xs_row1[i][1]+0.05, xs_row1[i+1][0]-0.05, ROW1_Y + BOX_H/2)

# Row 2: Delay-encrypted
ax.text(LABEL_COL_END - 0.15, ROW2_Y + BOX_H/2,
        'Delay-encrypted', ha='right', va='center',
        fontsize=10.5, fontweight='bold', color='#222')

labels2 = ['Submit', 'Concealed', 'Reveal', 'Order', 'Confirm']
colors2 = [C_BLUE, C_ORANGE, C_ORANGE, C_BLUE, C_BLUE]
x = FIRST_BOX_X
xs_row2 = []
for t, c in zip(labels2, colors2):
    box(x, ROW2_Y, BOX_W, BOX_H, t, c)
    xs_row2.append((x, x+BOX_W))
    x += BOX_W + GAP
for i in range(len(xs_row2)-1):
    harrow(xs_row2[i][1]+0.05, xs_row2[i+1][0]-0.05, ROW2_Y + BOX_H/2)

fig.savefig(OUT, dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("png2.png saved:", OUT)
