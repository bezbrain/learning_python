bill_amount = float(input("What is the amount of your bill? "))

tip_amount = float(input("How much are you giving as tip in percentage? 10, 12, 15? "))

split_bill = int(input("Slit bill amoung how many people? "))

tip_calculation = (tip_amount / 100) * bill_amount

final_bill = (bill_amount + tip_calculation) / split_bill

print("Your final bill is: " + str(final_bill))