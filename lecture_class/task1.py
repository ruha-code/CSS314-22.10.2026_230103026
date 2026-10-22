
import os
import platform
import time
import numpy as np

student_id = 230103026

print("Student ID:", student_id)
print("OS:", platform.system())
print("CPU:", platform.processor())
print("Logical cores:", os.cpu_count())

np.random.seed(student_id)
arr = np.random.random(20_000_000).astype(np.float64)

start = time.perf_counter()

total = np.sum(arr)
std = np.std(arr)

end = time.perf_counter()

print("Array size:", len(arr))
print("Sum:", total)
print("Standard deviation:", std)
print("Execution time:", (end - start) * 1000, "ms")
