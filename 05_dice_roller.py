# =============================================================================
# Program 5: Dice Roller Simulator
# =============================================================================
# Concepts Used: import random, Functions (def, parameters, return),
#                for loop, f-strings, lists
#
# What this program does:
#   - Defines a function to simulate rolling a dice
#   - Asks the user how many dice to roll
#   - Rolls all the dice and shows each result
#   - Calculates the total and average of all rolls
#   - Uses ASCII art to display the dice face
# =============================================================================

# --- Step 1: Importing the random module ---
# The 'random' module gives us tools to generate random numbers.
# We need to import it at the top before using it.
import random

# --- Step 2: Defining a function to roll a single dice ---
# A function is a reusable block of code. We define it with 'def'.
# This function takes no parameters and RETURNS a random number (1-6).
def roll_dice():
    """Simulates rolling a single 6-sided dice and returns the result."""
    # random.randint(1, 6) generates a random integer between 1 and 6 (inclusive)
    result = random.randint(1, 6)
    return result  # 'return' sends the value back to wherever the function was called


# --- Step 3: Defining a function to display a dice face ---
# This function takes a number and prints a visual representation of the dice.
def display_dice(number):
    """Displays an ASCII art dice face for the given number."""
    # We use a dictionary to map each number to its dice face art
    dice_faces = {
        1: "[ 🎲 1 ]",
        2: "[ 🎲 2 ]",
        3: "[ 🎲 3 ]",
        4: "[ 🎲 4 ]",
        5: "[ 🎲 5 ]",
        6: "[ 🎲 6 ]",
    }
    # .get() safely retrieves a value from the dictionary
    print(f"  {dice_faces.get(number, '[?]')}")


# --- Step 4: Main program ---
print("🎲 Welcome to the Dice Roller Simulator!\n")

# Ask how many dice the user wants to roll
num_dice = int(input("How many dice would you like to roll? "))

# Create an empty list to store all the roll results
all_rolls = []

print(f"\nRolling {num_dice} dice...\n")

# --- Step 5: Rolling the dice using a for loop ---
# range(1, num_dice + 1) gives us numbers 1, 2, 3, ... up to num_dice
for i in range(1, num_dice + 1):
    # Call our roll_dice function and store the returned value
    roll_result = roll_dice()
    # Add the result to our list using .append()
    all_rolls.append(roll_result)
    # Display the roll number and the dice face
    print(f"  Dice {i}:", end="")
    display_dice(roll_result)

# --- Step 6: Calculating statistics ---
# sum() adds up all numbers in a list
# len() gives us the count of items in a list
total = sum(all_rolls)
average = total / len(all_rolls)

# --- Step 7: Displaying the summary ---
print(f"\n{'=' * 35}")
print(f"📊 Results: {all_rolls}")
print(f"📈 Total:   {total}")
print(f"📉 Average: {average:.2f}")  # :.2f formats to 2 decimal places
print(f"{'=' * 35}")

# --- What we learned ---
# 1. Functions with 'return': send a value back to the caller
# 2. random.randint(a, b): generates a random integer between a and b
# 3. Lists to collect results: start empty, use .append() in a loop
# 4. sum() and len(): built-in functions to work with lists
# 5. String formatting :.2f: limits decimal places in f-strings
