# Gustafson's 1024-processor results

In 1988, Gustafson, Montry, and Benner reported three scientific applications running on Sandia's 1024-processor nCUBE hypercube: wave mechanics, fluid dynamics, and structural analysis. Their paper reported fixed-size speedups of 502–637 and scaled speedups of 1009–1020 when the problem size per processor was held constant.

The scaled results came from increasing the problem with the processor count. With 1024 processors and a measured serial share around 0.4% in Gustafson's example, the formula gives

\[
S=1024-0.004(1023)=1019.908.
\]

The near-1000 speedup was possible because this was not the same fixed job used in Amdahl's model. Each processor handled a similar amount of work as the global problem grew. The authors also noted practical losses from communication, I/O, redundant work, and load imbalance; their result was close to, but below, ideal linear speedup.

The original study is Gustafson, Montry, and Benner, [“Development of Parallel Methods for a 1024-Processor Hypercube” (1988)](https://rsim.cs.illinois.edu/arch/qual_papers/systems/6.pdf). Gustafson's short explanation is in [“Reevaluating Amdahl's Law” (1988)](https://users.cs.utah.edu/~hari/teaching/paralg/Gustafson88.pdf).
