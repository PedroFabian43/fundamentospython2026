from class33mascotas import Mascotas

print("Registro de mascotas")

listaMascotas = []

for i in range(3):
    print("------------------------")
    mascota = Mascotas()
    print("Introduce el nombre de la mascota", (i + 1))
    mascota.nombre = input()
    print("Introduce la especie de tu mascota:")
    mascota.especie = input()
    print("Introduce el año de nacimiento de tu mascota:")
    mascota.nacimiento = int(input())
    print("Introduce el año de adopción de tu mascota:")
    mascota.adopcion = int(input())
    listaMascotas.append(mascota)

for animal in listaMascotas:
    print("------------------------")
    print("Información de la mascota")
    print("Nombre:", animal.nombre)
    print("Especie:", animal.especie)
    print("Año de nacimiento:", animal.nacimiento)
    print("Año de adopción:", animal.adopcion)
    print("Tiempo en refugio:", animal.getPerrera())
print("------------------------")
print("Fin de programa")
