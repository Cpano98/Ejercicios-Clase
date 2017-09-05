#encoding: UTF-8

print ("""Calcula el pago por boletos para el concierto
Autor: Carlos Pano Hernández""")

#Paso 2
totalA = float(input("Número de boletos para zona A:"))

#Paso 3
totalB = float(input("Número de boletos para zona B:"))

#Paso 4, 5 y 6
precioTotalA = totalA*900
precioTotalB = totalB*350
precioTotal = precioTotalA + precioTotalB

#Paso 7
print ("Total por los boletos de la zona A:", "$",precioTotalA)
print ("Total por los boeltos de la zona B:", "$",precioTotalB)
print ("-------------------------------------------------")
print ("Total por todos los boletos:", "$",precioTotal)

