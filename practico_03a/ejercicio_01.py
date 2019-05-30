# Implementar la funcion crear_tabla, que cree una tabla Persona con:
# - IdPersona: Int() (autoincremental)
# - Nombre: Char(30)
# - FechaNacimiento: Date()
# - DNI: Int()
# - Altura: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base() # Metadatos
engine = create_engine('sqlite:///mibase.db')
Base.metadata.bind = engine

DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

class Persona(Base):
    __tablename__ = 'Persona'
    IdPersona = Column(Integer, primary_key=True)
    Nombre = Column(String(30), nullable=False)
    FechaNacimiento = Column(String(19), nullable=False)
    DNI = Column(Integer)
    Altura = Column(Integer)

def crear_tabla():
 # Crea todas las tablas definidas en los metadatos
 Base.metadata.create_all(engine)

def borrar_tabla():
 # Crea todas las tablas definidas en los metadatos
 Persona.__table__.drop()

crear_tabla()
# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        #borrar_tabla()
    return func_wrapper
