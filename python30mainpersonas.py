#importamos la clase
from class30persona import Persona
print("Manejando clases persona")
#Creamos una persona

persona1 = Persona()
persona1.nombre = "Paco"
persona1.apellidos = "Perez"
persona1.annonacimiento = 2001
persona1.pais = "España"

print(persona1.getNombreCompleto())
print("Edad persona 1:", persona1.getEdadFalsa(10))
print("Edad persona 1:", persona1.getEdad())
print("Pais de procedencia:", persona1.pais)

persona2 = Persona()
print("Persona 2 pais:", persona2.pais)
print("Fin de programa")

#podemos imprimir la persona pero de inicio nos dará un codido raro
print(persona1)

