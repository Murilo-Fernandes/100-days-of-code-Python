from turtle import Turtle, Screen
import random

t = Turtle()
screen = Screen()

def move_forward():
    t.forward(10)

def move_backward():
    t.backward(10)

def turn_left():
    t.left(10)

def turn_right():
    t.right(10)

def clear():
    t.clear()
    t.penup()
    t.home()

screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='d', fun=turn_right)
screen.onkey(key='space', fun=clear)
screen.exitonclick()

