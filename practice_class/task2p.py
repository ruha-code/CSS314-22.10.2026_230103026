import math
import time
import threading
import numpy as np

student_id = 230103026
TOTAL_SAMPLES = 40_000_000
NUM_THREADS = 4
samples_per_thread = TOTAL_SAMPLES // NUM_THREADS
BATCH_SIZE = 50_000

print("=" * 55)
print("TASK 2 - PRNG State Bottleneck (Monte Carlo Pi)")
print("=" * 55)
print("Student ID           :", student_id)
print("Total sample points  :", f"{TOTAL_SAMPLES:,}")
print("Number of threads    :", NUM_THREADS)
print("Samples per thread   :", f"{samples_per_thread:,}")
print("=" * 55)

shared_rng = np.random.default_rng(student_id)
shared_lock = threading.Lock()
hits_shared = [0] * NUM_THREADS

def worker_shared(tid):
    local_hits = 0
    remaining = samples_per_thread
    while remaining > 0:
        current_batch = min(remaining, BATCH_SIZE)
        with shared_lock:
            points = shared_rng.random((current_batch, 2))
        local_hits += np.count_nonzero(points[:, 0]**2 + points[:, 1]**2 <= 1.0)
        remaining -= current_batch
    hits_shared[tid] = local_hits

threads = []
for tid in range(NUM_THREADS):
    t = threading.Thread(target=worker_shared, args=(tid,))
    threads.append(t)

start_time = time.perf_counter()
for t in threads:
    t.start()
for t in threads:
    t.join()
time_shared = time.perf_counter() - start_time

pi_shared = 4.0 * sum(hits_shared) / TOTAL_SAMPLES
error_shared = abs(pi_shared - math.pi)
time_shared_ms = time_shared * 1000


hits_indep = [0] * NUM_THREADS

def worker_independent(tid):
    seed = (student_id * 10) + tid
    local_rng = np.random.default_rng(seed)
    local_hits = 0
    remaining = samples_per_thread
    while remaining > 0:
        current_batch = min(remaining, BATCH_SIZE)
        points = local_rng.random((current_batch, 2))
        local_hits += np.count_nonzero(points[:, 0]**2 + points[:, 1]**2 <= 1.0)
        remaining -= current_batch
    hits_indep[tid] = local_hits

threads = []
for tid in range(NUM_THREADS):
    t = threading.Thread(target=worker_independent, args=(tid,))
    threads.append(t)

start_time = time.perf_counter()
for t in threads:
    t.start()
for t in threads:
    t.join()
time_indep = time.perf_counter() - start_time

pi_indep = 4.0 * sum(hits_indep) / TOTAL_SAMPLES
error_indep = abs(pi_indep - math.pi)
time_indep_ms = time_indep * 1000

speedup = time_shared / time_indep

print()
print("--- 1. Shared PRNG (with Mutex Lock) ---")
print(f"Computed Pi    : {pi_shared:.6f}")
print(f"Absolute Error : {error_shared:.6f}")
print(f"Wall Time      : {time_shared_ms:.2f} ms")

print()
print("--- 2. Independent PRNG (No Lock / Thread-Local State) ---")
print(f"Computed Pi    : {pi_indep:.6f}")
print(f"Absolute Error : {error_indep:.6f}")
print(f"Wall Time      : {time_indep_ms:.2f} ms")

print()
print("=" * 55)
print(f"Speedup Factor : {speedup:.2f}x faster without PRNG locking")
print("=" * 55)
