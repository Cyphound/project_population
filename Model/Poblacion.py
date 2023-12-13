import math
import time
from os import system

class Poblacion:
    def __init__(self, poblacion_inicial, tasa_crecimiento):
        """
        Inicializa la clase Poblacion con la población inicial y la tasa de crecimiento.

        Args:
        - poblacion_inicial (float): Población inicial.
        - tasa_crecimiento (float): Tasa de crecimiento.
        """
        self.poblacion = poblacion_inicial
        self.tasa_crecimiento = tasa_crecimiento

    def crecimiento_exponencial(self, tiempo):
        """
        Calcula el crecimiento exponencial de la población en función del tiempo.

        Args:
        - tiempo (float): Tiempo para el cual se calcula el crecimiento.

        Returns:
        - float: Crecimiento exponencial en el tiempo dado.
        """
        crecimiento = self.poblacion * math.exp(self.tasa_crecimiento * tiempo)
        return crecimiento

    def afectar_crecimiento(self, intensidad_enfermedad, tiempo_enfermedad, poblacion):
        """
        Afecta el crecimiento de la población debido a una enfermedad.

        Args:
        - intensidad_enfermedad (float): Intensidad de la enfermedad.
        - tiempo_enfermedad (float): Tiempo durante el cual la enfermedad afecta la población.
        - poblacion (float): Población actual.

        Returns:
        - float: Población afectada después de aplicar el factor de la enfermedad.
        """
        factor_enfermedad = math.exp(-intensidad_enfermedad * tiempo_enfermedad)
        self.poblacion = self.poblacion * factor_enfermedad
        return self.poblacion
    
# Main
    
# Cambia el valor de la variable estado a True para ejecutar el programa
estado = False

if estado:

    # Parámetros iniciales
    poblacion_inicial = 10
    tasa_crecimiento = 0.6
    intensidad_enfermedad = 0.3
    tiempo_enfermedad = 5
    tiempo_simulado = 10

    # Crear objeto de la clase Poblacion
    poblacion_obj = Poblacion(poblacion_inicial, tasa_crecimiento)

    # Calcular crecimiento exponencial para el primer mes
    crecimiento_simulado = poblacion_obj.crecimiento_exponencial(1)

    # Inicializar contador para el tiempo de enfermedad
    j = 1

    # Simulación del crecimiento poblacional
    for i in range(1, tiempo_simulado + 1):
        system("cls")  # Limpiar la consola
        print(f"Población después de {i} meses (crecimiento exponencial): {round(crecimiento_simulado)}")

        # Evitar la división por cero al incrementar i en el primer ciclo
        if i == 1: i += 1

        # Afectar el crecimiento debido a la enfermedad
        if j < tiempo_enfermedad:
            poblacion_obj.afectar_crecimiento(intensidad_enfermedad, j, crecimiento_simulado)
            print(f"Población afectada por enfermedad: {round(poblacion_obj.poblacion)}, después de {j} meses")
            j += 1

        # Calcular el crecimiento exponencial para el próximo mes
        crecimiento_simulado = poblacion_obj.crecimiento_exponencial(i)

        # Esperar 1 segundo antes de mostrar la siguiente iteración
        time.sleep(1)
