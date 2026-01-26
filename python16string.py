print("Ejemplo clase STRING")

texto = "primero pYthon"
#Vamos a probar diferentes metodos
print("upper ", texto.upper())
print("lower ", texto.lower())
print("replace ", texto.replace("o", "@"))
print("letra 0: ", texto[0])
print("Longitud: ", len(texto))
print("find(p):", texto.find("p"))
print("find(z): ", texto.find("z"))
print("rfind(p): ", texto.rfind("p"))
print("starstwith(a) ", texto.startswith("a"))
print("endswith(n): ", texto.endswith("n"))

#Sobrecarga de metodo: es añadir condiciones extra al método. como en el caso del find.rfind("p") 
#Aqui es un metodo pero al añadir el (,1) le añado condiciones extra y se "sobrecarga"
print("find(p, index): ", texto.find("p", 1))

#Metodos para saber del contenido de  un texto. normalmente van a salir false si son varias palabras pues los " " (espacios) cuentan y ni son letras o numeros

print("isdigit() ", texto.isdigit())
print("isalpha() ", texto.isalpha())
print("isalnum() ", texto.isalnum()) #Letras y números

#probamos slicing, llamado substring
#Recuperar una parte de un texto
subcadena = texto[2: ]
print("texto[2: ] ", subcadena)
print(texto[3: ]) #Es lo mismo sin variables
#En python podemos recuperar desde una posición hasta otra
subcadena = texto[2: 5]
print("texto[2:5] ", subcadena)
print(texto[2:5]) #Es lo mismo sin variables

#Podemos recorrer cada caracter con un bucle preferentemente un bucle FOR pero sirve WHILE
longitud = len(texto) #si la longitud es 10 el bucle automáticamente contará al final pues aunque el indice acaba en 9, son 10 caracteres
for i in range(longitud):
    letra = texto[i]
    print("letra[" + str(i) + "] =" + letra)
#Los parentesis () se usan en acciones, los corchetes [] se usan en conjuntos por ejemplo conjuntos de letras o strings

#Inclusopodemos validar lo que nos ofrece un usuario....

print("Introduce un numero: ")
#dato = int(input()) #aquí está guardando un int por lo que va a dar error por eso esta vez no lo ponemos como int si no lo dejamos como está
dato = input()
if(dato.isdigit() == True):
    print("Me has dado un número")
else:
    print("Que me des un número!!!")