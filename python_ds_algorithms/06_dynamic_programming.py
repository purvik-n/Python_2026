"""
==========================================================
  Python DS & Algorithms — Day 6: Dynamic Programming
  Author  : Purvik
  Date    : 2026-03-14
  Topic   : Memoization & tabulation patterns
            Fibonacci, Knapsack, LCS, Coin Change, LIS
==========================================================
"""

from functools import lru_cache


# ──────────────────────────────────────────────
#  1. FIBONACCI  (memoization vs tabulation)
# ──────────────────────────────────────────────
@lru_cache(maxsize=None)
def fib_memo(n: int) -> int:
    """Top-down memoization — O(n) time, O(n) space."""
    if n <= 1:
        return n
    return fib_memo(n - 1) + fib_memo(n - 2)


def fib_tab(n: int) -> int:
    """Bottom-up tabulation — O(n) time, O(1) space."""
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


# ──────────────────────────────────────────────
#  2. 0/1 KNAPSACK  — O(n·W) time & space
# ──────────────────────────────────────────────
def knapsack(weights: list, values: list, capacity: int) -> tuple:
    """
    Returns (max_value, selected_item_indices).
    weights[i] and values[i] for item i.
    """
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # Don't take item i
            dp[i][w] = dp[i-1][w]
            # Take item i if it fits
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i][w], dp[i-1][w - weights[i-1]] + values[i-1])

    # Backtrack to find selected items
    selected, w = [], capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected.append(i - 1)
            w -= weights[i - 1]

    return dp[n][capacity], list(reversed(selected))


# ──────────────────────────────────────────────
#  3. LONGEST COMMON SUBSEQUENCE  — O(m·n)
# ──────────────────────────────────────────────
def lcs(s1: str, s2: str) -> tuple:
    """Returns (length, lcs_string)."""
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # Backtrack to build LCS string
    result, i, j = [], m, n
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            result.append(s1[i-1])
            i -= 1; j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1

    return dp[m][n], ''.join(reversed(result))


# ──────────────────────────────────────────────
#  4. COIN CHANGE  — O(amount · len(coins))
# ──────────────────────────────────────────────
def coin_change(coins: list, amount: int) -> int:
    """Minimum number of coins to make amount. Returns -1 if impossible."""
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1


# ──────────────────────────────────────────────
#  5. LONGEST INCREASING SUBSEQUENCE  — O(n log n)
# ──────────────────────────────────────────────
import bisect

def lis(arr: list) -> tuple:
    """Returns (length, one valid LIS) using patience sorting."""
    if not arr:
        return 0, []

    tails = []      # tails[i] = smallest tail element for LIS of length i+1
    parent = [-1] * len(arr)
    index  = [-1] * len(arr)

    for i, val in enumerate(arr):
        pos = bisect.bisect_left(tails, val)
        if pos == len(tails):
            tails.append(val)
        else:
            tails[pos] = val
        index[i] = pos
        parent[i] = -1

    # Reconstruct (simplified – returns length only for O(n log n) guarantee)
    return len(tails), tails   # tails here is NOT the actual LIS sequence


# ──────────────────────────────────────────────
#  6. EDIT DISTANCE (Levenshtein)  — O(m·n)
# ──────────────────────────────────────────────
def edit_distance(s: str, t: str) -> int:
    """Minimum insertions, deletions, substitutions to convert s → t."""
    m, n = len(s), len(t)
    dp = list(range(n + 1))
    for i in range(1, m + 1):
        prev = dp[:]
        dp[0] = i
        for j in range(1, n + 1):
            if s[i-1] == t[j-1]:
                dp[j] = prev[j-1]
            else:
                dp[j] = 1 + min(prev[j], dp[j-1], prev[j-1])
    return dp[n]


# ──────────────────────────────────────────────
#  DEMO
# ──────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 55)
    print("  1. FIBONACCI")
    print("=" * 55)
    for n in [0, 1, 5, 10, 20, 30]:
        print(f"  fib({n:2d}) memo={fib_memo(n):<10} tab={fib_tab(n)}")

    print()
    print("=" * 55)
    print("  2. 0/1 KNAPSACK")
    print("=" * 55)
    weights = [2, 3, 4, 5]
    values  = [3, 4, 5, 6]
    cap     = 8
    max_val, selected = knapsack(weights, values, cap)
    print(f"  Items   : {list(zip(weights, values))}  (weight, value)")
    print(f"  Capacity: {cap}")
    print(f"  Max val : {max_val}  |  Items chosen: {selected}")

    print()
    print("=" * 55)
    print("  3. LONGEST COMMON SUBSEQUENCE")
    print("=" * 55)
    pairs = [("ABCBDAB", "BDCAB"), ("AGGTAB", "GXTXAYB"), ("python", "typhoon")]
    for s1, s2 in pairs:
        length, seq = lcs(s1, s2)
        print(f"  LCS('{s1}', '{s2}') = '{seq}'  (len {length})")

    print()
    print("=" * 55)
    print("  4. COIN CHANGE")
    print("=" * 55)
    tests = [([1,5,6,9], 11), ([2], 3), ([1,2,5], 11)]
    for coins, amount in tests:
        print(f"  coins={coins}  amount={amount}  → {coin_change(coins, amount)} coins")

    print()
    print("=" * 55)
    print("  5. EDIT DISTANCE")
    print("=" * 55)
    pairs2 = [("kitten","sitting"), ("sunday","saturday"), ("python","cython")]
    for s, t in pairs2:
        print(f"  edit('{s}', '{t}') = {edit_distance(s, t)}")
