# USA States game
import turtle
import pandas

IMAGE = "blank_states_img.gif"

screen = turtle.Screen()
screen.addshape(IMAGE)
screen.title("U.S States Game")

turtle.shape(IMAGE)

user_score = 0
user_answers = []

states = pandas.read_csv("50_states.csv")
states_list = states["state"].to_list()

while user_score < 50:
    user_prompt = screen.textinput(f"Guess the state {user_score}/50", "Enter a new state name or \"Exit\" to exit: ")
    user_prompt = user_prompt.title()

    if user_prompt == "Exit":
        states_to_learn = [state for state in states_list if state not in user_answers]

        states_to_learn_csv = pandas.DataFrame(states_to_learn)
        states_to_learn_csv.to_csv("States To Learn.csv")
        break

    if user_prompt in states_list and (user_prompt not in user_answers):
        tur = turtle.Turtle()
        tur.hideturtle()
        tur.penup()
        state_data = states[states['state'] == user_prompt]
        tur.goto(int(state_data.x), int(state_data.y))
        tur.write(state_data.state.item(), align="center")
        user_score += 1
        user_answers.append(user_prompt)
