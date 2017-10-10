#encoding: UTF-8
#Autor: Carlos Pano Hernández
#Prueba ciclo while

import turtle


def main():

    radio=int(input("Radio:"))
    while radio>0:
        x=int(input("x:"))
        y = int(input("y:"))
        turtle.goto(x,y)
        turtle.circle(radio)
        radio=int(input("Radio:"))

    turtle.exitonclick()

main()