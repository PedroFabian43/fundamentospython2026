print("Vamos a ver que numero es mayor")
#Variables
n1 = int(input("Dime el primer número: "))
n2 = int(input("Dime el segundo número: "))
n3 = int(input("Dime el tercer número: "))

mayor = 0
intermedio = 0
menor = 0

if( n1 > n2 and n1 > n3):
    mayor = n1
    if(n2 > n3):
        intermedio = n2
        menor = n3
    else:
        intermedio = n3
        menor = n2
elif( n2 > n1 and n2 > n3):
    mayor = n2
    if(n1 > n3):
        intermedio = n1
        menor = n3
    else:
        intermedio = n3
        menor = n1
else:
    mayor = n3
    if(n1 > n2):
        intermedio = n1
        menor = n2
    else:
        intermedio = n2
        menor = n1

print("El mayor es:", mayor)
print("El intermedio es:", intermedio)
print("El menor es:", menor)
print("Fin de programa")