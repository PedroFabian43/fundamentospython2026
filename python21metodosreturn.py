
#METODOS RETURN
#este metodo convierte a mayusculas
#Y nos lo devuelve en mayusculas

def convertirMayusculas(texto):
    return texto.upper() #Con esto nos lo devuelve en mayusculas al llamar a la funcion
#Otro metodo que convierte todo en minusculas
def convertirminusculas(texto):
    return texto.lower() #Nos devuelve el texto en minusculas

def concatenar(texto1, texto2):
    resultado = texto1 + " " + texto2
    return resultado #Nos devuelve el resultado porque si no lo tendriamos

#METODOS DE ACCION
def mostrarMenu():
    print("Seleccione opción")
    print("1.- Convertir a mayusculas")
    print("2.- Convertir a minusculas")
    print("3.- Concatenar textos")

#PROGRAMA PRINCIPAL MAIN
print("Ejemplo metodos return")
print("Introduce un texto:")
valor = input()
mostrarMenu()
opcion = int(input())
resultado = ""
if(opcion == 1):
    resultado = convertirMayusculas(valor)
    #print(convertirMayusculas(valor)) Se puede hacer así, es una manera distinta la cual no necesita de variable
elif(opcion == 2):
    resultado = convertirminusculas(valor)
elif(opcion == 3):
    print("Dame otro texto:")
    otro = input()
    resultado = concatenar(valor, otro)

print(resultado)
print("Fin de programa")