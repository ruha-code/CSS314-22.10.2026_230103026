# Weak scaling for a 3D stencil

For a cubic domain, computation is proportional to its volume, `N^3`, while exchange across the outer surface is proportional to `N^2`. Under weak scaling, volume grows with processor count:

\[
N^3\propto P\quad\Longrightarrow\quad N\propto P^{1/3}.
\]

The surface-to-volume ratio is

\[
\frac{N^2}{N^3}=\frac1N\propto P^{-1/3}.
\]

So the outer boundary cost becomes smaller relative to the total computation as the global domain grows. There is a practical detail: in a distributed stencil, each processor also exchanges halo cells with its neighbors. If local subdomains stay the same size, that per-processor communication-to-computation ratio stays roughly constant, rather than falling with `P`. Network contention can make it worse.
