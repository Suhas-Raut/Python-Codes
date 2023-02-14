import turtle as t
import random

bob = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    new_color = (r, g, b)
    return new_color


bob.pensize(3)
bob.speed("fastest")

def draw_spirograph(size_of_the_gaps):
  for _ in range(int(360 / size_of_the_gaps)):
      bob.color(random_color())
      bob.circle(150)
      bob.setheading(bob.heading() + size_of_the_gaps)

draw_spirograph(5)

screen = t.Screen()
screen.bgcolor("Black")
screen.exitonclick()
