from silla import silla
class avion:
    SILLASEJECUTIVAS = 8
    SILLASECONOMICAS = 42

    def __init__(self):
        self.sillasEjecutivas = []
        self.sillasEconomicas = []
        
        self.asosiacionsillasejecutivas

    def asosiacionsillasejecutivas(self):
        for i in range(self.SILLASEJECUTIVAS):
            if ((i+1)%2)==0:
                self.sillasEjecutivas.append(silla((i+1), False, "pasillo"))
            else:
                self.sillasEjecutivas.append(silla((i+1), False, "ventana"))

    def asosiacionSillasEconomicas(self):
        for i in range(self.SILLASECONOMICAS):
            if i % 3 == 1:
                self.sillasEconomicas.append(silla((i+1), True, "centro"))
            elif i % 3 == 2:
                self.sillasEconomicas.append(silla((i+1), True, "pasillo"))
            else:
                self.sillasEconomicas.append(silla((i+1), True, "ventana"))
