#Autor: Carlos Pano Hernandez

#-------------------------
#Ecuacion de segundo grado
#-------------------------
print("Obten las soluciones de x en la ecuacion de Segundo grado:")
#Paso 1 ----------------------------------------------
coeficienteA = input('''Inserte el coeficiente "a":''')
coeficienteB = input('''Inserte el coeficiente "b":''')
coeficienteC = input('''Inserte el coeficiente "c":''')
a = int(coeficienteA)
b = int(coeficienteB)
c = int(coeficienteC)
#Paso 2---Calcular X1---------------------------------
x1 =(-b + (b*b -(4*a*c)**0.5))/ (2*a)

#Paso 3--Calcular X2----------------------------------
x2=(-b- (b*b -(4*a*c)**0.5))/ (2*a)

print ("x1="), x1
print ("x2="), x2