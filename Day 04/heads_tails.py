# Heads or Tails Game 
import random 

choice = int(input("Heads or Tails? Type 0 for Heads and 1 for Tails: ")) 
answer = random.randint(0, 1) 
if choice == answer:
    print("You win!")
else:
    print("You lose!")
