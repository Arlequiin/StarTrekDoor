from turtle import *
length=200
from math import pi
rotation=pi*(10/3)
speed(1000)
for i in range(60):
    
    for j in range(4):
        forward(length)
        left(90)
    length-=rotation
    left(pi)#3*(1-(rotation/100))
    penup()
    forward(rotation)
    pendown()
    print(rotation)
    rotation*=(1-(5/100))#(1-(pi/100))
mainloop()