# encoding: UTF-8
# Autor: Carlos Pano Hernández
# Descripción: Primera prueba de listas

def main():
    lista = []
    dato = int(input("Dato:"))

    while dato != -1:
        lista.append(dato)
        dato = int(input("Dato:"))

    print("Datos leídos:",lista)
    print("Número de datos:",len(lista))
    
    print("Mayor:", max(lista))
    print("Menor:", min(lista))

    promedio = sum(lista) / len(lista)
    print("Promedio:", promedio)

    print("Datos al revés:")
    for i in range(1,len(lista)+1):
        print(lista[-i], end=",")

main()
