# Deriving Gustafson's speedup

Normalize the parallel runtime to one unit. It consists of serial time `s` and parallel time `p`:

\[
s+p=1.
\]

The serial part takes `s` time on one processor. The parallel work takes `p` time on `P` processors, so on one processor that same work would take `Pp`. Thus the equivalent serial runtime is

\[
T_{serial}=s+Pp.
\]

Since parallel runtime is one unit, speedup is

\[
S(P)=\frac{s+Pp}{s+p}=s+Pp.
\]

Let `α=s`. From `s+p=1`, we get `p=1-α`. Substitution gives

\[
\begin{aligned}
S(P)&=\alpha+P(1-\alpha)\\
    &=P-\alpha(P-1).
\end{aligned}
\]

This is Gustafson's scaled speedup formula. At `P=1`, it gives `S(1)=1`, as expected.
