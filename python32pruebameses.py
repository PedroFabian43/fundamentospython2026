from class32mes import Mes

print("Trabajando con clases")
listaMeses = []
for i in range(3):
    #Aquí creamos un nuevo mes
    mes = Mes()
    print("Introduce el mes", (i + 1))
    mes.nombre = input()
    print("Introduce la temperatura máxima")
    mes.tempMax = int(input())
    print("Introduce la temperatura mínima")
    mes.tempMin = int(input())
    listaMeses.append(mes)
#Recorremos los mese sque hemos almacenado
mediaAnual = 0
for dato in listaMeses:
    print(dato.nombre)
    print("Máxima:", str(dato.tempMax))
    print("Minima:", dato.tempMin)
    print("Media:", dato.getTempMed())
    mediaAnual = mediaAnual + dato.getTempMed()
print("Media anual ", mediaAnual)