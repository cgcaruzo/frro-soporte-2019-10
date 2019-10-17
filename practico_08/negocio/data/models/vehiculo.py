from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, REAL

Base = declarative_base()
# [Vehículo]
# - id: integer (clave primaria, auto-incremental, único)
# - nombre: string (longitud 100)
# - patente: string (longitud 100)
# - capacidad: real
class Vehiculo(Base):
    __tablename__ = 'vehiculos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100))
    patente = Column(String(100))
    capacidad = Column(REAL)