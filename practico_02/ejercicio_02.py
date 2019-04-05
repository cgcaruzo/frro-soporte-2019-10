# Implementar la clase Circulo que contiene un radio, y sus métodos area y perimetro.
from math import pi

class Circulo:

    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return pi*self.radio*self.radio

    def perimetro(self):
        return 2*pi*self.radio

c = Circulo(3)
assert(c.area() == pi*3*3)
assert(c.perimetro() == 2*pi*3)
