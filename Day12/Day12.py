# Number guessing game.
import random

def choose_secret_number():
    """Choose a random number between 1 and 100"""
    return random.randint(1,100) # Define the secret number  

def get_attempts():
    """Return the amount of attempts, based on the difficulty"""
    while True:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if difficulty == "easy":
            return 10
        elif difficulty == "hard":
            return 5
        else:
            print("Invalid difficulty level. Choose 'easy' or 'hard'.")

def play_game(secret_number, attempts):
    """Code that runs the game"""
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        
        if guess > secret_number:
            print("Too high.\nGuess again.\n")
            attempts -= 1
        elif guess < secret_number:
            print("Too low.\nGuess again.\n")
            attempts -= 1
        else:
            print(f"You got it! The answer was {secret_number}.")
            return
        
        if attempts == 0:
            print("You've run out of guesses. Try again.")
            return
        
def start_game():
    """Start the number guessing game!!"""
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number beetween 1 and 100.")
    secret_number = choose_secret_number()
    attempts = get_attempts()

    play_game(secret_number=secret_number,attempts=attempts)

while input("Wanna play a guessing number game? Type 'y' for yes or anything else for no: ") == 'y':
    start_game()
else:
    print("See you next time!")
            



