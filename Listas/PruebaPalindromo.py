# encoding: UTF-8
    # Autor: Carlos Pano Hernández
# Descripción: Detector si una palabra es palíndromo.

def main():
    cadena = input("Cadena:")
    cadena=cadena.upper()

    original= list(cadena)
    sinEspacios=[]

    for dato in original:
        if dato !="":
            sinEspacios.append(dato)

    alReves=[]
    for dato in sinEspacios:
        alReves.insert(0,dato)

    if alReves == sinEspacios:
        print("ES palindromo")

    else:
        print("NO es palindromo")

main()


