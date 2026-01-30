print("Listas con Python")
#LISTA
#La sintaxis es o entre palabras con _ o con la segunda inicial en adelante con Mayúscula.
#La lista se hace SIEMPRE entre []
listaNumeros = [3,5,7,11,2,9,88]
#Aqui podemos mostran en pantalla directamente la lista entera
#Con un print(lintanumeros) entre el () la variable de la lista y ya

#con SORT podemos ordenarlos de menor a mayor o de A a Z
#listaNumeros.sort()

#con SORT(reverse = True) lo ordenamos de mayor a menor y de Z a A
#listaNumeros.sort(reverse = True)

#Podemos recorrer uno a uno cada elemento de la lista con un bucle for (TODO EMPIEZA EN 0)
for i in range(len(listaNumeros)):
    print(listaNumeros[i])

#Las listas pueden ser de cualquier tipo:
listaNombres = ["Ana","Paco","Juan","Gonzalo", "Pedro", "Juan"]
#Accedemos al nombre por su posición en el índice
print("Nombre: ", listaNombres[2])
print("Nombre: ", listaNombres[4])

#Podemos añadir elementos nuevos con append y estos aparecerán en el final
listaNombres.append("Marta")

#También podemos insertar un elemento en una posición concreta con insert
listaNombres.insert(1,"Rebeca") #Con estó irá a la posición uno y colocará el nuevo nombre empujando a todos los demás en una posición

#Con el método remove() puedes eliminar al primer elemento que se llamé asi que encuentre, si hay más, los deja.
#listaNombres.remove("Juan")

#Podemos eliminar por posición/Índice con .pop()
listaNombres.pop(3)#Solo puede tener otra instrucción, es de uno en uno

#Podemos borrar rangos y varios con del (como si fuera def)
del listaNombres[0:2]

#Podemos preguntar por elementos en la lista con "" in nombreLista
#El nombre debe ser exacto porque diferencia de mayúsculas y minúsculas
repuesta = "Diana" in listaNombres
print("Existe: ", repuesta)

#Podemos recorrer cada elemento con bucle for aún siendo textos
for i in range(len(listaNombres)):
    print(listaNombres[i])

#Podemos borrar la lista entera con .clear()
listaNombres.clear()
print(listaNumeros)
print(listaNombres)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

print("Tuplas")
#La sintaxis es la misma que las listas
#Es una lista de elementos estáticos, es decir, una vez se crea, no se puede modificar de ninguna manera
#Esta también puede ser de lo que se quiera, numero o texto, etc...
#Se diferencia porque la tupla se hace con () pero al hacer print se puede elegir uno de dentro, pero nada mas
tupla = ("Leche", "Cacao", "Avellanas", "Azucar")
print("Tupla: ", tupla[1])
print(tupla)

#La razon de usar la tupla en vez de la lista es por que si es una lista cerrada y no modificable en plan los meses o paises y tal, es más cómodo y nadie lo toca.

for elem in tupla:
    print(tupla)

