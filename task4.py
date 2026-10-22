import time
import threading

TOTAL_ITEMS = 1000
NUM_WORKERS = 4

print("Total items:", TOTAL_ITEMS)
print("Parallel workers:", NUM_WORKERS)

def workload(i):
    cost = 0.0001 * (i % 20)
    if cost > 0:
        time.sleep(cost)

finish_times_static = [0.0] * NUM_WORKERS

def worker_static(worker_id):
    start_index = worker_id * 250
    end_index = start_index + 250
    for i in range(start_index, end_index):
        workload(i)
    finish_times_static[worker_id] = time.perf_counter()

threads = []
for i in range(NUM_WORKERS):
    t = threading.Thread(target=worker_static, args=(i,))
    threads.append(t)

start_time = time.perf_counter()
for t in threads:
    t.start()
for t in threads:
    t.join()
static_total_time = time.perf_counter() - start_time

static_delta = max(finish_times_static) - min(finish_times_static)
next_item = 0
lock = threading.Lock()
finish_times_dynamic = [0.0] * NUM_WORKERS

def worker_dynamic(worker_id):
    global next_item
    while True:
        with lock:
            if next_item >= TOTAL_ITEMS:
                break
            item = next_item
            next_item += 1
        workload(item)
    finish_times_dynamic[worker_id] = time.perf_counter()

threads = []
for i in range(NUM_WORKERS):
    t = threading.Thread(target=worker_dynamic, args=(i,))
    threads.append(t)

start_time = time.perf_counter()
for t in threads:
    t.start()
for t in threads:
    t.join()
dynamic_total_time = time.perf_counter() - start_time

dynamic_delta = max(finish_times_dynamic) - min(finish_times_dynamic)

print()
print("Strategy A (Static Chunk Distribution):")
print("Total Execution Time :", round(static_total_time, 4), "s")
print("Thread Finish Delta  :", round(static_delta * 1000, 2), "ms")

print()
print("Strategy B (Dynamic Scheduling):")
print("Total Execution Time :", round(dynamic_total_time, 4), "s")
print("Thread Finish Delta  :", round(dynamic_delta * 1000, 2), "ms")

print()
print("Comparison:")
print("Dynamic is faster by :", round(static_total_time / dynamic_total_time, 2), "x")
print("Delta reduction      :", round(static_delta / dynamic_delta, 2), "x less imbalance")
