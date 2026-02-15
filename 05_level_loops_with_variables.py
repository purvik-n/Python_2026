# -----------------------------------------------------------------------------------
# Level 5: Loops with Variables
# Concept: Repeating Actions & Updating Variables
#
# Goal: Use loops to update a variable multiple times.
# -----------------------------------------------------------------------------------

print("--- Countdown Timer ---")

# 1. While Loop
# Keeps running as long as the condition is True
count = 5  # Start variable at 5
while count > 0:
    print(f"Countdown: {count}")
    count = count - 1  # Update variable (decrease by 1)

print("Blast off! \U0001F680")  # Rocket emoji

# 2. For Loop (Range)
# Runs a specific number of times
print("\n--- Multiplication Table ---")
number = 3
print(f"Showing x{number} table:")

# The variable 'i' changes automatically from 1 to 10
for i in range(1, 11): 
    result = number * i
    print(f"{number} x {i} = {result}")

# 3. Accumulator Variable
# Summing numbers
print("\n--- Summing Numbers ---")
total_sum = 0  # Initialize variable

for num in range(1, 6): # 1, 2, 3, 4, 5
    print(f"Adding {num} to total...")
    total_sum = total_sum + num

print(f"Final Total: {total_sum}")

# -----------------------------------------------------------------------------------
# Expected Output:
# --- Countdown Timer ---
# Countdown: 5
# Countdown: 4
# ...
# Blast off!
#
# --- Multiplication Table ---
# Showing x3 table:
# 3 x 1 = 3
# ...
# 3 x 10 = 30
# 
# --- Summing Numbers ---
# Final Total: 15
# -----------------------------------------------------------------------------------
