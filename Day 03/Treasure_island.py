# This code will be an interactive treasure hunt game where the player has to make choices to find the treasure.

# Welcoming the player
print("""  _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                                                 
 """)

print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")

print("\nYou're at a crossroad. Where do you want to go? Type 'l' for left or 'r' for right.")
choice1 = input().lower()

if choice1 == 'r':
    print("\nYou fell into a hole. Game Over.")
elif choice1 == 'l':
    print("\nYou come to a lake. There is an island in the middle of the lake.")
    print("Type 's' to swim across or 'w' to wait for a boat.")
    choice2 = input().lower()
    if choice2 == 's':
        print("\nYou get attacked by a trout. Game Over.")

    elif choice2 == 'w':
        print("\nYou arrive at the island unharmed.")
        print("There is a house with three doors. One 'red', one 'yellow', and one 'blue'")
        print("Type 'y' for yellow, 'r' for red, or 'b' for blue.")
        choice3 = input().lower()

        if choice3 == "b":
            print("\nYou enter a room full of bats. Game Over.")
        elif choice3 == "r":
            print("\nYou enter a room of fire. Game Over.")
        elif choice3 == "y":
            print("\nYou found the treasure! You Win!")