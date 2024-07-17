#Dalyn Stiles
#July 03 2024
#P4Lab1
#turtles
import turtle
#Make a pop up window
wn=turtle.Screen ()
wn.bgcolor("lightgreen")
wn.title("Dalyn and my turtle")
#make a square
dalyn=turtle.Turtle()
dalyn.shape('turtle')
dalyn.color('green')
dalyn.pensize(6)
for i in [0,1,2,3]:
    dalyn.forward(50)
    dalyn.left(90)
#make a triangle
turtlepet=turtle.Turtle()
turtlepet.shape('turtle')
turtlepet.color('blue')
turtlepet.pensize(10)
for i in [0,1,2,3]:
    turtlepet.forward(100)
    turtlepet.left(120)

turtle.done()
