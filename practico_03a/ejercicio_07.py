# Implementar la funcion agregar_peso, que inserte un registro en la tabla PersonaPeso.
# Debe validar:
# - que el ID de la persona ingresada existe (reutilizando las funciones ya implementadas).
# - que no existe de esa persona un registro de fecha posterior al que queremos ingresar.

# Debe devolver:
# - ID del peso registrado.
# - False en caso de no cumplir con alguna validacion.

import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from practico_03a.ejercicio_02 import agregar_persona
from practico_03a.ejercicio_06 import reset_tabla, PersonaPeso
from practico_03a.ejercicio_04 import buscar_persona

Base = declarative_base()
engine = create_engine('sqlite:///mibase.db')
Base.metadata.bind = engine

DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

def agregar_peso(idPersona, fecha, peso):
    persona = buscar_persona(idPersona)
    if persona:
        r = session.query(PersonaPeso).filter(PersonaPeso.IdPersona == idPersona, PersonaPeso.Fecha > fecha).all()
        if r == []:
               personaP = PersonaPeso()
               personaP.IdPersona = idPersona
               personaP.Fecha = fecha
               personaP.Peso = peso
               session.add(personaP)
               session.commit()
               resultado = session.query(PersonaPeso).order_by(PersonaPeso.IdPeso).first()
               return resultado.IdPeso
        else:
              return False
    else:
        return False

@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 26), 80) > 0
    # id incorrecto
    assert agregar_peso(200, datetime.datetime(1988, 5, 15), 80) == False
    # registro previo al 2018-05-26
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 16), 80) == False

if __name__ == '__main__':
    pruebas()
