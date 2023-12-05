import math
from Efectos import Efecto

class Poblacion:
    def __init__(self, tiempo, tasaCrecimiento): 
        self.__tiempo = tiempo
        self.__tasaCrecimiento = tasaCrecimiento
        self.__poblacionInicial = 2
        self.__efecto = None

    # Getters
    def getTiempo(self):
        return self.__tiempo
    def getTasaCrecimiento(self):
        return self.__tasaCrecimiento
    def getPoblacionInicial(self):
        return self.__poblacionInicial
    def getEfecto(self):
        return self.__efecto
    
    # Setters
    def setTiempo(self, tiempo):
        self.__tiempo = tiempo
    def setTasaCrecimiento(self, tasaCrecimiento):
        self.__tasaCrecimiento = tasaCrecimiento
    def setPoblacionInicial(self, poblacionInicial):
        self.__poblacionInicial = poblacionInicial
    def setEfecto(self, efecto):
        self.__efecto = efecto

    # Metodos
    def __str__(self):
        return f"Tiempo: {self.__tiempo},
        \nTasa de crecimiento: {self.__tasaCrecimiento}\nPoblacion inicial: {self.__poblacionInicial}"
    
    def simularCrecimiento(self, tasa = None, inicio = None, fin = None):
        if tasa is not None and inicio is not None and fin is not None:
            self.__efecto = Efecto(tasa, inicio, fin)
        poblacion = self.__poblacionInicial * math.exp(self.__tasaCrecimiento * self.__tiempo)
        poblacion = self.__efecto.calcularCrecimiento(poblacion, self.__tiempo)
        return round(poblacion)

    def mostrarPoblacion(self):
        return f"Despues de {self.__tiempo} meses, la poblacion sera de {self.simularCrecimiento()} habitantes"
    
# Main
    
# test = Poblacion(12, 0.8)
# print (test.mostrarPoblacion())
    
enfermedad = Efecto(-0.3, 0, 6)

poblacion = Poblacion(12, 0.7)

print(poblacion.simularCrecimiento(-0.3, 0, 6))