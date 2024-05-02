class silla:
    CLASE = {
        'eje':'Ejecutiva',
        'eco':'Economica'
    }
    UBICACION = {
        'ventana':'ventana',
        'centro':'centro',
        'pasillo':'pasillo'
    }

    def __init__(self,pNumero,pClase,pUbicacion):
        # self.__numero = pNumero
        # self.__clase = (self.CLASE[ "eje"], self.CLASE["eco"])[pClase]
        # # forma 2 ternarios 
        # # self.calse = self.CLASE.eco if pClase == 'economica' else self.CLASE.eje
        # if pUbicacion == "ventana":
        #     self.__Ubicacion = self.UBICACION["ventana"]
        # elif pUbicacion == "centro":
        #     self.__Ubicacion = self.UBICACION["centro"]
        # elif pUbicacion == "pasillo":
        #     self.__Ubicacion = self.UBICACION["pasillo"]
        # else:
        #     self.__Ubicacion = None

        self.__pasajero = None
        self.setNumero(pNumero)
        self.setClase(pClase)
        self.setUbicacion(pUbicacion)

    def asignarPasajero(self, pPasajero):
        self.__pasajero = pPasajero

    def desAsignar(self,):
        self.__numero = None
        self.__pasajero = None

    def sillaAsgnada(self):
        # return (False, True)[self.__numero is not None]
        return False if self.__numero == None else True
    
    def setNumero(self, pNumero):
        self.__numero = pNumero

    def getNumero(self):
        return self.__numero
    
    def getUbicacion(self):
        return self.__Ubicacion
    def setUbicacion(self,pUbicacion):
        if pUbicacion == "ventana":
            self.__Ubicacion = self.UBICACION["ventana"]
        elif pUbicacion == "centro":
            self.__Ubicacion = self.UBICACION["centro"]
        elif pUbicacion == "pasillo":
            self.__Ubicacion = self.UBICACION["pasillo"]
        else:
            self.__Ubicacion = None
    def getclase(self):
        return self.__clase
    def setclase(self,pClase):
        self.__clase = (self.CLASE[ "eje"], self.CLASE["eco"])[pClase]
    def getPasajero(self):
        return self.__pasajero
    