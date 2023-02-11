[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![Suhas Raut](https://img.shields.io/badge/Made%20By-Suhas%20Raut-%2300C0A3?style=for-the-badge&logo=github&logoColor=00C0A3)](https://github.com/Suhas-Raut)

# Turtle Graphics 

## Square 🔳

Code : 
```
from turtle import Turtle, Screen

bob = Turtle()
bob.shape("arrow")
bob.pencolor("Red")
bob.pensize(5)
for i in range(4):
    bob.forward(100)
    bob.right(90)


screen = Screen()
screen.exitonclick()

```
Output :
<img align="center" alt="coding" width="400" src="https://github.com/Suhas-Raut/Python-Codes/blob/master/GettingStarted-PythonCodes/Turtle-Graphics/Output1.png">
