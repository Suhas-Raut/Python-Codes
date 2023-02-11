# By Penup And Pendown drawing states
import turtle as new

bob = new.Turtle()
bob.pensize(3)
for _ in range(18):
    bob.forward(10)
    bob.penup()
    bob.forward(10)
    bob.pendown()

screen = new.Screen()
screen.exitonclick()
