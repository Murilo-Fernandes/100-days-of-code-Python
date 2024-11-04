# The Blackjack game 
import random 
import os 

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card 

def calculate_score(cards):
    """Take a list of cards, and return the scored calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0 
    elif sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards) 

user_cards = []
computer_cards = []
is_game_over = False

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

choice = input("Do you want to play a blackjack game? Type 'y' or 'n': ").lower()

if choice == "y":
    while not is_game_over: 
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}\n")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True

        else:
            another_card = input("Type 'y' to get another card or type 'p' to pass: ").lower()

            if another_card == "y":
                user_cards.append(deal_card())

            else:
                is_game_over = True

                while computer_score < 17:
                    computer_cards.append(deal_card())
                    computer_score = calculate_score(computer_cards)
                print(f"Computer cards are: {computer_cards}. Total score: {computer_score}.\n")

    print(f"Your final hand is: {user_cards}, total score: {user_score}")
    print(f"Computers final hand is: {computer_cards}, total score: {computer_score}")

    if user_score > 21:
        print("You went over 21. You lose!")
    elif computer_score > 21 or user_score > computer_score:
        print("Congrats, you won!")
    elif user_score < computer_score:
        print("You lose buddy.")
    else: 
        print("I'm afraid thats a draw.")
else:
    print("I think you typed something wrong, see you next time.")
