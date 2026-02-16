# -----------------------------------------------------------------------------------
# Level 9: OOP with Variables
# Concept: Classes and Objects
#
# Goal: Group variables (attributes) and functions (methods) into a Class.
# -----------------------------------------------------------------------------------

# 1. Defining a Class
# A Class is a blueprint for creating objects.
class Car:
    def __init__(self, brand, model, color):
        # These are "Instance Variables" - variables unique to each car
        self.brand = brand
        self.model = model
        self.color = color
        self.speed = 0 # Default variable
    
    def accelerate(self):
        self.speed = self.speed + 10
        print(f"The {self.color} {self.brand} accelerates to {self.speed} km/h.")

    def brake(self):
        self.speed = 0
        print(f"The {self.brand} has stopped.")

print("--- Car Showroom ---")

# 2. Creating Objects (Instances)
# We create two different variables using the same Class blueprint
car1 = Car("Toyota", "Corolla", "Red")
car2 = Car("Tesla", "Model 3", "White")

# 3. Using Object Variables
print(f"Car 1 is a {car1.color} {car1.brand}.")
print(f"Car 2 is a {car2.color} {car2.brand}.")

# 4. Using Object Methods
car1.accelerate()
car1.accelerate()
car2.accelerate()
car1.brake()

# -----------------------------------------------------------------------------------
# Expected Output:
# --- Car Showroom ---
# Car 1 is a Red Toyota.
# Car 2 is a White Tesla.
# The Red Toyota accelerates to 10 km/h.
# The Red Toyota accelerates to 20 km/h.
# The White Tesla accelerates to 10 km/h.
# The Toyota has stopped.
# -----------------------------------------------------------------------------------
