from turtle import Turtle

SPEED = 0


class Paddle(Turtle):
    def __init__(self, cor):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(1, 4, 0)
        self.setheading(90)
        self.speed(SPEED)
        self.goto(cor)

    def up(self):
        self.forward(20)

    def down(self):
        self.forward(-20)
