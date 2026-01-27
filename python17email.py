
print("Validación de e-mail")
email = input("Introduce tu e-mail: ")
email = email.lower()
if(email.find("@") == -1): #podria haberse usado un email.count == 0 pues como cuenta cuantas y no su indice sería 0
    print("Tu e-mail necesita una @") 
elif(email.startswith("@") or email.endswith("@")): #Se podia haber hecho un .find("@") == 0 para que la busque en la posición del indice 0 osea el primer caracter
    print("Tu e-mail no puede empezar ni acabar por @")
elif(email.count("@") >= 2):
    print("Tu e-mail solo puede contener una @")
elif(email.find(".") == -1):
    print("Tu e-mail necesita un .")
elif(email.find(".", email.find("@")) == -1):
    print("Tu e-mail necesita un . detrás de la @")
#elif(email.rfind(".") < email.find("@")): Se podría haber buscado el . desde la derecha y si su posición 
#   print("Tu e-mail necesita un . detrás de la @")
elif(email.startswith(".") or email.endswith(".")):
    print("Tu e-mail no puede empezar ni acabar por .")
else:
    post_punto = email.rfind(".") #Se usa rfind y no find porque si hay un punto en el email a parte del de detrás de la @ va a contar eso.
    dominio = email[post_punto + 1: ]
    if(len(dominio) < 2 or len(dominio) > 3):
        print("El dominio no es válido. Debe ser de entre 2-3 carácteres")
    else: 
        print("Tu e-mail es válido")
        #print(email)
print("Fin de programa")
        
#Puedes poner como inicio de búsqueda en caso de que el texto venga de un input un .find("aquí el texto de inicio")






    
