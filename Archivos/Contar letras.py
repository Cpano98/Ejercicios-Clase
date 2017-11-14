# encoding: UTF-8
# Autor: Carlos Pano Hernández
    # Contar letras de Don Quijote

def main():
    dLetras={}

    entrada=open("quijote.txt","r",encoding="UTF-8")
    contenido=entrada.read().lower()
    entrada.close()

    for letra in contenido: #VISITA cada caracter
        if letra.isalpha():
            if letra in dLetras:
                dLetras[letra] +=1

            else:
                dLetras[letra]=1

    print(dLetras)

    listaLetras=[]
    listaFrecuencias=[]

    for t in dLetras.items():
        listaLetras.append(t[0])
        listaFrecuencias.append(t[1])

    import matplotlib.pyplot as plot

    x=list(range(len(listaLetras)))
    plot.plot(x,listaFrecuencias) #Genera gráfica

    plot.xlabel("Letras")
    plot.ylabel("Frecuencia")
    plot.xticks(x,listaLetras,rotation="vertical")

    plot.show()

    #Tabla en un archivo
    salida=open("frecuencia.txt","w",encoding="UTF-8")
    salida.write("Letra/tFrecuencia")

    for t in dLetras.items():
        salida.write(t[0] + "-"+str(t[1])+"/n")
    salida.close()


main()