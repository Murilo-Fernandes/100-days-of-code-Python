# It's a guess the number game 
import random 
import os 

def game(): 
    """This function will run the number guessing game."""
    os.system('cls')
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1, 100) 
    attempts = 0
    guessed = False

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        attempts = 10
    elif difficulty == "hard":
        attempts = 5
    else:
        print("Invalid choice. Defaulting to hard mode.")
        attempts = 5
    print(f"You have {attempts} attempts to guess the number.")

    while not guessed and attempts > 0:
        print(f"You have {attempts} attempts remaining.")
        guess = int(input("Make a guess: "))
        os.system('cls')

        if guess < 1 or guess > 100:
            print("Please guess a number between 1 and 100.")
            continue

        if guess < number_to_guess:
            print(f"{guess} is too low. Try again.")
            attempts -= 1

        elif guess > number_to_guess:
            print(f"{guess} is too high. Try again.")
            attempts -= 1
            
        else:
            print(f"Congratulations! You guessed the number {number_to_guess} correctly!")
            guessed = True
    
    if attempts == 0 and not guessed:
        print(f"Sorry, you've run out of attempts. The number was {number_to_guess}.")
        
    play_again = input("Do you want to play again? Type 'y' or 'n': ").lower()
    if play_again == "y":
        game()
    else:
        print("Thanks for playing! Goodbye!")

game()