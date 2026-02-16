# -----------------------------------------------------------------------------------
# Level 6: Functions with Data Types
# Concept: Reusable Code (Arguments & Return Values)
#
# Goal: Pass variables into functions and get new variables out.
# -----------------------------------------------------------------------------------

# 1. Defining a Function
# This function takes two variables (width, height) and returns one (area)
def calculate_area(width, height):
    area = width * height
    return area

# 2. Defining a Function with default values
def greet_user(name="Guest"):
    return f"Hello, {name}! Welcome back."

# --- Main Program Starts ---
print("--- Area Calculator ---")

# Calling the function
room_w = 5
room_h = 4
room_area = calculate_area(room_w, room_h) # Pass variables in

print(f"A room of {room_w}x{room_h} has an area of: {room_area}")

# Calling function with user input
print("\n--- Greeter ---")
user = "Purvik"
message = greet_user(user) # Returns a string
print(message)

# Calling without argument
print(greet_user()) # Uses default "Guest"

# -----------------------------------------------------------------------------------
# Expected Output:
# --- Area Calculator ---
# A room of 5x4 has an area of: 20
#
# --- Greeter ---
# Hello, Purvik! Welcome back.
# Hello, Guest! Welcome back.
# -----------------------------------------------------------------------------------
