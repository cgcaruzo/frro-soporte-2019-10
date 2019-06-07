# Implementar la clase Persona que cumpla las siguientes condiciones:
# Atributos:
# - nombre.
# - edad.
# - sexo (H hombre, M mujer).
# - peso.
# - altura.
# Métodos:
# - es_mayor_edad(): indica si es mayor de edad, devuelve un booleano.
# - print_data(): imprime por pantalla toda la información del objeto.
# - generar_dni(): genera un número aleatorio de 8 cifras y lo guarda dentro del atributo dni.
from random import randint

class Persona:

    def __init__(self, nombre, edad, sexo, peso, altura):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.peso = peso
        self.altura = altura
        self.generar_dni()

    def es_mayor_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False

    # llamarlo desde __init__
    def generar_dni(self):
        self.dni = randint(00000000,99999999)

    def print_data(self):
        print(self.nombre,' ', self.edad, ' ', self.sexo, ' ', self.peso, ' ', self.altura, ' ', self.dni)
        pass

p = Persona('Roberto', 25, 'H', 80, 175)
h = Persona('Carla', 16, 'M', 65, 165)

assert(p.es_mayor_edad() == True)
assert(h.es_mayor_edad() == False)