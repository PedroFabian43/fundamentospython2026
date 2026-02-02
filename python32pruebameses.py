from class32mes import Mes

print("Trabajando con clases")

enero = Mes()
enero.nombre = "Enero"
enero.tempMax = 9
enero.tempMin = -2

print("Media Enero:", enero.getTempMed(), "ºC")

mes2 = Mes()
mes2.nombre = "Febrero"
mes2.tempMax = 12
mes2.tempMin = 4

print("Media Febrero:", mes2.getTempMed(), "ºC")