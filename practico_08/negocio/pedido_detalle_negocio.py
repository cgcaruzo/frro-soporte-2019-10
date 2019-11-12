# Implementar los metodos de la capa de negocio de detalles.

from practico_08.negocio.data.models.models import PedidoDetalle
from practico_08.negocio.data.pedido_detalle_data import DatosPedidoDetalle


class LongitudInvalida(Exception):
    pass

class NegocioPedidoDetalle(object):
    MAX_CARACTERES = 100

    def __init__(self):
        self.datos = DatosPedidoDetalle()

    def buscar(self, id_detalle):
        """
        Devuelve la instancia del detalle, dado su id.
        Devuelve None si no encuentra nada.
        :rtype: PedidoDetalle
        """
        return self.datos.buscar(id_detalle)

    def buscar_pedido(self, pedido_id):
        """
        Devuelve la instancia del detalle, dado su id.
        Devuelve None si no encuentra nada.
        :rtype: PedidoDetalle
        """
        return self.datos.buscar_pedido(pedido_id)

    def todos(self):
        """
        Devuelve listado de todos los detalles.
        :rtype: list
        """
        return self.datos.todos()

    def alta(self, detalle):
        """
        Da de alta un detalle.
        Se deben validar las 3 reglas de negocio primero.
        Si no validan, levantar la excepcion correspondiente.
        Devuelve True si el alta fue exitoso.
        :type detalle: PedidoDetalle
        :rtype: bool
        """
        det = self.datos.alta(detalle)
        if det is not None:
            return True
        else:
            return False

    def baja(self, id_detalle):
        """
        Borra el detalle especificado por el id.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        return self.datos.baja(id_detalle)

    def modificacion(self, detalle):
        """
        Modifica un detalle.
        Se debe validar la regla 2 primero.
        Si no valida, levantar la excepcion correspondiente.
        Devuelve True si la modificacion fue exitosa.
        :type detalle: PedidoDetalle
        :rtype: bool
        """
        """
        try:
            self.regla_1(detalle)
        except LongitudInvalida as e:
            print(e.args)
            return False
"""
        self.datos.modificacion(detalle)
        return True

    def regla_1(self, detalle):
        """
        Validar la longitud de nombre y marca
        :type detalle: PedidoDetalle
        :raise: LongitudInvalida
        :return: bool
        """
        if (len(detalle.nombre) > self.MAX_CARACTERES or len(detalle.marca) > self.MAX_CARACTERES):
            raise LongitudInvalida('Longitud inválida')
            return False
        else:
            return True
