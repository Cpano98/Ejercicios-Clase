#Autor: Carlos Pano Hernandez

print("Calcula el area de cualquier esfera...")
print("""
""")
entradaRadio = input("Inserte radio de la Esfera:")
radio = int(entradaRadio)
pi = 3.141592

areaSuperficie = 4*pi*radio**2
volumenEsfera = 4/3*pi*radio**3
diametroEsfera = radio*2

print "Area:",areaSuperficie
print "Volumen:",volumenEsfera
print "Diametro:",diametroEsfera
