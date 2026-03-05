# -----------------------------------------------------------------------------------
# Level 2: Input and Types
# Concept: Taking Input from User
#
# Goal: Understand that input() always returns a String (text).
# -----------------------------------------------------------------------------------

# Outputting the header for user registration
print("--- User Registration ---")

# 1. Taking input
# The input() function asks the user for data.
username = input("Enter your username: ")
age = input("Enter your age: ")  # Even if I type a number, this will be a String!

# 2. Displaying the input
print("\n--- Registration Complete ---")
# Printing out the captured user details
print("Welcome,", username)
print("Age received:", age)

# 3. Proof that input is a String
# Let's check the type of 'age'
print("\n--- Data Type Check ---")
print("Type of 'age' variable:", type(age))

# Important Note: Since 'age' is a string, we cannot do math like: age + 5 yet.
# We will fix this in Level 3!

# -----------------------------------------------------------------------------------
# Expected Output (Example):
# --- User Registration ---
# Enter your username: Purvik
# Enter your age: 25
#
# --- Registration Complete ---
# Welcome, Purvik
# Age received: 25
#
# --- Data Type Check ---
# Type of 'age' variable: <class 'str'>
# -----------------------------------------------------------------------------------
