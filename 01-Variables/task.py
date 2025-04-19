bill_amount = float(input("What is the amount of your bill? "))

tip_amount = float(input("How much are you giving as tip in percentage? 10, 12, 15? "))

split_bill = int(input("Slit bill amoung how many people? "))

tip_calculation = (tip_amount / 100) * bill_amount

final_bill = (bill_amount + tip_calculation) / split_bill

round_value = f"{final_bill:.2f}" # format the final bill to 2 decimal places including the cents (that is, instead of 27.0, it should be 27.00)

print("Your final bill is: " + str(round_value))