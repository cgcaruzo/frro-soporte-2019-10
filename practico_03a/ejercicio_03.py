# Implementar la funcion borrar_persona, que elimina un registro en la tabla Persona.
# Devuelve un booleano en base a si encontro el registro y lo borro o no.

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

def borrar_persona(id_persona):
    persona = session.query(Persona).filter_by(IdPersona=id_persona).first()
    if persona:
        session.delete(persona)
        session.commit()
        return True
    else:
        return False

@reset_tabla
def pruebas():
    idpersona=agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert borrar_persona(idpersona)
    assert borrar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
