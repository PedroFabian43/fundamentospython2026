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
dninum = dni[0: len(dni) - 1]
dninum = int(dninum)
validdni = libreria24validaciones.validDni(dninum)

print(validdni)
print("Fin de programa")



