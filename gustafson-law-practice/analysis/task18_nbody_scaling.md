# N-body methods under weak scaling

Assume a constant amount of work per processor and that the main force calculation is parallel. Then total work per iteration must grow proportionally to `P`.

| Method | Work per iteration | Particle count for constant work per processor |
|---|---|---|
| Direct all-pairs | `O(N^2)` | `N^2 ∝ P`, so `N ∝ P^{1/2}` |
| Barnes–Hut tree code | `O(N log N)` | `N log N ∝ P`, approximately `N ∝ P/log P` |

If initialization is a fixed serial cost, its ratio to the parallel force work falls as the workload grows in either case. Barnes–Hut adds tree construction and irregular traversal, which can introduce serial work and imbalance; its actual serial/parallel ratio depends on how those stages are parallelized. These growth rates are idealized and do not include communication costs.
