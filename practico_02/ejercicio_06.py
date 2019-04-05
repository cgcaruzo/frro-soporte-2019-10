# Implementar la clase Persona con un constructor donde reciba una fecha de nacimiento.
# La clase además debe contener un método edad, que no recibe nada y devuelva la edad de la
# persona (entero).
# Para obtener la fecha actual, usar el método de clase "now" de la clase datetime (ya importada).

from datetime import datetime
class Persona:

    # nacimiento es un objeto datetime.datetime
    def __init__(self, nacimiento):
        self.nacimiento = nacimiento

    def edad(self):
        hoy = datetime.now()
        edad = hoy.year - self.nacimiento.year
        if hoy.month < self.nacimiento.month:
            diferencia = 1
        elif hoy.month > self.nacimiento.month:
            diferencia = 0
        else:
            if hoy.day < self.nacimiento.day:
                diferencia = 1
            else:
                diferencia = 0

        edad = edad - diferencia

        return edad

nac = datetime.strptime('May 19 1990  1:33PM', '%b %d %Y %I:%M%p')
p = Persona(nac)
assert(p.edad() == 28)


