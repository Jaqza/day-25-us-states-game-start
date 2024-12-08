import turtle as t
import pandas as pd

screen = t.Screen()
screen.title("U.S. States Guess Game")
screen.setup(800, 600)
image = "blank_states_img.gif"
screen.addshape(image)
t.shape(image)
points = 49
writer = t.Turtle()
writer.hideturtle()
writer.penup()
data = pd.read_csv("50_states.csv")
guessed_states = []
while points < 50:
    answer = screen.textinput(f"{points}/{len(data.state)} correct states","Gues another state").title()
    for state in data.state:
        if state == answer:
            if answer not in guessed_states:
                new_x = int(data[data.state == answer].x.iloc[0])
                new_y = int(data[data.state == answer].y.iloc[0])
                writer.goto(new_x,new_y)
                writer.write(answer)
                guessed_states.append(answer)
                points += 1
screen.exitonclick()