print("This is a treasure map!")
print("Welcome to the treasure island!\nYour mission is to find the treasure.")
choice1 = input("You're at a crossroad. Which way do you want to go? Left or Right: ").capitalize()

if choice1 == "Left":
    choice2 = input("You've come to a lake. There is an island in the middle of the lake.\n Type 'wait' to wait for a boat and 'swim' to swim across the river. ").capitalize()
    if choice2 == "Wait":
        choice3 = input("You waited for a boat and crossed the river safely.\n  Now you reach a room with three doors: one red, one blue, and one yellow.\n Which door do you choose? ").capitalize()
        if choice3 == "Red":
            print("Magically you set yourself on fire. You died.")
        elif choice3 == "Blue":
            print("It starts raining swords. You died.")
        elif choice3 == "Yellow":
            print("Now you're rich! You found the treasure.")
        else:
            print("You died because you don't know how to write.")
    elif choice2 == "Swim":
        print("You tried to swim across and got eaten by a crocodile.")
    else:
        print("Invalid choice. Game over.")
else:
    print("You're already dead.")
