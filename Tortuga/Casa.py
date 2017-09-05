#encoding:: UTF-8
#Autor: Carlos Pano Hernández - A01066264
#Este programa hará una casita.

import turtle

turtle.shape("turtle")
turtle.color("green")

def dibujarCuadro(longitud):
    turtle.forward(longitud)
    turtle.left(90)
    turtle.forward(longitud)
    turtle.left(90)
    turtle.forward(longitud)
    turtle.left(90)
    turtle.forward(longitud)
    turtle.left(90)

def dibujarRectangulo(ancho,alto):
    turtle.forward(ancho)
    turtle.left(90)
    turtle.forward(alto)
    turtle.left(90)
    turtle.forward(ancho)
    turtle.left(90)
    turtle.forward(alto)
    turtle.left(90)

def dibujarTriangulo(longitud):
    turtle.forward(longitud)
    turtle.left(120)
    turtle.forward(longitud)
    turtle.left(120)
    turtle.forward(longitud)
    turtle.left(120)

def dibujarArbol(alto,ancho):
    turtle.forward(ancho)
    turtle.left(90)
    turtle.forward(alto)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(120)
    turtle.forward(125)
    turtle.left(120)
    turtle.forward(125)
    turtle.left(120)
    turtle.forward(75)
    
    turtle.forward(alto)


def main():
    dibujarArbol(100,25)
    turtle.exitonclick()
main()