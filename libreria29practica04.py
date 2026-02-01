def getNumero():
    aux = input()
    if(aux.isdigit() == False):
        return False
    else:
        return int(aux)

def listaNumeros(numero1, numero2):
    suma = 0
    resultado = 0
    listaNarcisistas = []
    for i in range(numero1, numero2 + 1):
        resultado = i
        longitud = len(str(resultado))
        for digito in str(resultado):
            numero = int(digito)
            multi = numero ** longitud
            suma = suma + multi
        if(suma == resultado):
            listaNarcisistas.append(suma)
        suma = 0
    return listaNarcisistas