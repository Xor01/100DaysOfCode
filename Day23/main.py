import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()


player = Player()
car = CarManager()
score_board = Scoreboard()

screen.onkeypress(player.up, "Up")


game_is_on = True
while game_is_on:
    score_board.score()
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_cars()
