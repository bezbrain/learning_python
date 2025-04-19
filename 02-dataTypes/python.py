# Primitive data type
string_value = 'Hellopp' 
string_length = len(string_value)
# print(string_length)

# Last character of the string
last_character = string_value[string_length -1]
# print(last_character)

# print(123456789)

# Floating point numbers: More like decimal number

# Type Conversion or Type Casting
stringified_number = '1234'
# Convert string to integer
number = int(stringified_number)
# print(type(number))

# print('Number of letters in your name: ' + str(len(input("Enter your name: "))))

# Mathematical Operation
print(2 + 3) # Addition
print(2 - 3) # Subtraction
print(2 * 3) # Multiplication
print(2 / 3) # Division (Cast type to float)
print(2 // 3) # Floor Division (do not cast type to float, that is, only convert to integer)
print(2 ** 3) # Exponentiation
print(2 % 3) # Modulus (Remainder)
print(2 + 3 * 4) # Order of operation
print(2 + (3 * 4)) # Order of operation
print(2 + 3 * 4 - 5) # Order of operation
print(2 + 3 * (4 - 5)) # Order of operation
