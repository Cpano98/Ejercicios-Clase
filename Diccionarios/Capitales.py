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

estados = ["Aguascalientes", "Baja California", "Baja California Sur", "Campeche", "Coahuila", "Colima", "Chiapas", "Chihuahua",
           "Distrito Federal", "Durango", "Guanajuato", "Guerrero", "Hidalgo", "Jalisco", "México", "Michoacán", "Morelos", "Nayarit", "Nuevo León",
           "Oaxaca","Puebla", "Querétaro", "Quintana Roo", "San Luis Potosí", "Sinaloa", "Sonora", "Tabasco", "Tamaulipas", "Tlaxcala", "Veracruz", "Yucatán",
           "Zacatecas"]

def seleccionarEstado():
    estado=estados[random.randint(0,len(estados)-1)]
    estados.remove(estado)
    return estado

def compararEstadoCapital(estado,capitalEstado):

    capital=capitales.get(estado)

    if capital==capitalEstado:
        print("¡Correcto!")

    else:
        print("Incorrecto :( --- su capital es:", capital)

def jugarCapitales():
    while len(estados)>=2:

        estado=seleccionarEstado()
        print("¿Cuál es la capital de:",estado,"?")
        capitalEstado=input("Su capital es:")
        print("")
        compararEstadoCapital(estado,capitalEstado)

        print("----------------------------------")

        estado = seleccionarEstado()
        print("¿Cuál es la capital de:", estado, "?")
        capitalEstado = input("Su capital es:")
        print("")
        compararEstadoCapital(estado, capitalEstado)
        print("----------------------------------")

def main():
    print("")
    print("¡Hola! Vamos a aprender las capitales... Recuerda escribir tus respuestas con acentos, espacios y mayúsculas. ¡Comencemos!")
    print("----------------------------------------")

    numeroJugadores=int(input("Ingresa el número de jugadores (máximo 6 participantes):"))
    print("Se preguntarán 5 capitales diferentes para los:", numeroJugadores,"jugadores")
    print("----------------------------------------")
    print("Ingrese: "
          "1 para comenzar a jugar."
    
          " 2 para salir.")

    seleccion=int(input("Ingrese su selección:"))

    while seleccion >=0:

        if seleccion==1:
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

        seleccion = int(input("Ingrese su selección:"))

main()
