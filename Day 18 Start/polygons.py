from turtle import Turtle, Screen

colors = ["red", "orange", "yellow", "green", "black", "blue", "purple", "cyan", "magenta", "pink"]
tela = Screen()
magic = Turtle()

num_sides = 10

def draw_polygon(sides):
    angle = 360 / sides
    for _ in range(sides):
        magic.forward(100)
        magic.left(angle)

for shape_side_n in range(3, num_sides + 1):
    magic.color(colors[shape_side_n % len(colors)])
    draw_polygon(shape_side_n)

tela.exitonclick()