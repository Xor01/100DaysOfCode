from turtle import Screen
from paddle import Paddle


screen = Screen()
paddle1 = Paddle()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(600, 600)

screen.exitonclick()
