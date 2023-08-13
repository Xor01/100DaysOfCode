# Snake Game OOP
from turtle import Screen
from snake import Snake
from food import Food
from scoreBoard import ScoreBoard
from time import sleep

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()
screen.listen()

screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.right, "Right")
screen.onkeypress(snake.left, "Left")

game_on = True

while game_on:
    screen.update()
    sleep(0.1)

    # Detect collision with the food
    snake.move_snake()
    if snake.snakes_list[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # Detect collision with the wall
    if abs(snake.snakes_list[0].xcor()) > 280 or abs(snake.snakes_list[0].ycor()) > 280:
        score.reset_score()
        snake.reset_snake()

    # Detect collision with the tail
    for segment in snake.snakes_list[1:]:
        if snake.snakes_list[0].distance(segment) < 10:
            score.reset_score()
            snake.reset_snake()

screen.exitonclick()
