# ============================================================
# Program 11: Palindrome Checker
# Concepts: String slicing, string methods, functions, loops
# ============================================================

# A palindrome is a word/phrase that reads the same forwards and backwards
# Examples: "racecar", "madam", "level", "A man a plan a canal Panama"

def clean_string(text):
    """
    Remove spaces and punctuation, convert to lowercase.
    This allows us to check phrases like 'A man a plan a canal Panama'.
    """
    # Keep only alphabetic characters and convert to lowercase
    cleaned = ""
    for char in text:
        if char.isalpha():
            cleaned += char.lower()
    return cleaned


def is_palindrome(text):
    """
    Check if the given text is a palindrome.
    Uses Python's slice [::-1] to reverse the string.
    """
    cleaned = clean_string(text)  # Clean the input first
    reversed_text = cleaned[::-1]  # Reverse using slicing
    return cleaned == reversed_text  # Compare original vs reversed


def main():
    print("=" * 45)
    print("       🔁  Palindrome Checker  🔁")
    print("=" * 45)
    print("A palindrome reads the same forwards & backwards.")
    print("Examples: racecar, madam, level\n")

    # Keep checking until the user wants to quit
    while True:
        user_input = input("Enter a word or phrase (or 'quit' to exit): ").strip()

        # Exit condition
        if user_input.lower() == "quit":
            print("\n👋 Thanks for using Palindrome Checker!")
            break

        # Empty input check
        if not user_input:
            print("⚠️  Please enter something!\n")
            continue

        # Check and display result
        if is_palindrome(user_input):
            print(f'✅ "{user_input}" IS a palindrome! 🎉\n')
        else:
            print(f'❌ "{user_input}" is NOT a palindrome.\n')

        # Show the cleaned version for learning
        cleaned = clean_string(user_input)
        print(f"   Cleaned version: '{cleaned}'")
        print(f"   Reversed:        '{cleaned[::-1]}'\n")


# Entry point
if __name__ == "__main__":
    main()
