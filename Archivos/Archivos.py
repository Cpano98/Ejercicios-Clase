# encoding: UTF-8
# Autor: Carlos Pano Hernández
# Muestra el uso de archivos

def main():
    nombre = input("Teclea el nombre del archivo que quieres ver:")
    entrada = open(nombre, "r",encoding="UTF-8")

    numeroLinea = 1
    for linea in entrada:
        print(numeroLinea, linea.rstrip())
        numeroLinea += 1

    entrada.close()


main()
