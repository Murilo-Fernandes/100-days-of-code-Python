# This is the blackjack game program that simulates a simple version of the game.
import random 
import os 

def deal_card():
    """This function will return a random card from the cards list."""
    cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards) 

def calculate_score(cards):
    """This function will calculate the score of the cards."""

    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def check_winner(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You Win"
    elif user_score > computer_score:
        return "You Win"
    else: 
        return "You lose"

def game():
    while True:  
        is_game_over = False
        user_cards = []
        computer_cards = []
        user_score = -1
        computer_score = -1

        for _ in range(2):
            user_cards.append(deal_card())
            computer_cards.append(deal_card())

        while not is_game_over:
            user_score = calculate_score(user_cards)
            computer_score = calculate_score(computer_cards)
            print(f"Your cards are: {user_cards}, current score: {user_score}")
            print(f"Computer's first card: {computer_cards[0]}")

            if user_score == 0 or computer_score == 0 or user_score > 21:
                is_game_over = True
            else: 
                choice = input("Type 'y' to get another card or 'n' to pass: ").lower()
                if choice == "y":
                    user_cards.append(deal_card())
                else:
                    is_game_over = True

        while computer_score != 0 and computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)

        print(f"Your final hand: {user_cards}, final score: {user_score}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
        print(check_winner(user_score, computer_score))

        play_again = input("Type 'y' to play again or 'n' to exit: ").lower()
        if play_again == "n":
            print("Goodbye!")
            break  
        elif play_again == "y":
            os.system('cls')  
        else:
            print("Invalid input. Exiting the game.")
            break

game()











