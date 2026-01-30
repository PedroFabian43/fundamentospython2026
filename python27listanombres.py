#En este programa necesitamos:
#El programa va a pedir 5 nombres al usuario
#dichos nombres los mostraremos al final, despues de haberlo pedido.

#Si el usuario introduce un nombre repetido, le pedimos otro nombre de nuevo

#VERISON 2

#Que no importe que el nombre esté en mayusculas o minusculas

print("Nombres de listas")
listaNombres = []
while(len(listaNombres) <= 5):
    print("Dame un nombre")
    nombre = input()
    if (len(listaNombres) == 0):
        listaNombres.append(nombre)
    else:
        existe = False
        for elem in listaNombres:
            if(elem.upper() == nombre.upper()):
                    existe = True
                    break
        if(existe == False): 
            listaNombres.append(nombre)
    
print("----------------")
for n in listaNombres:
    print(n)
print("Fin de programa")
