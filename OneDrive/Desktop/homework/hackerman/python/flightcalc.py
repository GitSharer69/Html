import time
import turtle
import math
t=turtle.pen()
def arclength():
    # take input diameter and angle .
    d= float(input("please Enter the diameter of circle: "))
    Angle = float(input("please Enter the angle value: "))
    # checking for the angle validation 
    if Angle >= 360:
        print("Invalid angle entered ")
        return
    #calculate  arc length.
    Arc_length = (math.pi*d) * (Angle/360)
    print("the arc Length will be : %.2f" %Arc_length)
arclength()



    