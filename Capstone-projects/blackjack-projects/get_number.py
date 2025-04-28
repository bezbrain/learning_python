import random


def generate_number():
    """Generate a number randomly from a list"""
    possible_number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    get_random_number = random.choice(possible_number)
    # print(get_random_number)
    return get_random_number
