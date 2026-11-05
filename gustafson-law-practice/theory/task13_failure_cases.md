# Cases where weak scaling breaks down

## Distributed FFT

A distributed FFT uses local transforms and repeated data exchanges, often global transposes. As the global problem grows, the number of communication stages and messages increases. Network latency and congestion add time even when each processor's local data stays fixed, so total runtime is not constant.

## Breadth-first search on a power-law graph

Some vertices have far more edges than others. Expanding the graph can create larger hubs and uneven frontiers, causing processors to do different amounts of work. Concurrent updates to popular vertices also contend on shared state. The slowest partition and synchronization determine each level's time, so adding processors does not preserve runtime.

Both examples violate the ideal assumption that the parallel fraction grows with `P` while communication and imbalance stay negligible.
