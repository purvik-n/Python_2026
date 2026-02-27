# =============================================================================
# Program 9: Number Guessing Game
# =============================================================================
# Concepts Used: import random, while loop, Conditionals (if/elif/else),
#                try/except (Error Handling), Variables as counters
#
# What this program does:
#   - The computer picks a random number between 1 and 100
#   - The user tries to guess the number
#   - After each guess, the program gives a hint: "Too high" or "Too low"
#   - Tracks the number of attempts it takes to guess correctly
#   - Uses try/except to handle invalid input gracefully
# =============================================================================

import random  # We need this to generate a random number

# --- Step 1: The computer picks a secret number ---
# random.randint(1, 100) generates a random integer between 1 and 100 (inclusive)
secret_number = random.randint(1, 100)

# --- Step 2: Setting up game variables ---
attempts = 0  # Counter for how many guesses the user makes
max_attempts = 10  # Maximum number of allowed guesses
guessed = False  # Boolean flag: becomes True when user guesses correctly

print("🔢 NUMBER GUESSING GAME 🔢")
print("=" * 40)
print(f"I'm thinking of a number between 1 and 100.")
print(f"You have {max_attempts} attempts to guess it!")
print("=" * 40)

# --- Step 3: Main game loop ---
# The loop continues as long as:
#   1. The user hasn't guessed correctly (not guessed)
#   2. They still have attempts left (attempts < max_attempts)
while not guessed and attempts < max_attempts:
    # --- Step 4: Getting user input with error handling ---
    # try/except handles errors gracefully instead of crashing.
    # If the user types "abc" instead of a number, int() would crash.
    # The 'except' block catches that error and shows a friendly message.
    try:
        guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts} — Enter your guess: "))
    except ValueError:
        # ValueError occurs when int() can't convert the input to a number
        print("⚠️ Please enter a valid number!")
        continue  # 'continue' skips the rest of the loop and goes back to the top

    # Increase the attempt counter
    attempts += 1

    # --- Step 5: Comparing the guess to the secret number ---
    if guess == secret_number:
        # The user guessed correctly!
        guessed = True  # Set the flag to True to exit the loop
        print(f"\n🎉 CONGRATULATIONS! You guessed it!")
        print(f"   The number was {secret_number}.")
        print(f"   It took you {attempts} attempt(s)!")

        # Give a rating based on attempts
        if attempts <= 3:
            print("   🌟 Incredible! Are you a mind reader?")
        elif attempts <= 5:
            print("   🎯 Great job! Very impressive!")
        elif attempts <= 7:
            print("   👍 Good work! Not bad at all!")
        else:
            print("   😅 Phew! Just in time!")

    elif guess < secret_number:
        # The guess is too low
        remaining = max_attempts - attempts
        print(f"📉 Too LOW! Try a higher number. ({remaining} attempts left)")

    else:
        # The guess is too high (guess > secret_number)
        remaining = max_attempts - attempts
        print(f"📈 Too HIGH! Try a lower number. ({remaining} attempts left)")

# --- Step 6: If the user ran out of attempts ---
if not guessed:
    print(f"\n💀 GAME OVER! You ran out of attempts.")
    print(f"   The secret number was: {secret_number}")
    print("   Better luck next time! 🍀")

# --- What we learned ---
# 1. random.randint(): generates a random number in a range
# 2. while loop with conditions: loop continues until conditions are met
# 3. try/except: handles errors without crashing the program
# 4. continue: skips to the next iteration of the loop
# 5. Boolean flag (guessed): tracks whether a condition has been met
# 6. Counter variable (attempts): tracks how many times something occurs
