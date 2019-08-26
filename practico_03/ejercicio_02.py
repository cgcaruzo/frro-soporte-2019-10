# Implementar la funcion agregar_persona, que inserte un registro en la tabla Persona
# y devuelva los datos ingresados el id del nuevo registro.

import datetime
import sqlite3

from practico_03.ejercicio_01 import reset_tabla

def agregar_persona(nombre, nacimiento, dni, altura):
    db = sqlite3.connect('mibase')
    cursor = db.cursor()
    cSQL = "INSERT INTO Persona (Nombre, FechaNacimiento, DNI, Altura) VALUES (?,?,?,?)"
    tdatos = (nombre, str(nacimiento), dni, altura)
    cursor.execute(cSQL, tdatos)
    db.commit()
    db.close()

    return cursor.lastrowid

@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    id_marcela = agregar_persona('marcela gonzalez', datetime.datetime(1980, 1, 25), 12164492, 195)
    assert id_juan > 0
    assert id_marcela > id_juan

if __name__ == '__main__':
    pruebas()