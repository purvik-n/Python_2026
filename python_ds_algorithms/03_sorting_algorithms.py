"""
==========================================================
  Python DS & Algorithms — Day 3: Sorting Algorithms
  Author  : Purvik
  Date    : 2026-03-14
  Topic   : Bubble, Selection, Insertion, Merge, Quick Sort
==========================================================
"""

import random
import time


# ──────────────────────────────────────────────
#  BUBBLE SORT  — O(n²) time | O(1) space
# ──────────────────────────────────────────────
def bubble_sort(arr: list) -> list:
    """Repeatedly swap adjacent elements that are out of order."""
    a = arr.copy()
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:          # already sorted — early exit
            break
    return a


# ──────────────────────────────────────────────
#  SELECTION SORT  — O(n²) time | O(1) space
# ──────────────────────────────────────────────
def selection_sort(arr: list) -> list:
    """Select the minimum element repeatedly and place it at the front."""
    a = arr.copy()
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a


# ──────────────────────────────────────────────
#  INSERTION SORT  — O(n²) time | O(1) space
# ──────────────────────────────────────────────
def insertion_sort(arr: list) -> list:
    """Build the sorted array one item at a time."""
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


# ──────────────────────────────────────────────
#  MERGE SORT  — O(n log n) time | O(n) space
# ──────────────────────────────────────────────
def merge_sort(arr: list) -> list:
    """Divide the list in half, sort each half, then merge."""
    if len(arr) <= 1:
        return arr.copy()

    mid = len(arr) // 2
    left  = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)


def _merge(left: list, right: list) -> list:
    result, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# ──────────────────────────────────────────────
#  QUICK SORT  — O(n log n) avg | O(n²) worst | O(log n) space
# ──────────────────────────────────────────────
def quick_sort(arr: list) -> list:
    """Partition around a pivot and recursively sort sub-lists."""
    if len(arr) <= 1:
        return arr.copy()
    pivot = arr[len(arr) // 2]
    left   = [x for x in arr if x <  pivot]
    middle = [x for x in arr if x == pivot]
    right  = [x for x in arr if x >  pivot]
    return quick_sort(left) + middle + quick_sort(right)


# ──────────────────────────────────────────────
#  COUNTING SORT  — O(n + k) time | O(k) space
# ──────────────────────────────────────────────
def counting_sort(arr: list) -> list:
    """Works for non-negative integers. k = max value."""
    if not arr:
        return []
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    result = []
    for val, cnt in enumerate(count):
        result.extend([val] * cnt)
    return result


# ──────────────────────────────────────────────
#  BENCHMARK HELPER
# ──────────────────────────────────────────────
def benchmark(func, data, label):
    start = time.perf_counter()
    result = func(data)
    elapsed = (time.perf_counter() - start) * 1000
    print(f"  {label:<20}: {elapsed:.3f} ms  |  first 5: {result[:5]}")


# ──────────────────────────────────────────────
#  DEMO
# ──────────────────────────────────────────────
if __name__ == "__main__":
    small = [64, 34, 25, 12, 22, 11, 90]
    print("=" * 50)
    print("  SORTING ALGORITHMS DEMO  (small list)")
    print("=" * 50)
    print(f"Original         : {small}")
    print(f"Bubble Sort      : {bubble_sort(small)}")
    print(f"Selection Sort   : {selection_sort(small)}")
    print(f"Insertion Sort   : {insertion_sort(small)}")
    print(f"Merge Sort       : {merge_sort(small)}")
    print(f"Quick Sort       : {quick_sort(small)}")
    print(f"Counting Sort    : {counting_sort(small)}")

    print()
    print("=" * 50)
    print("  BENCHMARK  (1 000 random integers)")
    print("=" * 50)
    large = random.sample(range(10_000), 1_000)
    benchmark(bubble_sort,    large, "Bubble Sort")
    benchmark(selection_sort, large, "Selection Sort")
    benchmark(insertion_sort, large, "Insertion Sort")
    benchmark(merge_sort,     large, "Merge Sort")
    benchmark(quick_sort,     large, "Quick Sort")
    benchmark(sorted,         large, "Python built-in")
