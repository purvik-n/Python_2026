# -----------------------------------------------------------------------------------
# Level 3: Type Conversion (Casting)
# Concept: Changing Data Types
#
# Goal: Convert string input into numbers to perform math.
# -----------------------------------------------------------------------------------

print("--- Simple Calculator ---")

# 1. Input is always a string
num1_str = input("Enter first number: ")
num2_str = input("Enter second number: ")

# 2. Converting (Casting) to Integers
# We use int() to convert text "10" into number 10.
num1 = int(num1_str)
num2 = int(num2_str)

# 3. Performing Math
result_sum = num1 + num2
result_diff = num1 - num2

# 4. Display Results
print("\n--- Results ---")
print("Sum:", result_sum)
print("Difference:", result_diff)

# 5. Float Conversion Example
# Creating a variable directly with type conversion
price = float(input("\nEnter price of item: "))
tax = price * 0.10  # 10% tax
total = price + tax

print(f"Total price with tax: {total}")

# -----------------------------------------------------------------------------------
# Expected Output (Example):
# --- Simple Calculator ---
# Enter first number: 10
# Enter second number: 5
#
# --- Results ---
# Sum: 15
# Difference: 5
#
# Enter price of item: 100
# Total price with tax: 110.0
# -----------------------------------------------------------------------------------
