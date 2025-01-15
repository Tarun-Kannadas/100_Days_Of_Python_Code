# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

# def compare_bids(bidding_dictionary):
#     winner = ""
#     highest_bid = 0
#     for bidder in bidding_dictionary:
#         bid_amount = bidding_dictionary[bidder]
#         if bid_amount > highest_bid:
#             highest_bid = bid_amount
#             winner = bidder
#
#     print(f"The winner is {winner} with a bid of ${highest_bid}")

import art

print(art.logo)

continue_auction = True

dictionary = {}

print("Welcome to the Auction!")

while continue_auction:

    name = input("What is your name?: ")
    bid = int(input("What's your bid? $"))

    dictionary[name] = bid

    continue_bid = input("Are there other bidders? Yes? or No? ").lower()

    if continue_bid == "yes":
        print("\n"*50)

    if continue_bid == "no":
        continue_auction = False
        # compare_bids(dictionary)
        winner = max(dictionary, key=dictionary.get)
        print(f"The winner is {winner} with an amount of ${dictionary[winner]}")
