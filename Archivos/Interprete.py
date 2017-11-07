# encoding: UTF-8
# Autor: Roberto Martínez Román
# Muestra cómo utilizar pygame para escribir programas que dibujan en la pantalla

import pygame

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255,255,255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
NEGRO=(0,0,0)
ROJO = (255, 0, 0)


def interpretar(comandos, ventana):
    for instruccion in comandos:
        datos=instruccion.lower().split()
        if datos[0]=="r":
            #Rectángulo
            x=int(datos[1])
            y=int(datos[2])

            ancho=int(datos[3])
            alto=int(datos[4])

            pygame.draw.rect(ventana, NEGRO, (x, y, ancho, alto), 2)

        elif datos[0]=="c":
            x = int(datos[1])
            y = int(datos[2])
            radio=int(datos[3])

            pygame.draw.rect(ventana, NEGRO, (x, y),radio)

        elif datos[0] == "l":
            x1=int(datos[1])
            x2 = int(datos[3])

            y1 = int(datos[2])
            y2=int(datos[4])

            pygame.draw.line(ventana,NEGRO,(x1,y1),(x2,y2),2)




def dibujar(comandos):
    # Ejemplo del uso de pygame
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
        ventana.fill(BLANCO)

        # Dibujar, aquí haces todos los trazos que requieras
        interpretar(comandos,ventana)

        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps

    pygame.quit()   # termina pygame


def main():
    nombre=input("Teclea el programa que quieres ejecutar:")
    entrada=open(nombre,"r")
    comandos=entrada.readlines()
    entrada.close()

    dibujar(comandos)


main()
