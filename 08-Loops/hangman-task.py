# Generate a random word
# Generate as many blanks as letters in word
# Ask the user to guess a letter
# Is the guessed letter in the word?
# If yes, replace the blank with the letter; else lose a life
# Have they run out of lives? If yes, GAME OVER
# Have they filled all spaces and still have at least one life? If yes, declare them as winner

import random

all_words = ["name", "bring", "first"]
total_lives = 6

random_word = random.choice(all_words)
print(random_word)

# placeholder = ""
# for position in range(0, len(random_word)):
#     placeholder += "_"

# print(placeholder)


game_over = False
correct_letters = []

while not game_over:
    chosen_letter = input("Guess a letter: ").lower()
    display = ""
    total_lives -= 1
    for letter in random_word:
        if letter == chosen_letter:
            # print("first")
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            # print("second")
            display += letter
        else:
            # print("third")
            display += "-"
    print(display)

    if "-" not in display:
        game_over = True
        print("You won")
    if "-" in display and total_lives == 0:
        game_over = True
        print("You lost")
