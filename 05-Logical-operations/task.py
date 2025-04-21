# Logical operators: AND, OR and NOT

import sys

print("Welcome to Treasure Island. Your mission is to find the treasure")

# Level one
# Level one
direction = input("left or right ")
different_directions_str = direction.lower()

level_two = ""
level_three = ""

if different_directions_str == "left":
    level_two = input("swim or wait ")
elif different_directions_str == "right":
    print("Game Over")
    sys.exit()
else:
    print("What you have input is not in the right format for level 1")
    sys.exit()


# Level two
# Level two
diff_level_two_str = level_two.lower()
if diff_level_two_str == "wait":
    level_three = input("Which door? red, blue or yellow? ")
elif diff_level_two_str == "swim":
    print("Game Over")
    sys.exit()
else:
    print("What you have input is not in the right format for level 2")
    sys.exit()

# Level three
# Level three
diff_level_three_str = level_three.lower()
if diff_level_three_str == "yellow":
    print("Congratulations, you won!")
elif diff_level_three_str == "red":
    print("Game Over")
    sys.exit()
elif diff_level_three_str == "blue":
    print("Game Over")
    sys.exit()
else:
    print("What you have input is not in the right format for level 3")
    sys.exit()
