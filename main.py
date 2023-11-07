import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
state = data["state"]
correct_guesses = []
score = 0

while len(correct_guesses) < 51:
    answer_state = screen.textinput(f"{score}/50 States Correct", "What's another state's name? ")
    answer_state_cap = answer_state.capitalize()
    check_state_exist = answer_state_cap == state
    if check_state_exist.value_counts().get(True, 0):
        state_turtle = turtle.Turtle()
        state_turtle.penup()
        state_turtle.hideturtle()
        state_row = data[check_state_exist]
        x_cor = state_row.iloc[0]["x"]
        y_cor = state_row.iloc[0]["y"]
        state_turtle.setposition(x_cor, y_cor)
        state_turtle.write(f"{answer_state_cap}", move=False, align="center", font=("Arial", 8, "normal"))
        score += 1
        correct_guesses.append(answer_state_cap)
    else:
        answer_state = screen.textinput("f{score}/50 States Correct", "What's another state's name? ")
        answer_state_cap = answer_state.capitalize()

turtle.mainloop()
