from turtle import Turtle, Screen
import random
import turtle as t

t.colormode(255)  # Enable RGB color mode

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def draw_spirograph():
    for angle in range(0, 360, size_of_gap):
        t.color(random_color())
        t.setheading(angle)
        t.circle(100)

t = Turtle()
screen = Screen()
size_of_gap = 3
t.speed("fastest")

draw_spirograph()

screen.exitonclick()