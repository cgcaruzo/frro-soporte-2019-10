# Implementar la funcion crear_tabla, que cree una tabla Persona con:
# - IdPersona: Int() (autoincremental)
# - Nombre: Char(30)
# - FechaNacimiento: Date()
# - DNI: Int()
# - Altura: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

import datetime
import sqlite3

def crear_tabla():
    db = sqlite3.connect('mibase')
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS Persona(IdPersona INTEGER PRIMARY KEY ASC, Nombre TEXT(30), FechaNacimiento TEXT(19), DNI INTEGER, Altura INTEGER)")
    db.commit()
    db.close()

def borrar_tabla():
    db = sqlite3.connect('mibase')
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS Persona")
    db.commit()
    db.close()


# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper