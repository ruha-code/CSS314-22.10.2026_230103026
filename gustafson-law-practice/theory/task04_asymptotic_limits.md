# Efficiency as processor count grows

For Gustafson's law,

\[
E_G(P)=\frac{S(P)}{P}=1-\alpha+\frac{\alpha}{P}.
\]

Therefore,

\[
\lim_{P\to\infty} E_G(P)=1-\alpha.
\]

The serial fraction still reduces efficiency, but the limit is positive when `α < 1`.

For Amdahl's law, with fixed serial fraction `s`,

\[
E_A(P)=\frac{S_A(P)}{P}=\frac{1}{sP+(1-s)}.
\]

If `s > 0`, then `\lim_{P\to\infty}E_A(P)=0`, since the denominator grows without bound. If `s=0`, efficiency remains 1. The difference comes from holding the workload fixed in Amdahl's model and expanding it in Gustafson's model.
