# encoding: UTF-8
# Autor: Abigail Cerda, Anaid Labat, Carlos Pano Hernández
# Prueba capitales

import random

capitales = {'Aguascalientes': 'Aguascalientes', 'Baja California': 'Mexicali', 'Baja California Sur': 'La Paz',
             'Campeche': 'Campeche', 'Coahuila': 'Saltillo', 'Colima': 'Colima', 'Chiapas': 'Tuxtla Gutiérrez',
             'Chihuahua': 'Chihuahua', 'Distrito Federal': 'Ciudad de México', 'Durango': 'Durango',
             'Guanajuato': 'Guanajuato', 'Guerrero': 'Chilpancingo', 'Hidalgo': 'Pachuca', 'Jalisco': 'Guadalajara',
             'México': 'Toluca', 'Michoacán': 'Morelia', 'Morelos': 'Cuernavaca', 'Nayarit': 'Tepic',
             'Nuevo León': 'Monterrey', 'Oaxaca': 'Oaxaca', 'Puebla': 'Puebla', 'Querétaro': 'Querétaro',
             'Quintana Roo': 'Chetumal', 'San Luis Potosí': 'San Luis Potosí', 'Sinaloa': 'Culiacán',
             'Sonora': 'Hermosillo', 'Tabasco': 'Villahermosa', 'Tamaulipas': 'Ciudad Victoria', 'Tlaxcala': 'Tlaxcala',
             'Veracruz': 'Xalapa', 'Yucatán': 'Mérida', 'Zacatecas': 'Zacatecas'}

estados = ["Aguascalientes", "Baja California", "Baja California Sur", "Campeche", "Coahuila", "Colima", "Chiapas",
           "Chihuahua",
           "Distrito Federal", "Durango", "Guanajuato", "Guerrero", "Hidalgo", "Jalisco", "México", "Michoacán",
           "Morelos", "Nayarit", "Nuevo León",
           "Oaxaca", "Puebla", "Querétaro", "Quintana Roo", "San Luis Potosí", "Sinaloa", "Sonora", "Tabasco",
           "Tamaulipas", "Tlaxcala", "Veracruz", "Yucatán",
           "Zacatecas"]


def seleccionarEstado():
    estado = estados[random.randint(0, len(estados) - 1)]
    estados.remove(estado)
    return estado


def compararEstadoCapital(estado, capitalEstado):
    capital = capitales.get(estado)

    if capital == capitalEstado:
        print("¡Correcto!")

    else:
        print("Incorrecto :( --- su capital es:", capital)


def jugarCapitales():
    puntosJugadorDos = 0
    puntosJugadorUno = 0

    while len(estados) >= 1:

        estado = seleccionarEstado()
        print("JUGADOR 1: ¿Cuál es la capital de:", estado, "?")
        capitalEstado = input("Su capital es:")
        print("")
        compararEstadoCapital(estado, capitalEstado)

        if capitalEstado == capitales.get(estado):
            puntosJugadorUno = puntosJugadorUno + 1
            print("Tu puntuación es de:", puntosJugadorUno)

        else:
            puntosJugadorUno = puntosJugadorUno - 0.5
            print("Tu puntuación es de:", puntosJugadorUno)

        print("----------------------------------")

        estado = seleccionarEstado()
        print("JUGADOR 2: ¿Cuál es la capital de:", estado, "?")
        capitalEstado = input("Su capital es:")
        print("")
        compararEstadoCapital(estado, capitalEstado)

        if capitalEstado == capitales.get(estado):
            puntosJugadorDos = puntosJugadorDos + 1
            print("Tu puntuación es de:", puntosJugadorDos)

        else:
            puntos = puntosJugadorDos - 0.5
            print("Tu puntuación es de:", puntosJugadorDos)

        print("----------------------------------")

    if puntosJugadorUno > puntosJugadorDos:
        print("¡Felicidades jugador 1! Ganaste con:", puntosJugadorUno, "Superando al jugador 2 por:",
              puntosJugadorUno - puntosJugadorDos, "- Jugador 2, tuviste:", puntosJugadorDos)
    elif puntosJugadorDos > puntosJugadorUno:
        print("¡Felicidades jugador 2! Ganaste con:", puntosJugadorDos, "Superando al jugador 1 por:",
              puntosJugadorDos - puntosJugadorUno, "- Jugador 1, tuviste:", puntosJugadorUno)
    elif puntosJugadorUno == puntosJugadorDos:
        print("¡Felicidades! Ambos se saben muy bien las capitales, tuvieron un total de:", puntosJugadorUno, "puntos")


def main():
    print("")
    print(
        "¡Hola! Vamos a aprender las capitales de México... RECUERDA escribir tus respuestas con acentos, espacios y mayúsculas. ")
    print("¡¡¡Consigue a un compañero y que empiece la COMPETENCIA!!!")
    print("----------------------------------------")
    print("Ingrese: "
          "1 para comenzar a jugar."

          " 2 o cualquier otro número para salir.")

    seleccion = int(input("Ingrese su selección:"))

    while seleccion >= 0:

        if seleccion == 1:
            print("¡Empecemos!")
            print("----------------------------------------")
            jugarCapitales()
            print("")
            print("Gracias por jugar, espero que hayas aprendido :) ¡Hasta luego!")
            break

        else:
            print("¡Hasta luego!")
            print("----------------------------------------")
            print("")
            break


main()
