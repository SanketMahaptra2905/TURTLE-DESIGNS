from turtle import *
from colorsys import *
tracer(2)
bgcolor("black")
pensize(2)
h = 0
def draw(x, y):
    circle(5+y, 69)
    left(x)
    circle(3+2*y, 60)
goto(0, 10)
for i in range(150):
    c = hsv_to_rgb(h, 1, 1)
    h += 0.007
    color(c)
    up()
    draw(90, i)
    draw(180, i)
    down()
    draw(1/2, i-i)
    draw(180, i/2)
    draw(120, i-i)
    hideturtle()
done()
