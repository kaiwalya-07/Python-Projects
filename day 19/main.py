from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def mov_for():
    tim.forward(10)


def mov_back():
    tim.backward(10)


def turn_l():
    new_h = tim.heading() + 10
    tim.setheading(new_h)


def turn_r():
    new_h = tim.heading() - 10
    tim.setheading(new_h)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(mov_for, "w")
screen.onkey(mov_back, "s")
screen.onkey(turn_l, "a")
screen.onkey(turn_r, "d")
screen.onkey(clear, "c")
screen.exitonclick()
