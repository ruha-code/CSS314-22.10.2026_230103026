# Gustafson and Sun–Ni speedup

Gustafson's law assumes a fixed runtime and workload growth proportional to processor count:

\[
S_G(P)=\alpha+(1-\alpha)P.
\]

Sun–Ni's memory-bounded model scales the workload according to available memory. In its simplified form,

\[
S_{SN}(P)=P\frac{\bar g(P)+\alpha[1-\bar g(P)]}
{\bar g(P)+\alpha[P-\bar g(P)]},
\]

where `\bar g(P)` is the workload growth enabled by the `P`-fold memory capacity. If `\bar g(P)=P`, the formula reduces to Gustafson's law. If work grows faster than memory (for example, matrix multiplication work `O(N^3)` versus storage `O(N^2)`), `\bar g(P)>P` and Gustafson can underestimate achievable scaled speedup. If communication, replication, or unusable memory keeps effective workload growth below `P`, Gustafson can overestimate it.

Sun and Ni's model makes the memory constraint explicit, while Gustafson's law fixes runtime. The memory growth function and communication costs depend on the application and machine. [Sun and Ni, “Scalable Problems and Memory-Bounded Speedup” (1993)](https://www.cs.iit.edu/~scs/psfiles/scalable93.pdf).
