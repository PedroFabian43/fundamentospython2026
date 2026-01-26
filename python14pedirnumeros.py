print("INICIO")

numero = int(input("Dame un número: "))
contador = 0
suma = numero

while(numero != 0):
    numero = int(input("Dame otro número: "))
    contador = contador + 1
    suma = suma + numero

print("Números solicitados:", contador)
print("La suma total es:", suma)


