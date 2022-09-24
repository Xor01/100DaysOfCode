from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.return_to_origin()

    def up(self):
        if self.ycor() < FINISH_LINE_Y:
            self.forward(MOVE_DISTANCE)

    def return_to_origin(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() == FINISH_LINE_Y:

            return True
        else:
            return False
