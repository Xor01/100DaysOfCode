from random import randint, choice
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.cars_list = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_num = randint(1, 6)
        if random_num == 2 or random_num == 6:
            car = Turtle(shape="square")
            car.penup()
            car.shapesize(1, 2, 0)
            car.color(choice(COLORS))
            car.goto(300, randint(-250, 250))
            self.cars_list.append(car)

    def move_cars(self):
        for car in self.cars_list:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
