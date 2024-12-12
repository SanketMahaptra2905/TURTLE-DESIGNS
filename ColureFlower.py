# @eng.yem1
from turtle import *
from colorsys import *
bgcolor("black")
speed(0)
h = 0.3
pensize(2)
for i in range(105):
    h += 0.0090
    color(hsv_to_rgb(h, 1, 1))
    rt(70)
    fd(i)
    circle(i*2, -10)
    lt(100)
    up()
    fd(i)
    down()
    circle(i*2, -90)
    rt(230)
    hideturtle()
done()
