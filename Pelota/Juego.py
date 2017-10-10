# encoding: UTF-8
# Autor: Carlos Pano Hernández
# Rebote de pelota

import pygame

# Dimensiones de la pantalla
ANCHO = 801
ALTO = 801
# Colores
BLANCO = (255,255,255)  # R,G,B en el rango [0,255]
NEGRO = (0,0,0)
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)

def rebotar():

    #Pelota
    x=ANCHO//2
    y=ALTO//2
    radio=15
    DX= +4 #derecha (suma)
    DY= +8

    #Raqueta
    ANCHO_RAQUETA = 10
    ALTO_RAQUETA = 100
    yRaqueta= ALTO//2


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
        ventana.fill(NEGRO)

        #DibujarRaqueta:
        pygame.draw.rect(ventana,BLANCO,(0,yRaqueta,ANCHO_RAQUETA,ALTO_RAQUETA))

        #DibujarPelota:
        pygame.draw.circle(ventana,BLANCO,(x,y),radio)

        #Movimiento:
        x += DX
        y += DY

        if y>=ALTO-radio or y<=radio:
            DY= -DY

        if x>=ANCHO-radio:
            DX= -DX

        #Colisión:
        if x<=ANCHO_RAQUETA and y>=yRaqueta and y<=yRaqueta+ALTO_RAQUETA:
            DX=-DX

        pygame.display.flip()  # Actualiza trazos
        reloj.tick(120)  # 40 fps

    pygame.quit()  # termina pygame


def main():
    rebotar()

main()
