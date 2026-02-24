
# ============================================================
# Advanced Python - Async / Await (asyncio)
# ============================================================
# asyncio lets you write concurrent code using coroutines.
# Great for I/O-bound tasks: network requests, DB queries, etc.

import asyncio
import time
import random


# ------ 1. Basic Coroutine ------
async def say_hello(name: str, delay: float):
    await asyncio.sleep(delay)   # non-blocking sleep
    print(f"Hello, {name}!")


# asyncio.run() is the entry point
asyncio.run(say_hello("World", 0.1))


# ------ 2. Running tasks concurrently with gather() ------
async def fetch_data(endpoint: str) -> dict:
    """Simulate an async HTTP request."""
    latency = random.uniform(0.05, 0.3)
    await asyncio.sleep(latency)
    return {"endpoint": endpoint, "status": 200, "latency": round(latency, 3)}


async def main_gather():
    endpoints = ["/users", "/products", "/orders", "/auth"]
    start = time.perf_counter()
    results = await asyncio.gather(*[fetch_data(ep) for ep in endpoints])
    elapsed = time.perf_counter() - start
    for r in results:
        print(r)
    print(f"Total time: {elapsed:.3f}s  (sequential would be ~{sum(r['latency'] for r in results):.3f}s)")


asyncio.run(main_gather())


# ------ 3. Task creation & cancellation ------
async def long_running_task(name: str):
    try:
        for i in range(10):
            print(f"{name}: step {i}")
            await asyncio.sleep(0.1)
    except asyncio.CancelledError:
        print(f"{name} was CANCELLED")
        raise   # always re-raise CancelledError


async def main_cancel():
    task = asyncio.create_task(long_running_task("MyTask"))
    await asyncio.sleep(0.35)   # let it run 3 steps
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        pass
    print("Done.")


asyncio.run(main_cancel())


# ------ 4. Async Context Manager ------
class AsyncDB:
    async def __aenter__(self):
        print("Connecting to DB…")
        await asyncio.sleep(0.05)
        return self

    async def __aexit__(self, *args):
        print("Disconnecting from DB…")
        await asyncio.sleep(0.02)

    async def query(self, sql: str):
        await asyncio.sleep(0.05)
        return [{"id": 1, "sql": sql}]


async def main_db():
    async with AsyncDB() as db:
        rows = await db.query("SELECT * FROM users")
        print(rows)


asyncio.run(main_db())


# ------ 5. Async Generator ------
async def async_range(start, stop, step=1):
    current = start
    while current < stop:
        await asyncio.sleep(0)   # yield control
        yield current
        current += step


async def main_async_gen():
    async for val in async_range(0, 5):
        print(val, end=" ")
    print()


asyncio.run(main_async_gen())
