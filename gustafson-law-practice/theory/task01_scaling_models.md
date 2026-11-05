# Amdahl's Law and Gustafson's Law

| Model | Workload as `P` increases | Main assumption |
|---|---|---|
| Amdahl | Total workload stays fixed. | The parallel part is divided among more processors. |
| Gustafson | Total workload grows with `P`. | Parallel runtime stays about constant as the problem grows. |

Amdahl's Law is called **fixed-size scaling** because the problem stays the same size. Its normalized runtime is

\[
T(P)=s+\frac{1-s}{P},
\]

where `s` is the serial fraction. As `P` approaches infinity, the parallel part gets smaller, but the serial part remains. For `s > 0`, speedup is limited to `1/s`.

Gustafson's Law is called **fixed-time scaling** because runtime is kept constant while more work is done. If `α` is the serial fraction measured on the parallel run, then

\[
S(P)=\alpha+(1-\alpha)P.
\]

Here the workload grows proportionally to `P`. For a `d`-dimensional grid, each side grows approximately as `P^{1/d}`. So Amdahl describes running the same problem faster, while Gustafson describes solving a larger problem in similar time.
