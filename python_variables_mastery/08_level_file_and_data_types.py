# -----------------------------------------------------------------------------------
# Level 8: File and Data Types
# Concept: Reading and Writing Files
#
# Goal: Save variable data to a file so it's not lost when the program ends.
# -----------------------------------------------------------------------------------

filename = "game_save.txt"

# 1. Writing to a file
# 'w' mode means Write (overwrites existing file)
player_name = "Purvik"
score = 5000

print(f"--- Saving Data for {player_name} ---")

with open(filename, "w") as file:
    file.write(f"Player: {player_name}\n")
    # We must convert numbers to string to write them
    file.write(f"Score: {str(score)}\n") 
    
print("Game saved successfully!")

# 2. Reading from a file
# 'r' mode means Read
print("\n--- Loading Data ---")

with open(filename, "r") as file:
    content = file.read() # Reads entire file into a String variable
    print("File Content Loaded:")
    print(content)

# -----------------------------------------------------------------------------------
# Expected Output:
# --- Saving Data for Purvik ---
# Game saved successfully!
#
# --- Loading Data ---
# File Content Loaded:
# Player: Purvik
# Score: 5000
# -----------------------------------------------------------------------------------
