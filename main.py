import turtle as t
import pandas as pd

screen = t.Screen()
screen.title("U.S. States Guess Game")
screen.setup(800, 600)
image = "blank_states_img.gif"
screen.addshape(image)
t.shape(image)
writer = t.Turtle()
writer.hideturtle()
writer.penup()
data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
while len(guessed_states) < 50:
    answer = screen.textinput(f"{len(guessed_states)}/50 correct states","Gues another state").title()
    if answer == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        print(missing_states)
        break
    if answer in all_states:
        states_data = data[data.state == answer]
        writer.goto(states_data.x.item(), states_data.y.item()) # I have used int(states_data.x) it worked too
        writer.write(answer)
        guessed_states.append(answer)

