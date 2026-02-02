class Coche:
    #Declaramos las variables en el __init__
    def __init__(self):
        self.marca = ""
        self.modelo = ""
        self.velocidad = 0
        self.estado = False
    
    def getVelocidadMaxima(self):
        return 140

    def arrancar(self):
        self.estado = True
        print("Coche arrancado")

    def detener(self):
        if(self.estado == False):
            print("El coche ya está parado")
        else:
            self.estado = False
            print("El coche se detuvo")

    def acelerar(self):
        if(self.estado == False):
            print("El coche está parado")
        else:
            self.velocidad = self.velocidad + 20
            print("Su velocidad es de:", self.velocidad)

    def frenar(self):
        if(self.velocidad == 0):
            print("Ya está parado")
        else:
            self.velocidad = self.velocidad - 10
            print("Su velocidad es de:", self.velocidad)