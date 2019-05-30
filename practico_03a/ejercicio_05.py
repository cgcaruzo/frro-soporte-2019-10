# Implementar la funcion actualizar_persona, que actualiza un registro de una persona basado en su id.
# Devuelve un booleano en base a si encontro el registro y lo actualizo o no.

import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from practico_03a.ejercicio_01 import Persona

from practico_03a.ejercicio_01 import reset_tabla
from practico_03a.ejercicio_02 import agregar_persona
from practico_03a.ejercicio_04 import buscar_persona

Base = declarative_base() # Metadatos
engine = create_engine('sqlite:///mibase.db')
Base.metadata.bind = engine

DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

def actualizar_persona(id_persona, nombre, nacimiento, dni, altura):
    persona = session.query(Persona).filter_by(IdPersona=id_persona).first()
    if persona:
        persona.Nombre = nombre
        persona.FechaNacimiento = nacimiento
        persona.DNI = dni
        persona.Altura = altura
        session.commit()
        return True
    else:
        return False


@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    actualizar_persona(id_juan, 'juan carlos perez', datetime.datetime(1988, 4, 16), 32165497, 181)
    assert buscar_persona(id_juan) == (1, 'juan carlos perez', str(datetime.datetime(1988, 4, 16)), 32165497, 181)
    assert actualizar_persona(123, 'nadie', datetime.datetime(1988, 4, 16), 12312312, 181) is False

if __name__ == '__main__':
    pruebas()
