#encoding: UTF-8
#Autor: Carlos Pano Hernández
#Tabla del 7

def imprimirTabla(tabla):
    print("Tabla del",tabla)
    for factor in range(1,11):
        resultado=tabla*factor
        print("%d x %d = %d" %(tabla,factor, resultado))

def main():
    #imprimirTabla(int(input("Introduzca el número:")))
    for t in range(1,11):
        imprimirTabla(t)
        print("-------")

main()