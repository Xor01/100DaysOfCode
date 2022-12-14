from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.snakes_list = []
        self.creat_snake()

    def creat_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segments(position)

    def add_segments(self, position):
        new_snake = Turtle(shape="square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(position)
        self.snakes_list.append(new_snake)

    def extend(self):
        self.add_segments(self.snakes_list[-1].position())

    def reset_snake(self):
        for seg in self.snakes_list:
            seg.goto(1000, 10)
        self.snakes_list.clear()
        self.creat_snake()


    def move_snake(self):
        for seg in range(len(self.snakes_list) - 1, 0, -1):
            new_x = self.snakes_list[seg - 1].xcor()
            new_y = self.snakes_list[seg - 1].ycor()
            self.snakes_list[seg].goto(new_x, new_y)
        self.snakes_list[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.snakes_list[0].heading() != DOWN:
            self.snakes_list[0].setheading(UP)

    def down(self):
        if self.snakes_list[0].heading() != UP:
            self.snakes_list[0].setheading(DOWN)

    def right(self):
        if self.snakes_list[0].heading() != LEFT:
            self.snakes_list[0].setheading(RIGHT)

    def left(self):
        if self.snakes_list[0].heading() != RIGHT:
            self.snakes_list[0].setheading(LEFT)
