# Logical operators: AND, OR and NOT

import sys

print("Welcome to Treasure Island. Your mission is to find the treasure")

# Level one
# Level one
direction = input("left or right ")
different_directions_str = direction.upper() or direction.capitalize() or direction

level_two = ""
level_three = ""

if (
    different_directions_str == "left"
    or different_directions_str == "Left"
    or different_directions_str == "LEFT"
):
    level_two = input("swim or wait ")
elif (
    different_directions_str == "right"
    or different_directions_str == "Right"
    or different_directions_str == "RIGHT"
):
    print("Game Over")
    sys.exit()
else:
    print("What you have input is not in the right format for level 1")
    sys.exit()


# Level two
# Level two
diff_level_two_str = level_two.upper() or level_two.capitalize() or level_two
if (
    diff_level_two_str == "wait"
    or diff_level_two_str == "Wait"
    or diff_level_two_str == "WAIT"
):
    level_three = input("Which door? red, blue or yellow? ")
elif (
    diff_level_two_str == "swim"
    or diff_level_two_str == "Swim"
    or diff_level_two_str == "SWIM"
):
    print("Game Over")
    sys.exit()
else:
    print("What you have input is not in the right format for level 2")
    sys.exit()

# Level three
# Level three
diff_level_three_str = level_three.upper() or level_three.capitalize() or level_three
if (
    diff_level_three_str == "yellow"
    or diff_level_three_str == "Yellow"
    or diff_level_three_str == "YELLOW"
):
    print("Congratulations, you won!")
elif (
    diff_level_three_str == "red"
    or diff_level_three_str == "Red"
    or diff_level_three_str == "RED"
):
    print("Game Over")
    sys.exit()
elif (
    diff_level_three_str == "blue"
    or diff_level_three_str == "Blue"
    or diff_level_three_str == "BLUE"
):
    print("Game Over")
    sys.exit()
else:
    print("What you have input is not in the right format for level 3")
    sys.exit()
