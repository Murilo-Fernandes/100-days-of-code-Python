import random 
import super_heroes
import os

def get_random_word(word_list):
    """Returns a random word from the given list of words."""
    return random.choice(word_list).upper()  # Selects a random word and converts it to uppercase

def iniciar_jogo():
    print("Welcome to Hangman game! Words with spaces will be separated by a hyphen.")
    print("You have 6 lives to guess the word.")
    checked_letters = []  # List to keep track of guessed letters
    lives = 6  # Total lives the player has
    game_over = False  # Flag to indicate if the game is over
    word = get_random_word(super_heroes.secret_words)  # Fetch a random word from the super_heroes module
    display = "_" * len(word)  # Create a display string with underscores for each letter in the word

    while not game_over:  # Main game loop
        print("Lives left: ", lives)  # Display remaining lives
        print(display)  # Display the current state of the guessed word
        guess = input("Guess a letter: ").upper()  # Get the player's guess and convert it to uppercase
        os.system('cls')  # Clear the console (Windows-specific command)
        if len(guess) != 1:  # Ensure the player enters only one letter
            print("Please enter a single letter.")
            continue 

        if guess in checked_letters:  # Check if the letter has already been guessed
            print("You already guessed that letter.")
            continue

        elif guess in word:  # If the guessed letter is in the word
            display = ""  # Reset the display string
            for letter in word:  # Rebuild the display string with correctly guessed letters
                if letter in checked_letters or letter == guess:
                    display += letter 
                else:
                    display += "_"
            checked_letters.append(guess)  # Add the guessed letter to the list of checked letters

        else:  # If the guessed letter is not in the word
            lives -= 1  # Decrease the player's lives
            checked_letters.append(guess)  # Add the guessed letter to the list of checked letters
            print("Incorrect guess.")

        if lives == 0:  # If the player runs out of lives
            print("Game Over! The word was:", word)
            game_over = True  # End the game

        if display == word:  # If the player has guessed the entire word
            print("Congratulations! You guessed the word:", word)
            choice = input("Do you want to play again? (Y/N): ").upper()  # Ask if the player wants to play again
            if choice == "Y":  # Restart the game if the player chooses "Y"
                game_over = True
                os.system('cls')  # Clear the console
                iniciar_jogo()  # Restart the game
            else:  # End the game if the player chooses "N"
                print("Thanks for playing!")
                game_over = True
                break
