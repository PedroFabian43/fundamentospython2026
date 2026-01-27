#FUNCIONES
def menuCalculadora():
    print("Seleccione una opción")
    print("0.- Salir")
    print("1.- Sumar")
    print("2.- Restar")
    print("3.- Multiplicar")

def sumaNum(numero1, numero2):
    suma = numero1 + numero2
    return suma

def restaNum(numero1, numero2): 
    #resta = numero1 - numero2 Se puede hacer directamente
    return numero1 - numero2

def multiNum(numero1, numero2):
    multi = numero1 * numero2
    return multi

#PROGRAMA MAIN
print("Juego dos números")
print("--------------------------------")
#VARIABLES
print("Introduce el primer número:")
num1 = int(input())

print("Introduce el segundo número:")
num2 = int(input())

#Si queremos que cuando pulse 0 el usuario salga del bucle, creamos la variable
#Se le da un valor por defecto para que entre
opcion = -1
while(opcion != 0):
    menuCalculadora()
    opcion = int(input("Tu opción: "))
    resultado = 0

    if (opcion == 1):
        resultado = sumaNum(num1, num2)

    elif(opcion == 2):
        resultado = restaNum(num1, num2)

    elif(opcion == 3):
        resultado = multiNum(num1, num2)

    else:
        ("No es una opción válida")

    print("Tu resultado es:", resultado)
    print("--------------------------------")
print("Fin de programa")



