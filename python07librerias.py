print("Librerias Python")
#Necesitamos la parte entera del resultado

#resultado = int(7 / 3)

#print(resultado)

#print("Fin de programa")

#Necesitamos redondear al alza la parte entera del resultado
#No se puede de forma nativa en python hacerlo
#La unica forma de hacer operaciones matemáticas complejas es usando CLASES HERRAMIENTA osea LIBRERIAS.

#math es una LIBRERIA INTEGRADA EN PYTHON
#import math 
# from math import floor, ceil // Sirve para solamente importar floor y ceil de math y no tener que escribir math.floor, solamente floor y lo que sea

#resultado2 = 5 / 3
#print(resultado2)
#print("Floor", math.floor(resultado2)) #math.floor sirve para redondear hacia abajo una división con decimales
#print("Ceil", math.ceil(resultado2)) #math.ceil sirve para redondear hacia arriba una división con decimales
#print("Fin del programa")

from math import floor, ceil
n1 = 7
n2= 3
resultado2= n1 / n2
celi = ceil(resultado2)
flora = floor(resultado2)
print(resultado2)
print("Floor", flora)
print("Ceil", celi)
print("Fin")





