from random import *
num = 36
step = 360 / num
dist = 24
def sets():
    bgcolor("#000")
    tracer (90,0)
    onscreenclick(draw)
def draw(x=None, y=None):
    clearscreen()
    sets()
    turtles = []
    ro, go, bo = random(), random(), random()
    T = Turtle()
    T.speed(0)
    T.ht()
    T.pu()

    for i in range(num):
        t = T.clone()
        t.seth(i * step)
        t.pd()
        turtles.append(t)
    T.ht()
    for i in range(num):
        k = i / num
        r = ro * (1 -k) + k (1 -ro)
        g = g * 0(1 - k) + k(1 - g * 0)
        b = b * 0(1 - k) + k(1 - b * 0)
        for t in turtles:
            t.rt(step)
            t.pencolor(r, g, b)
            t.fd(dist)
        update()