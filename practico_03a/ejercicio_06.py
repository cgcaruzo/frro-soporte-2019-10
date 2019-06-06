# Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
# - IdPersona: Int() (Clave Foranea Persona)
# - Fecha: Date()
# - Peso: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from practico_03a.ejercicio_01 import Persona

from practico_03a.ejercicio_01 import borrar_tabla, crear_tabla

Base = declarative_base() # Metadatos
engine = create_engine('sqlite:///mibase.db')
Base.metadata.bind = engine

DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

class PersonaPeso(Base):
    __tablename__ = 'PersonaPeso'
    IdPeso = Column(Integer, primary_key=True)
    Fecha = Column(String(19), nullable=False)
    Peso = Column(Integer)
    IdPersona = Column(Integer, ForeignKey(Persona.IdPersona))
    personaP = relationship(Persona)

def crear_tabla_peso():
    Base.metadata.create_all(engine)

def borrar_tabla_peso():
    PersonaPeso.__table__.drop()

crear_tabla_peso()
# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper
