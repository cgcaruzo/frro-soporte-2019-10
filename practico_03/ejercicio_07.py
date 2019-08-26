# Implementar la funcion agregar_peso, que inserte un registro en la tabla PersonaPeso.
# Debe validar:
# - que el ID de la persona ingresada existe (reutilizando las funciones ya implementadas).
# - que no existe de esa persona un registro de fecha posterior al que queremos ingresar.

# Debe devolver:
# - ID del peso registrado.
# - False en caso de no cumplir con alguna validacion.

import sqlite3
import datetime

from practico_03.ejercicio_02 import agregar_persona
from practico_03.ejercicio_06 import reset_tabla
from practico_03.ejercicio_04 import buscar_persona


def agregar_peso(id_persona, fecha, peso):
    persona = buscar_persona(id_persona)
    if persona:
        db = sqlite3.connect('mibase')
        cursor = db.cursor()
        posterior = cursor.execute("SELECT IdPeso FROM PersonaPeso WHERE date(Fecha) > date(?)", (fecha,)).fetchone()
        if posterior:
            db.commit()
            db.close()
            return False
        else:
            cursor.execute("INSERT into PersonaPeso (IdPersona, Fecha, Peso) VALUES (?,?,?)", (id_persona, str(fecha), peso))
            db.commit()
            db.close()
            return cursor.lastrowid
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
