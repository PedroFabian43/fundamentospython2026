#En un programa que deseamos ejecutar
#Los métodos se escriben en el inicio
#La sintaxis de los métodos  se escriben con la primera inicial en minúscula pero el resto en mayúscula
#EJ: primer (Solo una inicial y es minus) o primerMetodo (Al ser 2 iniciales la segunda en adelante va en mayuscula)


def primerMetodo():
    print("Primer Metodo")
def segundoMetodo():
    print("Segundo Metodo")

def metodoSaludar(nombre):
    print("Hola "+ nombre)
#Si no son llamados no se ejecutan

#Esto es el programa principal
print("Ejemplo de métodos")
#En el programa principal llamamos a los metodos
primerMetodo()
segundoMetodo()
metodoSaludar(nombre = "456")
print("Fin de programa")


