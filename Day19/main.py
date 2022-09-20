import turtle
from random import randint


def race(turtle_obj):
    while True:
        for turtleX in turtle_obj:
            if turtleX.position() < (220, 0):
                turtleX.forward(randint(1, 5))
            else:
                return turtleX.color()


screen = turtle.Screen()
screen.setup(500, 500)

colors = ["blue", "yellow", "green", "purple", "red"]
turtles_name = []
c = -50
for turtle_index in range(0, 5):
    tur = turtle.Turtle(shape="turtle")
    tur.color(colors[turtle_index])
    tur.penup()
    tur.goto(-240, c)
    c += 40
    turtles_name.append(tur)
user_guess = screen.textinput("Your bid", "Enter a color for the winning turtle: ").lower()

winner_color = race(turtles_name)[0]

if user_guess == winner_color:
    print(f"You've won the {winner_color} turtle is the winner.")
else:
    print(f"You've lost the {winner_color} turtle is the winner.")
screen.exitonclick()

