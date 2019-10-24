# Implementar los metodos de la capa de datos de productos.


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from practico_08.negocio.data.models.producto import Base, Producto

class DatosProducto(object):

    def __init__(self):
        engine = create_engine('sqlite:///delivery.db')
        Base.metadata.bind = engine
        db_session = sessionmaker()
        db_session.bind = engine
        self.session = db_session()
        Base.metadata.create_all(engine)

    def buscar(self, id_producto):
        """
        Devuelve la instancia del producto, dado su id.
        Devuelve None si no encuentra nada.
        :rtype: Producto
        """
        try:
            producto = self.session.query(Producto).filter_by(id=id_producto).first()
            return producto
        except:
            return None

    def todos(self):
        """
        Devuelve listado de todos los productos en la base de datos.
        :rtype: list
        """
        productos = self.session.query(Producto).all()
        return productos

    def borrar_todos(self):
        """
        Borra todos los productos de la base de datos.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        try:
            self.session.query(Producto).delete()
            self.session.commit()
            return True
        except:
            return False

    def alta(self, producto):
        """
        Devuelve el Producto luego de darlo de alta.
        :type producto: Producto
        :rtype: Producto
        """
        self.session.add(producto)
        self.session.commit()
        return producto

    def baja(self, id_producto):
        """
        Borra el producto especificado por el id.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        producto = self.buscar(id_producto)
        if producto is None:
            return False
        else:
            try:
                self.session.delete(producto)
                self.session.commit()
                return True
            except:
                return False

    def modificacion(self, producto):
        """
        Guarda un producto con sus datos modificados.
        Devuelve el Producto modificado.
        :type producto: Producto
        :rtype: Producto
        """
        p = self.buscar(producto.id)
        p.nombre = producto.nombre
        p.marca = producto.marca
        p.costo_kilo = producto.costo_kilo
        self.session.commit()
        return p

def pruebas():
    # alta
    datos = DatosProducto()
    datos.borrar_todos()
    producto = datos.alta(Producto(nombre='Maintenance Criadores Perro Adulto', marca='Natural', costo_kilo=135.55))
    assert producto.id > 0

    # baja
    assert datos.baja(producto.id) == True

    # buscar
    producto_2 = datos.alta(Producto(nombre='Old Prince Perro Adulto', marca='Catycan', costo_kilo=174.54))
    assert datos.buscar(producto_2.id) == producto_2

    # modificacion
    producto_3 = datos.alta(Producto(nombre='Alimento Balanceado Premium', marca='Tizano', costo_kilo=147.35))
    producto_3.nombre = 'Alimento Balanceado Premium'
    producto_3.marca = 'Dizano'
    producto_3.costo_kilo = 148.55
    datos.modificacion(producto_3)
    producto_3_modificado = datos.buscar(producto_3.id)
    assert producto_3_modificado.id == producto_3.id
    assert producto_3_modificado.nombre == 'Alimento Balanceado Premium'
    assert producto_3_modificado.marca == 'Dizano'
    assert producto_3_modificado.costo_kilo == 148.55

    # todos
    assert len(datos.todos()) == 2

    # borrar todos
    #datos.borrar_todos()
    #assert len(datos.todos()) == 0


if __name__ == '__main__':
    pruebas()
