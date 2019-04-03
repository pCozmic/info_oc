import turtle
from datetime import datetime
turtle.delay(0)
c = turtle.Turtle()
s = turtle.Turtle()
m = turtle.Turtle()
h = turtle.Turtle()
turtle.speed(0)
s.color("red")
c.ht()
s.ht()
m.ht()
h.ht()

def cadran():
    c.penup()
    c.home()
    c.setheading(0)
    
    for i in range(60):
        c.penup()
        c.home()
        c.setheading(i*6)
        length = 10
        size = 1
        if i % 5 == 0:
            length = 20
            size = 2
            if i % 3 == 0:
                size = 5
                length = 50
        c.pensize(size)
        c.forward(300 - length)
        c.pendown()
        c.forward(length)
def a_min(minute):
    m.penup()
    m.home()
    m.setheading(90 - 6*minute)
    m.pendown()
    for i in range(5):
        
        m.pensize(5-i)
        m.forward(30)
        
def a_sec(sec):
    s.penup()
    s.home()
    s.setheading(90 - 6*sec)
    s.pendown()
    s.pensize(2)
    s.forward(-40)
    s.forward(240)
    s.pensize(30)
    s.forward(1)
def a_h(hour):
    
    h.penup()
    h.home()
    h.setheading(90 - 30*hour)
    h.pendown()
    for i in range(6):
        
        h.pensize(5-i)
        h.forward(20)
        
        
    
        
last_s = -1
last_m = -1
last_h = -1


cadran()

while 1:
    t_s = datetime.now().second
    if t_s != last_s:
        s.clear()
        last_s = t_s
        a_sec(t_s)
        
        
    t_h = datetime.now().hour
    if t_h != last_h:
        h.clear()
        a_h(t_h)
        last_h = t_h
        
    t_m = datetime.now().minute
    if t_m != last_m:
        dt = 60/t_s if t_s != 0 else 1
        m.clear()
        last_m = t_m
        a_min(t_m)
        
    
    
    
    
    
    


