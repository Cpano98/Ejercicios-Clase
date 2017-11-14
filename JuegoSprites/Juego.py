# encoding: UTF-8
# Autor: Roberto Martínez Román
# Muestra cómo utilizar pygame para escribir programas que dibujan en la pantalla

import pygame

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)


def dibujarMenu(ventana, botonJugar):
    ventana.blit(botonJugar.image, botonJugar.rect)


def dibujarJuego(ventana, listaEnemigos, listaBalas):
    for enemigo in listaEnemigos:
        ventana.blit(enemigo.image, enemigo.rect)

    for bala in listaBalas:
        ventana.blit(bala.image, bala.rect)


def actualizarBalas(listaBalas, listaEnemigos):
    for bala in listaBalas:
        bala.rect.top -= 20
        if bala.rect.top <= 0:
            listaBalas.remove(bala)
            continue    #Regresa al inicio del ciclo

        borrarBala = False

        for k in range(len(listaEnemigos) - 1, -1, -1):
            enemigo = listaEnemigos[k]

            if bala.rect.colliderect(enemigo):
                listaEnemigos.remove(enemigo)
                borrarBala = True
                break

        if borrarBala:
            listaBalas.remove(bala)


def dibujar():
    # Ejemplo del uso de pygame
    pygame.init()  # Inicializa pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana de dibujo
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución

    estado = "menu"  # Agregar jugando, fin, etc.

    # Cargar imágenes
    imgBtnJugar = pygame.image.load("buttonJugar.png")

    # Sprite
    botonJugar = pygame.sprite.Sprite()
    botonJugar.image = imgBtnJugar
    botonJugar.rect = imgBtnJugar.get_rect()
    botonJugar.rect.left = ANCHO // 2 - botonJugar.rect.width // 2
    botonJugar.rect.top = ALTO // 2 - botonJugar.rect.height // 2

    # Enemigos
    listaEnemigos = []
    imgEnemigo = pygame.image.load("enemigo.png")

    # Balas
    listaBalas = []
    imgBala = pygame.image.load("bala.jpg")

    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

            # Mouse en los diferentes estados...
            elif evento.type == pygame.MOUSEBUTTONDOWN:  # El usuario hizo click
                # Posición del mouse
                xm, ym = pygame.mouse.get_pos()
                if estado == "menu":
                    # Posición del botón
                    xb, yb, anchoB, altoB = botonJugar.rect
                    if xm > xb and xm <= xb + anchoB:
                        if ym >= yb and ym <= yb + altoB:
                            # Cambiar de ventana/estado
                            estado = "jugando"

                # Ventana jugando, dibujar enemigos
                elif estado == "jugando":
                    enemigo = pygame.sprite.Sprite()
                    enemigo.image = imgEnemigo
                    enemigo.rect = imgEnemigo.get_rect()
                    enemigo.rect.left = xm - enemigo.rect.width // 2
                    enemigo.rect.top = ym - enemigo.rect.height // 2
                    listaEnemigos.append(enemigo)

            elif evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_SPACE:
                    bala = pygame.sprite.Sprite()
                    bala.image = imgBala
                    bala.rect = imgBala.get_rect()
                    bala.rect.left = ANCHO // 2
                    bala.rect.top = ALTO - bala.rect.height
                    listaBalas.append(bala)

        # Borrar pantalla
        ventana.fill(BLANCO)

        # Dibujar, aquí haces todos los trazos que requieras
        if estado == "menu":
            dibujarMenu(ventana, botonJugar)

        elif estado == "jugando":
            dibujarJuego(ventana, listaEnemigos, listaBalas)
            actualizarBalas(listaBalas, listaEnemigos)

        pygame.display.flip()  # Actualiza trazos
        reloj.tick(40)  # 40 fps

    pygame.quit()  # termina pygame


def main():
    dibujar()


main()
