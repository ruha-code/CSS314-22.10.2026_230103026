# Speedup for `α = 0.04`

Use

\[
S(P)=P-0.04(P-1), \qquad E(P)=\frac{S(P)}{P}.
\]

For example, at `P=16`, `S=16-0.04(15)=15.4` and `E=15.4/16=0.9625`.

| Processors `P` | Scaled speedup `S(P)` | Efficiency `E(P)` |
|---:|---:|---:|
| 16 | 15.40 | 96.2500% |
| 64 | 61.48 | 96.0625% |
| 256 | 245.80 | 96.0156% |
| 1,024 | 983.08 | 96.0039% |
| 4,096 | 3,932.20 | 96.0010% |
| 16,384 | 15,728.68 | 96.0002% |

The speedup grows almost linearly with `P`. Efficiency approaches `1-α=96%`; across this range it drops by only 0.2498 percentage points.
