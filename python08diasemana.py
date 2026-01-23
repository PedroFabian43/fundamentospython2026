print("Vamos a calcular que dia de la semana es")

from math import floor 

dia = int(input("Dime un dia: "))
mes = int(input("Dime un mes: "))
anno = int(input("Dime un año: "))

if(mes == 1):
    mes = 13
    anno = anno - 1
elif(mes == 2):
    mes = 14
    anno = anno - 1

n1 = floor(((mes + 1)* 3) / 5)
n2 = floor(anno / 4)
n3 = floor(anno / 100)
n4 = floor(anno / 400)
n5 = dia + (mes * 2) + anno + n1 + n2 - n3 + n4 + 2
n6 = floor(n5 / 7)
n7 = n5 - (n6 * 7)
resultado = floor(n7)

if(mes == 13):
    mes = 1
    anno = anno + 1
elif(mes == 14):
    mes = 2
    anno = anno + 1

if(resultado == 0):
    print("Sábado")
    print("Es día Sábado", str(dia)+"/"+str(mes)+"/"+str(anno))
elif(resultado == 1):
    print("Domingo")
    print("Es día Domingo", str(dia)+"/"+str(mes)+"/"+str(anno))
elif(resultado == 2):
    print("Lunes")
    print("Es día Lunes", str(dia)+"/"+str(mes)+"/"+str(anno))
elif(resultado == 3):
    print("Martes")
    print("Es día Martes", str(dia)+"/"+str(mes)+"/"+str(anno))
elif(resultado == 4):
    print("Miércoles")
    print("Es día Miércoles", str(dia)+"/"+str(mes)+"/"+str(anno))
elif(resultado == 5):
    print("Jueves")
    print("Es día Jueves", str(dia)+"/"+str(mes)+"/"+str(anno))
else:
    print("Viernes")
    print("Es día Viernes", str(dia)+"/"+str(mes)+"/"+str(anno))

print("Fin de programa")









