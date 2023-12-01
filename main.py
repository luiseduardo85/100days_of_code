import random
import turtle
from turtle import Turtle, Screen
import random

rgb_colors = [(229, 228, 227), (226, 224, 225), (198, 175, 119), (125, 36, 23), (187, 157, 50), (170, 104, 56), (5, 56, 83), (201, 216, 205), (109, 67, 85), (39, 35, 34), (223, 224, 227), (84, 141, 61), (20, 122, 175), (111, 161, 176), (75, 38, 48), (8, 67, 47), (65, 154, 134), (132, 41, 43), (184, 98, 81), (183, 180, 181), (210, 200, 108), (178, 201, 186), (150, 180, 170), (90, 143, 158), (28, 81, 59), (193, 190, 192), (17, 78, 98), (215, 184, 172), (190, 190, 195), (78, 72, 31)]
turtle.colormode(255)

tiny = Turtle()

tiny.penup()
tiny.hideturtle()
tiny.shape("turtle")
tiny.color("SkyBlue")

tiny.setheading(225)
tiny.forward(300)
tiny.setheading(0)
dots = 100

for dots in range(1, dots + 1):
    tiny.dot(20, random.choice(rgb_colors))
    tiny.forward(50)

    if dots % 10 == 0:
        tiny.setheading(90)
        tiny.forward(50)
        tiny.setheading(180)
        tiny.forward(500)
        tiny.setheading(0)


screen = Screen()
screen.exitonclick()
