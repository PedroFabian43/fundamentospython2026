print("Juguemos a un juego")

#print("Dime un número")
#n1 = input()

#print("Dime otro número")
#n2 = input()

n1 = int(input("Dime un número: "))
n2 = int(input("Dime otro número: "))

if (n1 > n2):
    print("El mayor es ", n1)
elif (n1 == n2):
    print("Ambos números son iguales")
else:
    print("El mayor es ", n2)

print("Fin del programa")
