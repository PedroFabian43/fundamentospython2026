print("Tabla de multiplicar:")

numero = int(input("Dame un número: "))
resultado = 0

print("------------------------------")

for i in range(1, 11):
    resultado = numero * i
    print(numero,"*",i, "=", resultado)

print("------------------------------")

print("Fin de programa")