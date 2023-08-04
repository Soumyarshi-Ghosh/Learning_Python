# Draw a 'turtle star'

from turtle import *

pen(shown=False) # Hide the pen icon
speed(0) # 0 is fastest. Then it goes from 1 (slowest) to 10 (fast)

angle = 15 # A number that is a factor of 360, although non-factors give interesting results too
repeats = 360//angle

# Mix of colours (in RGB)
red = 240
green = 0
blue = 120

fillcolor("yellow") # A hexadecimal value as a string, or color as a word
begin_fill() # Comment this out if you don't want any fill

for i in range(repeats):
    red += 15 # experiment with value
    if red > 255:
        red -= 256
    green += 15 # experiment with value
    if green > 255:
        green -= 256
    blue += 20 # experiment with value
    if blue > 255:
        blue -= 256
    redhex = hex(red)
    greenhex = hex(green)
    bluehex = hex(blue)
    colorstring = '#' + redhex[2:].zfill(2) + greenhex[2:].zfill(2) + bluehex[2:].zfill(2)
    pencolor(colorstring)
    forward(300) # size of shape
    left(180 - angle)
    
end_fill()
done()
