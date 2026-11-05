# Multi-phase workload

The serial phases are disk I/O and broadcast (`2%`) and synchronization (`6%`). Together they give

\[
\alpha=0.02+0.06=0.08.
\]

The remaining `92%` is parallel computation. Using `S(P)=P-0.08(P-1)`:

| Processors `P` | Calculation | Scaled speedup |
|---:|---|---:|
| 512 | `512 - 0.08(511)` | 471.12 |
| 2,048 | `2,048 - 0.08(2,047)` | 1,884.24 |

The serial phases remain in the runtime, while the parallel computation scales with processor count.
