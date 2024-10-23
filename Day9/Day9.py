# blind auction program 
import os 

bidders = {}
bidding_finished = False

def find_highest_bidder(bidding_list):
    highest_bid = 0
    winner = ""
    for bidder in bidding_list:
        bid_amount = bidding_list[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner}, with a bid of ${highest_bid:2}")

while not bidding_finished:
    print("Welcome to the secret auction program!")
    name = input("What is your name: ")
    price = float(input("What is your bid value: $"))
    bidders[name] = price 
    while True:
        should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
        if should_continue == "yes":
            os.system('cls')
            break
        elif should_continue == "no":
            bidding_finished = True 
            find_highest_bidder(bidding_list=bidders)
            break
        else: 
            print("You typed something wrong.")
            

