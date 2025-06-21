import turtle
from turtle import Turtle, Screen
donnatello = Turtle() 

my_screen = Screen()
print(my_screen.canvheight)  # Print the height of the screen
# This will keep the window open until clicked
donnatello.shape("turtle")
donnatello.color("red", "lightblue")  # Set the color of the turtle
donnatello.speed(2)  # Set the speed of the turtle
donnatello.forward(50)
donnatello.circle(50)
donnatello.forward(50)
donnatello.circle(50)
donnatello.forward(50)
donnatello.circle(50)
my_screen.exitonclick()  