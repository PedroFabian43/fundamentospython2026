print("ejemplos de bucles")

print("WHILE")
#Necesitamos una variable fuera del bucle
#Para nuestra condicion
contador = 0

while (contador <= 5):
    print("Contador:", contador)
    #Hasta aquí es un bucle infinito y eso es MUY PELIGROSO
    #Necesitamos cambiar el valor para darle un final al bucle
    contador = contador + 1

#En un bucle FOR, se declara la variable contador
#En la definición del bule, es decir, despues del for
#Dicha variable suele llamarse i, z o k como ejemplo
#Hacemos un FOr de 0-5
print("FOR")
for i in range (5+1):
    print("Valor de i:", i)
#Tenemos la posibilidad de indicar un numero de inicio y un numero final
#Hacemos un for de 2-8
for z in range(2, 8+1):
    print("z:", z)

print("Fin de programa")
