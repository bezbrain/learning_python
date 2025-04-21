# Write a programme to display head or tail randomly

import random
import math

head_or_tail = ["Head", "Tail"]

random_number = random.random() * 2
# print(random_number)
round_off = math.ceil(random_number)
# print(round_off)

print(head_or_tail[round_off - 1])
