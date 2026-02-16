# -----------------------------------------------------------------------------------
# Level 1: Variables Intro
# Concept: Basic Variables and Data Types
#
# Goal: Learn how to store different types of data in variables.
# -----------------------------------------------------------------------------------

# 1. Storing data in variables
# A variable is like a container that holds data.
player_name = "Alex"        # String (Text)
player_score = 100          # Integer (Whole number)
player_health = 95.5        # Float (Decimal number)
is_active = True            # Boolean (True/False)

# 2. Printing variable values
print("--- Player Stats ---")
print("Name:", player_name)
print("Score:", player_score)
print("Health:", player_health)
print("Active Player?", is_active)

# 3. Checking data types
# Python can tell you what type of data is inside a variable using type()
print("\n--- Data Types ---")
print("Type of player_name:", type(player_name))
print("Type of player_score:", type(player_score))
print("Type of player_health:", type(player_health))
print("Type of is_active:", type(is_active))

# -----------------------------------------------------------------------------------
# Expected Output:
# --- Player Stats ---
# Name: Alex
# Score: 100
# Health: 95.5
# Active Player? True
#
# --- Data Types ---
# Type of player_name: <class 'str'>
# Type of player_score: <class 'int'>
# Type of player_health: <class 'float'>
# Type of is_active: <class 'bool'>
# -----------------------------------------------------------------------------------
