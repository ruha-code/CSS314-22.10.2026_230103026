# Weak-scaling measurements

The benchmark kept `500,000` numerical work items per process and collected five runs at each worker count. The timed interval excludes pool startup. Mean and sample standard deviation are in `benchmarks/summary.csv`.

| Processes | Mean time (s) | Standard deviation (s) | Measured scaled speedup |
|---:|---:|---:|---:|
| 1 | 0.05709 | 0.00363 | 1.00 |
| 2 | 0.05860 | 0.00127 | 1.95 |
| 4 | 0.06128 | 0.00072 | 3.73 |
| 8 | 0.08678 | 0.01018 | 5.26 |
| 16 | 0.15219 | 0.01018 | 6.00 |

Scaled speedup is calculated as `P × T₁ / Tₚ`, since each configuration processes `P` times the one-process workload. Least-squares fitting of `S(P)=1+(1-α)(P-1)` gives `α_observed ≈ 0.5986`. The fitted value describes this small local benchmark and its hardware; it is not an application-independent constant.
