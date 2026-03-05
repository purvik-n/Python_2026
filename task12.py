import random
# Defining a list of friends for random selection
friends = ["Aman", "Rahul", "Sonia", "Priya", "Amit"]
# 1 option
# Directly using random choice
print(random.choice(friends))
# 2 option 
rendom_index = random.randint(0,4)
print(friends[rendom_index])