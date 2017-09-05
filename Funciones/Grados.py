#encoding: UTF-8

#Convierte F a C
def convertirFaC(gradosF):
    #Calcular
    gradosC=(gradosF-32)/1.8
    #regresar
    return gradosC

def main():
    gf=float(input("Temperatura en Fahrenheit:"))
    gc=convertirFaC(gf)
    print("%d F equivalen a %.2f C"%(gf,gc))

main()