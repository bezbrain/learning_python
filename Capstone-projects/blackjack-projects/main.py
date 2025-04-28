# The Blackjack game
# The Blackjack game
# The Blackjack game
# The goal is to be as close to 21 as possible than the opponent
# First, you request for a number, and the computer also request for a number.
# You can quit the game at any point if you believe you are close to 21 already than your opponent.
# If you go beyond 21, you have lost already

import get_number
import declare_winner


start_game = input(
    "Do you want to start the Blackjack game now? Type 'y' for yes and 'n' for no? "
)

is_start = True
your_card_total = 0
computer_card_total = 0
my_turn = True
computer_turn = False


def game_over():
    """Activate game over"""
    global is_start, your_card_total, computer_card_total, my_turn, computer_turn
    is_start = False
    your_card_total = 0
    computer_card_total = 0
    my_turn = True
    computer_turn = False


while start_game == "y" and is_start:
    request_statement = input("Type 'y' to get a card, type 'n' to pass: ")
    generate_number = get_number.generate_number()

    if my_turn:
        if request_statement == "y":
            your_card_total += generate_number
            print(f"Your total card score is {your_card_total}")
            my_turn = False
            computer_turn = True
            if your_card_total >= 21:
                declare_winner.declare_winner_func(your_card_total, computer_card_total)
                game_over()

        else:
            print(
                f"Your card total is {your_card_total} while computer's is {computer_card_total}"
            )
            declare_winner.declare_winner_func(your_card_total, computer_card_total)
            game_over()

    else:
        if request_statement == "y":
            computer_card_total += generate_number
            print(f"Computer total is now: {computer_card_total}")
            my_turn = True
            computer_turn = False
            if computer_card_total >= 21:
                declare_winner.declare_winner_func(your_card_total, computer_card_total)
                game_over()
        else:
            print(
                f"Computer, your card total is {computer_card_total} while your opponent's is {your_card_total}"
            )
            declare_winner.declare_winner_func(your_card_total, computer_card_total)
            game_over()
