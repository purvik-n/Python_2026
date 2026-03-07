# =============================================================================
# Program 3: Even or Odd Checker with Range Analysis
# =============================================================================
# Concepts Used: for loop, range(), Modulo operator (%), Conditionals,
#                Variables as counters
#
# What this program does:
#   - Asks the user for a start and end number
#   - Loops through every number in that range
#   - Checks if each number is even or odd using the modulo operator (%
#   - Counts how many even and odd numbers there are
#   - Displays a summary at the end
# =============================================================================

# --- Step 1: Getting the range from the user ---
# We use int() to convert the input string to a whole number
start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))

# --- Step 2: Setting up counter variables ---
# These variables will keep track of how many even and odd numbers we find.
# We initialize them to 0 before the loop starts.
even_count = 0
odd_count = 0

# --- Step 3: Looping through the range ---
# range(start, end + 1) generates numbers from 'start' up to and INCLUDING 'end'.
# Without the +1, range() would stop one number before the end.
print(f"\n📊 Checking numbers from {start} to {end}:\n")

for number in range(start, end + 1):
    # The modulo operator (%) gives us the REMAINDER after division.
    # If a number divided by 2 has remainder 0, it's EVEN.
    # If a number divided by 2 has remainder 1, it's ODD.
    if number % 2 == 0:
        print(f"  {number} → Even ✅")
        even_count += 1  # Same as: even_count = even_count + 1
    else:
        print(f"  {number} → Odd  ❌")
        odd_count += 1  # Same as: odd_count = odd_count + 1

# --- Step 4: Displaying the summary ---
total = even_count + odd_count
print(f"\n{'=' * 35}")
print(f"📈 SUMMARY:")
print(f"  Total numbers checked: {total}")
print(f"  Even numbers: {even_count}")
print(f"  Odd numbers:  {odd_count}")
print(f"{'=' * 35}")

# --- What we learned ---
# 1. for loop: repeats code for each item in a sequence
# 2. range(start, end+1): generates a sequence of numbers
# 3. Modulo operator (%): returns the remainder of division
# 4. Counter variables: we initialize to 0 and += 1 inside the loop
# 5. Combining loops and conditionals to analyze data
