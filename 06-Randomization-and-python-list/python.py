# Randomization and Python Lists
import random
import sys


random_number = random.randint(1, 5)

what_to_choose = int(input("What is your guess number between 1 t0 5? "))

if what_to_choose == random_number:
    print(
        f"I am proud of you, your guess was correct with the system which was {random_number}"
    )
else:
    print(
        f"I am sorry to inform you that your guess was incorrect. The system chose {random_number}"
    )
