# encoding: UTF-8
# Autor: Carlos Pano Hernández
# Imprime número al revés

# encoding: UTF-8
# Autor: Roberto Martínez Román
# Muestra cómo utilizar pygame para escribir programas que dibujan en la pantalla

import pygame, math

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255]
VERDE = (0, 122, 0)
ROJO = (255, 0, 0)
NEGRO = (0, 0, 0)


def dibujarEjes(ventana):
    pygame.draw.line(ventana, VERDE, (ANCHO // 2, 0), (ALTO // 2, ALTO))
    pygame.draw.line(ventana, VERDE, (0, ANCHO // 2), (ANCHO, ALTO // 2))


def dibujarFuncion(ventana):

    for angulo in range(-720,720):
        anguloRad=math.radians(angulo)
        y=int(150*math.cos(anguloRad))
        pygame.draw.circle(ventana,ROJO,(angulo+ANCHO//2,ALTO//2-y),2)


def dibujar():
    # Ejemplo del uso de pygame
    pygame.init()  # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana de dibujo
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        # Borrar pantalla
        ventana.fill(NEGRO)

        # Dibujar, aquí haces todos los trazos que requieras
        dibujarEjes(ventana)
        dibujarFuncion(ventana)

        pygame.display.flip()  # Actualiza trazos
        reloj.tick(40)  # 40 fps

    pygame.quit()  # termina pygame


def invertirNumero(n):
    invertido = 0
    while n >= 10:
        digitoDerecha = n % 10
        invertido = invertido * 10 + digitoDerecha
        n = n // 10

    invertido = invertido * 10 + n

    return invertido


def main():
    dibujar()
    print(invertirNumero(123))


main()
