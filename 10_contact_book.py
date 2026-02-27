# =============================================================================
# Program 10: Contact Book Manager
# =============================================================================
# Concepts Used: Dictionaries (nested), Functions, while loop, try/except,
#                Conditionals, f-strings, String methods
#
# What this program does:
#   - Creates a simple contact book stored in a dictionary
#   - Each contact has: name (key) → phone and email (values as nested dict)
#   - Supports: Add, Search, View All, Delete, and Exit
#   - Uses functions to organize code into reusable blocks
#   - error handling with try/except for robustness
# =============================================================================

# --- Step 1: Setting up the contact book ---
# We use a DICTIONARY where:
#   KEY = contact name (string)
#   VALUE = another dictionary with 'phone' and 'email'
# This is called a NESTED DICTIONARY (a dictionary inside a dictionary).
contacts = {}


# --- Step 2: Defining functions for each operation ---

def add_contact():
    """Adds a new contact to the contact book."""
    print("\n--- Add New Contact ---")
    name = input("Enter contact name: ").strip().title()
    # .strip() removes extra spaces
    # .title() capitalizes the first letter of each word (e.g., "john doe" → "John Doe")

    # Check if the contact already exists
    if name in contacts:
        print(f"⚠️ '{name}' already exists! Use a different name.")
        return  # 'return' exits the function early without doing anything more

    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip().lower()

    # Add the contact as a nested dictionary
    contacts[name] = {
        "phone": phone,
        "email": email
    }
    print(f"✅ Contact '{name}' added successfully!")


def search_contact():
    """Searches for a contact by name."""
    print("\n--- Search Contact ---")
    name = input("Enter the name to search: ").strip().title()

    # Use .get() to safely retrieve a value from the dictionary
    # .get() returns None if the key doesn't exist (instead of crashing)
    contact = contacts.get(name)

    if contact:
        # If the contact was found, display their details
        print(f"\n📇 Contact Found:")
        print(f"   Name:  {name}")
        print(f"   Phone: {contact['phone']}")
        print(f"   Email: {contact['email']}")
    else:
        print(f"❌ Contact '{name}' not found.")


def view_all_contacts():
    """Displays all contacts in the contact book."""
    print("\n--- All Contacts ---")

    # Check if the dictionary is empty
    if len(contacts) == 0:
        print("📋 Your contact book is empty.")
        return

    print(f"\n{'Name':<20} {'Phone':<15} {'Email':<25}")
    print("-" * 60)

    # .items() returns each key-value pair from the dictionary
    # 'name' gets the key, 'info' gets the nested dictionary value
    for name, info in contacts.items():
        print(f"{name:<20} {info['phone']:<15} {info['email']:<25}")

    print(f"\n📊 Total contacts: {len(contacts)}")


def delete_contact():
    """Deletes a contact from the contact book."""
    print("\n--- Delete Contact ---")
    name = input("Enter the name to delete: ").strip().title()

    # Check if the contact exists before trying to delete
    if name in contacts:
        # 'del' keyword removes a key-value pair from a dictionary
        del contacts[name]
        print(f"🗑️ Contact '{name}' has been deleted.")
    else:
        print(f"❌ Contact '{name}' not found. Nothing to delete.")


# --- Step 3: Main program loop ---
print("📱 CONTACT BOOK MANAGER 📱")
print("=" * 40)

while True:
    # Display the menu
    print("\n📋 MENU:")
    print("  1. Add Contact")
    print("  2. Search Contact")
    print("  3. View All Contacts")
    print("  4. Delete Contact")
    print("  5. Exit")

    # try/except to handle any unexpected input
    try:
        choice = input("\nChoose an option (1-5): ").strip()
    except Exception:
        print("⚠️ Something went wrong. Please try again.")
        continue  # Go back to the top of the loop

    # Call the appropriate function based on the user's choice
    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        view_all_contacts()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print(f"\n👋 Goodbye! You have {len(contacts)} contacts saved.")
        print("   (Note: Contacts are not saved to a file in this version.)")
        break
    else:
        print("❌ Invalid option! Please enter 1, 2, 3, 4, or 5.")

# --- What we learned ---
# 1. Nested Dictionaries: a dictionary inside a dictionary for complex data
# 2. Dictionary methods: .get() for safe access, .items() for looping, del for removal
# 3. Functions to organize code: each action is its own function
# 4. 'return' without a value: exits a function early
# 5. String methods: .strip() removes spaces, .title() capitalizes words
# 6. try/except: catches errors to prevent the program from crashing
# 7. 'in' keyword: checks if a key exists in a dictionary
