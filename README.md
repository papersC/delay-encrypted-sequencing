# Delay-Encrypted Sequencing for Layer-2 Rollups: A Latency–Welfare Evaluation

Code accompanying the IEEE Access paper by N. Ababneh and K. Almi'ani.
It simulates MEV extraction (front-running and sandwich attacks) on a Layer-2 rollup sequencer
under delay encryption and reproduces every figure in the paper.

## Requirements

- Python 3.9 or later
- numpy, scipy, matplotlib (tested with numpy 2.5, scipy 1.18, matplotlib 3.11)

```bash
git clone https://github.com/papersC/delay-encrypted-sequencing.git
cd delay-encrypted-sequencing
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Running the experiments

```bash
python sim4.py          # all experiments + result figures (png3–png10)
python fig_intro.py     # Fig. 1  conceptual overview   -> fig_overview.png
python fig_pipeline.py  # pipeline comparison           -> png2.png
python fig_sysmodel.py  # system model diagram          -> fig_sysmodel.png
```

All outputs go to `./figures/`. To use another folder, set `OUT_DIR`:

```bash
OUT_DIR=results python sim4.py
```

The full run takes under 10 seconds on a laptop. Seeds are fixed (`42` for the main
experiments, `123` for the backtest), so results are reproducible.

## What `sim4.py` runs

| # | Experiment | Output |
|---|------------|--------|
| 1 | Main experiment: 5 delay levels (0, 250, 500, 1000, 2000 ms), 100 runs × 10,000 tx, Mann–Whitney U tests vs. baseline | `png3.png` (MEV by attack type), `png4.png` (latency) |
| 2 | Sequencer Nash equilibrium: profit-maximising hardware advantage α* per delay | `png6.png` |
| 3 | Microeconomic welfare with risk aversion ρ ∈ {0, 0.25, 0.5, 1.0} | `png7.png` |
| 4 | 365-day backtest on synthetic traces calibrated to L2 activity | `png9.png` |
| 5 | Sensitivity to sequencer advantage α ∈ {0.05, 0.15, 0.40} | `png8.png` |
| 6 | Sensitivity to MEV flow share (10%, 30%, 55%) | `png10.png` |
| 7 | Functional-form check of the extraction probability (exponential, linear, logistic) | `png5.png` |

A results summary is printed to the console. Expected output (main experiment):

```
Baseline  : MEV=23.70±0.51, Lat=251ms
Low       : MEV=10.38±0.34, Lat=502ms, Δ=-56.2%
Medium    : MEV=4.70±0.20,  Lat=750ms, Δ=-80.2%
High      : MEV=1.01±0.08,  Lat=1250ms, Δ=-95.7%
Very High : MEV=0.07±0.02,  Lat=2250ms, Δ=-99.7%
```

## Key parameters

Defined at the top of `sim4.py`:

| Parameter | Value | Meaning |
|-----------|-------|---------|
| `N_TX`, `N_RUNS` | 10,000, 100 | transactions per run, runs per setting |
| `BASE_LATENCY` | 250 ms | confirmation latency without delay |
| `MEV_FRONTRUN`, `MEV_SANDWICH` | 0.0045, 0.0120 ETH | value per successful attack |
| `FRAC_FRONTRUN` | 0.55 | share of MEV opportunities that are front-runs |
| `T_FRONT`, `T_SAND_RATIO` | 350 ms, 0.65 | decay constants of the extraction probability |
| `GAMMA_ETH`, `ALPHA_MAX` | 132 ETH, 0.60 | quadratic hardware cost, max sequencer advantage |

## Repository layout

```
sim4.py           simulation, statistics and result figures
fig_intro.py      overview figure
fig_pipeline.py   pipeline comparison figure
fig_sysmodel.py   system model figure
requirements.txt  Python dependencies
```

## Citation

If you use this code, please cite the IEEE Access paper
"Delay-Encrypted Sequencing for Layer-2 Rollups: A Latency–Welfare Evaluation" (Ababneh and Almi'ani).
