from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

# [Pedido]
# - id: integer (clave primaria, auto-incremental, único)
# - dirección: string (longitud 100)
# - fecha de carga: string (longitud 10)
# - fecha de entrega: string (longitud 10)
class Pedido(Base):
    __tablename__ = 'pedidos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    direccion = Column(String(100))
    fecha_carga = Column(String(10))
    fecha_entrega = Column(String(10))