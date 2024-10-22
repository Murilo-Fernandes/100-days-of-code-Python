# This is a light version of the code in the course, because i didn't download the hangman stuff

import random

word_list = ["Batgirl", "Kenzie", "Jezabel"]
secret_word = random.choice(word_list).lower()

display = "_" * len(secret_word)
guessed_letters = ""
print(display)
lifes = 5

while lifes > 0:
    guess = input("Guess a letter: ").lower()
    if len(guess) == 1:
        if guess in guessed_letters:
            print(f"You already guessed the letter: {guess}")
            continue
        guessed_letters += guess
        
        if guess not in secret_word:
            lifes -= 1
            if lifes != 0:
                print(f"You guessed wrong, and lost 1 life. Now you have only {lifes}")
            else:
                print("You lost the game!")
                break
            continue

        display = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display += letter
            else:
                display += "_"
        
        print(display)
        
        if display == secret_word:
            print(f"The secret word was {secret_word}! \nCongratulations, you guessed it!")
            break
    else:
        print("Digite apenas uma letra!")
