import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from random import randint
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

cars = []

player = Player()
for _ in range(10, randint(50, 100)):
    car = CarManager()
    cars.append(car)
screen.onkeypress(player.up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    for i in cars:
        i.move()
