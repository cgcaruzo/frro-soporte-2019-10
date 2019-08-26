# Implementar la funcion borrar_persona, que elimina un registro en la tabla Persona.
# Devuelve un booleano en base a si encontro el registro y lo borro o no.

import datetime
import sqlite3

from practico_03.ejercicio_01 import reset_tabla
from practico_03.ejercicio_02 import agregar_persona


def borrar_persona(id_persona):
    db = sqlite3.connect('mibase')
    cursor = db.cursor()
    sel = cursor.execute("SELECT IdPersona FROM Persona WHERE IdPersona = ?",(id_persona,))
    persona = sel.fetchone()
    if persona:
        dSQL = "DELETE FROM Persona WHERE IdPersona = ?"
        res = cursor.execute(dSQL,(id_persona,))
        db.commit()
        db.close()
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
