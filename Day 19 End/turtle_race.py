from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor("black") 
turtles = []

colors = ["red", "orange", "yellow", "green", "cyan", "purple"]
num = 0

for turtle in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[num])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=100 - turtle * 40)
    num += 1
    turtles.append(new_turtle)

user_bet = screen.textinput(title="Make your bet!", prompt="Enter the name of the turtle you think will win:")

if user_bet:
    is_race_on = True

while is_race_on:
    
    for turtle in turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You lose! The {winning_color} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()