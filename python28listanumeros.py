#Programa que nos va a pedir números hasta que introduzcamos el valor -1

#Al final del programa necesitamos mostrar los siguientes datos.
#La suma total de los números
#Numeros introducidos
#Números pares
#numeros impares
#Suma pares
#Suma impares

#mostrar los pares, inpares y los numeros introducidos

listaNum = []
listaPar = []
listaImpar = []
suma = 0
sumapar = 0
sumaimpar = 0

stop = False
contador = 0
contadorpar = 0
contadorimpar = 0
while (stop == False):
    print("Introduce un número:")
    num = int(input())
    suma = suma + num
    if(num == -1):
        stop = True
        break
    
    if(num % 2 == 0):
        listaPar.append(num)
        contador = contador + 1
        contadorpar = contadorpar + 1
        sumapar = sumapar + num

    else:
        listaImpar.append(num)
        contador = contador + 1
        contadorimpar = contadorimpar + 1
        sumaimpar = sumaimpar + num

    listaNum.append(num)

listaImpar.sort()
listaPar.sort()
listaNum.sort()

print("----------------------------------")
print("Resultados")
print("Números introducidos:", contador)
print("Números pares:", contadorpar)
print("Números impares:", contadorimpar)
print("La suma de los pares es:", sumapar)
print("La suma de los impares es:", sumaimpar)
print("La suma total es:", suma)


print("----------------------------------")
print("Lista de todos los numeros:")
for num in listaNum:
    print(num)
    
print("----------------------------------")
print("Lista de todos los pares:")
for num in listaPar:
    print(num)

print("----------------------------------")
print("Lista de todos los impares:")
for num in listaImpar:
    print(num)

print("----------------------------------")
print("Fin de programa")


