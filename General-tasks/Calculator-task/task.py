is_continue = True
is_first_number = True


def check_sign(sign, first, second):
    if sign == "+":
        return first + second
    elif sign == "-":
        return first - second
    elif sign == "/":
        return first / second
    elif sign == "*":
        return first * second
    else:
        print("Invalid operation sign")


result = 0

while is_continue:
    if is_first_number:
        first_number = float(input("What is the first number? "))

    operation_signs_list = print(
        "What is the operation you want to perform? \n + \n - \n * \n / \n"
    )
    operation_sign = input("Pick an operation: ")

    # Check if sign is correct
    if (
        operation_sign != "+"
        or operation_sign != "-"
        or operation_sign != "/"
        or operation_sign != "*"
    ):
        print("INVALID SIGN INPUT")
        operation_signs_list = print(
            "What is the operation you want to perform? \n + \n - \n * \n / \n"
        )
        operation_sign = input("Pick an operation: ")

    next_number = float(input("What is the next number? "))

    if is_first_number:
        result = check_sign(operation_sign, first_number, next_number)
        print(f"{first_number} {operation_sign} {next_number} = {result}")
    else:
        result = check_sign(operation_sign, result, next_number)
        print(f"{result} {operation_sign} {next_number} = {result}")

    want_continue = input(
        f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: "
    )
    if want_continue == "y":
        is_continue = True
        is_first_number = False
    elif want_continue == "n":
        is_continue = False
        is_first_number = True
    else:
        print("You have typed the wrong input. Type either 'n' or 'y'")
        is_continue = True
        is_first_number = False
        want_continue = input(
            f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: "
        )
