import turtle
import pandas

IMAGE = "blank_states_img.gif"

screen = turtle.Screen()
screen.addshape(IMAGE)
screen.title("U.S States Game")

turtle.shape(IMAGE)

finish = False
user_score = 0
user_answers = []
while not finish:
    user_prompt = screen.textinput(f"Guess the state {user_score}/50", "Enter another state name: ")
    states = pandas.read_csv("50_states.csv")

    states_list = states["state"].to_list()



    if user_prompt.title() in states_list and (user_prompt.title() not in user_answers):
        tur = turtle.Turtle()
        tur.hideturtle()
        tur.penup()
        state_data = states[states['state'] == user_prompt]
        tur.goto(int(state_data.x), int(state_data.y))
        tur.write(state_data.state.item(), align="center")
        user_score += 1
        user_answers.append(user_prompt)
    elif user_score == 50:
        finish = True

turtle.mainloop()
