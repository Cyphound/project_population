# Cuando se creo este codigo, yo y Dios sabiamos como funcionaba
# Ahora solo Dios lo sabe, asi que aumenta el contador si no lo haces funcionar.
# Intentos Fallidos: 1

import math

class Efecto:
    def __init__(self, valor, inicio, fin):
        self.__valor = valor
        self.__inicio = inicio
        self.__fin = fin

    # Getters
    def getValor(self):
        return self.__valor
    def getInicio(self):
        return self.__inicio
    def getFin(self):
        return self.__fin
    
    # Setters
    def setValor(self, valor):
        self.__valor = valor
    def setInicio(self, inicio):
        self.__inicio = inicio
    def setFin(self, fin):
        self.__fin = fin

    # Metodos
    def calcularCrecimiento(self, poblacion, tiempo):
        if tiempo < self.__inicio:
            return poblacion
        elif tiempo > self.__fin:
            return poblacion
        else:
            # La enfermedad disminuye la población a un ritmo de valor/mes
            return poblacion * math.exp(tiempo * self.__valor)


