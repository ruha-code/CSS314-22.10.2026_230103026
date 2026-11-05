# Gustafson's Law Practice

This repository compares fixed-size and scaled-size parallel workloads. Amdahl's Law is useful when the job stays the same size. Gustafson's Law is useful when each processor keeps a similar amount of work and the total problem grows. Weak scaling is limited when communication, memory use, imbalance, or synchronization grows with the machine.

The calculations use the task's assumptions. Where a quantity was missing, the assumption is stated in its file. The benchmark is a small local Python experiment, not a general hardware result.

## Run the scripts

Install the plotting dependency:

```bash
python -m pip install matplotlib
```

Generate strong/weak scaling data and plots (default: `P=1..65,536` by powers of two and five serial fractions):

```bash
python benchmarks/simulator.py
```

Run the weak-scaling benchmark and fit Gustafson's serial fraction:

```bash
python benchmarks/weak_scale_bench/weak_scale_bench.py --thread-counts 1,2,4,8,16 --work-items 500000 --runs 5 --output benchmarks/results.csv
python benchmarks/fit_gustafson.py --input benchmarks/results.csv --output-dir plots
```

## Contents

### Theory

| Task | File |
|---:|---|
| 01 | `theory/task01_scaling_models.md` |
| 02 | `theory/task02_derivation.md` |
| 03 | `theory/task03_serial_invariance.md` |
| 04 | `theory/task04_asymptotic_limits.md` |
| 05 | `theory/task05_historical_ncube.md` |
| 11 | `theory/task11_sun_ni_comparison.md` |
| 12 | `theory/task12_communication_penalty.md` |
| 13 | `theory/task13_failure_cases.md` |
| 14 | `theory/task14_isoefficiency.md` |
| 15 | `theory/task15_energy_scaling.md` |

### Calculations

| Task | File |
|---:|---|
| 06 | `calculations/task06_parametric_table.md` |
| 07 | `calculations/task07_tolerable_serial.md` |
| 08 | `calculations/task08_cross_divergence.md` |
| 09 | `calculations/task09_multicomponent.md` |
| 10 | `calculations/task10_memory_growth.md` |
| 16 | `calculations/task16_gemm_scaling.md` |
| 17 | `calculations/task17_stencil_scaling.md` |

### Analysis

| Task | File |
|---:|---|
| 18 | `analysis/task18_nbody_scaling.md` |
| 19 | `analysis/task19_monte_carlo.md` |
| 20 | `analysis/task20_graph_processing.md` |
| 23 | `analysis/task23_empirical_results.md` |
| 24 | `analysis/task24_hardware_audit.md` |

### Benchmarks and generated outputs

- **Task 21:** `benchmarks/simulator.py`, `benchmarks/simulator_results.csv`, and `benchmarks/simulator_comparison.png` / `.pdf`.
- **Task 22:** `benchmarks/weak_scale_bench/weak_scale_bench.py` and its run guide at `benchmarks/weak_scale_bench/README.md`.
- **Task 23:** raw runs in `benchmarks/results.csv`; fitting code in `benchmarks/fit_gustafson.py`; calculated means and standard deviations in `plots/summary.csv`; fitted value in `plots/fit_summary.txt`.
- **Task 24:** empirical comparison in `plots/scaling_comparison.png` and vector `plots/scaling_comparison.pdf`; hardware notes in `analysis/task24_hardware_audit.md`.
- **Task 25:** this repository guide.

## Main results

The ideal scaled speedup is `S(P)=P-α(P-1)`, with efficiency approaching `1-α`. The local weak-scaling experiment measured `α_observed ≈ 0.5986` over 1–16 worker processes. At higher process counts its runtime increased, showing the limits of this workload and host. The value is specific to the measured code, settings, and machine.
