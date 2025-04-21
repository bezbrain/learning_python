import random
import math

friends = ["Ola", "Mike", "Segun", "Timothy", "Alade", "Austin"]

random_number = math.floor(random.random() * len(friends))
# print(random_number)

print(f"{friends[random_number]} will be paying the bill")

# Using the chioce method on random to get the random item from the list
print(random.choice(friends))
