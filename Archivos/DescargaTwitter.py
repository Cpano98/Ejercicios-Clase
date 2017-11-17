import requests

url = "https://twitter.com/abidelpra"
info = requests.get(url)

listaLineas = info.text.split("\n")
indice = 0
linea = listaLineas[indice]

while 'u-hiddenVisually">Seguidores' not in linea:
    indice += 1
    linea = listaLineas[indice]

linea = listaLineas[indice + 1]

print("*****", linea, "*****")

tokens = linea.split()

#print(tokens)
datos = tokens[2].split("=")
seguidores = int(datos[1])
print("-----------------------")
print("Seguidores:", seguidores)

for linea in listaLineas:
    if "TweetTextSize" in linea:
        inicial=linea[linea.index('">') +2:]
