import turtle

tur = turtle.Turtle()


def forward():
    tur.forward(20)


def backward():
    tur.backward(20)


def left():
    tur.left(10)


def right():
    tur.right(-10)


def clear():
    tur.clear()
    tur.penup()
    tur.home()
    tur.pendown()


screen = turtle.Screen()
screen.listen()
screen.onkey(forward, "w")
screen.onkey(backward, "s")
screen.onkey(left, "a")
screen.onkey(right, "d")
screen.onkey(clear, "c")
screen.exitonclick()
