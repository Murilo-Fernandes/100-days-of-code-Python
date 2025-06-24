import random
from turtle import Turtle, Screen
import turtle as t 

t.colormode(255)  # Enable RGB color mode

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

tela = Screen()
magic = Turtle()
tela.bgcolor("black")
magic.pensize(12)
magic.speed("fastest")

directions = [0, 90, 180, 270]


for _ in range(100):
    magic.color(random_color())
    magic.forward(30)
    magic.setheading(random.choice(directions))

tela.exitonclick()