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
    costo_kilo = Column(REAL)

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