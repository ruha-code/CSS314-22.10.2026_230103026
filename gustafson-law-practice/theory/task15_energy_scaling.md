# Energy in a weak-scaling run

Let each of `P` nodes draw idle power `P_idle` and dynamic power `P_active` during computation. For a constant runtime `T`, total energy is

\[
E_P=P(P_{idle}+P_{active})T.
\]

On one node the energy is `E_1=(P_idle+P_active)T`, so `E_P/E_1=P`. With the same wall-clock time, weak scaling therefore uses about `P` times as much energy in this simple model. It solves a larger problem, however. The model ignores changes in power state, cooling, communication energy, and periods when some nodes are idle.
