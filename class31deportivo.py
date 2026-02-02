from class31coche import Coche
#Importamos la clase que vamos a usar para la herencia
class Deportivo(Coche):

    def getVelocidadMaxima(self):
        #La clase super se refiere a la clase de la que se está heredando
        velocidadCoche = super().getVelocidadMqaxima()
        return velocidadCoche + 100

    def turbo(self):
        self.velocidad += 100
        print("A tope!!!!!!", self.velocidad)

    def acelerar(self):
        self.velocidad += 40
        print("Acelerando en deportivo!!", self.velocidad)