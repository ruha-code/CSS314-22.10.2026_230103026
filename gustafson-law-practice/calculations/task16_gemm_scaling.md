# Matrix dimension under weak scaling

For dense matrix multiplication, the work is proportional to `N^3`. To keep runtime constant as processor count grows, total work must grow proportionally to `P`:

\[
N^3\propto P\quad\Longrightarrow\quad N\propto P^{1/3}.
\]

Memory is proportional to `N^2`, so it grows as `P^{2/3}`.

| Processor ratio `P` | Dimension ratio `N/N_0` | Memory ratio |
|---:|---:|---:|
| 1 | 1 | 1 |
| 8 | 2 | 4 |
| 64 | 4 | 16 |
| 512 | 8 | 64 |

For example, multiplying the processor count by 8 requires doubling the matrix dimension to keep the amount of computation per processor about the same.
