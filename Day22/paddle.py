from turtle import Turtle

SPEED = 0


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(1, 4, 0)
        self.setheading(90)
        self.speed(SPEED)
        self.goto(240, 0)

    def up(self):
        self.forward(10)

    def down(self):
        self.forward(-10)
