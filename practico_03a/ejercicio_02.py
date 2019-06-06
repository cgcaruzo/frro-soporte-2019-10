# Implementar la funcion agregar_persona, que inserte un registro en la tabla Persona
# y devuelva los datos ingresados el id del nuevo registro.

import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from practico_03a.ejercicio_01 import Persona
from practico_03a.ejercicio_01 import reset_tabla

Base = declarative_base() # Metadatos
engine = create_engine('sqlite:///mibase.db')
Base.metadata.bind = engine

DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

def agregar_persona(nombre, nacimiento, dni, altura):
    persona = Persona()
    persona.Nombre = nombre
    persona.FechaNacimiento = nacimiento
    persona.DNI = dni
    persona.Altura = altura

    session.add(persona)
    session.commit()
    return persona.IdPersona

@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    id_marcela = agregar_persona('marcela gonzalez', datetime.datetime(1980, 1, 25), 12164492, 195)
    assert id_juan > 0
    assert id_marcela > id_juan

if __name__ == '__main__':
    pruebas()
