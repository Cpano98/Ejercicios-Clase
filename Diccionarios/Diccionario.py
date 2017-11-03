# encoding: UTF-8
    # Autor: Carlos Pano Hernández
#Prueba diccionarios

def menu():
    print("")
    print("1. Traducir Inglés - Español")
    print("2. Traducir Español - Inglés")
    print("0. Salir--------------------")
    print("")

    respuesta=int(input("Teclea tu opción:"))
    return respuesta


def traducirInglésEspañol():
    d={"hello":"hola","world":"mundo","house":"casa"}
    palabra=input("Teclea tu palabra:")
    if palabra in d:
        print("En español",palabra,"es:",d[palabra])

    else:
        print(palabra,"no está en la Base de datos")


def traducirEspañolIngles():
    d = {"hola": "hello", "mundo": "world", "casa": "house"}
    palabra = input("Teclea tu palabra:")
    if palabra in d:
        print("En inglés", palabra, "es:", d[palabra])
    else:
        print(palabra, "no está en la Base de datos")

def main():
    opcion=menu()

    while opcion !=0:
        #Procesa -opcion-

        if opcion==1:
            traducirInglésEspañol()

        elif opcion==2:
            traducirEspañolIngles()

        opcion=menu()

main()