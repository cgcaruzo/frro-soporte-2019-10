from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, REAL

Base = declarative_base()

# [Producto]
# - id: integer (clave primaria, auto-incremental, único)
# - nombre: string (longitud 100)
# - marca: string (longitud 100)
# - costo x peso: real
class Producto(Base):
    __tablename__ = 'productos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100))
    marca = Column(String(100))
    costo_unitario = Column(REAL)