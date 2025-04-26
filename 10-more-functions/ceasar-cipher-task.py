# Ceasar used to encode his instruction using some patterns. We want to write a progaramme to handle the encoding and decoding

# Example: If the code is ABCD and the shift number is 2, then A becomes C, B becomes D, C becomes E, and D becomes F. So, the encrypted code will be   CDEF

import string

letters = list(string.ascii_lowercase)
# print(letters)

code_status = input('Type "encode" to encrypt, type "decode" to decrypt: ')
plain_text = input("Type your message: ").lower()
shift_number = int(input("Type the shift number: "))

encrypted_code_list = []

for letter in plain_text:
    wrapped_index = 0
    indexValue = letters.index(letter) + 1
    if (indexValue + shift_number) >= len(letters):
        wrapped_index = ((indexValue + shift_number) % len(letters)) + shift_number - 1
    else:
        wrapped_index = shift_number + indexValue - 1

    # print("index value", indexValue)
    # print("letters length", len(letters))
    # print("wrapped index", wrapped_index)
    mimic_letter = letters[wrapped_index]
    encrypted_code_list.append(mimic_letter)

print(encrypted_code_list)

# Concatinate string in array
encrypted_code = ""

for char in encrypted_code_list:
    encrypted_code += char

print(encrypted_code.upper())
