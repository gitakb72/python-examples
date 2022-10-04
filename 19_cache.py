import time
from functools import cache

@cache
def slow_calculation(n):
    print("Function called")
    time.sleep(n)
    return n ** 2

print("Running without cache...")
start = time.perf_counter()
sq5 = slow_calculation(5)
assert sq5 == 25
end = time.perf_counter()
runtime = int((end - start) * 1e6)
print(f"Time taken: {runtime}µs")

print("---")

print("Running with cache...")
start = time.perf_counter()
sq5 = slow_calculation(5)
assert sq5 == 25
end = time.perf_counter()
runtime = int((end - start) * 1e6)
print(f"Time taken: {runtime}µs")

print("---")

info = slow_calculation.cache_info()
print(f"Cache misses: {info.misses}")  # 1 miss from first attempt
print(f"Cache hits: {info.hits}")  # 1 hit from second attempt
