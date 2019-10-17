from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.Producto import Base, Producto


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
    producto = datos.alta(Producto(nombre='Pedigree', marca='Grande', costo_kilo=135))
    assert producto.id > 0

    # baja
    assert datos.baja(producto.id) == True

    # buscar
    producto_2 = datos.alta(Producto(nombre='Comida para perro', marca='Fijand', costo_kilo=140))
    assert datos.buscar(producto_2.id) == producto_2



    # modificacion
    producto_3 = datos.alta(Producto(nombre='Susana', marca='Gimenez'))
    producto_3.nombre = 'Moria'
    producto_3.marca = 'Casan'
    datos.modificacion(producto_3)
    producto_3_modificado = datos.buscar(producto_3.id)
    assert producto_3_modificado.id == producto_3.id
    assert producto_3_modificado.nombre == 'Moria'
    assert producto_3_modificado.marca == 'Casan'

    # todos
    assert len(datos.todos()) == 2

    # borrar todos
    datos.borrar_todos()
    assert len(datos.todos()) == 0


if __name__ == '__main__':
    pruebas()
