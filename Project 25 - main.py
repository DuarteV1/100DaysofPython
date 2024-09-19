import turtle
import pandas

# Screen details - Change the Image
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Check if the guess is among the 50 states
# Create a list with only the name of the states
us_states_data = pandas.read_csv("50_states.csv")
states_name_list = us_states_data["state"].to_list()
x_states_list = us_states_data["x"].to_list()
y_states_list = us_states_data["y"].to_list()
print(y_states_list)
print(x_states_list)
guessed_list = []
count = 0

while count < 50:
    answer_state = screen.textinput(title=f"{count}/50 Guess the State", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in states_name_list:
            if state not in guessed_list:
                missing_states.append(state)

        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_to_learn.csv")
        break

    if answer_state in states_name_list:
        # Write correct guesses onto the map
        # state_row = us_states_data[us_states_data["state"] == answer_state]
        # print(state_row)
        answer_index = states_name_list.index(answer_state)
        x_cor = x_states_list[answer_index]
        y_cor = y_states_list[answer_index]
        # print(f"{x_cor} \n{y_cor}")

        if answer_state not in guessed_list:
            guessed_list.append(answer_state)
        count = len(guessed_list)

        # Now I need a turtle Printer
        t = turtle.Turtle()
        t.shape("circle")
        t.shapesize(0.5, 0.5)
        t.penup()
        t.goto(x_cor, y_cor)
        t.pendown()
        t.write(f"{answer_state}", align="center", font=('Courier', 15, 'normal'))
