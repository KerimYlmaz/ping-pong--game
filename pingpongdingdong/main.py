from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("PING PONG")


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.right_up, "Up")
screen.onkey(r_paddle.right_down, "Down")
screen.onkey(l_paddle.left_up, "w")
screen.onkey(l_paddle.left_down, "s")
game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    elif ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    elif ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    elif ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    elif ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()