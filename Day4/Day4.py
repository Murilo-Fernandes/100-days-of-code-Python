import random

options = ["Rock", "Paper", "Scissor"]
choice = int(input("What do you choose? 0 for Rock, 1 for Paper or 2 for Scissor: "))
computer_choice = random.randint(0, 2)
print(f"You choosed {options[choice]}")

if choice < 0 or choice >= 3:
    print("You typed something invalid. You lost.")
elif choice == 0 and computer_choice == 2:
    print(f"Computer choosed {options[computer_choice]}! \nYou won!")
elif choice == 2 and computer_choice == 0:
    print(f"Computer choosed {options[computer_choice]}! \nYou lost!")
elif choice > computer_choice:
    print(f"Computer choosed {options[computer_choice]}! \nYou won!")
elif choice < computer_choice:
    print(f"Computer choosed {options[computer_choice]}! \nYou lost!")
elif choice == computer_choice:
    print(f"Computer choosed {options[computer_choice]}! \nIt's a draw!")