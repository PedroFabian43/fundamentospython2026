class Mascotas:

    def __init__(self):
        self.nombre = ""
        self.especie = ""
        self.nacimiento = 0
        self.adopcion = 0

    def getPerrera(self):
        return self.adopcion - self.nacimiento