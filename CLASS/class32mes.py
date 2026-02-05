class Mes:
    #Creamos el constructor init con las variables
    def __init__(self):
        self.nombre = ""
        self.tempMin = 0
        self.tempMax = 0

    def getTempMed(self):
        media = (self.tempMax + self.tempMin) / 2
        return media
    