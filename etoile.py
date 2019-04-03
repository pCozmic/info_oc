import turtle
from math import sin, cos

a = turtle.Turtle()
turtle.delay(0)
a.speed(0)
a.ht()
a.penup()
turtle.colormode(255)
def setc(i):
    col = [int(127-127*sin(i/10)),int( 127 - 127*cos(i/5)), int(127-127*sin(i/7))]
    a.color(col)
def etoile(n, taille):
    for i in range(n):
        a.forward(taille)
        a.left(180-180/n)
col = 0
def spirale(alpha):
    a.forward(20)
    a.penup()
    angle = 1
    
    a.setheading(alpha)
    a.forward(30)
    for i in range(20):
        a.left(angle)
        angle += 0.7
        a.forward(i*2)
        a.pendown()
        etoile(2*int(i/5)+3, i*2)
        a.penup()
        setc(col + i*5)
for i in range(6):
    a.home()
    a.left(i*60)
    a.forward(70)
    spirale(90+i*60)
    col += 100
        
