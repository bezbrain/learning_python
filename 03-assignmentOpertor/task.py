# Tip calculator

welcome_statement = "Welcome to the tip calculator!"
print(welcome_statement)

total_bill = float(input("What was the total bill? "))

tip = float(input("How much would you like to tip? 10, 12, or 15? "))

tip_calculation = ((tip) / 100) * (total_bill)

amount_with_tip = total_bill + tip_calculation

split_bill = int(input("How many people to split the bill? "))

splited_bill = amount_with_tip / split_bill

new_total_bill = round(splited_bill, 2)

print(f"Each person should pay: ${new_total_bill}")
