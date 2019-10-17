from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()
# [Vehículo]
# - id_vehiculo: integer (clave primaria, auto-incremental, único)
# - nombre: string (longitud 100)
# - patente: string (longitud 100)
# - capacidad: real