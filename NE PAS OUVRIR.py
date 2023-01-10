from turtle import *

pensize(3)
fillcolor("purple")
pencolor("black")

##begin_fill()
for i in range (6):
    forward(100)
    left(60)

forward(200)
##begin_fill()
for i in range (6):
    forward(100)
    left(60)

right(90)
forward(300)
right(90)
left(60)
forward(100)
right(120)
forward(100)
right(30)
forward(300)
right(90)

##end_fill()
exitonclick()