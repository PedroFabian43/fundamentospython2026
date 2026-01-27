print("Sumemos números")
#VARIABLES
cifra = input("Dame una cifra: ")
suma = 0
#OPERACIONES
if(cifra.isdigit() == False):
    print("Error: Solo se permiten números")
else:
    longitud = len(cifra)
    for i in range(longitud):
        #necesito cada número del texto
        num = cifra[i]#Con esto cada vez recorre una posición distinta y guarda un número de la cifra distinto entonce sse vuelve el número que suma y así hatsa acabar
        #Con los [] lo que hago es especificar que quiero transformar en num a el número en la que se encuentra i en es emomento del bucle y no toda la cifra.
        suma = suma + int(num) 
        #Convierto el texto en números para sumarlos y se suman cada vez que el bucle se repite.
print(suma)
print("Fin de programa")

#En vez de con un if se puede hacer con un while para que lo puedas repetir.

#while(cifra.isdigit() == False):
#   print("error no son numeros. intentalo de nuevo")
#   cifra = input("Dame una cifra: ").


