'''main_schemas'''

import enum 
from datetime import datetime, date
from typing import Optional
from pydantic import BaseModel 

# Products 

class ProductosBase(BaseModel): 
    nombre: str
    descripcion : Optional[str] = None 
    id_categoria: Optional[int] = None
    id_proveedor: Optional[int] = None
    activo: bool = True
    empleado: Optional[str] = None

class Producto(ProductosBase): 
    id_producto: int
    fecha_creacion: datetime
    class config: 
        from_attributes = True


#category 

class CategoriaBase(BaseModel): 
    nombre: str
    descripcion: Optional[str] = None

class Categoria(CategoriaBase): 
    id_categoria: int 

    class Config: 
        from_attributes = True 

#suppliers

class ProveedorBase(BaseModel): 
    nombre: str
    direccion: Optional[str]= None
    telefono: Optional[str]= None
    correo: Optional[str]
    contacto: Optional[str] = None

class Proveedor(ProveedorBase): 
    id_proveedor: int
    
    class Config: 
        from_attribute : True

class InventarioBase(BaseModel): 
    id_producto: int
    numero_lote: str 
    cantidad_stock: int 
    minimo_stock: int 
    precio_venta: float
    precio_compra: float 
    empleado: str 
    fecha_caducidad: date

class Inventario(InventarioBase): 
    id_inventario: int
    fecha_caducidad: datetime

    class Config: 
        from_attribute = True 

#Movimiento

class TipoMovimiento(str, enum.Enum):
    ENTRADA = "Entrada"
    SALIDA = "Salida"

class MovimientoBase(BaseModel):
    id_inventario: int
    tipo_movimiento: TipoMovimiento  # Debe ser el nombre que esperas en la respuesta
    cantidad: int
    empleado: Optional[str] = None

class MovimientoCreate(MovimientoBase):
    pass

class Movimiento(MovimientoBase):
    id_movimiento: int
    fecha_movimiento: datetime
    total: Optional[float] = None

    class Config:
        from_attribute = True