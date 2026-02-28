# ============================================================
# Program 18: Caesar Cipher Encoder/Decoder
# Concepts: String manipulation, ord(), chr(), modulo operator
# ============================================================

# The Caesar Cipher is one of the oldest encryption techniques.
# It shifts each letter by a fixed number of positions in the alphabet.
# Example with shift 3: A→D, B→E, Z→C

# ord('A') returns 65, ord('a') returns 97
# chr(65) returns 'A'
# These built-in functions help us work with ASCII values.

def caesar_cipher(text, shift, mode="encode"):
    """
    Encode or decode a message using the Caesar Cipher.
    
    Args:
        text  : The message to encrypt or decrypt
        shift : Number of positions to shift (0–25)
        mode  : 'encode' to encrypt, 'decode' to decrypt
    
    Returns:
        The resulting encoded or decoded string
    """
    result = ""
    
    # For decoding, reverse the shift direction
    if mode == "decode":
        shift = -shift

    for char in text:
        if char.isalpha():
            # Determine base: 65 for uppercase (A), 97 for lowercase (a)
            base = ord('A') if char.isupper() else ord('a')
            
            # Shift the character and wrap around using modulo 26
            # ord(char) - base  → gives position 0–25
            # + shift            → shifts by n positions
            # % 26               → wraps around if it goes past Z
            # + base             → converts back to ASCII
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)      # Convert ASCII back to character
        else:
            result += char              # Non-letters stay unchanged (spaces, numbers, !)

    return result


def main():
    print("=" * 50)
    print("  🔐  Caesar Cipher Encoder / Decoder  🔐")
    print("=" * 50)
    print("Shifts letters by a fixed number of positions.\n")

    while True:
        print("\n--- Options ---")
        print("  1. Encode a message")
        print("  2. Decode a message")
        print("  3. Quit")

        choice = input("\nSelect option: ").strip()

        if choice == "3":
            print("\n🔐 Goodbye! Keep your secrets safe!")
            break

        elif choice in ("1", "2"):
            mode = "encode" if choice == "1" else "decode"
            message = input(f"Enter the message to {mode}: ")

            try:
                shift = int(input("Enter shift value (1–25): "))
                shift = shift % 26  # Normalize to 0–25
            except ValueError:
                print("⚠️  Invalid shift. Using default shift of 3.")
                shift = 3

            # Process the cipher
            output = caesar_cipher(message, shift, mode)

            print(f"\n  {'Original' if mode == 'encode' else 'Encoded'} : {message}")
            print(f"  {'Encoded ' if mode == 'encode' else 'Decoded '} : {output}")
            print(f"  Shift Used : {shift}")

            # Fun: show full alphabet shift table for small shifts
            if shift <= 10:
                print(f"\n  Alphabet mapping (shift {shift}):")
                original = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                shifted  = original[shift:] + original[:shift]
                print(f"  Original: {original}")
                print(f"  Shifted : {shifted}")

        else:
            print("⚠️  Invalid choice. Select 1, 2, or 3.")


if __name__ == "__main__":
    main()
