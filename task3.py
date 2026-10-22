import os
import time
import threading

N = (os.cpu_count() or 16) // 2
ITERATIONS = 50_000_000

print(f"Physical cores (N): {N}")
print(f"Iterations per thread: {ITERATIONS:,}")

shared_counts = [0] * N

def worker_unpadded(i):
    for _ in range(ITERATIONS):
        shared_counts[i] += 1

threads = [threading.Thread(target=worker_unpadded, args=(i,)) for i in range(N)]

start = time.perf_counter()
for t in threads:
    t.start()
for t in threads:
    t.join()
time_unpadded = time.perf_counter() - start


shared_counts_local = [0] * N

def worker_local(i):
    local_val = 0
    for _ in range(ITERATIONS):
        local_val += 1
    shared_counts_local[i] = local_val

threads = [threading.Thread(target=worker_local, args=(i,)) for i in range(N)]

start = time.perf_counter()
for t in threads:
    t.start()
for t in threads:
    t.join()
time_local = time.perf_counter() - start


ratio = time_unpadded / time_local

print()
print("=" * 45)
print("RESULTS: Unpadded Shared vs Padded/Local")
print("=" * 45)
print(f"Unpadded Shared Time : {time_unpadded:.4f} s")
print(f"Padded/Local Time    : {time_local:.4f} s")
print(f"Execution Ratio      : {ratio:.2f}x")
print("=" * 45)
