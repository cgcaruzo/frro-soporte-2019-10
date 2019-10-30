# Implementar los metodos de la capa de negocio de productos.

from practico_08.negocio.data.models.models import Producto
from practico_08.negocio.data.producto_data import DatosProducto


class LongitudInvalida(Exception):
    pass

class NegocioProducto(object):
    MAX_CARACTERES = 100

    def __init__(self):
        self.datos = DatosProducto()

    def buscar(self, id_producto):
        """
        Devuelve la instancia del producto, dado su id.
        Devuelve None si no encuentra nada.
        :rtype: Producto
        """
        return self.datos.buscar(id_producto)

    def todos(self):
        """
        Devuelve listado de todos los productos.
        :rtype: list
        """
        return self.datos.todos()

    def alta(self, producto):
        """
        Da de alta un producto.
        Se deben validar las 3 reglas de negocio primero.
        Si no validan, levantar la excepcion correspondiente.
        Devuelve True si el alta fue exitoso.
        :type producto: Producto
        :rtype: bool
        """
        try:
            self.regla_1(producto)
        except LongitudInvalida as e:
            print(e.args)
            return False

        prod = self.datos.alta(producto)
        if prod is not None:
            return True
        else:
            return False

    def baja(self, id_producto):
        """
        Borra el producto especificado por el id.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        return self.datos.baja(id_producto)

    def modificacion(self, producto):
        """
        Modifica un producto.
        Se debe validar la regla 2 primero.
        Si no valida, levantar la excepcion correspondiente.
        Devuelve True si la modificacion fue exitosa.
        :type producto: Producto
        :rtype: bool
        """
        try:
            self.regla_1(producto)
        except LongitudInvalida as e:
            print(e.args)
            return False

        self.datos.modificacion(producto)
        return True

    def regla_1(self, producto):
        """
        Validar la longitud de nombre y marca
        :type producto: Producto
        :raise: LongitudInvalida
        :return: bool
        """
        if (len(producto.nombre) > self.MAX_CARACTERES or len(producto.marca) > self.MAX_CARACTERES):
            raise LongitudInvalida('Longitud inválida')
            return False
        else:
            return True
