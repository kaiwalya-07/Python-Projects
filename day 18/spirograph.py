import turtle as t
import random
from turtle import Screen

tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


tim.speed("fastest")


def draw_spi(size_gap):
    for _ in range(int(360 / size_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_gap)

draw_spi(5)
########### Challenge 5 - Spirograph ########
screen = Screen()
screen.exitonclick()
