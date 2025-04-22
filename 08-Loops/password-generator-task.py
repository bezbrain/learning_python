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
for letter in letters:
    random_numbers = math.floor(random.random() * len(letters))
    chosen_letter = letters[random_numbers]
    required_letters += chosen_letter
    if len(required_letters) == number_of_letters:
        break
print(required_letters)

# Extract required number of symbols
required_symbols = ""
for symbol in special_characters:
    random_numbers = math.floor(random.random() * len(special_characters))
    chosen_special_character = special_characters[random_numbers]
    required_symbols += chosen_special_character
    if len(required_symbols) == number_of_symbols:
        break
print(required_symbols)

# Extract required number of numbers
required_numbers = ""
for number in number_string:
    random_numbers = math.floor(random.random() * len(number_string))
    chosen_number = number_string[random_numbers]
    required_numbers += chosen_number
    if len(required_numbers) == number_of_numbers:
        break
print(required_numbers)

my_static_password = f"{required_letters}{required_symbols}{required_numbers}"

# Convert to list
string_to_list = list(my_static_password)
# Shuffle the list
random.shuffle(string_to_list)

# Join back to a string
my_dynamic_password = "".join(string_to_list)
print(my_dynamic_password)
