print("Rango de números pares")
inicial = int(input("Inicio del bucle: "))
numero_final = int(input("Final del bucle: "))
#Que tipo de bucle se puede usar? Se puede usar ambos

for i in range(inicial, numero_final + 1):
    #Deberiamos preguntar si el número es par
    if(i % 2 == 0):
        #PAR
        print(i)


while(inicial <= numero_final):
    if(inicial % 2 == 0):
        print(inicial)
    #Incrementamos su valor
    inicial = inicial + 1
print("---------------------------------")
print("Fin de programa")