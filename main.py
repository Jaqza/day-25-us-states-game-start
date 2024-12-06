# obraz 725 * 491
from turtle import Screen , Turtle
import pandas as pd
from scoreboard import Scoreboard
import time
FONT = ("Courier", 10, "normal")
states = pd.read_csv("50_states.csv")
screen = Screen()
screen.setup(725, 500)
screen.bgpic("./blank_states_img.gif")
screen.title("Guess USA States my version")
screen.tracer(0)
tim = Turtle()
tim.hideturtle()
tim.penup()
tim.color("blue")
scoreboard = Scoreboard()
scoreboard.max_points = len(states.state)
scoreboard.update()
# scoreboard.points = 49 a little cheat to test end of program
checking_list = []
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(1.5)
    guess = screen.textinput("How many states do you know?", "Guess").title()
    if scoreboard.points == len(states.state):
        tim.goto(-280, 180)
        tim.write("Congratulations you have won",font=("Courier", 24, "normal"))
        screen.update()
        time.sleep(5)
        is_game_on = False
    for state in states.state:
        if guess == state:
            guessed_state = state = states[states.state == guess]
            new_x = int(guessed_state.x.iloc[0])
            new_y = int(guessed_state.y.iloc[0])
            tim.goto(new_x,new_y)
            tim.write(guess, font=FONT)
            if guess not in checking_list:
                checking_list.append(guess)
                scoreboard.add_point()
    else:
        pass

# screen.exitonclick()
