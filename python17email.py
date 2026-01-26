print("Inicio")

email = input("Introduce tu e-mail: ")

if(email.find("@") == -1):
    print("tu e-mail necesita una @")
elif(email.find(".") == -1):
    print("Tu e-mail necesita un .")
elif(email.startswith("@") or email.endswith("@")):
    print("Tu e-mail no puede empezar ni acabar por @")
elif(email.count("@") >= 2):
    print("Tu e-mail solo puede contener una @")
elif(email.startswith(".") or email.endswith(".")):
    print("Tu e-mail no puede empezar ni acabar por .")
elif(email.find("@.") == -1):
    print("Tu e-mail tiene que tener un . detrás del @")





    
