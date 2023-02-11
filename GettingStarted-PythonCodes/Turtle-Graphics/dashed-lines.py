# By Using Black and White Color
from turtle import Turtle, Screen

 bob = Turtle()
 bob.pensize(3)
 for _ in range(18):
     bob.pencolor("Black")
     bob.forward(10)
     bob.pencolor("White")
     bob.forward(10)

 screen = Screen()
 screen.exitonclick()
