from class31coche import Coche
from class31deportivo import Deportivo
print("conduciendo")
depor = Deportivo()
print("Velocidad Máxima del deportivo", depor.getVelocidadMaxima())
depor.arrancar()
depor.acelerar()
depor.turbo()

car = Coche()
print("Velocidad Máxima del coche", car.getVelocidadMaxima())
car.marca = "Pontiac"
car.modelo = "Firebird"

print(car.marca + " " + car.modelo)
car.arrancar()
car.acelerar()
car.acelerar()
car.frenar()

