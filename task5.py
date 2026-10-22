import os
import time
import threading
import numpy as np

a = 2.5
b = 1.0


logical_cores = os.cpu_count() or 16
physical_cores = logical_cores // 2
num_threads = logical_cores

print(f"CPU cores: {physical_cores} physical / {logical_cores} logical")
print("Worker threads:", num_threads)


sizes = [100, 1000, 10000, 100000, 1000000, 10000000]

print()
print("=" * 65)
print("TASK 5 - The Overhead Crossover Point")
print("Vector operation: y[i] = a * x[i] + b")
print("=" * 65)
print(f"{'N (Size)':<12} | {'Serial (ms)':<14} | {'Parallel (ms)':<14} | {'Status':<8} | {'Speedup':<8}")
print("-" * 65)

results = []

for N in sizes:
    x = np.ones(N, dtype=np.float64)
    y_serial = np.empty(N, dtype=np.float64)
    y_parallel = np.empty(N, dtype=np.float64)

    start = time.perf_counter()
    y_serial[:] = a * x + b
    time_serial = time.perf_counter() - start

    chunk = N // num_threads

    def worker(tid):
        start_idx = tid * chunk
        end_idx = start_idx + chunk if tid != num_threads - 1 else N
        y_parallel[start_idx:end_idx] = a * x[start_idx:end_idx] + b

    threads = []
    for tid in range(num_threads):
        t = threading.Thread(target=worker, args=(tid,))
        threads.append(t)

    start = time.perf_counter()
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    time_parallel = time.perf_counter() - start

    speedup = time_serial / time_parallel
    if time_parallel < time_serial:
        status = "FASTER"
    else:
        status = "SLOWER"

    results.append({
        "N": N,
        "serial": time_serial,
        "parallel": time_parallel,
        "status": status,
        "speedup": speedup
    })

    print(f"{N:<12,d} | {time_serial * 1000:<14.4f} | {time_parallel * 1000:<14.4f} | {status:<8} | {speedup:6.2f}x")

crossover_start = None
crossover_end = None

for i in range(len(results) - 1):
    if results[i]["status"] == "SLOWER" and results[i + 1]["status"] == "FASTER":
        crossover_start = results[i]["N"]
        crossover_end = results[i + 1]["N"]
        break

print("=" * 65)
print("\nExact Crossover Range on this hardware:")
if crossover_start is not None and crossover_end is not None:
    print(f"-> Multi-threading shifts from SLOWER to FASTER between N = {crossover_start:,} and N = {crossover_end:,}")
else:
    print("-> No crossover point detected in the tested range.")
