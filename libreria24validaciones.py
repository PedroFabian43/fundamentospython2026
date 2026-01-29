def validIsbn(isbn):
    
    longitud = len(isbn)
    suma = 0
    if (isbn.isdigit() == False or longitud != 10):
        return False

    if (longitud == 10):
        for i in range(longitud):
            cifra = isbn[i]
            
            multi = int(cifra) * (i+1)
            suma = suma + multi

    if(suma % 11 == 0):
        return True
        
    else:
        return False
    

def validDni(numerodni):

    letradni = int(numerodni) - (int(numerodni / 23) * 23)

    if (letradni == 0):
        return "T"
    elif (letradni == 1):
        return "R"
    elif (letradni == 2):
        return "W"
    elif (letradni == 3):
        return "A"
    elif (letradni == 4):
        return "G"
    elif (letradni == 5):
        return "M"
    elif (letradni == 6):
        return "Y"
    elif (letradni == 7):
        return "F"
    elif (letradni == 8):
        return "P"
    elif (letradni == 9):
        return "D"
    elif (letradni == 10):
        return "X"
    elif (letradni == 11):
        return "B"
    elif (letradni == 12):
        return "N"
    elif (letradni == 13):
        return "J"
    elif (letradni == 14):
        return "Z"
    elif (letradni == 15):
        return "S"
    elif (letradni == 16):
        return "Q"
    elif (letradni == 17):
        return "V"
    elif (letradni == 18):
        return "H"
    elif (letradni == 19):
        return "L"
    elif (letradni == 20):
        return "C"
    elif (letradni == 21):
        return "K"
    elif (letradni == 22):
        return "E"
    else:
        return "T"


    

def comprobDni(dni):
    letra = validDni(dni)
    if(letra == dni[dni + 1: ]):
        comprob = True
    else:
        comprob = False
    return comprob
