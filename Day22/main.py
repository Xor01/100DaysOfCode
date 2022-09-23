from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep
screen = Screen()
screen.setup(800, 600)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")

screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

game_on = True

while game_on:
    sleep(0.05)
    screen.update()
    ball.move()

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with the paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()



screen.exitonclick()
