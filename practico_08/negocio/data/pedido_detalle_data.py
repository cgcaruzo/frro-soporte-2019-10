# Implementar los metodos de la capa de datos de pedido_detalle.


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from practico_08.negocio.data.models.models import Base, PedidoDetalle

class DatosPedidoDetalle(object):

    def __init__(self):
        engine = create_engine('sqlite:///delivery.db')
        Base.metadata.bind = engine
        db_session = sessionmaker()
        db_session.bind = engine
        self.session = db_session()
        Base.metadata.create_all(engine)

    def buscar(self, id_detalle):
        """
        Devuelve la instancia del detalle, dado su id.
        Devuelve None si no encuentra nada.
        :rtype: PedidoDetalle
        """
        try:
            detalle = self.session.query(PedidoDetalle).filter_by(id=id_detalle).first()
            return detalle
        except:
            return None

    def todos(self):
        """
        Devuelve listado de todos los pedido_detalle en la base de datos.
        :rtype: list
        """
        pedido_detalle = self.session.query(PedidoDetalle).all()
        return pedido_detalle

    def borrar_todos(self):
        """
        Borra todos los pedido_detalle de la base de datos.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        try:
            self.session.query(PedidoDetalle).delete()
            self.session.commit()
            return True
        except:
            return False

    def alta(self, detalle):
        """
        Devuelve el PedidoDetalle luego de darlo de alta.
        :type detalle: PedidoDetalle
        :rtype: PedidoDetalle
        """
        self.session.add(detalle)
        self.session.commit()
        return detalle

    def baja(self, id_detalle):
        """
        Borra el detalle especificado por el id.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        detalle = self.buscar(id_detalle)
        if detalle is None:
            return False
        else:
            try:
                self.session.delete(detalle)
                self.session.commit()
                return True
            except:
                return False

    def modificacion(self, detalle):
        """
        Guarda un detalle con sus datos modificados.
        Devuelve el PedidoDetalle modificado.
        :type detalle: PedidoDetalle
        :rtype: PedidoDetalle
        """
        d = self.buscar(detalle.id)
        d.pedido_id = detalle.pedido_id
        d.producto_id = detalle.producto_id
        d.cantidad = detalle.cantidad
        self.session.commit()
        return d
