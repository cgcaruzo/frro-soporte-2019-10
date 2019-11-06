# Implementar los metodos de la capa de datos de pedidos.


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from practico_08.negocio.data.models.models import Base, Pedido

class DatosPedido(object):

    def __init__(self):
        engine = create_engine('sqlite:///delivery.db')
        Base.metadata.bind = engine
        db_session = sessionmaker()
        db_session.bind = engine
        self.session = db_session()
        Base.metadata.create_all(engine)

    def buscar(self, id_pedido):
        """
        Devuelve la instancia del pedido, dado su id.
        Devuelve None si no encuentra nada.
        :rtype: Pedido
        """
        try:
            pedido = self.session.query(Pedido).filter_by(id=id_pedido).first()
            return pedido
        except:
            return None

    def buscar_direccion_fecha(self, direccion_pedido, fecha_pedido):
        """
        Devuelve la instancia del socio, dado su dni.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        try:
            pedidos = self.session.query(Pedido).filter_by(direccion=direccion_pedido, fecha_entrega=fecha_pedido).first()
            return pedidos
        except:
            return None

    def todos(self):
        """
        Devuelve listado de todos los pedidos en la base de datos.
        :rtype: list
        """
        pedidos = self.session.query(Pedido).all()
        return pedidos

    def borrar_todos(self):
        """
        Borra todos los pedidos de la base de datos.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        try:
            self.session.query(Pedido).delete()
            self.session.commit()
            return True
        except:
            return False

    def alta(self, pedido):
        """
        Devuelve el Pedido luego de darlo de alta.
        :type pedido: Pedido
        :rtype: Pedido
        """
        self.session.add(pedido)
        self.session.commit()
        return pedido

    def baja(self, id_pedido):
        """
        Borra el pedido especificado por el id.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        pedido = self.buscar(id_pedido)
        if pedido is None:
            return False
        else:
            try:
                self.session.delete(pedido)
                self.session.commit()
                return True
            except:
                return False

    def modificacion(self, pedido):
        """
        Guarda un pedido con sus datos modificados.
        Devuelve el Pedido modificado.
        :type pedido: Pedido
        :rtype: Pedido
        """
        p = self.buscar(pedido.id)
        p.direccion = pedido.direccion
        p.fecha_carga = pedido.fecha_carga
        p.fecha_entrega = pedido.fecha_entrega
        self.session.commit()
        return p

def pruebas():
    # alta
    datos = DatosPedido()
    datos.borrar_todos()
    pedido = datos.alta(Pedido(direccion='Pellegrini 2201', fecha_carga='2019-10-05', fecha_entrega='2019-10-10'))
    assert pedido.id > 0

    # baja
    assert datos.baja(pedido.id) == True

    # buscar
    pedido_2 = datos.alta(Pedido(direccion='Pellegrini 2202', fecha_carga='2019-10-04', fecha_entrega='2019-10-10'))
    assert datos.buscar(pedido_2.id) == pedido_2

    # modificacion
    pedido_3 = datos.alta(Pedido(direccion='Zeballos 2120', fecha_carga='2019-10-06', fecha_entrega='2019-10-10'))
    pedido_3.direccion = 'Zeballos 2125'
    pedido_3.fecha_carga = '2019-10-07'
    pedido_3.fecha_entrega = '2019-10-09'
    datos.modificacion(pedido_3)
    pedido_3_modificado = datos.buscar(pedido_3.id)
    assert pedido_3_modificado.id == pedido_3.id
    assert pedido_3_modificado.direccion == 'Zeballos 2125'
    assert pedido_3_modificado.fecha_carga == '2019-10-07'
    assert pedido_3_modificado.fecha_entrega == '2019-10-09'

    # todos
    assert len(datos.todos()) == 2

    # borrar todos
    #datos.borrar_todos()
    #assert len(datos.todos()) == 0


if __name__ == '__main__':
    pruebas()
