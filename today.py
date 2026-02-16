# Day 1: Random Number Generation
import random

# Generate a random integer between 1 and 10 (inclusive)
random_integer = random.randint(1,10)

# Output the random integer
print(random_integer)


# Generate a random float between 0.0 and 1.0
random_float = random.random()

# Output the random float
print(random_float)


# Generate a random float between 1 and 10
random_float = random.uniform(1,10)
print(random_float)

random_heads_or_tails = random.randint(0,1)
if random_heads_or_tails == 1:
    print("Heads")
else:
    print("Tails")