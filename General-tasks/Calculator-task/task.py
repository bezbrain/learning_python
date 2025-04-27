is_continue = True
is_first_number = True


# Perform arithmetics
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


# Operation list
def operation():
    print("What is the operation you want to perform? \n + \n - \n * \n / \n")
    return input("Pick an operation: ")


result = 0
result_in_text = ""

while is_continue:
    if is_first_number:
        first_number = float(input("What is the first number? "))

    operation_sign = operation()

    # Check if sign is correct
    while operation_sign not in ["+", "-", "/", "*"]:
        print("INVALID SIGN INPUT")
        operation_sign = operation()

    next_number = float(input("What is the next number? "))

    if is_first_number:
        result = check_sign(operation_sign, first_number, next_number)
        result_in_text = f"{first_number} {operation_sign} {next_number} = {result}"
        print(result_in_text)
    else:
        result_in_text = result  # Set text result to the latest result
        result = check_sign(operation_sign, result, next_number)
        print(f"{result_in_text} {operation_sign} {next_number} = {result}")

    want_continue = input(
        f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: "
    ).lower()

    # Check if y or n is typed correctly
    if want_continue == "y":
        is_continue = True
        is_first_number = False
    elif want_continue == "n":
        is_continue = False
        is_first_number = True
        print(f"Your final result is {result}")
    else:
        while want_continue not in ["y", "n"]:
            print("YOU HAVE TYPED THE WRONG INPUT. Type either 'n' or 'y'")
            is_continue = True
            is_first_number = False
            want_continue = input(
                f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: "
            ).lower()
