import turtle

turtle.shape("turtle")


def dibujarCuadro(longitud):
    turtle.forward(longitud)
    turtle.left(90)
    turtle.forward(longitud)
    turtle.left(90)
    turtle.forward(longitud)
    turtle.left(90)
    turtle.forward(longitud)


dibujarCuadro(50)
turtle.left(90)
turtle.forward(50)
dibujarCuadro(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
dibujarCuadro(50)
turtle.left(180)
turtle.forward(100)
turtle.right(180)
dibujarCuadro(50)

