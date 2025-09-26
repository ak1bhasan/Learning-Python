import art

print(art.logo)

def find_highest_bidder( bidding_dictionary ):
    winner = max( bidding_dictionary, key = bidding_dictionary.get )
    highest_bid = bidding_dictionary[winner]

    print(f"The winner is {winner} with a bid of $ {highest_bid}.")

bids = {}
continue_bidding = True

while continue_bidding:
    name = input("What is your name?:  ")
    price = int(input("What is your bid?: $ "))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 30)

