# Memory limit for a 3D grid

Each node has `32 GB` of memory. With `n` nodes, total memory is `32n GB`. The question does not specify bytes per grid cell, so assume one 8-byte double precision value per cell and use decimal GB (`1 GB = 10^9 bytes`). Ignoring halos and other arrays, the limit is

\[
8N^3\le 32n\times10^9,
\qquad
N_{max}=\left\lfloor\left(\frac{32n\times10^9}{8}\right)^{1/3}\right\rfloor.
\]

| Nodes `n` | Total memory | Maximum cubic dimension `N` |
|---:|---:|---:|
| 64 | 2.048 TB | 6,349 |
| 512 | 16.384 TB | 12,699 |

The node count increases by 8, so the side length doubles approximately (`8^{1/3}=2`). Actual usable dimensions would be smaller if the solver stores multiple arrays or needs halo cells.
