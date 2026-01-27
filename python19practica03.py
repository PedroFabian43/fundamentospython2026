print("------VALIDANDO ISBN------")

#VARIABLES
isbn = input("Introduzca número ISBN: ")
resultado = 0
suma = 0
longitud = len(isbn)

#Revisamos que todos son dígitos
while (isbn.isdigit() == False):
    print("Error: el ISBN no contiene letras. Inténtalo de nuevo")
    isbn = input("Dime tu ISBN: ")

#Revisamos que la longitud sea correcta.
if(longitud != 10): #En este caso esto es como poner (longitud >= 11 or longitud <= 9) pero mas corto. 
    print("Error: no es un ISBN válido")
    print("Fin del programa")
else: 
    for i in range(longitud):
        cifra = isbn[i]
        #Hacemos que el caracter actual en el que está el bucle sea una variable.
        multi = int(cifra) * (i+1)
        #En esta operación estoy multiplicando el número que se encuentre en la posición actual de i por el número del bucle que és.
        # En este caso es (i+1) porque no necesito el bucle 0 para nada, solo los siguiente los cuales se incrementan cada vez. El bucle 0 es 1 y el bucle 1 es 2 y así.
        #print(isbn[i],"*",i+1, "=", multi)
        suma = suma + multi
        #print("Suma:", suma)

#Revisamos que el calculo final esté correcto
if(suma % 11 == 0):
    print("CORRECTO")
else:
    print("INCORRECTO")
print("------FIN VALIDACIÓN------")

