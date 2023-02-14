# heart-with-turtl
from math import sin, pi
import turtle
t = turtle.Turtle()
wn = turtle.Screen()
t.shape("turtle")
wn.bgcolor("black")
t.speed(10000000000000000)


colors = ["thistle1","hot pink", "light pink", "deep pink","palevioletred1"] #use turtle's colour list

def color(iteration):
    t.pencolor(colors[iteration % len(colors)])
    
def at(x, y):
    t.penup()
    t.home()
    t.forward(x)
    t.left(90) #angle of shape
    t.forward(y)
    t.pendown()

def heart(size, shape):
    t.pensize(5)
    radius = size * sin(shape * pi / 180) / (1 + sin((90 - shape) * pi / 180))
    t.right(shape)
    t.forward(size)
    t.circle(radius, 180 + shape)
    t.right(180)
    t.circle(radius, 180 + shape)
    t.forward(size)
    t.left(180 - shape)

def hearts():
    turtle.delay(0)
    for iteration in range(1, 33): #loop
        color(iteration)
        at(0, iteration * -5)
        heart(iteration * 10, 45)
        
hearts()
