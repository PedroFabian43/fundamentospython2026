print("Diccionarios")

#Los diccionarios son estructuras de datos que se rigen por el conjunto de pares key-value
#Todo elemento tiene una key asociada y se asocia en par.

#Los diccionarios se crean con .dict()
provincias = dict()

#Luego los elementos se añaden con variable = {Y aquí dentro los elementos con las keys como un if}
provincias = {
    924 : "Badajoz",    
    956:  "Cádiz",    
    958 : "Granada",    
    959 : "Huelva",    
    91 : "Madrid",    
    95 : "Málaga"
}

#Para recuperar un solo elemento por su key osea obtener su valor se usa .get()
dato = provincias.get(959)
print(dato)
#En caso de que una key no exista, imprimirá None que significa que no hay ninguna así

#Podemos recorrer cada clave y value con un for y el .items()
for clave, valor in provincias.items():
    print("Key: ", clave , "Valor: ", valor)
#Aquí puedo elegir si quiero imprimir uno solo o ambos.

#Tambien podemos recorrer solamente claves con .keys() 
for clave in provincias.keys():
    print(clave)
#O solo recorrer los values con .values()
for value in provincias.values():
    print(value)

#Podemos añadir elementos nuevos en el diccionario con .setdefault(key, value)
provincias.setdefault(925, "Toledo")

#En caso de que la key ya exista NO va a saltar error pero ignora la orden
provincias.setdefault(925, "Juancarlos") #Esta directamente es ignorada porque ya existiría la 925

#Pero si que podemos repetir el value pues solo es un texto
provincias.setdefault(933, "Toledo")#Esta si se va a hacer pues el value no importa solo el key

#Podemos eliminar un elemento por su key con .pop(key)
provincias.pop(924) #Borra la key y el value
#EN CASO D ENO EXISTIR LA CLAVE BORRADA SALTARA ERROR ASIQUE SIEMPRE BORRAR CON PRECAUCIÓN

#Para finalizar podemos borrar el diccionario entero con .clear() como las listas
provincias.clear() #ESTO ES IRRECUPERABLE EN CASO DE QUE EL USUARIO LO CREE CUIDADO.

print(provincias)
