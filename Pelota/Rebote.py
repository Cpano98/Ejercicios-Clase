# encoding: UTF-8
# Autor: Carlos Pano Hernández
# Rebote de pelota

import pygame

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255,255,255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)

def rebotar():

    x=ANCHO//2
    y=ALTO//2
    radio=20
    DX= +4 #derecha (suma)
    DY= +8

    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Para limitar los fps
    termina = False # Bandera para saber si termina la ejecución

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        # Borrar pantalla
        ventana.fill(VERDE_BANDERA)

        #DibujarPelota:
        pygame.draw.circle(ventana,ROJO,(x,y),radio)

        #Movimiento:
        x += DX
        y += DY

        if y>=ALTO-radio or y<=radio:
            DY= -DY

        if x>=ANCHO-radio or x<=radio:
            DX= -DX



        pygame.display.flip()  # Actualiza trazos
        reloj.tick(120)  # 40 fps

    pygame.quit()  # termina pygame


def main():
    rebotar()

main()