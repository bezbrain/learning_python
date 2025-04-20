constant = 2
your_number = float(input("Input your number: "))

result = your_number % constant

if result == 0:
    print("You are correct, no remainder")
else:
    print("There is a remainder, hence not correct")
