# Implementar la funcion buscar_persona, que devuelve el registro de una persona basado en su id.
# El return es una tupla que contiene sus campos: id, nombre, nacimiento, dni y altura.
# Si no encuentra ningun registro, devuelve False.

import datetime
import sqlite3

from practico_03.ejercicio_01 import reset_tabla
from practico_03.ejercicio_02 import agregar_persona


def buscar_persona(id_persona):
    db = sqlite3.connect('mibase')
    cursor = db.cursor()
    sel = cursor.execute("SELECT IdPersona, Nombre, FechaNacimiento, DNI, Altura FROM Persona WHERE IdPersona = ?",(id_persona,))
    persona = sel.fetchone()
    db.commit()
    db.close()
    if persona:
        return persona
    else:
        return False


@reset_tabla
def pruebas():
    juan = buscar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert juan == (1, 'juan perez', str(datetime.datetime(1988, 5, 15)), 32165498, 180)
    assert buscar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
