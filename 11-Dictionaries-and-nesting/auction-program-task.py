# Write a program that collects the name of a bidder
# Collects the bid amount
# Allows an instruction to select if there are more bidders. If yes, the process above should run again

bid_confirmation = "yes"
all_bidders = []

while bid_confirmation == "yes":
    bidder_name = input("What is your name? ")
    bid_amount = int(input("What is your bid?: $"))
    bid_confirmation = input(
        "Are there any other bidders? Type 'yes' or 'no' \n"
    ).lower()

    # Push dictionary into list
    all_bidders.append({"name": bidder_name, "amount": bid_amount})
    if bid_confirmation == "no":
        highest_bid = max(all_bidders, key=lambda x: x["amount"])
        print(
            f"The highest bidder is {highest_bid['name']} and they paid ${highest_bid['amount']}"
        )
        bid_confirmation = "no"
