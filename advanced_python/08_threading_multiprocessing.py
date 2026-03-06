
# ============================================================
# Advanced Python - Concurrency: Threading vs Multiprocessing
# ============================================================
# Python has the GIL (Global Interpreter Lock) which means only
# one thread runs Python bytecode at a time.
#
#   threading    → great for I/O-bound tasks  (network, disk)
#   multiprocessing → great for CPU-bound tasks (heavy computation)

import threading
import multiprocessing
import time
import queue
import os


# ==================== THREADING ====================

# ------ 1. Basic Thread ------
def worker(name: str, n: int):
    print(f"[Thread {name}] started  (pid={os.getpid()})")
    time.sleep(n * 0.1)
    print(f"[Thread {name}] finished after {n*0.1:.1f}s")


threads = [threading.Thread(target=worker, args=(f"T{i}", i)) for i in range(1, 4)]
for t in threads: t.start()
for t in threads: t.join()


# ------ 2. Thread-safe queue (producer/consumer) ------
def producer(q: queue.Queue, items: list):
    for item in items:
        q.put(item)
        time.sleep(0.05)
    q.put(None)   # sentinel


def consumer(q: queue.Queue):
    while True:
        item = q.get()
        if item is None:
            break
        print(f"Consumed: {item}")
        q.task_done()


q: queue.Queue = queue.Queue()
p = threading.Thread(target=producer, args=(q, list(range(5))))
c = threading.Thread(target=consumer, args=(q,))
p.start(); c.start()
p.join(); c.join()


# ------ 3. Lock to protect shared state ------
counter = 0
lock = threading.Lock()


def increment(n: int):
    global counter
    for _ in range(n):
        with lock:
            counter += 1


threads = [threading.Thread(target=increment, args=(10_000,)) for _ in range(5)]
for t in threads: t.start()
for t in threads: t.join()
print(f"Final counter: {counter}")   # always 50000


# ==================== MULTIPROCESSING ====================

def cpu_heavy(n: int) -> int:
    """Compute sum of squares – CPU-bound."""
    return sum(i * i for i in range(n))


if __name__ == "__main__":
    numbers = [2_000_000] * 4

    # Sequential
    start = time.perf_counter()
    results = [cpu_heavy(n) for n in numbers]
    seq_time = time.perf_counter() - start

    # Parallel with Pool.map
    start = time.perf_counter()
    with multiprocessing.Pool() as pool:
        results_parallel = pool.map(cpu_heavy, numbers)
    par_time = time.perf_counter() - start

    print(f"Sequential:  {seq_time:.3f}s")
    print(f"Parallel:    {par_time:.3f}s")
    print(f"Speedup:     {seq_time / par_time:.2f}x")
    assert results == results_parallel
