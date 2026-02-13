
# ============================================================
# Advanced Python - Generators & Iterators
# ============================================================
# A generator is a special function that yields values lazily.
# This saves memory because it doesn't store all values at once.

# ------ 1. Basic Generator ------
def count_up(start, stop):
    """Yield numbers from start to stop."""
    current = start
    while current <= stop:
        yield current   # pauses here and resumes on next()
        current += 1


gen = count_up(1, 5)
print(next(gen))   # 1
print(next(gen))   # 2
for val in gen:    # continues from 3
    print(val)


# ------ 2. Infinite Generator ------
def infinite_counter(start=0):
    n = start
    while True:
        yield n
        n += 1


counter = infinite_counter(10)
print([next(counter) for _ in range(5)])   # [10, 11, 12, 13, 14]


# ------ 3. Generator Expression ------
# Like list comprehension but lazy
squares_gen = (x ** 2 for x in range(1, 1_000_001))
# Doesn't allocate 1 million items in memory!
print(next(squares_gen))   # 1
print(next(squares_gen))   # 4


# ------ 4. Custom Iterator Class ------
class FibIterator:
    """Iterator that yields Fibonacci numbers up to max_val."""
    def __init__(self, max_val):
        self.max_val = max_val
        self.a, self.b = 0, 1

    def __iter__(self):
        return self   # the iterator IS the iterable

    def __next__(self):
        if self.a > self.max_val:
            raise StopIteration
        value = self.a
        self.a, self.b = self.b, self.a + self.b
        return value


for fib in FibIterator(100):
    print(fib, end=" ")
print()


# ------ 5. send() to Generator (Two-Way Communication) ------
def accumulator():
    total = 0
    while True:
        value = yield total   # send data IN, yield data OUT
        if value is None:
            break
        total += value


acc = accumulator()
next(acc)              # prime the generator
print(acc.send(10))   # 10
print(acc.send(20))   # 30
print(acc.send(5))    # 35
