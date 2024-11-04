# The Blackjack game 
import random 
import os 

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card 

def calculate_score(cards):
    """Take a list of cards, and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 21
    elif sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards) 

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 21:
        return "Lose, opponent has a blackjack!"
    elif u_score == 21:
        return "Win with a Blackjack!"
    elif u_score > 21:
        return "You went over. You lose!"
    elif c_score > 21:
        return "Opponent went over. You win!"
    elif u_score > c_score:
        return "You win!"
    else:
        return "You lose!"

def blackjack():    
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over: 
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}\n")

        if user_score == 21 or computer_score == 21 or user_score > 21:
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
    print(f"Computer's final hand is: {computer_cards}, total score: {computer_score}")

    print(compare(u_score=user_score, c_score=computer_score))

while input("\nWanna play a blackjack game? 'y' for yes or anything for no: ") == "y":
    os.system('cls')
    blackjack()
else: 
    print("See you next time.")
