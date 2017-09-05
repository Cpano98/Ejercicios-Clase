#encoding:UTF-8
#Autor: Carlos Pano Hernández - A01066264

#Convertidor dolar a peso
def convertirDolarPeso(dolarC):
    #Calcular
    pM=(dolarC*14.36)/1
    #regresar
    return pM

def main():
    dC=float(input("¿Cuántos dólares quieres convertir?:"))
    pesosM=convertirDolarPeso(dC)
    print("%.2f dólares canadienses son: %.2f"%(dC,pesosM))

main()