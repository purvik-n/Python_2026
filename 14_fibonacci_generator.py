# ============================================================
# Program 14: Fibonacci Sequence Generator
# Concepts: Loops, recursion, generators, memoization
# ============================================================

# The Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
# Each number is the SUM of the two numbers before it.
# Formula: F(n) = F(n-1) + F(n-2), with F(0)=0, F(1)=1

# --------------------------------------------------
# Method 1: Using a simple iterative approach (most efficient)
# --------------------------------------------------
def fibonacci_iterative(n):
    """
    Generate the first n numbers of the Fibonacci sequence.
    Returns a list. This is the most efficient method for large n.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]

    sequence = [0, 1]  # Start with the first two numbers
    for i in range(2, n):
        # Each new number = sum of the last two
        next_num = sequence[-1] + sequence[-2]
        sequence.append(next_num)
    return sequence


# --------------------------------------------------
# Method 2: Recursive with memoization (cache results)
# --------------------------------------------------
memo = {}  # Dictionary to store already-calculated values

def fibonacci_recursive(n):
    """
    Recursively calculate the nth Fibonacci number.
    Uses memoization to avoid recalculating the same values.
    """
    if n in memo:
        return memo[n]       # Return cached result
    if n <= 0:
        return 0
    if n == 1:
        return 1

    # Recursively calculate and cache the result
    result = fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
    memo[n] = result
    return result


def main():
    print("=" * 50)
    print("     🌀  Fibonacci Sequence Generator  🌀")
    print("=" * 50)
    print("Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...\n")

    while True:
        try:
            n = int(input("How many Fibonacci numbers to generate? (1–100): "))
            if 1 <= n <= 100:
                break
            else:
                print("⚠️  Please enter a number between 1 and 100.")
        except ValueError:
            print("⚠️  Invalid input. Please enter a whole number.")

    # Generate using iterative method
    sequence = fibonacci_iterative(n)

    print(f"\n📋 First {n} Fibonacci numbers (iterative):")
    # Print in rows of 10 for readability
    for i, num in enumerate(sequence):
        print(f"{num:>10}", end="")
        if (i + 1) % 10 == 0:
            print()  # New line every 10 numbers
    print("\n")

    # Show a single Fibonacci number using recursive method
    idx = n - 1
    print(f"🔁 Fibonacci({idx}) using recursion = {fibonacci_recursive(idx)}")
    print(f"\n✅ Sum of all {n} numbers = {sum(sequence)}")


if __name__ == "__main__":
    main()
