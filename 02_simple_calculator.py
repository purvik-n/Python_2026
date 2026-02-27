# =============================================================================
# Program 2: Simple Calculator
# =============================================================================
# Concepts Used: input(), Type Casting (int/float), Conditionals (if/elif/else),
#                Arithmetic Operators (+, -, *, /, //, %, **)
#
# What this program does:
#   - Asks the user to enter two numbers
#   - Asks the user to pick an operation (+, -, *, /)
#   - Performs the chosen operation and displays the result
#   - Handles invalid input using conditionals
# =============================================================================

# --- Step 1: Getting numbers from the user ---
# input() always returns a STRING, so we use float() to convert it to a number.
# float() allows decimal numbers like 3.5 (int() would only allow whole numbers).
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# --- Step 2: Asking which operation to perform ---
print("\nChoose an operation:")
print("  + for Addition")
print("  - for Subtraction")
print("  * for Multiplication")
print("  / for Division")
operation = input("\nEnter your choice (+, -, *, /): ")

# --- Step 3: Using if/elif/else to perform the correct operation ---
# We compare the 'operation' variable to each possible value using ==
if operation == "+":
    # Addition: adds two numbers together
    result = num1 + num2
    print(f"\n✅ {num1} + {num2} = {result}")

elif operation == "-":
    # Subtraction: subtracts second number from the first
    result = num1 - num2
    print(f"\n✅ {num1} - {num2} = {result}")

elif operation == "*":
    # Multiplication: multiplies two numbers together
    result = num1 * num2
    print(f"\n✅ {num1} * {num2} = {result}")

elif operation == "/":
    # Division: divides first number by the second
    # IMPORTANT: We must check if num2 is 0, because dividing by zero causes an error!
    if num2 == 0:
        print("\n❌ Error: Cannot divide by zero!")
    else:
        result = num1 / num2
        print(f"\n✅ {num1} / {num2} = {result}")

else:
    # If the user typed something other than +, -, *, /
    print("\n❌ Invalid operation! Please choose +, -, *, or /")

# --- What we learned ---
# 1. Type Casting: float() converts a string to a decimal number
# 2. Conditionals: if/elif/else lets us run different code based on conditions
# 3. Comparison operator == checks if two values are equal
# 4. Division by zero is a common error we should always handle
# 5. Arithmetic operators: + (add), - (subtract), * (multiply), / (divide)
