#Programa MAIN
import libreria29practica04

print("Numeros listaNarcisistas")

#VARIABLES
aux = 0

#Primer número
print("Dime un valor inicial:")
num1 = libreria29practica04.getNumero()
while(num1 == False):
    print("Eso no es un número. Introduzca un número:")
    num1 = libreria29practica04.getNumero()

#Segundo número
print("Dame un valor final:")
num2 = libreria29practica04.getNumero()
while(num2 == False):
    print("Eso no es un número. Introduzca un número:")
    num2 = libreria29practica04.getNumero()

#Ordenamos en caso de ser necesario
if(num1 > num2):
    aux = num1
    num1 = num2
    num2 = aux

#Pasamos los datos a las funciones
narcisistas = libreria29practica04.listaNumeros(num1, num2)

#Mostramos el resultado
print("-------------------------------")
print("Los números narcisistas son:")
print(narcisistas)
print("-------------------------------")
print("Fin de programa")