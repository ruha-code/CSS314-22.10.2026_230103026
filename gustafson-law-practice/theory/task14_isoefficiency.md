# Isoefficiency under weak scaling

The isoefficiency function describes how total work `W` must grow with processor count `P` to keep parallel efficiency constant. In an ideal Gustafson weak-scaling program, each processor receives a fixed amount of work `w`. Therefore,

\[
W(P)=Pw=\Theta(P).
\]

If the serial fraction `α` stays constant, efficiency is

\[
E(P)=\frac{S(P)}P=1-\alpha+\frac{\alpha}{P},
\]

which approaches `1-α`. Thus, under Gustafson's assumptions, the isoefficiency function is linear: `W(P)=Θ(P)` maintains approximately constant efficiency.

This result depends on the assumptions of fixed work per processor and bounded serial overhead. If communication or synchronization grows with `P`, efficiency can fall and the workload may need to grow faster. That rate depends on the algorithm and cannot be determined from Gustafson's formula alone.
