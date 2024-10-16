'''main_models'''

import enum
from sqlalchemy import Column, Integer, String, DECIMAL,Text, DATE, BOOLEAN, ForeignKey, TIMESTAMP
from sqlalchemy.types import Enum as SQLALchemyEnum 
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .Conexion import Base

class TipoMovimiento(str, enum.Enum): 
   ENTRADA = "Entrada"
   SALIDA = "Salida"

class Categoria(Base): 

   __tablename__ = 'categorias' 

   id_categoria = Column(Integer, primary_key= True, autoincrement= True, index= True)
   nombre = Column(String(255),nullable=False)
   descripcion = Column(Text,nullable=True)

   producto = relationship("Producto", back_populates= "categoria")


class Proveedor(Base): 
   __tablename__ = 'proveedores'

   id_proveedor = Column(Integer, primary_key=True,autoincrement= True, index= True)
   nombre = Column(String(255),nullable=False)
   direccion = Column(Text, nullable=True)
   telefono = Column(String(20), nullable= True)
   correo= Column(String(255), nullable= True)
   contacto = Column(String(255), nullable= True)

   producto = relationship("Producto", back_populates= "proveedor")

class Producto(Base): 
   __tablename__ = 'productos'

   id_producto = Column(Integer, primary_key=True, autoincrement= True, index= True)
   nombre = Column(String(100), nullable=False)
   descripcion = Column(Text, nullable= True)
   id_categoria = Column(Integer, ForeignKey("categorias.id_categoria"), nullable=True)
   id_proveedor = Column(Integer, ForeignKey("proveedores.id_proveedor"), nullable=True)    
   activo = Column(BOOLEAN, default=True)
   fecha_creacion = Column(TIMESTAMP, server_default=func.current_timestamp()) 
   empleado = Column(String(100), nullable=True)

   #relationship
   categoria = relationship("Categoria", back_populates= "producto")
   proveedor = relationship("Proveedor", back_populates= "producto")
   inventario = relationship("Inventario", back_populates="producto")

class Inventario(Base): 
   __tablename__ = 'inventarios'

   id_inventario = Column(Integer, primary_key=True, autoincrement= True, index= True)
   id_producto = Column(Integer, ForeignKey("productos.id_producto"), nullable= True)
   numero_lote = Column(String(50), nullable= False)
   cantidad_stock = Column(Integer, nullable= False)
   minimo_stock = Column(Integer, nullable= False)
   precio_venta = Column(DECIMAL(10,2),nullable=False)
   precio_compra = Column(DECIMAL(10,2),nullable=False)
   empleado = Column(String(100), nullable=True)
   fecha_caducidad = Column(DATE, nullable=False)
   fecha_creacion = Column(TIMESTAMP, server_default=func.current_timestamp())


   producto = relationship("Producto", back_populates= "inventario")
   movimiento = relationship("Movimiento", back_populates= "inventario")
   liquidacion = relationship("Liquidacion", back_populates= "inventario")


class Movimiento(Base): 
   __tablename__ = 'movimientos'

   id_movimiento = Column(Integer, primary_key=True, autoincrement=True, index=True)
   id_inventario = Column(Integer, ForeignKey("inventarios.id_inventario"), nullable=False)
   tipo_movimiento = Column(SQLALchemyEnum(TipoMovimiento), nullable=False) 
   cantidad = Column(Integer, nullable=False)
   total = Column(DECIMAL(10,2), nullable=True)
   empleado = Column(String(100), nullable=True) 
   fecha_movimiento = Column(TIMESTAMP, server_default=func.current_timestamp())

   inventario = relationship("Inventario", back_populates= "movimiento")

class Liquidacion(Base): 
   
   __tablename__ = 'liquidaciones'

   id_liquidacion = Column(Integer, primary_key=True, autoincrement=True, index=True)
   id_inventario = Column(Integer, ForeignKey("inventarios.id_inventario"), nullable=False)
   cantidad = Column(Integer, nullable=False)
   precio_unidad = Column(DECIMAL(10,2),nullable=False)
   total = Column(DECIMAL(10,2), nullable=True)
   empleado = Column(String(100), nullable=True)
   fecha_liquidacion = Column(TIMESTAMP, server_default=func.current_timestamp()) 

   inventario = relationship("Inventario", back_populates= "liquidacion")