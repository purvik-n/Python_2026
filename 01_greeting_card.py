# =============================================================================
# Program 1: Personalized Greeting Card Generator
# =============================================================================
# Concepts Used: Variables, Strings, f-strings, input(), print()
#
# What this program does:
#   - Asks the user for their name, favorite color, and a hobby
#   - Uses f-strings to create a personalized greeting card message
#   - Demonstrates how variables store data and how we use them in strings
# =============================================================================

# --- Step 1: Taking user input and storing it in variables ---
# The input() function pauses the program and waits for the user to type something.
# Whatever the user types is stored as a STRING in the variable.
name = input("What is your name? ")
favorite_color = input("What is your favorite color? ")
hobby = input("What is your favorite hobby? ")

# --- Step 2: Creating the greeting card using f-strings ---
# f-strings (formatted string literals) let us embed variables directly inside strings.
# We put an 'f' before the opening quote, and use {variable_name} to insert values.

print("\n" + "=" * 50)  # \n creates a new line, "=" * 50 repeats "=" fifty times
print(f"🎉  WELCOME, {name.upper()}!  🎉")  # .upper() converts text to UPPERCASE
print("=" * 50)

# Using f-strings to build multiple lines of the greeting
print(f"\n✨ Here's your personalized greeting card: ✨\n")
print(f"  Dear {name},")
print(f"  Your favorite color is {favorite_color} — great choice!")
print(f"  We hear you love {hobby}. Keep doing what you love!")
print(f"\n  Wishing you an amazing day ahead! 🌟")
print(f"\n  — From your Python program 🐍")
print("\n" + "=" * 50)

# --- What we learned ---
# 1. Variables store data (name, favorite_color, hobby)
# 2. input() gets data from the user
# 3. f-strings let us mix variables into strings easily
# 4. String methods like .upper() transform text
# 5. String multiplication ("=" * 50) repeats characters
