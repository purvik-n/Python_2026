# =============================================================================
# Program 4: Interactive Shopping List Manager
# =============================================================================
# Concepts Used: Lists, while loop, list methods (append, remove, clear),
#                len(), conditionals, input validation
#
# What this program does:
#   - Shows a menu to the user with options: Add, Remove, View, Clear, Exit
#   - Uses a while loop to keep the program running until the user exits
#   - Demonstrates common list operations like append, remove, and indexing
# =============================================================================

# --- Step 1: Creating an empty list to store shopping items ---
# A list is created using square brackets []. It can hold multiple items.
shopping_list = []

# --- Step 2: Main program loop ---
# A while True loop runs FOREVER until we use 'break' to stop it.
# This is perfect for menu-driven programs where the user keeps interacting.
print("🛒 Welcome to the Shopping List Manager!\n")

while True:
    # Showing the menu options every time the loop runs
    print("\n--- MENU ---")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. View shopping list")
    print("4. Clear entire list")
    print("5. Exit")

    choice = input("\nPick an option (1-5): ")

    # --- Option 1: Add an item ---
    if choice == "1":
        item = input("Enter the item to add: ").strip()  # .strip() removes extra spaces
        # .append() adds an item to the END of the list
        shopping_list.append(item)
        print(f"✅ '{item}' has been added to your list!")

    # --- Option 2: Remove an item ---
    elif choice == "2":
        if len(shopping_list) == 0:
            # len() returns the number of items in a list
            print("⚠️ Your list is already empty! Nothing to remove.")
        else:
            # Show current items so the user knows what they can remove
            print("Current items:", shopping_list)
            item = input("Enter the item to remove: ").strip()
            # Check if the item actually exists in the list before removing
            if item in shopping_list:
                # .remove() deletes the FIRST occurrence of the item
                shopping_list.remove(item)
                print(f"🗑️ '{item}' has been removed.")
            else:
                print(f"❌ '{item}' was not found in your list.")

    # --- Option 3: View the list ---
    elif choice == "3":
        if len(shopping_list) == 0:
            print("📋 Your shopping list is empty.")
        else:
            print(f"\n📋 Your Shopping List ({len(shopping_list)} items):")
            # enumerate() gives us both the INDEX (position) and the ITEM
            for index, item in enumerate(shopping_list, start=1):
                print(f"  {index}. {item}")

    # --- Option 4: Clear the entire list ---
    elif choice == "4":
        # .clear() removes ALL items from the list at once
        shopping_list.clear()
        print("🧹 Shopping list has been cleared!")

    # --- Option 5: Exit ---
    elif choice == "5":
        print(f"\n👋 Goodbye! You had {len(shopping_list)} items in your list.")
        break  # 'break' exits the while loop and ends the program

    else:
        print("❌ Invalid choice! Please enter 1, 2, 3, 4, or 5.")

# --- What we learned ---
# 1. Lists: ordered collections that can grow and shrink
# 2. List methods: .append() adds, .remove() deletes, .clear() empties
# 3. while True + break: creates a loop that runs until we decide to stop
# 4. len(): returns the number of items in a list
# 5. 'in' keyword: checks if an item exists in a list
# 6. enumerate(): gives index + value when looping through a list
