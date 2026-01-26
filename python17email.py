
email = input("Introduce tu e-mail: ")
post_punto = email.find(".")
email = email.lower()
if(email.find("@") == -1):
    print("Tu e-mail necesita una @") 
elif(email.startswith("@") or email.endswith("@")):
    print("Tu e-mail no puede empezar ni acabar por @")
elif(email.count("@") >= 2):
    print("Tu e-mail solo puede contener una @")
elif(email.find(".") == -1):
    print("Tu e-mail necesita un .")
elif(email.find(".", email.find("@")) == -1):
    print("Tu e-mail necesita un . detrás de la @")
elif(email.startswith(".") or email.endswith(".")):
    print("Tu e-mail no puede empezar ni acabar por .")
else:
    dominio = email[post_punto + 1: ]
    if(len(dominio) < 2 or len(dominio) > 3):
        print("El dominio no es válido. Debe ser de entre 2-3 carácteres")
    else: 
        print("Tu e-mail es válido")
        print(email)
        print("Fin de programa")
        







    
