# This is a Secret Auction program that allows users to place bids on items.
# The program keeps track of the highest bid and the winner's name.
import os 
def clear():
    os.system('cls')

def auction():
    dict = {}
    while True: 
        name = input("Enter your name: ")
        bid = float(input("Enter your bid: $"))
        dict[name] = bid 
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
        
    for key in dict:
        if dict[key] == max(dict.values()):
            winner = key 
            winning_bid = dict[key]
    clear()
    print(f"The winner is {winner} with a bid of ${winning_bid:.2f}")

            
auction()



