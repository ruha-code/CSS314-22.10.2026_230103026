import time
import threading

NUM_THREADS = 4
OPS_PER_THREAD = 2_000_000
EXPECTED_TOTAL = NUM_THREADS * OPS_PER_THREAD  # 8,000,000

print("=" * 50)
print("TASK 6 - Synchronization Cost & Data Loss")
print("=" * 50)
print("Parallel threads:", NUM_THREADS)
print(f"Increments per thread: {OPS_PER_THREAD:,}")
print(f"Expected final value: {EXPECTED_TOTAL:,}")
print("=" * 50)

def yield_cpu():
    pass

counter_unsafe = 0

def worker_unsafe():
    global counter_unsafe
    for _ in range(OPS_PER_THREAD):
        current = counter_unsafe
        yield_cpu()
        counter_unsafe = current + 1

threads = []
for _ in range(NUM_THREADS):
    t = threading.Thread(target=worker_unsafe)
    threads.append(t)

start_time = time.perf_counter()
for t in threads:
    t.start()
for t in threads:
    t.join()
time_unsafe = time.perf_counter() - start_time

lost_updates = EXPECTED_TOTAL - counter_unsafe
lost_percentage = (lost_updates / EXPECTED_TOTAL) * 100.0

counter_locked = 0
lock = threading.Lock()

def worker_locked():
    global counter_locked
    for _ in range(OPS_PER_THREAD):
        with lock:
            counter_locked += 1

threads = []
for _ in range(NUM_THREADS):
    t = threading.Thread(target=worker_locked)
    threads.append(t)

start_time = time.perf_counter()
for t in threads:
    t.start()
for t in threads:
    t.join()
time_locked = time.perf_counter() - start_time

time_penalty = time_locked - time_unsafe
slowdown_factor = time_locked / time_unsafe

print()
print("--- 1. Unsynchronized Run (Race Conditions) ---")
print(f"Expected final value : {EXPECTED_TOTAL:,}")
print(f"Actual final value   : {counter_unsafe:,}")
print(f"Updates lost         : {lost_updates:,}")
print(f"Percentage lost      : {lost_percentage:.2f}%")
print(f"Execution time       : {time_unsafe:.4f} s")

print()
print("--- 2. Synchronized Run (with Mutex/Lock) ---")
print(f"Expected final value : {EXPECTED_TOTAL:,}")
print(f"Actual final value   : {counter_locked:,}")
print(f"Updates lost         : {EXPECTED_TOTAL - counter_locked} (0.00%)")
print(f"Execution time       : {time_locked:.4f} s")

print()
print("=" * 50)
print("SYNCHRONIZATION TIME PENALTY")
print("=" * 50)
print(f"Lock time penalty    : +{time_penalty:.4f} s")
print(f"Slowdown factor      : {slowdown_factor:.2f}x slower due to lock overhead")
print("=" * 50)

