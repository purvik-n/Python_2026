import random

random_integer = random.randint(1,10)
print(random_integer)

random_float = random.random()
print(random_float)

random_float = random.uniform(1,10)
print(random_float)

random_heads_or_tails = random.randint(0,1)
if random_heads_or_tails == 1:
    print("Heads")
else:
    print("Tails")