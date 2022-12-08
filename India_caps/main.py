# import pandas
# import turtle
#
# idx = 0
#
# data_dict = {"state": [], "capitals": [], "x": [], "y": []}
#
#
# def get_pos(x, y):
#     global idx
#
#     coordinates.append((x, y))
#     print((x, y))
#     data_dict["state"].append(states[idx])
#     data_dict["capitals"].append(capitals[idx])
#     data_dict["x"].append(x)
#     data_dict["y"].append(y)
#
#     data=pandas.DataFrame(data_dict)
#     data.to_csv("stateCor.csv")
#
#     idx += 1
#     print_state()
#
#
# def print_state():
#     print(states[idx])
#
#
# screen = turtle.Screen()
# screen.title("India State Game")
# screen.setup(530, 636)
#
# image = "p1.gif"
# screen.addshape(image)
# turtle.shape(image)
#
# data = pandas.read_csv("statesAndCaps.csv")
#
# states = data.state.to_list()
# capitals = data.capital.to_list()
# coordinates = []
#
# turtle.listen()
# turtle.onscreenclick(get_pos, 1)
# print_state()
#
# turtle.mainloop()

import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. Games")
screen.setup(560, 636)

image = "Picture2.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("stateCor.csv")

write_turtle = turtle.Turtle()
write_turtle.hideturtle()
write_turtle.penup()
write_turtle.color("white")

states = data.state.to_list()

print(states)

score = 0

while score <= 35:
    usr_ans = str(screen.textinput(f"Score is {score}/35", "Guess the name of a state/union territory")).title()
    if usr_ans == "Exit":
        break
    if usr_ans in states:
        score += 1
        x_cor = int(data[data.state == usr_ans].x)
        y_cor = int(data[data.state == usr_ans].y)
        # print(x_cor,y_cor)
        write_turtle.goto(x_cor, y_cor)
        write_turtle.write(usr_ans, move=False, align="left", font=("Arial", 10, "bold"))
        states.remove(usr_ans)

states = {
    "states": states
}

states = pandas.DataFrame(states)
states.to_csv("states_to_learn.csv")
