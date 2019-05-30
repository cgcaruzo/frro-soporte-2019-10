# Implementar la funcion buscar_persona, que devuelve el registro de una persona basado en su id.
# El return es una tupla que contiene sus campos: id, nombre, nacimiento, dni y altura.
# Si no encuentra ningun registro, devuelve False.

import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from practico_03a.ejercicio_01 import Persona

from practico_03a.ejercicio_01 import reset_tabla
from practico_03a.ejercicio_02 import agregar_persona

Base = declarative_base() # Metadatos
engine = create_engine('sqlite:///mibase.db')
Base.metadata.bind = engine

DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

def buscar_persona(id_persona):
    persona = session.query(Persona).filter_by(IdPersona=id_persona).first()
    if persona:
        session.commit()
        print(persona)
        return (persona.IdPersona, persona.Nombre, persona.FechaNacimiento, persona.DNI, persona.Altura)
    else:
        session.commit()
        return False

@reset_tabla
def pruebas():
    juan = buscar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert juan == (1, 'juan perez', str(datetime.datetime(1988, 5, 15)), 32165498, 180)
    assert buscar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
