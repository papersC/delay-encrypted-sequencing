#!/usr/bin/env python3
"""System model diagram with all components."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

fig, ax = plt.subplots(figsize=(7.5, 5.5))
ax.set_xlim(0, 10); ax.set_ylim(0, 7.2)
ax.axis('off')

C_BLUE='#1f4e79'; C_TEAL='#2e75b6'; C_GREEN='#548235'
C_RED='#c00000'; C_ORANGE='#ed7d31'
C_LIGHT='#dce6f1'; C_LIGHTRED='#fce4e4'; C_LIGHTGREEN='#e2efda'

def box(x, y, w, h, text, ec, fc, fs=7, bold=False):
    b = FancyBboxPatch((x,y), w, h, boxstyle="round,pad=0.06", facecolor=fc, edgecolor=ec, lw=1.2)
    ax.add_patch(b)
    ax.text(x+w/2, y+h/2, text, ha='center', va='center', fontsize=fs, color=ec, 
            fontweight='bold' if bold else 'normal')

def arr(x1,y1,x2,y2, c='#333', lw=1.2, style='->'):
    ax.annotate('', xy=(x2,y2), xytext=(x1,y1), arrowprops=dict(arrowstyle=style, color=c, lw=lw))

def lbl(x,y,t,fs=6,c='#555',ha='center'):
    ax.text(x,y,t,ha=ha,va='center',fontsize=fs,color=c,style='italic')

# Title
ax.text(5, 7.0, 'System Model: Delay-Encrypted Rollup with Strategic Sequencer', 
        ha='center', fontsize=9.5, fontweight='bold', color=C_BLUE)

# ─── Layer: Users ───
ax.text(0.3, 6.35, 'User Layer', fontsize=7, color='#777', fontweight='bold')
for i, (lbl_t, x) in enumerate([('User 1\ntx₁', 0.5), ('User 2\ntx₂', 2.0), ('User N\ntxₙ', 3.5)]):
    box(x, 5.7, 1.1, 0.55, lbl_t, C_BLUE, C_LIGHT, fs=6.5)
ax.text(3.05, 5.97, '...', fontsize=12, ha='center', va='center', color='#888')

# Arrows down to encryption
for x in [1.05, 2.55, 4.05]:
    arr(x, 5.7, x, 5.35, C_BLUE, 0.8)

# ─── Encryption box ───
box(0.3, 4.6, 4.5, 0.7, 'Time-Lock Encryption  (puzzle difficulty = δ)', C_ORANGE, '#fff3e0', fs=7, bold=True)
lbl(5.3, 4.95, 'E(txᵢ) = Enc(txᵢ, δ)', fs=6.5, c=C_ORANGE, ha='left')

arr(2.55, 4.6, 2.55, 4.25, C_ORANGE, 0.8)

# ─── Encrypted Mempool ───
box(0.3, 3.5, 4.5, 0.7, 'Encrypted Mempool  [E(tx₁), E(tx₂), ..., E(txₙ)]', C_TEAL, '#e8f0fe', fs=6.5, bold=True)

arr(4.8, 3.85, 5.5, 3.85, C_TEAL, 1.0)

# ─── Sequencer block (right side) ───
# Big sequencer box
b = FancyBboxPatch((5.5, 2.5), 4.2, 2.2, boxstyle="round,pad=0.1", facecolor=C_LIGHTRED, edgecolor=C_RED, lw=1.5)
ax.add_patch(b)
ax.text(7.6, 4.45, 'Centralized Sequencer', ha='center', fontsize=8, fontweight='bold', color=C_RED)

# Sub-boxes inside sequencer
box(5.8, 3.7, 1.7, 0.55, 'Hardware\nInvestment α', C_RED, 'white', fs=6)
box(7.8, 3.7, 1.6, 0.55, 'Puzzle Solver\nδ_eff = δ(1−α)', C_ORANGE, 'white', fs=6)
box(5.8, 2.75, 1.7, 0.65, 'MEV Strategy\nFront-run / \nSandwich', C_RED, 'white', fs=6)
box(7.8, 2.75, 1.6, 0.65, 'Profit\nΠ = R(α,δ)\n− γα²', C_ORANGE, 'white', fs=6)

arr(7.5, 3.97, 7.8, 3.97, '#666', 0.7)
arr(6.65, 3.7, 6.65, 3.4, '#666', 0.7)
arr(8.6, 3.7, 8.6, 3.4, '#666', 0.7)

# ─── Nash equilibrium annotation ───
box(5.8, 1.55, 3.8, 0.7, 'Best response: α*(δ) = argmax Π(α,δ)\nα* monotonically decreasing in δ', C_RED, '#fff0f0', fs=6.5)
arr(7.7, 2.75, 7.7, 2.25, C_RED, 0.9)

# ─── L1 Settlement ───
box(0.3, 1.55, 4.5, 0.7, 'L1 Base Chain Settlement (Ethereum)', C_GREEN, C_LIGHTGREEN, fs=7, bold=True)

# Arrow from sequencer output down to L1
arr(5.5, 3.0, 4.8, 2.1, C_GREEN, 1.0)
lbl(4.8, 2.65, 'ordered\nbatch', fs=5.5, c=C_GREEN)

# ─── Welfare at bottom ───
box(0.3, 0.25, 9.4, 0.95, '', C_BLUE, '#f0f4fa')
ax.text(5.0, 0.88, 'User Welfare:  W = 1 − E[M/M_max] − ρ·Var[M/M_max] − c·(l - l_0)', 
        ha='center', fontsize=7.5, fontweight='bold', color=C_BLUE, family='serif')
ax.text(5.0, 0.48, 'Risk-neutral (ρ=0) ← → Risk-averse (ρ=1.0)  |  Latency cost c  |  Baseline l_0 = 250 ms',
        ha='center', fontsize=6.5, color='#555')

arr(2.55, 1.55, 2.55, 1.2, C_BLUE, 0.8)
arr(7.7, 1.55, 7.7, 1.2, C_RED, 0.8)

fig.savefig("/sessions/kind-sweet-hopper/mnt/Delay-Encrypted_Sequencing_for_Layer-2_Rollups_IEEEAccess_(Pro)/fig_sysmodel.png",
            dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("System model diagram saved.")
