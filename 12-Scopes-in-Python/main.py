# Local vs Global scopes
# Note that there is no block scope in Python
enemies = 1


def define_enemies():
    enemies = 2  # Here, we are not trying to reassign value to the enemies variable but this is an entirely different variable
    print(f"enemies inside function: {enemies}")


define_enemies()
print(f"enemies outside function: {enemies}")


# Modifying global variable
# If for example we want to tap into the global variable from the local scope, we can do this
def increase_enemies():
    """Have access to the global variable and modify"""
    global enemies  # Note that you don't want to do this very often because it looks somehow confusing and it is prone to creating bug errors
    enemies += 1
    print(f"The value of enemies is now {enemies}")


increase_enemies()


# How to modify the global scope without using the 'global enemies' declaration
def increase_by_two(enemy):
    """Use parameter to change the value of the global variable"""
    return enemy + 2


print(f"Increase enemies by 2 to become {increase_by_two(enemies)}")
