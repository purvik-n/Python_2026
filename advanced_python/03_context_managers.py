
# ============================================================
# Advanced Python - Context Managers
# ============================================================
# Context managers handle resource setup and teardown automatically.
# The `with` statement ensures cleanup even if an exception occurs.

from contextlib import contextmanager, asynccontextmanager
import time


# ------ 1. Class-based Context Manager ------
class Timer:
    """Context manager to time a code block."""

    def __enter__(self):
        self._start = time.perf_counter()
        return self   # bound to `as` variable

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.perf_counter() - self._start
        print(f"Elapsed: {elapsed:.4f}s")
        return False   # don't suppress exceptions


with Timer() as t:
    total = sum(range(1_000_000))
print(f"Sum: {total}")


# ------ 2. Generator-based Context Manager ------
@contextmanager
def managed_resource(name):
    print(f"Acquiring: {name}")
    try:
        yield name.upper()   # what gets bound to `as`
    finally:
        print(f"Releasing: {name}")   # runs even on exception


with managed_resource("database connection") as res:
    print(f"Using: {res}")


# ------ 3. Nested Context Managers ------
@contextmanager
def temp_directory():
    import tempfile, shutil, os
    path = tempfile.mkdtemp()
    print(f"Created temp dir: {path}")
    try:
        yield path
    finally:
        shutil.rmtree(path)
        print("Cleaned up temp dir.")


with temp_directory() as tmp:
    # Simulate writing a file
    file_path = f"{tmp}/data.txt"
    with open(file_path, "w") as f:
        f.write("Hello from context manager!\n")
    with open(file_path) as f:
        print(f.read())


# ------ 4. Suppress specific exceptions ------
from contextlib import suppress

with suppress(FileNotFoundError):
    open("this_file_does_not_exist.txt")   # won't crash
print("Continued after suppressed error.")


# ------ 5. ExitStack - Dynamic context managers ------
from contextlib import ExitStack

files = ["a.txt", "b.txt", "c.txt"]
with ExitStack() as stack:
    handles = [stack.enter_context(open(f, "w")) for f in files]
    for i, fh in enumerate(handles):
        fh.write(f"File {i}\n")
print("All files written and closed via ExitStack.")
