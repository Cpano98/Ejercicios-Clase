#encoding: UTF-8
#Autor: Carlos Pano Hernández
#Tabla del 7

def imprimirTabla():
    print("Tabla del 7")
    for factor in range(1,101):
        resultado=7*factor
        print("7 x %d = %d" %(factor, resultado))

def main():
    imprimirTabla()

main()