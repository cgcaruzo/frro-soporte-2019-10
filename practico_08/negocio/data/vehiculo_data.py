# Implementar los metodos de la capa de datos de vehiculos.


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from practico_08.negocio.data.models.models import Base, Vehiculo

class DatosVehiculo(object):

    def __init__(self):
        engine = create_engine('sqlite:///delivery.db', connect_args={'check_same_thread':False})
        Base.metadata.bind = engine
        db_session = sessionmaker()
        db_session.bind = engine
        self.session = db_session()
        Base.metadata.create_all(engine)

    def buscar(self, id_vehiculo):
        """
        Devuelve la instancia del vehiculo, dado su id.
        Devuelve None si no encuentra nada.
        :rtype: Vehiculo
        """
        try:
            vehiculo = self.session.query(Vehiculo).filter_by(id=id_vehiculo).first()
            return vehiculo
        except:
            return None

    def buscar_patente(self, patente_vehiculo):
        """
        Devuelve la instancia del vehículo, dada una patente.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        try:
            vehiculos = self.session.query(Vehiculo).filter_by(patente=patente_vehiculo).first()
            return vehiculos
        except:
            return None

    def todos(self):
        """
        Devuelve listado de todos los vehiculos en la base de datos.
        :rtype: list
        """
        vehiculos = self.session.query(Vehiculo).all()
        return vehiculos

    def borrar_todos(self):
        """
        Borra todos los vehiculos de la base de datos.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        try:
            self.session.query(Vehiculo).delete()
            self.session.commit()
            return True
        except:
            return False

    def alta(self, vehiculo):
        """
        Devuelve el Vehiculo luego de darlo de alta.
        :type vehiculo: Vehiculo
        :rtype: Vehiculo
        """
        self.session.add(vehiculo)
        self.session.commit()
        return vehiculo

    def baja(self, id_vehiculo):
        """
        Borra el vehiculo especificado por el id.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        vehiculo = self.buscar(id_vehiculo)
        if vehiculo is None:
            return False
        else:
            try:
                self.session.delete(vehiculo)
                self.session.commit()
                return True
            except:
                return False

    def modificacion(self, vehiculo):
        """
        Guarda un vehiculo con sus datos modificados.
        Devuelve el Vehiculo modificado.
        :type vehiculo: Vehiculo
        :rtype: Vehiculo
        """
        v = self.buscar(vehiculo.id)
        v.nombre = vehiculo.nombre
        v.patente = vehiculo.patente
        v.capacidad = vehiculo.capacidad
        self.session.commit()
        return v

def pruebas():
    # alta
    datos = DatosVehiculo()
    datos.borrar_todos()
    vehiculo = datos.alta(Vehiculo(nombre='Kangoo001', patente='ABC123', capacidad=2000))
    assert vehiculo.id > 0

    # baja
    assert datos.baja(vehiculo.id) == True

    # buscar
    vehiculo_2 = datos.alta(Vehiculo(nombre='Kangoo002', patente='ABC321', capacidad=2200))
    assert datos.buscar(vehiculo_2.id) == vehiculo_2

    # modificacion
    vehiculo_3 = datos.alta(Vehiculo(nombre='Partner001', patente='ABC456', capacidad=1800))
    vehiculo_3.nombre = 'Partner007'
    vehiculo_3.patente = 'ABC457'
    vehiculo_3.capacidad = 1900
    datos.modificacion(vehiculo_3)
    vehiculo_3_modificado = datos.buscar(vehiculo_3.id)
    assert vehiculo_3_modificado.id == vehiculo_3.id
    assert vehiculo_3_modificado.nombre == 'Partner007'
    assert vehiculo_3_modificado.patente == 'ABC457'
    assert vehiculo_3_modificado.capacidad == 1900

    # todos
    assert len(datos.todos()) == 2

    # borrar todos
    #datos.borrar_todos()
    #assert len(datos.todos()) == 0


if __name__ == '__main__':
    pruebas()
