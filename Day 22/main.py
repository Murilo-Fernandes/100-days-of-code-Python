from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time 
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)  # Turn off animation for smoother movement 

r_paddle = Paddle((350, 0))  # Right paddle
l_paddle = Paddle((-350, 0))  # Left paddle
ball = Ball()  # Create a ball instance
scoreboard = Scoreboard()  # Create a scoreboard instance

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()

    if (ball.xcor() > 328 and ball.distance(r_paddle) < 50) or (ball.xcor() < -328 and ball.distance(l_paddle) < 50):
        ball.bounce_x()

    if ball.xcor() > 390:
        ball.reset()
        scoreboard.l_point()

    if ball.xcor() < -390:
        ball.reset()
        scoreboard.r_point()

screen.exitonclick()  # Wait for a click to exit the game