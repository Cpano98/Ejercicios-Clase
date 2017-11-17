import requests

url="https://twitter.com/realDonaldTrump"
info=requests.get(url)

if info.status_code==200: #Lectura correcta
    #print(info.text)       #Procesa los datos

listaLineas=info.text.split("/n")


