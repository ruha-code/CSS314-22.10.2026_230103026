import os
import platform
import time
from concurrent.futures import ThreadPoolExecutor
import numpy as np

# Student & System Information
student_id = 230103026
max_cores = os.cpu_count() or 4

print("Student ID:", student_id)
print("OS:", platform.system())
print("CPU:", platform.processor())
print("Logical cores:", max_cores)

# Generate identical random dataset as Task 1
np.random.seed(student_id)
arr = np.random.random(20_000_000).astype(np.float64)

print("Array size:", len(arr))

# Sequential baseline sum for correctness verification
seq_start = time.perf_counter()
seq_sum = np.sum(arr)
seq_end = time.perf_counter()
print("Sequential sum:", seq_sum)
print(f"Sequential execution time: {(seq_end - seq_start) * 1000:.4f} ms\n")

# Parallel summation across worker threads
def parallel_sum(array, num_workers):
    chunk_size = (len(array) + num_workers - 1) // num_workers
    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        futures = []
        for i in range(num_workers):
            start = i * chunk_size
            end = min(start + chunk_size, len(array))
            if start < end:
                futures.append(executor.submit(np.sum, array[start:end]))
        return sum(f.result() for f in futures)

# Warmup run to initialize threading subsystem
_ = parallel_sum(arr[:10000], 1)

# Benchmark worker counts: [1, 2, 4, max_cores, max_cores * 2]
worker_counts = [1, 2, 4, max_cores, max_cores * 2]
P = 0.95  # 95% parallelizable code

# Measure wall-clock time for each worker count
wall_times = {}
for workers in worker_counts:
    t_start = time.perf_counter()
    total = parallel_sum(arr, workers)
    t_end = time.perf_counter()
    wall_times[workers] = t_end - t_start

# Baseline wall-clock time T(1)
t1 = wall_times[1]

# Formatted Table Output
header = "Cores | Wall Time | Speedup | Amdahl Upper Bound"
print(header)
print("-" * len(header))

for workers in worker_counts:
    t_p = wall_times[workers]
    speedup = t1 / t_p
    amdahl_bound = 1.0 / ((1.0 - P) + (P / workers))
    print(f"{workers:5d} | {t_p:8.4f}s | {speedup:6.2f}x | {amdahl_bound:17.2f}x")

print()
print(f"Amdahl Theoretical Max Speedup (P={P}, p->inf): {1.0 / (1.0 - P):.2f}x")
