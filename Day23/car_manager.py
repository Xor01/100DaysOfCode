from random import randint, choice
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 2, 0)
        self.left(90)
        self.setheading(180)
        self.color(choice(COLORS))
        self.penup()
        self.goto(randint(350, 660), randint(-230, 230))

    def move(self):
        self.forward(STARTING_MOVE_DISTANCE)
