# Escribir una clase Estudiante, que herede de Persona, y que agregue las siguientes condiciones:
# Atributos:
# - nombre de la carrera.
# - año de ingreso a la misma.
# - cantidad de materias de la carrera.
# - cantidad de materias aprobadas.
# Métodos:
# - avance(): indica que porcentaje de la carrera tiene aprobada.
# - edad_ingreso(): indica que edad tenia al ingresar a la carrera (basándose en el año actual).
from datetime import datetime
from ejercicio_03 import Persona

class Estudiante(Persona):

    def __init__(self, carrera, anio, cantidad_materias, cantidad_aprobadas):
        self.carrera = carrera
        self.anio = anio
        self.cantidad_materias = cantidad_materias
        self.cantidad_aprobadas = cantidad_aprobadas

    def avance(self):
        print(self.cantidad_aprobadas *100 / self.cantidad_materias)

    # implementar usando modulo datetime
    def edad_ingreso(self):
        print(self.edad - (datetime.now().year - self.anio))
        pass

e = Estudiante('ISI', 2008, 35, 25)
e.edad = 25