from turtle import Screen
from paddle import Paddle


screen = Screen()
paddle1 = Paddle()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(600, 600)

screen.listen()

screen.onkeypress(paddle1.up, "Up")
screen.onkeypress(paddle1.down, "Down")


screen.exitonclick()
