from turtle import *
length=100
rotation=5
speed(1000)
for i in range(20):
    for j in range(4):
        forward(length)
        left(90)
    length-=rotation
    left(3*(1-(rotation/100)))#3
    penup()
    forward(rotation)
    pendown()
    print(rotation)
    rotation*=1-(i/100)
mainloop()