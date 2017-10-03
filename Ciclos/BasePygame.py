# encoding: UTF-8
# Autor: Roberto Martínez Román y Carlos Pano Hernández
# Muestra cómo utilizar pygame para escribir programas que dibujan en la pantalla

import pygame
from random import randint

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800

# Colores
BLANCO = (255,255,255)  # R,G,B en el rango [0,255]. Paleta de colores.
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)

def dibujar():
    # Ejemplo del uso de pygame
    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Para limitar los fps. Se debe bajar para reducir la sobrecarga a la computadora.
    termina = False # Bandera para saber si termina la ejecución

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        # Borrar pantalla
        ventana.fill(BLANCO)

        # Dibujar, aquí haces todos los trazos que requieras
        pygame.draw.rect(ventana, VERDE_BANDERA, (30, 30, ANCHO-60, ALTO-60), 5)
        pygame.draw.circle(ventana, ROJO, (ANCHO//2, ALTO//2), 200, 2)
        pygame.draw.line(ventana,VERDE_BANDERA,(0,ALTO),(ANCHO,0),10)

        for y in range(0,ALTO,20):
            ALEATORIO=(randint(0,255),randint(0,255),randint(0,255))
            pygame.draw.line(ventana,ALEATORIO,(0,y),(ANCHO,y),2)

        for x in range(0,ANCHO,20):
            ALEATORIO = (randint(0, 255), randint(0, 255), randint(0, 255))
            pygame.draw.line(ventana,ALEATORIO,(x,0),(x,ALTO),2)

        pygame.display.flip()   # Actualiza trazos
        reloj.tick(60)          # 40 fps

    pygame.quit()   # termina pygame


def main():
    dibujar()


main()