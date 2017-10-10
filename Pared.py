# encoding: UTF-8
# Autor: Carlos Pano Hernández
# Prueba ciclo while

import turtle
from random import randint

def caminarTortuga():
    tortuga=turtle.Turtle() #Llamar tortuga
    willy=turtle.Turtle()
    willy.goto(0,50)
    while tortuga.xcor()<300 and willy.xcor()<300:
        tortuga.forward(randint(0,3))
        willy.forward(randint(0,2))

    turtle.exitonclick()

def main():
    caminarTortuga()

main()