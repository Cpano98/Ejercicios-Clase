#encoding: UTF-8
#Autor: Carlos Pano Hernández - A01066264
#Intrucciones: Condiciones

#Calcular el número mayor
def calcularMayor1(a,b):
    if a>b:
        m=a
    else:
        m=b
    return m

def calcularMayor2(c,d):
    if c>d:
        m=c
    else:
        m=d
    return m

def calcularMayor3(e,f):
    if e>f:
        m=e
    else:
        m=f
    return m

def main():
    a=int(input("Valor 1: "))
    b=int(input("Valor 2: "))
    c=int(input("Valor 3: "))
    d=int(input("Valor 4: "))

    comparacion1=calcularMayor1(a,b)
    comparacion2=calcularMayor2(comparacion1,c)
    comparacion3=calcularMayor3(comparacion2,d)

    print("El mayor es:", comparacion3)

main()