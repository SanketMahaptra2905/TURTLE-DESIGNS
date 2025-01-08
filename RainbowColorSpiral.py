from turtle import *
from colorsys import *
speed(0)
bgcolor("black")
h = 0
shape("turtle")
size = 5
for i in range(137):
    color(hsv_to_rgb(h, 1, 1))
    h += 0.008
    stamp()
    size += 1
    forward(size)
    right(30)
done()
