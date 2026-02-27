# =============================================================================
# Program 6: Temperature Converter (Celsius ↔ Fahrenheit)
# =============================================================================
# Concepts Used: Functions with parameters and return values, Conditionals,
#                Type Casting, while loop, String methods (.lower())
#
# What this program does:
#   - Provides two conversion functions: Celsius to Fahrenheit and vice versa
#   - Lets the user choose which conversion to perform
#   - Uses a loop so the user can do multiple conversions
#   - Demonstrates functions that RETURN values instead of just printing
# =============================================================================

# --- Step 1: Defining conversion functions ---
# These functions take a temperature value as a PARAMETER and RETURN the converted value.
# The formulas are standard physics/math formulas.

def celsius_to_fahrenheit(celsius):
    """
    Converts Celsius to Fahrenheit.
    Formula: F = (C × 9/5) + 32
    """
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit  # Returns the result to the caller


def fahrenheit_to_celsius(fahrenheit):
    """
    Converts Fahrenheit to Celsius.
    Formula: C = (F - 32) × 5/9
    """
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius  # Returns the result to the caller


# --- Step 2: A helper function to display the result nicely ---
# This function doesn't return anything — it just prints.
def display_result(original, original_unit, converted, converted_unit):
    """Displays the conversion result in a formatted way."""
    # :.2f rounds the number to 2 decimal places
    print(f"\n🌡️  {original:.2f}°{original_unit} = {converted:.2f}°{converted_unit}")


# --- Step 3: Main program loop ---
print("🌡️  Temperature Converter\n")

while True:
    # Show the menu options
    print("Choose a conversion:")
    print("  1. Celsius → Fahrenheit")
    print("  2. Fahrenheit → Celsius")
    print("  3. Exit")

    choice = input("\nYour choice (1/2/3): ")

    if choice == "1":
        # --- Celsius to Fahrenheit ---
        temp = float(input("Enter temperature in Celsius: "))
        # Call the function and store the RETURNED value
        result = celsius_to_fahrenheit(temp)
        display_result(temp, "C", result, "F")

    elif choice == "2":
        # --- Fahrenheit to Celsius ---
        temp = float(input("Enter temperature in Fahrenheit: "))
        # Call the function and store the RETURNED value
        result = fahrenheit_to_celsius(temp)
        display_result(temp, "F", result, "C")

    elif choice == "3":
        print("\n👋 Goodbye! Stay cool (or warm)! 🌡️")
        break  # Exit the while loop

    else:
        print("❌ Invalid choice! Please enter 1, 2, or 3.")

    print()  # Print a blank line for spacing

# --- What we learned ---
# 1. Functions with 'return': send a calculated value back to the caller
# 2. Storing returned values: result = function_name(argument)
# 3. Multiple functions can work together (converter + display)
# 4. While True + break: keep a program running until user wants to quit
# 5. Float formatting :.2f: shows exactly 2 decimal places
