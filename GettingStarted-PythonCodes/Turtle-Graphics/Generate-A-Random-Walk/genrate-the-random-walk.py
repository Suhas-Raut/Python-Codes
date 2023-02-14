from turtle import Turtle, Screen
import random

bob = Turtle()

########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]


bob.pensize(15)
bob.speed("fastest")

for _ in range(200):
    bob.color(random.choice(colours))
    bob.forward(30)
    bob.setheading(random.choice(directions))

screen = Screen()
screen.bgcolor("Black")
screen.exitonclick()
