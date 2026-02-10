
# ============================================================
# Advanced Python - Decorators
# ============================================================
# Decorators are a powerful pattern that allow us to wrap a
# function to extend its behaviour WITHOUT changing its code.
# They are heavily used in frameworks like Flask, Django, FastAPI.

import functools
import time


# ------ 1. Basic Decorator ------
def my_decorator(func):
    @functools.wraps(func)   # preserves __name__, __doc__ etc.
    def wrapper(*args, **kwargs):
        print(f"[Before] calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[After]  calling {func.__name__}")
        return result
    return wrapper


@my_decorator
def greet(name):
    """Say hello to someone."""
    print(f"Hello, {name}!")


greet("Purvik")


# ------ 2. Decorator with Arguments ------
def repeat(n):
    """Repeat a function call n times."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator


@repeat(3)
def shout(msg):
    print(msg.upper())


shout("python is awesome")


# ------ 3. Timing Decorator ------
def timer(func):
    """Measure execution time of a function."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__!r} took {end - start:.6f} seconds")
        return result
    return wrapper


@timer
def slow_sum(n):
    return sum(range(n))


slow_sum(1_000_000)


# ------ 4. Class-based Decorator ------
class Memoize:
    """Cache results of expensive function calls."""
    def __init__(self, func):
        self.func = func
        self.cache = {}
        functools.update_wrapper(self, func)

    def __call__(self, *args):
        if args not in self.cache:
            self.cache[args] = self.func(*args)
        return self.cache[args]


@Memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(35))   # Fast because of caching
