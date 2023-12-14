import turtle

import pandas
import pandas as pd
import time

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
# screen.tracer(0)

data = pd.read_csv("50_states.csv")
score = 0
states_list = list(data["state"])
no_of_states = len(states_list)

guessed_state = []

while len(guessed_state) < 50:
    # time.sleep(0.1)
    # screen.update()

    answer_state = screen.textinput(title=f"{score}/{no_of_states} States Correct", prompt="What's the state "
                                                                                           "you want to guess").title()
    if answer_state == "Exit":
        break


    if answer_state in states_list:
        if answer_state not in guessed_state: # makes sure there is no repeatition of state.
            score += 1
            guessed_state.append(answer_state)
            t = turtle.Turtle()
            t.penup()
            t.hideturtle()
            state = data[data["state"] == answer_state]
            y = int(state.y)
            x = int(state.x)
            t.goto(x, y)
            t.write(f"{answer_state}",align="left", font=("courier", 10, "normal"))
        else:
            pad = turtle.Turtle()
            pad.penup()
            pad.hideturtle()
            pad.goto(-200,250)
            pad.write(f"you have already written {answer_state}",align="left", font=("courier", 10, "normal"))
            time.sleep(3)
            pad.clear()

            continue


    else:
        p = turtle.Turtle()
        p.penup()
        p.hideturtle()
        p.goto(-200, 250)
        p.write(f" {answer_state} is not a state i know", align="left", font=("courier", 10, "normal"))
        time.sleep(3)
        p.clear()
        continue

# to check for the missing states
# missing_states = []
# for item in states_list:
#     if item not in guessed_state:
#
#         missing_states.append(item)
""" using list comprehension, lets do thisi same thing up"""
missing_states = [state for state in states_list if state not in guessed_state]
new_data = pd.DataFrame(missing_states)
new_data.to_csv("Things that i need to learn")


print(f"the missing states are : {missing_states}")
        # df = pandas.DataFrame(to_learn)
        # df.to_csv("what_i_need_learn.txt")





