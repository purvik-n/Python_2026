
# Working with Nested Lists and Handling IndexError

# 1. Nested Lists
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print("Dirty Dozen (Nested List):")
print(dirty_dozen)

# Accessing elements
print("\nAccessing the second list (vegetables):")
print(dirty_dozen[1])

print("\nAccessing the second item of the second list (Kale):")
print(dirty_dozen[1][1])


# 2. IndexError Example
# IndexError happens when you try to access an index that is out of range.

print("\n--- IndexError Example ---")
try:
    # fruits list has 7 items (index 0 to 6)
    # Trying to access index 7 will cause an error
    print(fruits[7])
except IndexError:
    print("An IndexError occurred! You tried to access an index that doesn't exist.")

# Another example with nested lists
try:
    # dirty_dozen has only 2 items (index 0 and 1)
    print(dirty_dozen[2])
except IndexError:
    print("Cannot access index 2 of dirty_dozen.")
