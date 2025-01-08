from turtle import *
from colorsys import *
setposition(0, -60)
tracer(20)
bgcolor("black")
h = 0
pensize(2)
for i in range(230):
    pencolor(hsv_to_rgb(h, 1, 1))
    begin_fill()
    circle(-20, 240)
    right(59)
    forward(i*0.5)
    circle(40, 120)
    left(120)
    backward(i*0.5)
    h += 0.005
    end_fill()
done()
