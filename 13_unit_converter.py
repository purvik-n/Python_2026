# ============================================================
# Program 13: Unit Converter
# Concepts: Dictionaries, functions, nested conditionals, loops
# ============================================================

# This program converts between common units:
# Length: km <-> miles, meters <-> feet
# Weight: kg <-> pounds
# Volume: liters <-> gallons

# Conversion factors stored in a dictionary for easy lookup
CONVERSIONS = {
    "km_to_miles":   0.621371,
    "miles_to_km":   1.60934,
    "meters_to_feet": 3.28084,
    "feet_to_meters": 0.3048,
    "kg_to_pounds":  2.20462,
    "pounds_to_kg":  0.453592,
    "liters_to_gallons": 0.264172,
    "gallons_to_liters": 3.78541,
}

# Menu options shown to the user
MENU = {
    "1": ("Kilometers → Miles",   "km_to_miles",      "km",      "miles"),
    "2": ("Miles → Kilometers",   "miles_to_km",      "miles",   "km"),
    "3": ("Meters → Feet",        "meters_to_feet",   "m",       "ft"),
    "4": ("Feet → Meters",        "feet_to_meters",   "ft",      "m"),
    "5": ("Kilograms → Pounds",   "kg_to_pounds",     "kg",      "lbs"),
    "6": ("Pounds → Kilograms",   "pounds_to_kg",     "lbs",     "kg"),
    "7": ("Liters → Gallons",     "liters_to_gallons","liters",  "gallons"),
    "8": ("Gallons → Liters",     "gallons_to_liters","gallons", "liters"),
}


def convert(value, conversion_key):
    """Perform the conversion using the factor from the CONVERSIONS dict."""
    factor = CONVERSIONS[conversion_key]
    return round(value * factor, 4)


def display_menu():
    """Print the conversion menu."""
    print("\n--- Select Conversion Type ---")
    for key, (label, *_) in MENU.items():
        print(f"  {key}. {label}")
    print("  0. Quit")


def main():
    print("=" * 45)
    print("      📐  Unit Converter  📐")
    print("=" * 45)

    while True:
        display_menu()
        choice = input("\nEnter choice: ").strip()

        if choice == "0":
            print("\n👋 Goodbye!")
            break
        elif choice in MENU:
            label, conv_key, from_unit, to_unit = MENU[choice]
            try:
                value = float(input(f"Enter value in {from_unit}: "))
                result = convert(value, conv_key)
                print(f"\n✅ {value} {from_unit} = {result} {to_unit}")
            except ValueError:
                print("⚠️  Please enter a valid number.")
        else:
            print("⚠️  Invalid choice. Try again.")


if __name__ == "__main__":
    main()
