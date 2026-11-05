# Monte Carlo and reduction overhead

Monte Carlo samples are mostly independent, so each processor can generate and process its own samples. Non-parallel time still comes from setup, distributing seeds or random-number streams, combining partial sums, and writing results.

Let `α` be the serial share without a reduction penalty. Gustafson's speedup is

\[
S(P)=P-\alpha(P-1).
\]

A balanced binary reduction combines partial results in about `log_2 P` stages. If each stage costs latency `L`, the reduction takes approximately `T_{red}=L\log_2P`. Treating this as added time, with computation normalized to one time unit, gives the simple model

\[
S_{MC}(P)\approx\frac{\alpha+(1-\alpha)P}{1+L\log_2P}.
\]

For example, at `P=1024`, the tree has 10 stages and costs about `10L`. This is much better than sending every partial result to one processor in sequence, which can take `O(P)` steps, but the tree cost still lowers speedup as `P` grows. The formula assumes `L` is in units of the normalized compute time and ignores bandwidth cost.
