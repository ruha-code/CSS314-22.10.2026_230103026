import os
import time
import threading
import numpy as np

student_id = 230103026
logical_cores = os.cpu_count() or 16
physical_cores = logical_cores // 2

print("Student ID:", student_id)
print("Logical cores:", logical_cores)
print("Physical cores used:", physical_cores)

N = 8000
np.random.seed(student_id)
matrix = np.random.random((N, N)).astype(np.float64)

chunk_size = N // physical_cores

results_a = [0.0] * physical_cores

def worker_mode_a(worker_id):
    row_start = worker_id * chunk_size
    row_end = row_start + chunk_size
    results_a[worker_id] = np.sum(matrix[row_start:row_end, :])

threads_a = []
for tid in range(physical_cores):
    t = threading.Thread(target=worker_mode_a, args=(tid,))
    threads_a.append(t)

start_a = time.perf_counter()
for t in threads_a:
    t.start()
for t in threads_a:
    t.join()
time_a = time.perf_counter() - start_a

results_b = [0.0] * physical_cores

def worker_mode_b(worker_id):
    col_start = worker_id * chunk_size
    col_end = col_start + chunk_size
    total = 0.0
    for c in range(col_start, col_end):
        total += np.sum(matrix[:, c])
    results_b[worker_id] = total

threads_b = []
for tid in range(physical_cores):
    t = threading.Thread(target=worker_mode_b, args=(tid,))
    threads_b.append(t)

start_b = time.perf_counter()
for t in threads_b:
    t.start()
for t in threads_b:
    t.join()
time_b = time.perf_counter() - start_b

runtime_a_ms = time_a * 1000
runtime_b_ms = time_b * 1000
penalty_factor = time_b / time_a

print()
print("=" * 50)
print("RESULTS: Spatial Cache Profiling")
print("=" * 50)
print(f"Mode A runtime (Row-Major)        : {runtime_a_ms:.2f} ms")
print(f"Mode B runtime (Column-Major)     : {runtime_b_ms:.2f} ms")
print(f"Cache penalty factor (Mode B / A) : {penalty_factor:.2f}x")
print("=" * 50)

