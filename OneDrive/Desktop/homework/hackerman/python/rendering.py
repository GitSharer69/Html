from operator import truediv
import turtle
t=turtle.Pen()
#squere
# t.forward(50)
# t.right(90)
# t.forward(50)
# t.right(90)
# t.forward(50)
# t.right(90)
#triangle
# t.forward(50)
# t.forward(50)
# t.right(120)
# t.forward(50)
# t.right(120)
# t.forward(50)

for i in range(0,2):
    for i in range(0,3):
        t.forward(50)
        t.right(120)
        t.forward(50)
        t.right(120)
        t.forward(50)
        t.left(60)
        t.forward(50)
        t.right(120)
        t.forward(50)
        t.right(120)
        t.forward(50)
        t.right(60)
    t.left(180)
    t.forward(50)


# t.forward(50)
# t.left(120)
# t.forward(50)
# t.left(120)
# t.forward(50)
# t.left(120)
# t.forward(25)
# for i in range(0,180):
#     t.forward(1)
#     t.right(2)

turtle.done()






