# -----------------------------------------------------------------------------------
# Level 7: Collections and Types
# Concept: Lists and Dictionaries
#
# Goal: Store multiple pieces of data in a single variable.
# -----------------------------------------------------------------------------------

# 1. Lists (Ordered Collection)
# Think of a List as a backpack holding items in order.
inventory = ["Sword", "Shield", "Potion"] # List of Strings

print("--- Inventory ---")
print("Full Inventory:", inventory)
print("First Item:", inventory[0])    # Index starts at 0

# Adding a new item variable to the list
new_item = "Map"
inventory.append(new_item)
print("Updated Inventory:", inventory)

# 2. Dictionaries (Key-Value Pairs)
# Think of a Dictionary as a contact book (Name -> Phone Number).
# Storing player stats in one variable:
player_stats = {
    "name": "Hero",
    "level": 5,
    "hp": 100,
    "is_alive": True
}

print("\n--- Player Stats (Dict) ---")
print("Player Name:", player_stats["name"])
print("Player Level:", player_stats["level"])

# Updating a value in the dictionary
player_stats["hp"] = 90
print("Player took damage! New HP:", player_stats["hp"])

# 3. Looping through a List
print("\n--- Listing Items ---")
for item in inventory:
    print(f"- {item}")

# -----------------------------------------------------------------------------------
# Expected Output:
# --- Inventory ---
# Full Inventory: ['Sword', 'Shield', 'Potion']
# First Item: Sword
# Updated Inventory: ['Sword', 'Shield', 'Potion', 'Map']
#
# --- Player Stats (Dict) ---
# Player Name: Hero
# Player Level: 5
# Player took damage! New HP: 90
#
# --- Listing Items ---
# - Sword
# - Shield
# - Potion
# - Map
# -----------------------------------------------------------------------------------
