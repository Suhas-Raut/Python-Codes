"""
To Extract The Colors From The Image
"""
# import colorgram
#
# rgb_colors = []
#
# colors = colorgram.extract("painting.jpg", 25)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     final_color = (r, g, b)
#     rgb_colors.append(final_color)
#
# print(rgb_colors)

import turtle as new
import random

bob = new.Turtle()
new.colormode(255)
colors_list = [(199, 174, 117), (215, 225, 218), (125, 37, 24), (163, 103, 56), (184, 158, 53), (6, 56, 82), (108, 68, 85), (46, 34, 32), (113, 160, 175), (23, 121, 170), (75, 37, 47), (66, 153, 135), (9, 66, 46), (87, 139, 59), (130, 39, 42), (182, 96, 80), (204, 202, 144), (144, 175, 158), (171, 151, 156), (178, 201, 185), (221, 181, 167), (31, 78, 61)]
total_dots = 100


bob.speed("fastest")
bob.hideturtle()
bob.setheading(225)
bob.penup()
bob.forward(300)
bob.setheading(0)

for color_count in range(1, total_dots + 1):
    bob.dot(20, random.choice(colors_list))
    bob.forward(50)

    """
    For Setting The Pointer To The Beginning 
    """
    if color_count % 10 == 0:
        bob.setheading(90)
        bob.forward(50)
        bob.setheading(180)
        bob.forward(500)
        bob.setheading(0)

screen = new.Screen()
screen.bgcolor("Black")
screen.exitonclick()


