# Scaling graph algorithms

Dense linear algebra divides regular blocks among processors, so work and communication are relatively predictable. Power-law graphs are less regular.

- **BFS:** frontier sizes change by level, hubs create uneven work, and multiple edges can contend when updating the same vertex.
- **PageRank:** each iteration gathers values along irregular edges. Partition boundaries require communication, and convergence checks add global reductions.

Even with a fixed number of vertices and edges per processor, graph partitioning, cache misses, hub contention, and synchronization can grow or vary with `P`. This makes constant runtime harder to achieve than for regular dense computations.
