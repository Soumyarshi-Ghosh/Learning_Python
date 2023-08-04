# Draw multiple shapes with nested for loops

from turtle import *
import random

pen(shown=False) # Hide the pen icon
speed(0) # 0 is fastest. Then it goes from 1 (slowest) to 10 (fast)

# Starting coordinates
x = -500
y = 300

# Initial mix of colours (in RGB)
red = 0
green = 0
blue = 200
    
for i in range(3):
    penup() # Don't draw a line when shifting position
    setpos(x, y)
    pendown() # Get ready to draw!
    angle = 15
    repeats = 360//angle
    
    green += 50
    blue -= 50

    for i in range(repeats):
        red += 5 # experiment with value
        if red > 255:
            red -= 256
        '''green += 15 # experiment with value
        if green > 255:
            green -= 256
        blue += 20 # experiment with value
        if blue > 255:
            blue -= 256'''
        redhex = hex(red)
        greenhex = hex(green)
        bluehex = hex(blue)
        colorstring = '#' + redhex[2:].zfill(2) + greenhex[2:].zfill(2) + bluehex[2:].zfill(2)
        pencolor(colorstring)
        forward(300) # size of shape
        left(180 - angle)
        # Add additional 'inner' shapes
        for i in range(12):
            forward(200)
            left(150)

    # Change starting coordinates
    x += 300
    y -= 200
    
done()
