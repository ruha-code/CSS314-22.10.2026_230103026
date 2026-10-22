import sys
import time
import threading
import numpy as np

student_id = 230103026
np.random.seed(student_id)

N = 2_000_000
NUM_THREADS = 4

print("=" * 60)
print("TASK 3 - Prefix Scan (Step Efficiency vs Work Efficiency)")
print("=" * 60)
print("Student ID       :", student_id)
print("Array size       :", f"{N:,}")
print("Parallel threads :", NUM_THREADS)
print("=" * 60)

arr = np.random.randint(1, 11, size=N, dtype=np.int64)

start_serial = time.perf_counter()
serial_output = np.cumsum(arr)
time_serial = time.perf_counter() - start_serial

chunk_size = N // NUM_THREADS
parallel_output = np.empty(N, dtype=np.int64)
chunk_sums = [0] * NUM_THREADS

def pass1_worker(worker_id):
    start_idx = worker_id * chunk_size
    end_idx = start_idx + chunk_size if worker_id != NUM_THREADS - 1 else N
    parallel_output[start_idx:end_idx] = np.cumsum(arr[start_idx:end_idx])
    chunk_sums[worker_id] = parallel_output[end_idx - 1]

def pass2_worker(worker_id, offset):
    start_idx = worker_id * chunk_size
    end_idx = start_idx + chunk_size if worker_id != NUM_THREADS - 1 else N
    parallel_output[start_idx:end_idx] += offset

start_parallel = time.perf_counter()

threads1 = []
for tid in range(NUM_THREADS):
    t = threading.Thread(target=pass1_worker, args=(tid,))
    threads1.append(t)
    t.start()
for t in threads1:
    t.join()

offsets = [0] * NUM_THREADS
for i in range(1, NUM_THREADS):
    offsets[i] = offsets[i - 1] + chunk_sums[i - 1]

threads2 = []
for tid in range(1, NUM_THREADS):
    t = threading.Thread(target=pass2_worker, args=(tid, offsets[tid]))
    threads2.append(t)
    t.start()
for t in threads2:
    t.join()

time_parallel = time.perf_counter() - start_parallel

if parallel_output[-1] != serial_output[-1]:
    print("Assertion Failed: parallel_output[-1] != serial_output[-1]")
    sys.exit(1)

status = "PASS" if parallel_output[-1] == serial_output[-1] else "FAIL"

time_serial_ms = time_serial * 1000
time_parallel_ms = time_parallel * 1000
speedup = time_serial / time_parallel

print()
header = "Serial Time (ms) | Parallel Time (ms) | Speedup | Verification Status (PASS/FAIL)"
print(header)
print("-" * len(header))
print(f"{time_serial_ms:16.2f} | {time_parallel_ms:18.2f} | {speedup:6.2f}x | {status:^32}")
