# Rock, Paper, Scissors Game
import random 

print("Welcome to Rock, Paper, Scissors!")
computer_choice = random.randint(0, 2)  # 0 for Rock, 1 for Paper, 2 for Scissors
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. "))

if choice == 0:
    print("You chose Rock.")
elif choice == 1:
    print("You chose Paper.")   
elif choice == 2:
    print("You chose Scissors.")

if computer_choice == 0:
    print("Computer chose Rock.")
elif computer_choice == 1:
    print("Computer chose Paper.")
elif computer_choice == 2:
    print("Computer chose Scissors.")

if choice >= 3 or choice < 0:
    print("Invalid choice. Please try again.")
elif choice == computer_choice:
    print("It's a draw.")
elif (choice == 0 and computer_choice == 2) or (choice == 1 and computer_choice == 0) or (choice == 2 and computer_choice == 1):
    print("You win!")
elif (choice == 0 and computer_choice == 1) or (choice == 1 and computer_choice == 2) or (choice == 2 and computer_choice == 0):
    print("You lose.")
