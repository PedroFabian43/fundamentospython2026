#IMPORTS
import libreria24validaciones
#MAIN
print("Validaciones")
print("Introduzca ISBN")
isbn = input()
validisbn = libreria24validaciones.validIsbn(isbn)

if(isbn == False):
    print("Tu ISBN no es un ISBN válido")
else:
    print("Tu ISBN es válido.")

print("Introduzca número DNI")
dni = input()
validdni = libreria24validaciones.validDni(dni)
comprob = libreria24validaciones.comprobDni(dni)

print(validdni)
print(comprob)
print("Fin de programa")



