import turtle
import pandas
import random

screen = turtle.Screen()
screen.title("Indian States Game")
image = "indian_states.gif"
t = turtle.Turtle()
screen.addshape(image)
screen.colormode(255)
t.shape(image)
random = random.Random()
data = pandas.read_csv("indian_states.csv")
total_states = len(data)
all_states = data["state"]
correct_guess = 0
answer_state = "Goa"

# to get x, y coordinates
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()


while correct_guess < total_states:
    answer_state = screen.textinput(title=f"{correct_guess}/{total_states} Guess the State", prompt="What's another "
                                                                                                    "state's "
                                                                                                    "name?").lower()
    if answer_state == "exit":
        break

    if f"{answer_state}" in all_states.values:
        state = data[data.state == f"{answer_state}"]
        correct_guess += 1
        pen = turtle.Turtle()
        pen.penup()
        pen.hideturtle()
        pen.color(random.randint(100, 150), random.randint(100, 150), random.randint(100, 150))

        # calling int on a single element Series is deprecated and will raise a TypeError in the future. Use int(
        # ser.iloc[0]) instead pen.goto(int(state.x), int(state.y)
        pen.goto(int(state.iloc[0, 1]), int(state.iloc[0, 2]))
        pen.write(f"{answer_state.capitalize()}", align="center", font=('Courier', 14, 'bold'))
        all_states = all_states.drop(all_states[all_states.values == answer_state].index)
df = pandas.DataFrame(all_states)
df.to_csv("remaining_states.csv")

