# Implementar los metodos de la capa de negocio de vehiculos.

from practico_08.negocio.data.models.models import Vehiculo
from practico_08.negocio.data.vehiculo_data import DatosVehiculo


class LongitudInvalida(Exception):
    pass

class ExistePatente(Exception):
    pass

class NegocioVehiculo(object):
    MAX_CARACTERES = 100

    def __init__(self):
        self.datos = DatosVehiculo()

    def buscar(self, id_vehiculo):
        """
        Devuelve la instancia del vehiculo, dado su id.
        Devuelve None si no encuentra nada.
        :rtype: Vehiculo
        """
        return self.datos.buscar(id_vehiculo)

    def todos(self):
        """
        Devuelve listado de todos los vehiculos.
        :rtype: list
        """
        return self.datos.todos()

    def alta(self, vehiculo):
        """
        Da de alta un vehiculo.
        Se deben validar las 2 reglas de negocio primero.
        Si no validan, levantar la excepcion correspondiente.
        Devuelve True si el alta fue exitoso.
        :type vehiculo: Vehiculo
        :rtype: bool
        """
        try:
            self.regla_1(vehiculo)
        except LongitudInvalida as e:
            print(e.args)
            return e.args

        try:
            self.regla_2(vehiculo)
        except ExistePatente as e:
            print(e.args)
            return e.args

        veh = self.datos.alta(vehiculo)
        if veh is not None:
            return True
        else:
            return False

    def baja(self, id_vehiculo):
        """
        Borra el vehiculo especificado por el id.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        return self.datos.baja(id_vehiculo)

    def modificacion(self, vehiculo):
        """
        Modifica un vehiculo.
        Se debe validar la regla 1 y 2 primero.
        Si no valida, levantar la excepcion correspondiente.
        Devuelve True si la modificacion fue exitosa.
        :type vehiculo: Vehiculo
        :rtype: bool
        """
        try:
            self.regla_1(vehiculo)
        except LongitudInvalida as e:
            print(e.args)
            return e.args

        self.datos.modificacion(vehiculo)
        return True

    def regla_1(self, vehiculo):
        """
        Validar la longitud de nombre y patente
        :type vehiculo: Vehiculo
        :raise: LongitudInvalida
        :return: bool
        """
        if (len(vehiculo.nombre) > self.MAX_CARACTERES or len(vehiculo.patente) > self.MAX_CARACTERES):
            raise LongitudInvalida('Longitud inválida')
        else:
            return True

    def regla_2(self, vehiculo):
        """
        Validar que no existan dos vehiculos con la misma patente
        :type vehiculo: Vehiculo
        :raise: ExisteVehiculo
        :return: bool
        """
        veh = self.datos.buscar_patente(vehiculo.patente)
        if veh is not None:
            raise ExistePatente('Ya existe un vehículo con la patente ingresada')
        else:
            return True
