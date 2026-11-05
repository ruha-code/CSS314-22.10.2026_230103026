# Weak-scaling benchmark

The Python program runs a fixed number of numerical operations per process using `multiprocessing`. It warms up the worker pool before timing, so process startup is excluded.

From the repository root, run:

```bash
python benchmarks/weak_scale_bench/weak_scale_bench.py --thread-counts 1,2,4,8,16 --work-items 500000 --runs 5 --output benchmarks/results.csv
python benchmarks/fit_gustafson.py --input benchmarks/results.csv --output-dir plots
```

The default worker counts range from 1 to the host's logical CPU count. The benchmark uses only Python's standard library; the fitting and simulator scripts require `matplotlib`.
