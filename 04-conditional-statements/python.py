amGood = True

my_age = int(input("What is your age? "))

if my_age >= 18:
    print("You are good to go")
    height = int(input("Please input your height "))
    if height > 170:
        print("You will be paying $20")
    else:
        print("You will be paying $300")
else:
    print("Sorry you cannot perform this action because you are less than 18 years")
