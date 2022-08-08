import random
import turtle as turtle_module

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
cols_list = [(252, 251, 239), (242, 253, 247), (253, 246, 252), (238, 244, 252),
             (232, 246, 85), (34, 189, 82), (91, 245, 184), (21, 16, 82), (211, 154, 101), (50, 17, 174),
             (88, 9, 46), (64, 36, 25), (227, 115, 196), (78, 216, 103), (121, 166, 220), (155, 86, 37), (39, 93, 171),
             (159, 11, 104), (230, 49, 151), (18, 97, 37), (126, 167, 18), (181, 178, 238), (93, 99, 228),
             (30, 139, 52), (172, 49, 133), (82, 241, 247), (236, 162, 217), (18, 61, 23), (40, 24, 249), (236, 51, 39)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(cols_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
