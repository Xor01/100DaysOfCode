from random import randint, choice
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars_list = []

    def create_car(self):
        random_num = randint(1, 6)
        if random_num == 2:
            car = Turtle(shape="square")
            car.penup()
            car.shapesize(1, 2, 0)
            car.color(choice(COLORS))
            car.goto(300, randint(-250, 250))
            self.cars_list.append(car)

    def move_cars(self):
        for car in self.cars_list:
            car.backward(STARTING_MOVE_DISTANCE)
