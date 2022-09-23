from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 4, 0)
        self.goto(240, 0)
        self.color("white")
        self.penup()

