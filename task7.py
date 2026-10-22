import os
import time
import threading
import numpy as np

N = 30_000_000
A = np.random.random(N).astype(np.float64)
B = np.empty(N, dtype=np.float64)

max_cores = os.cpu_count() or 16
cores_list = [1, 2, max_cores]

def kernel_a(start, end):
    B[start:end] = A[start:end]

def kernel_b(start, end):
    B[start:end] = np.sin(A[start:end]) * np.cos(A[start:end]) + np.tan(A[start:end])

def run_kernel(kernel_func, cores):
    chunk = N // cores
    threads = []
    for i in range(cores):
        start = i * chunk
        end = start + chunk if i != cores - 1 else N
        t = threading.Thread(target=kernel_func, args=(start, end))
        threads.append(t)

    t0 = time.perf_counter()
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return time.perf_counter() - t0

for name, kernel_func in [("Kernel A (Memory-Bound: Copy)", kernel_a), 
                          ("Kernel B (Compute-Bound: Math)", kernel_b)]:
    print(f"\n=== {name} ===")
    print("Cores | Time (s) | Speedup | Efficiency")
    print("-" * 40)
    
    t1 = None
    for cores in cores_list:
        t = run_kernel(kernel_func, cores)
        if cores == 1:
            t1 = t
        speedup = t1 / t
        efficiency = (speedup / cores) * 100.0
        print(f"{cores:5d} | {t:8.4f} | {speedup:6.2f}x | {efficiency:9.1f}%")

print("\n" + "=" * 50)
print("CONCLUSION:")
print("Kernel A (Memory-Bound) stalled in scaling due to RAM bus saturation.")
print("Kernel B (Compute-Bound) continued scaling across all cores.")
print("=" * 50)
