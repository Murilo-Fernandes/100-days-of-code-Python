import colorgram 
from turtle import Turtle, Screen 
import turtle as t
import random
t.colormode(255)  # Enable RGB color mode

t = Turtle()
screen = Screen()
# colors = colorgram.extract('Day 18 end\image.jpeg', 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
color_list = [(246, 244, 243), (235, 240, 246), (247, 240, 243), (240, 246, 243), (133, 164, 202), (225, 150, 101), (30, 43, 64), (201, 136, 148), (163, 59, 49), (236, 212, 88), (44, 101, 147), (136, 181, 161), (148, 64, 72), (51, 41, 45), (161, 32, 29), (60, 115, 99), (59, 48, 45), (170, 29, 32), (215, 83, 73), (236, 167, 157), (230, 163, 168), (36, 61, 55), (15, 96, 71), (33, 60, 106), (172, 188, 219), (194, 99, 108), (106, 126, 158), (18, 83, 105), (175, 200, 188), (35, 150, 209)]

t.penup()
t.hideturtle()
t.speed("fastest")
t.setheading(225)
t.forward(300)
t.setheading(0)
number_of_dots = 100
for dot_count in range(1, number_of_dots + 1):
    t.dot(20, random.choice(color_list))
    t.forward(50)

    if dot_count % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)

screen.exitonclick()
