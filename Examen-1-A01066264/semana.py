#encoding:UTF-8

#Paso 1
print ("Este programa determina el día de la semana de cierta fecha.")
print ("")

#Paso 2, 3 y 4
dia = int(input("Teclea el día:"))
mes = int(input("Teclea el mes:"))
year = int(input("Tecle el año:"))

#Paso 5
z0 = (14-mes)//12
y0 = year-z0
m0 = mes+(12*z0)-2

d0 = (dia + y0 + (y0/4)-(y0//100)+(y0//400)+((31*m0)//12))
d1 = int(d0%7)

#Paso 6
print("")
print ("Día de la semana:",d1)
print ("")

#Paso 7
print ("Aquí puedes consultar el día de la semana de la fecha:",dia,"/",mes,"/",year)
print ("""1, Lunes
2, Martes
3, Miércoles
4, Jueves
5, Viernes
6, Sábado
0, Domingo""")