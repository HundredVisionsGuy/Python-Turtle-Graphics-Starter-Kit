# SmileyFace.py
# by Hundred Visions Guy
# A template for future turtle graphics

# Import Statements
from turtle import *
import time

# Set the title Screen
title("Program Title Goes Here")

# Create 1 pen
p1 = Pen()  # pen 1

# Set the colors
p1.color('#2c95b5', 'gray')
p1.pensize(5)
bgcolor('#6699cc')

# Draw your picture below...
# Draw the face
p1.up()
p1.goto(0, -150)
p1.down()
p1.color("black", "yellow")
p1.begin_fill()
p1.circle(125)
p1.end_fill()

# Draw left eye
p1.up()
p1.goto(-50, 25)
p1.down()
p1.color("black", "white")
p1.begin_fill()
p1.circle(12)

# The pupil
p1.end_fill()
p1.color("black", "black")
p1.begin_fill()
p1.circle(4)
p1.end_fill()

# Draw right eye

# Draw the mouth

# Pause to show the picture, then quit
time.sleep(10)
bye()
