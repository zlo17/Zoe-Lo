# Zoe-Lo
from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.

### Write your code below:
var = input("how many sides?")
var = int(var)
t.fillcolor("blue violet")
t.begin_fill()
for sides in range (var):
    t.forward(200)
    t.right(360/(var))
for sides in range (var):
    t.forward(100)
    t.right(360/(var))
for sides in range (var):
        t.forward(50)
        t.right(360/(var))
for sides in range (var):
            t.forward(25)
            t.right(360/(var))
t.end_fill()

# Close window on click.
exitonclick()
