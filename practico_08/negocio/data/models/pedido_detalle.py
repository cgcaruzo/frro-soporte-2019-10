from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, REAL

Base = declarative_base()

# [PedidoDetalle]
# - id: integer (clave primaria, auto-incremental, único)
# - pedido_id: integer (clave foranea a Pedido)
# - producto_id: integer (clave foranea a Producto)
# - cantidad: real
class PedidoDetalle(Base):
    __tablename__ = 'pedidos_detalles'
    id = Column(Integer, primary_key=True, autoincrement=True)
    pedido_id = Column(Integer)
    producto_id = Column(Integer)
    cantidad = Column(REAL)