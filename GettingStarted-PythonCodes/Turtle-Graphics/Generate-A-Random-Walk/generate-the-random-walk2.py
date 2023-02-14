import turtle as t
import random

bob = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

directions = [0, 90, 180, 270]
bob.pensize(15)
bob.speed("fastest")

for _ in range(200):
    bob.color(random_color())
    bob.forward(30)
    bob.setheading(random.choice(directions))

screen = t.Screen()
screen.bgcolor("Black")
screen.exitonclick()
