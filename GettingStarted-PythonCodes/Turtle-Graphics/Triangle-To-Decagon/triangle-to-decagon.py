from turtle import Turtle, Screen
from random import choice

bob = Turtle()
bob.pensize(3)
color = ["Gold", "Maroon", "Cyan", "Magenta", "Blue", "Green", "Pink", "Violet", "Red", "Orange", "Yellow", "Brown" ]
sides = 3
angle = 360
for i in range(8):
    bob.pencolor(choice(color))
    for _ in range(sides):
        bob.forward(110)
        bob.right(angle/sides)
    sides += 1


screen = Screen()
screen.bgcolor("Black")
screen.exitonclick()
