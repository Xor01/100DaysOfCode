# Turtle Road Cross Game
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Cross Turtle")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
score_board = Scoreboard()

screen.onkeypress(player.up, "Up")

game_is_on = True
while game_is_on:
    score_board.print_score()
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # Detect winning to reset coordinate and increase speed
    if player.is_at_finish_line():
        player.return_to_origin()
        score_board.update_level()
        car_manager.level_up()

    # Detect collision  with cars
    for car in car_manager.cars_list:
        if car.distance(player) < 20:
            score_board.game_over()
            game_is_on = False

screen.exitonclick()
