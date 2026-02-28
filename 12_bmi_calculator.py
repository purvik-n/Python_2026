# ============================================================
# Program 12: BMI Calculator
# Concepts: Functions, conditionals, arithmetic, input validation
# ============================================================

# BMI (Body Mass Index) Formula:
#   BMI = weight (kg) / height (m) ^ 2
# It is a simple health screening tool.

def calculate_bmi(weight_kg, height_m):
    """
    Calculate BMI using weight in kg and height in meters.
    Returns the BMI value rounded to 2 decimal places.
    """
    if height_m <= 0:
        raise ValueError("Height must be greater than 0.")
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)


def get_bmi_category(bmi):
    """
    Return the BMI category based on WHO guidelines.
    Underweight < 18.5
    Normal: 18.5 - 24.9
    Overweight: 25 - 29.9
    Obese: >= 30
    """
    if bmi < 18.5:
        return "Underweight 🧊", "Consider eating more nutritious meals."
    elif bmi < 25:
        return "Normal weight ✅", "Great! Keep maintaining a healthy lifestyle."
    elif bmi < 30:
        return "Overweight ⚠️", "Consider more physical activity and balanced diet."
    else:
        return "Obese 🚨", "Please consult a healthcare professional."


def get_float_input(prompt):
    """
    Safely get a positive float value from the user.
    Keeps asking until a valid number is entered.
    """
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("⚠️  Value must be positive. Try again.")
            else:
                return value
        except ValueError:
            print("⚠️  Invalid input. Please enter a number.")


def main():
    print("=" * 45)
    print("        ⚖️  BMI Calculator  ⚖️")
    print("=" * 45)
    print("Calculate your Body Mass Index (BMI)\n")

    # Get user inputs
    weight = get_float_input("Enter your weight in kg: ")
    height = get_float_input("Enter your height in meters (e.g. 1.75): ")

    # Calculate BMI
    bmi = calculate_bmi(weight, height)
    category, advice = get_bmi_category(bmi)

    # Display results
    print("\n--- 📊 Your Results ---")
    print(f"  Weight : {weight} kg")
    print(f"  Height : {height} m")
    print(f"  BMI    : {bmi}")
    print(f"  Status : {category}")
    print(f"  Advice : {advice}")
    print("-" * 25)


if __name__ == "__main__":
    main()
