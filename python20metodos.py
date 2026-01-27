#En un programa que deseamos ejecutar
#Los métodos se escriben en el inicio
#La sintaxis de los métodos  se escriben con la primera inicial en minúscula pero el resto en mayúscula
#EJ: primer (Solo una inicial y es minus) o primerMetodo (Al ser 2 iniciales la segunda en adelante va en mayuscula)


def primerMetodo():
    #Este código jamas se ejecuta si no s ele llama explicitamente
    print("Primer Metodo")
def segundoMetodo():
    print("Segundo Metodo")

def saludar(nombre):
    print("Bienvenido a Pythom "+ nombre)

def despedirse(nombre, dia):
    print("Ha sido un placer hoy " + dia + ", Mr/Mrs "+ nombre)

#Esto es el programa principal
print("Ejemplo de métodos")
#En el programa principal llamamos a los metodos

saludar("Alumno")
primerMetodo()
segundoMetodo()
despedirse("Alumno", "Martes")
print("Fin de programa")


