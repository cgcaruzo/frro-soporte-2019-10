# Implementar los metodos de la capa de negocio de socios.

from practico_05.ejercicio_01 import Socio
from practico_05.ejercicio_02 import DatosSocio


class DniRepetido(Exception):
    pass


class LongitudInvalida(Exception):
    pass


class MaximoAlcanzado(Exception):
    pass


class NegocioSocio(object):

    MIN_CARACTERES = 3
    MAX_CARACTERES = 15
    MAX_SOCIOS = 200

    def __init__(self):
        self.datos = DatosSocio()

    def buscar(self, id_socio):
        """
        Devuelve la instancia del socio, dado su id.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        return self.datos.buscar(id_socio)

    def buscar_dni(self, dni_socio):
        """
        Devuelve la instancia del socio, dado su dni.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        return self.datos.buscar_dni(dni_socio)

    def todos(self):
        """
        Devuelve listado de todos los socios.
        :rtype: list
        """
        return self.datos.todos()

    def alta(self, socio):
        """
        Da de alta un socio.
        Se deben validar las 3 reglas de negocio primero.
        Si no validan, levantar la excepcion correspondiente.
        Devuelve True si el alta fue exitoso.
        :type socio: Socio
        :rtype: bool
        """
        try:
            self.regla_1(socio)
        except DniRepetido as e:
            print(e.args)
            return False

        try:
            self.regla_2(socio)
        except LongitudInvalida as e:
            print(e.args)
            return False

        try:
            self.regla_3()
        except MaximoAlcanzado as e:
            print(e.args)
            return False

        soc = self.datos.alta(socio)
        if soc is not None:
            return True
        else:
            return False

    def baja(self, id_socio):
        """
        Borra el socio especificado por el id.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        return self.datos.baja(id_socio)

    def modificacion(self, socio):
        """
        Modifica un socio.
        Se debe validar la regla 2 primero.
        Si no valida, levantar la excepcion correspondiente.
        Devuelve True si la modificacion fue exitosa.
        :type socio: Socio
        :rtype: bool
        """
        try:
            self.regla_2(socio)
        except LongitudInvalida as e:
            print(e.args)
            return False

        self.datos.modificacion(socio)
        return True

    def regla_1(self, socio):
        """
        Validar que el DNI del socio es unico (que ya no este usado).
        :type socio: Socio
        :raise: DniRepetido
        :return: bool
        """
        soc = self.datos.buscar_dni(socio.dni)
        if soc is not None:
            raise DniRepetido('DNI repetido')
            return False
        else:
            return True

    def regla_2(self, socio):
        """
        Validar que el nombre y el apellido del socio cuenten con mas de 3 caracteres pero menos de 15.
        :type socio: Socio
        :raise: LongitudInvalida
        :return: bool
        """
        if (len(socio.nombre) > self.MAX_CARACTERES or len(socio.nombre) < self.MIN_CARACTERES or len(socio.apellido) > self.MAX_CARACTERES or len(socio.apellido) < self.MIN_CARACTERES):
            raise LongitudInvalida('Longitud inválida')
            return False
        else:
            return True

    def regla_3(self):
        """
        Validar que no se esta excediendo la cantidad maxima de socios.
        :raise: MaximoAlcanzado
        :return: bool
        """
        cant = len(self.datos.todos())
        if cant >= self.MAX_SOCIOS:
            raise MaximoAlcanzado('Máximo alcanzado')
            return False
        else:
            return True
