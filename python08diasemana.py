print("Vamos a calcular que dia de la semana es")

from math import trunc 

dia = int(input("Dime un dia: "))
mes = int(input("Dime un mes: "))
anno = int(input("Dime un año: "))
#Añadimos los cambios por años bisiestos
if(mes == 1):
    mes = 13
    anno = anno - 1
elif(mes == 2):
    mes = 14
    anno = anno - 1
#Empezamos a hacer calculos
n1 = trunc(((mes + 1)* 3) / 5)
n2 = trunc(anno / 4)
n3 = trunc(anno / 100)
n4 = trunc(anno / 400)
n5 = dia + (mes * 2) + anno + n1 + n2 - n3 + n4 + 2
n6 = trunc(n5 / 7)
resultado = n5 - (n6 * 7)
#Volvemos a cambiar las variables por año bisiesto
if(mes == 13):
    mes = 1
    anno = anno + 1
elif(mes == 14):
    mes = 2
    anno = anno + 1
#Depende del resultado entre 0 o 6, sale un dia de la semana 
#Usando .zfill(2) le estoy diciendo que rellene el espacio hasta 2 osea añade un 0 si solo hay un número a la izquierda y si son 2 como el mes 10, no lo añade pues son 2
if(resultado == 0):
    print("Sábado")
    print("Es día Sábado", str(dia)+"/"+str(mes).zfill(2)+"/"+str(anno))
elif(resultado == 1):
    print("Domingo")
    print("Es día Domingo", str(dia)+"/"+str(mes).zfill(2)+"/"+str(anno))
elif(resultado == 2):
    print("Lunes")
    print("Es día Lunes", str(dia)+"/"+str(mes).zfill(2)+"/"+str(anno))
elif(resultado == 3):
    print("Martes")
    print("Es día Martes", str(dia)+"/"+str(mes).zfill(2)+"/"+str(anno))
elif(resultado == 4):
    print("Miércoles")
    print("Es día Miércoles", str(dia)+"/"+str(mes).zfill(2)+"/"+str(anno))
elif(resultado == 5):
    print("Jueves")
    print("Es día Jueves", str(dia)+"/"+str(mes).zfill(2)+"/"+str(anno))
else:
    print("Viernes")
    print("Es día Viernes", str(dia)+"/"+str(mes).zfill(2)+"/"+str(anno))

print("Fin de programa")









