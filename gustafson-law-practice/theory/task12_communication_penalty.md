# Adding communication overhead

Let the computation take one time unit on `P` processors, with serial fraction `α` and parallel fraction `1-α`. Its equivalent serial work is

\[
W_1=\alpha+(1-\alpha)P.
\]

If communication adds `C(P)` time units to the parallel run, its elapsed time becomes `1+C(P)`. The modified scaled speedup is therefore

\[
S_C(P)=\frac{\alpha+(1-\alpha)P}{1+C(P)}.
\]

For example, latency-dominated communication can be represented as `C(P)=c log_2 P`, while an all-to-all style cost may be approximated by `C(P)=c\sqrt{P}`. Here `c` converts the communication cost to the same time units as the normalized computation. For fixed nonzero `c`, these models give asymptotic speedups of about `P/log P` and `sqrt(P)`, respectively. The runtime is no longer constant, so speedup grows more slowly than the ideal Gustafson curve. This model assumes `C(P)` is additional to the normalized computation time.
