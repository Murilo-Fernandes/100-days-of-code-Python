# This is a Secret Auction program that allows users to place bids on items.
# The program keeps track of the highest bid and the winner's name.
import os 
def clear():
    os.system('cls')

def highest_bidder(bidders):
    for key in bidders:
        if bidders[key] == max(bidders.values()):
            winner = key 
            winning_bid = bidders[key]
    clear()
    print(f"The winner is {winner} with a bid of ${winning_bid:.2f}")

def auction():
    bidders = {}
    while True: 
        name = input("Enter your name: ")
        bid = float(input("Enter your bid: $"))
        bidders[name] = bid 
        while True: 
            more_bidders = input("Are there any other bidders? (yes/no): ").lower()
            if more_bidders == "no":
                break
            elif more_bidders == "yes":
                clear()
                break
            else:
                print("Please enter 'yes' or 'no'.")
                continue
        if more_bidders == "yes":
            clear()
            continue
        else:
            break
        
    highest_bidder(bidders)

            
auction()



