from turtle import Turtle, Screen

tiny = Turtle()
tiny.shape("turtle")
tiny.color("SteelBlue3")

stop = True

def draw(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        tiny.forward(100)
        tiny.right(angle)


while stop:
    dont_stop = input("deseja criar uma figura? ").lower()
    if dont_stop == "yes":
        num_sides = int(input("Digite a quantidade de lados: "))
        draw(num_sides)
    elif dont_stop == "no":
        stop = False



my_screen = Screen()
my_screen.exitonclick()
