# Serial fraction in the two models

The fractions in Amdahl's and Gustafson's laws are measured in different situations. Amdahl's `s` is the serial share of a fixed job, usually compared with its one-processor runtime. Gustafson's `α` is the serial share observed during a parallel run whose workload has grown to use `P` processors.

For the parallel run normalized to one time unit, the equivalent serial work is

\[
T_1=\alpha+(1-\alpha)P,
\]

so `S(P)=P-α(P-1)`. The serial time stays roughly constant while the parallel work grows. For example, at `P=1024` and `α=0.004`, this gives `S=1019.908`.

If the same number, `0.004`, were instead a fixed-job Amdahl fraction, speedup at 1024 processors would be about `201.1`, with a limit of `250`. There is no contradiction: the two fractions describe different workloads and reference runs. A serial fraction measured on a parallel, scaled workload does not directly set the Amdahl limit for a fixed-size job.
