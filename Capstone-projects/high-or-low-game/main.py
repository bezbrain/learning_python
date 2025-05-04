import random
import game_data


game_over = False
correct_answers = 0


# Function to structure the random peron
def person_func(name, description, country):
    return f"Name: {name} \n Description: {description} \n Country: {country}"


while not game_over:
    get_first_random_dictionary = random.choice(game_data.data)
    get_second_random_dictionary = random.choice(game_data.data)
    print(get_first_random_dictionary)
    print(get_second_random_dictionary)

    if get_second_random_dictionary == get_first_random_dictionary:
        get_second_random_dictionary = random.choice(game_data.data)

    A = person_func(
        get_first_random_dictionary["name"],
        get_first_random_dictionary["description"],
        get_first_random_dictionary["country"],
    )

    B = person_func(
        get_second_random_dictionary["name"],
        get_second_random_dictionary["description"],
        get_second_random_dictionary["country"],
    )

    more_popular_question = input(
        f"\n\n\n\nWho is more popular: \n A = {A} \n\n or \n\n B = {B} \n\n"
    ).lower()

    # Condition for chosen person
    if more_popular_question == "a":
        if (
            get_first_random_dictionary["follower_count"]
            > get_second_random_dictionary["follower_count"]
        ):
            print(
                f"\n\nYou are correct, {get_first_random_dictionary['name']} is more popular \n\n"
            )
            correct_answers += 1
        else:
            print(
                f"\n\nYou are NOT correct, {get_first_random_dictionary['name']} is NOT more popular. You got {correct_answers} correctly"
            )
            game_over = True
    elif more_popular_question == "b":
        if (
            get_second_random_dictionary["follower_count"]
            > get_first_random_dictionary["follower_count"]
        ):
            print(
                f"\n\nYou are correct, {get_second_random_dictionary['name']} is more popular \n\n"
            )
            correct_answers += 1
        else:
            print(
                f"\n\nYou are NOT correct, {get_second_random_dictionary['name']} is NOT more popular. You got {correct_answers} correctly"
            )
            game_over = True
    else:
        print("You have chosen an invalid option, please try again")
        more_popular_question = input(
            f"\n\n\n\nWho is more popular: \n A = {A} \n\n or \n\n B = {B} \n\n"
        ).lower()
