pizza_cost = 0

pizza_size = input("What Pizza size do you want? S, M or L? ")

if pizza_size == "S":
    pizza_cost = 15
    pepperoni = input("Add pepperoni for small pizza (Y or N)? ")
    if pepperoni == "Y":
        pizza_cost += 2
        # print(f"Your total cost is: ${pizza_cost + 2}")
    elif pepperoni == "N":
        pizza_cost
        # print(f"Your total cost is: ${pizza_cost}")
    else:
        print("You have typed an invalid option: Type Y or N")

elif pizza_size == "M":
    pizza_cost = 20
    pepperoni = input("Add pepperoni for medium pizza (Y or N)? ")
    if pepperoni == "Y":
        pizza_cost += 3
        # print(f"Your total cost is: ${pizza_cost + 3}")
    elif pepperoni == "N":
        pizza_cost
        # print(f"Your total cost is: ${pizza_cost}")
    else:
        print("You have typed an invalid option: Type Y or N")

elif pizza_size == "L":
    pizza_cost = 25
    pepperoni = input("Add pepperoni for large pizza (Y or N)? ")
    if pepperoni == "Y":
        pizza_cost += 3
        # print(f"Your total cost is: ${pizza_cost + 3}")
    elif pepperoni == "N":
        pizza_cost
        # print(f"Your total cost is: ${pizza_cost}")
    else:
        print("You have typed an invalid option: Type Y or N")
else:
    print("You have typed an invalid option: Type S, M or L")

extra_cheese = input("Add extra cheese for any size pizza (Y or N)? ")

# Condition of all three pizza types
if extra_cheese == "Y":
    pizza_cost += 1
    print(f"Your total cost is: ${pizza_cost}")
elif extra_cheese == "N":
    pizza_cost
    print(f"Your total cost is: ${pizza_cost}")
else:
    print("You have typed an invalid option: Type Y or N")
