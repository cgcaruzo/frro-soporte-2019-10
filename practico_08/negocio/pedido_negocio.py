# Implementar los metodos de la capa de negocio de pedidos.

from practico_08.negocio.data.models.models import Pedido
from practico_08.negocio.data.pedido_data import DatosPedido


class ExistePedido(Exception):
    pass

class NegocioPedido(object):

    def __init__(self):
        self.datos = DatosPedido()

    def buscar(self, id_pedido):
        """
        Devuelve la instancia del pedido, dado su id.
        Devuelve None si no encuentra nada.
        :rtype: Pedido
        """
        return self.datos.buscar(id_pedido)

    def todos(self):
        """
        Devuelve listado de todos los pedidos.
        :rtype: list
        """
        return self.datos.todos()

    def group_fecha_entrega(self):
        """
        Devuelve listado de todos los pedidos agrupados por fecha de entrega.
        :rtype: list
        """
        return self.datos.group_fecha_entrega()

    def buscar_fecha_entrega(self, fecha_entrega):
        """
        Devuelve listado de todos los pedidos agrupados por fecha de entrega.
        :rtype: list
        """
        return self.datos.buscar_fecha_entrega(fecha_entrega)

    def alta(self, pedido):
        """
        Da de alta un pedido.
        Se deben validar las 3 reglas de negocio primero.
        Si no validan, levantar la excepcion correspondiente.
        Devuelve True si el alta fue exitoso.
        :type pedido: Pedido
        :rtype: bool
        """
        try:
            self.regla_1(pedido)
        except ExistePedido as e:
            print(e.args)
            #return False
            return e.args

        ped = self.datos.alta(pedido)
        if ped is not None:
            return True
        else:
            return False

    def baja(self, id_pedido):
        """
        Borra el pedido especificado por el id.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        return self.datos.baja(id_pedido)

    def modificacion(self, pedido):
        """
        Modifica un pedido.
        Se debe validar la regla 2 primero.
        Si no valida, levantar la excepcion correspondiente.
        Devuelve True si la modificacion fue exitosa.
        :type pedido: Pedido
        :rtype: bool
        """
        try:
            self.regla_1(pedido)
        except ExistePedido as e:
            print(e.args)
            return False

        self.datos.modificacion(pedido)
        return True

    def regla_1(self, pedido):
        """
        Validar que no existan dos pedidos para la misma dirección para la misma fecha de entrega
        :type pedido: Pedido
        :raise: ExistePedido
        :return: bool
        """
        ped = self.datos.buscar_direccion_fecha(pedido.direccion, pedido.fecha_entrega)
        if ped is not None:
            raise ExistePedido('Ya existe un pedido para esa fecha de entrega')
        else:
            return True
