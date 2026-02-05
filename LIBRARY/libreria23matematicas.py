#En este script solo contendrá funciones/métodos
#FUNCIONES
def menuCalculadora():
    print("Seleccione una opción")
    print("0.- Salir")
    print("1.- Sumar")
    print("2.- Restar")
    print("3.- Multiplicar")
    print("4.- Cambiar números")

def sumaNum(numero1, numero2):
    suma = numero1 + numero2
    return suma

def restaNum(numero1, numero2): 
    #resta = numero1 - numero2 Se puede hacer directamente
    return numero1 - numero2

def multiNum(numero1, numero2):
    multi = numero1 * numero2
    return multi

#Vamos a crear un método que devolverá el número introducido
#En este método, tendremos un bucle infinito hasta que dé un número

def getNumero():
    print("Introduzca un número:")
    #Almacenamos lo que escriba el usuario en una variable String
    aux = input()
    #Entramos en un bucle mientras no sean números y lo hacemos como string porque isdigit() solo funciona con strings
    while(aux.isdigit() == False):
        print("Cifra no válida")
        print("Introduzca un número:")
        aux = input()
    #Convertimos el texto a número    
    return int(aux)
    #Podria crear una variable solo para hacer el int(aux) y ya pero así vale