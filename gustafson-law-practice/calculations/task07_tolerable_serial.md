# Maximum tolerable serial fraction

The required speedup is

\[
8192-\alpha(8192-1)\ge 7500.
\]

Solving for `α`:

\[
\alpha\le\frac{8192-7500}{8191}
       =\frac{692}{8191}
       \approx0.084483.
\]

Therefore, the maximum serial fraction is about **8.4483%**. At this value, `S(8192)=7500`; any larger fraction misses the target.
