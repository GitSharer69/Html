
# Python program to draw
# Spiral  Helix Pattern
import turtle
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
turtle.bgcolor('black')
t.pencolor("white")
t.right(90)
t.forward(300)
t.left(90)
t.forward(300)
t.left(90)
t.forward(300)
t.left(90)
t.forward(300)
for i in range(5):
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(300)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(300)
t.right(180)
t.forward(30)
for i in range(5):
    t.left(90)
    t.forward(300)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(300)
    t.left(90)
    t.forward(30)

turtle.done()