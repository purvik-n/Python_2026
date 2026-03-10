
# ============================================================
# Advanced Python - Functional Programming
# ============================================================
# Python supports functional programming paradigms via:
# map, filter, reduce, lambda, closures, currying, and more.

from functools import reduce, partial, lru_cache
from itertools import islice, chain, takewhile, dropwhile
import operator


# ------ 1. map / filter / reduce ------
numbers = list(range(1, 11))

squares    = list(map(lambda x: x ** 2, numbers))
evens      = list(filter(lambda x: x % 2 == 0, numbers))
total      = reduce(operator.add, numbers)

print("Squares:", squares)
print("Evens:  ", evens)
print("Total:  ", total)


# ------ 2. Closures ------
def make_multiplier(factor):
    """Returns a function that multiplies its arg by factor."""
    def multiplier(x):
        return x * factor   # closes over `factor`
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)
print(double(5), triple(5))   # 10  15


# ------ 3. Partial Application ------
def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube   = partial(power, exponent=3)
print(square(6), cube(3))   # 36  27


# ------ 4. Function Composition ------
def compose(*funcs):
    """Compose functions right-to-left: compose(f, g)(x) == f(g(x))."""
    def composed(x):
        result = x
        for f in reversed(funcs):
            result = f(result)
        return result
    return composed

normalize = compose(str.strip, str.lower, str.title)
print(normalize("  hELLO wORLD  "))   # "Hello World"


# ------ 5. Memoization with lru_cache ------
@lru_cache(maxsize=None)
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print([fib(i) for i in range(15)])
print(fib.cache_info())   # hits, misses, maxsize, currsize


# ------ 6. itertools recipes ------
# Chaining iterables
combined = list(chain(range(3), range(5, 8), "abc"))
print(combined)

# Take while condition holds
data = [2, 4, 6, 7, 8, 10]
print(list(takewhile(lambda x: x % 2 == 0, data)))   # [2, 4, 6]

# Drop while condition holds (then yield the rest)
print(list(dropwhile(lambda x: x % 2 == 0, data)))   # [7, 8, 10]

# Sliding window
def sliding_window(iterable, n):
    it = iter(iterable)
    window = list(islice(it, n))
    if len(window) == n:
        yield tuple(window)
    for item in it:
        window.pop(0)
        window.append(item)
        yield tuple(window)

print(list(sliding_window(range(6), 3)))
# [(0,1,2), (1,2,3), (2,3,4), (3,4,5)]
