import string
import random
import math

letters = list(string.ascii_letters)

special_characters = [
    "!",
    "@",
    "#",
    "$",
    "%",
    "^",
    "&",
    "*",
    "(",
    ")",
    "-",
    "_",
    "=",
    "+",
    "{",
    "}",
    "[",
    "]",
    "|",
    "\\",
    ":",
    ";",
    '"',
    "'",
    "<",
    ">",
    ",",
    ".",
    "?",
    "/",
]

# Stringify numbers
number_string = [str(i) for i in range(10)]

print("Welcome to the PyPassword Generator!")

number_of_letters = int(input("How many letters would you like in your password? "))

number_of_symbols = int(input("How many symbols would you like? "))

number_of_numbers = int(input("How many numbers would you like? "))

# Extract required number of letters
required_letters = ""
for letter in range(1, number_of_letters + 1):
    required_letters += random.choice(letters)
print(required_letters)

# Extract required number of symbols
required_symbols = ""
for symbol in range(1, number_of_symbols + 1):
    required_symbols += random.choice(special_characters)
print(required_symbols)

# Extract required number of numbers
required_numbers = ""
for number in range(1, number_of_numbers + 1):
    required_numbers += random.choice(number_string)
print(required_numbers)

my_static_password = f"{required_letters}{required_symbols}{required_numbers}"

# Convert to list
string_to_list = list(my_static_password)
# Shuffle the list
random.shuffle(string_to_list)

# Join back to a string
my_dynamic_password = "".join(string_to_list)
print(my_dynamic_password)
