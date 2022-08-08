from turtle import Turtle, Screen
import random

is_r = False
screen = Screen()
screen.setup(width=500, height=500)
u_bet = screen.textinput(title="Place your bet", prompt="Which turtle will win? Enter the color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-70, -40, -10, 20, 50, 80]
all_t = []

print(u_bet)

for turtle_ind in range(0, 6):
    new_t = Turtle(shape="turtle")
    new_t.color(colors[turtle_ind])
    new_t.penup()
    new_t.goto(x=-230, y=y_pos[turtle_ind])
    all_t.append(new_t)

if u_bet:
    is_r = True

while is_r:
    for turtle in all_t:
        if turtle.xcor() > 230:
            is_r = False
            winning_col = turtle.pencolor()
            if winning_col == u_bet:
                print(f"You have won! The {winning_col} turtle is winner")
            else:
                print(f"You have lost! The {winning_col} turtle is winner")
        r_d = random.randint(0, 10)
        turtle.forward(r_d)
screen.exitonclick()
