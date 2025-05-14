# This is a higher or lower game where the user has to guess wich football player has more goals 

from players import data 
import random 
import os 

def higher_or_lower():
    """Higher or Lower game where the user guesses which player has more goals."""
    
    print("Welcome to the Higher or Lower game!")
    print("Guess which player has more goals.")
    print("Type 'A' or 'B' to make your choice.")
    print("Let's play!\n")

    player_a = random.choice(data)
    player_b = random.choice(data)
    while player_a == player_b:
        player_b = random.choice(data)
    score = 0
    game = True

    while game: 
        print(f"Current score: {score}")
        if player_a == player_b:
            player_b = random.choice(data)

        print(f"Compare A: {player_a['name']}, a {player_a['description']}")
        print("VS")
        print(f"Against B: {player_b['name']}, a {player_b['description']}")

        choice = input("Who has more goals? Type 'A' or 'B': ").upper()

        if choice == 'A':

            if player_a['goals'] > player_b['goals']:
                os.system('cls')
                print(f"Correct! {player_a['name']} has {player_a['goals']} goals. {player_b['name']} has {player_b['goals']} goals.")
                

                if score > 0:
                    player_a = player_b
                    player_b = random.choice(data)
                    while player_a == player_b:
                        player_b = random.choice(data)
                else:
                    player_b = random.choice(data)

                score += 1

            else:
                os.system('cls')
                print(f"Wrong! {player_b['name']} has {player_b['goals']} goals. {player_a['name']} has {player_a['goals']} goals.")
                game = False

        elif choice == 'B':
            os.system('cls')
            if player_b['goals'] > player_a['goals']:
                print(f"Correct! {player_b['name']} has {player_b['goals']} goals. {player_a['name']} has {player_a['goals']} goals.")
                player_a = player_b
                player_b = random.choice(data)
                score += 1
            else:
                os.system('cls')
                print(f"Wrong! {player_b['name']} has {player_b['goals']}.")
                game = False
        else:
            os.system('cls')
            print("Invalid input. Please type 'A' or 'B'.")
            continue

    print("Game over. Your final score is:", score)
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != 'y':
        game = False
        print("Thanks for playing!")
    else:
        os.system('cls')
        higher_or_lower()


higher_or_lower()
