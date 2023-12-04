from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet ", prompt="Which turtle will win the race? enter a color: ")
colors = ["orange", "red", "blue", "green", "black", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtle = []
start_race = False


for i in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y=y_positions[i])
    all_turtle.append(new_turtle)

if user_bet:
    start_race = True

while start_race:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            start_race = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! the {winning_color} turtle is the winner")
            else:
                print(f"You lose! The {winning_color} turtle is the winner")

        distance = random.randint(0, 10)
        turtle.forward(distance)


screen.exitonclick()
