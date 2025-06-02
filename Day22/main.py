from turtle import Screen, Turtle
from ball import Ball
from paddle import Paddle
import time

from scoreboard import Scoreboard

# Screen
screen = Screen()
screen.setup(width=800, height=600, startx=0, starty=0)
screen.bgcolor("black")
screen.title("Bong Game")
screen.tracer(0)

# `Baddle`
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
#################################
screen.listen()

# `Right Player`
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

# `Left Player`
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

#################################

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detecting collisoin with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # bounce now
        ball.bounce_y()

    # detecting collision with the right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # when right paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # when left baddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
