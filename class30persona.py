#Las clases siempre empiezan en mayúscula
class Persona:
    #Podemos declarar  las propiedades aquí
    #Debemos asignar un valor sea vacío o no
    nombre = ""
    apellidos = ""
    pais = ""
    email = ""
    annonacimiento = 0

    #Podemos declarar las propiedades en el contructor directamente e iniciarlas
    #Es decir meter las variables dentro del __init__ como he escrito abajo
    #Es otra forma de hacer las cosas

    #Un constructor es el primer código que se va a leer al llamar a la clase
    #Se le conoce como __init__
    #En caso de que no necesite un constructor no lo pongo
    def __init__(self):
        self.pais = "Francia"
        #self.nombre = ""
        #self.apellidos = ""
        #self.pais = ""
        #self.email = ""
        #self.annonacimiento = 0

    
    #Los métodos son acciones sobre la clase persona
    def getNombreCompleto(self):
        return self.nombre + " " + self.apellidos
    
    def getEdad(self):
        return 2026 - self.annonacimiento
    
    def getEdadFalsa(self, annosquitados):
        return 2026 - self.annonacimiento - annosquitados
    
    #con esta funcion lo que hacemos es que cuando imprimamos el objeto d ela persona salga esto
    def __str__(self):
        return "Buenos dias"