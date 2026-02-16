# -----------------------------------------------------------------------------------
# Level 4: Conditions with Types
# Concept: Making Decisions (If/Else) by checking Variables
#
# Goal: Use variables to control the flow of the program.
# -----------------------------------------------------------------------------------

print("--- Age Verifier ---")

# 1. Start with variable input and conversion
try:
    age_str = input("Please enter your age: ")
    age = int(age_str)  # Convert string to integer for comparison

    # 2. Making Decisions
    # We check the value of the 'age' variable
    if age < 0:
        print("Error: Age cannot be negative.")

    elif age < 13:
        print("You are a Child.")

    elif age < 18:
        print("You are a Teenager.")

    elif age < 65:
        print("You are an Adult.")

    else:
        print("You are a Senior.")

    # 3. Combining logic
    # Boolean logic with variables
    has_id = True  # Pretend user has ID

    if age >= 18 and has_id == True:
        print("\nAccess Granted: You can enter the club.")
    else:
        print("\nAccess Denied: You are too young or missing ID.")

except ValueError:
    print("Invalid Input! Please enter a number.")

# -----------------------------------------------------------------------------------
# Expected Output (Example):
# --- Age Verifier ---
# Please enter your age: 20
# You are an Adult.
#
# Access Granted: You can enter the club.
# -----------------------------------------------------------------------------------
