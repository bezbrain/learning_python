def declare_winner_func(your_card_total, computer_card_total):
    """Function to declare a winner when game is over"""
    if your_card_total > computer_card_total and your_card_total < 21:
        print(f"So the closest to 21 is {your_card_total} YOU WON!")
    elif computer_card_total > your_card_total and computer_card_total < 21:
        print(f"So the closest to 21 is {computer_card_total}, COMPUTER WON!")
    elif your_card_total >= 21:
        print(
            f"Your current score is {your_card_total}. You are equal to 21 or have exceeded 21. YOU LOSY"
        )
    elif computer_card_total >= 21:
        print(
            f"Computer, your current score is {computer_card_total}. You are equal to 21 or have exceeded 21. COMPUTER LOST"
        )
    else:
        print(
            "There is no winner as you both have same number or you have both exceeded 21"
        )
