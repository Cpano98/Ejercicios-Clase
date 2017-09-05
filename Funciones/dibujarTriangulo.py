#encoding:UTF-8
#   Autor: Carlos Pano Hernández
#   Prueba TopDown para diseñar soluciones

import turtle
from math import *


def leerAltura():
    altura=int(input("Altura de tu triángulo:"))
    return altura


def dibujarTriangulo(lado):
    turtle.forward(lado)
    turtle.left(120)
    turtle.forward(lado)
    turtle.left(120)
    turtle.forward(lado)
    turtle.left(120)



def dibujar(altura):
    lado=calcularLado(altura)
    dibujarTriangulo(lado)
    return lado

def calcularLado(altura):
    lado=altura/sin(radians(60))
    return lado

def main():
    altura=leerAltura()
    dibujar(altura)
    turtle.exitonclick()

main()
