#encoding: UTF-8
#Autor: Carlos Pano Hernández - A01066264
#Intrucciones: Condiciones

#Calcular el número mayor
def calcularMayor(a,b):
    if a>b:
        return a
    else:
        return b

def main():
    a=int(input("Valor 1: "))
    b=int(input("Valor 2: "))

    mayor=calcularMayor(a,b)
    print("El mayor es:", mayor)

main()