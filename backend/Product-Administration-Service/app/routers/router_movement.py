'''router_movement'''
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app import models, schemas 
from app.utils import get_db

router = APIRouter(
    prefix= "/movement", 
    tags= ["Movement"]
)


@router.post("/movement/", response_model=schemas.Movimiento)
def create_movement(movement: schemas.MovimientoCreate, db: Session = Depends(get_db)):
    # Verificar si el inventario existe
    inventory = db.query(models.Inventario).filter(models.Inventario.id_inventario == movement.id_inventario).first()

    if not inventory:
        raise HTTPException(status_code=404, detail="Inventario no encontrado")

    # verifica si lo solicitado supera el minimo stock
    if movement.tipo_movimiento == schemas.TipoMovimiento.SALIDA:
        if inventory.cantidad_stock - movement.cantidad < inventory.minimo_stock:
            raise HTTPException(status_code=400, detail="No se puede realizar la salida, supera el minimo stock")

    # actualiza el stock
    if movement.tipo_movimiento == schemas.TipoMovimiento.ENTRADA:
        inventory.cantidad_stock += movement.cantidad
    elif movement.tipo_movimiento == schemas.TipoMovimiento.SALIDA:
        inventory.cantidad_stock -= movement.cantidad

    # Crear el registro del movimiento
    new_movement = models.Movimiento(
        id_inventario=movement.id_inventario,
        tipo_movimiento=movement.tipo_movimiento,  # Debe ser tipo_movimiento aquí
        cantidad=movement.cantidad,
        empleado=movement.empleado,
        total=inventory.precio_venta * movement.cantidad
    )

    db.add(new_movement)
    db.commit()
    db.refresh(new_movement)

    return new_movement  

@router.delete("/delete_movement/{id_movement}", response_model = schemas.Movimiento)
def delete_inventory_movement(id_movement: int, db: Session = Depends(get_db)): 

    inventory_movement = db.query(models.Movimiento).filter(
        models.Movimiento.id_movimiento == id_movement).first()
    
    if not inventory_movement: 
        raise HTTPException(status_code=404, detail= "Movimiento no encontrado")

    inventory = db.query(models.Inventario).filter(
        models.Inventario.id_inventario == inventory_movement.id_inventario).first()
    
    if not inventory: 
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    if inventory_movement.tipo_movimiento == schemas.TipoMovimiento.ENTRADA:
        inventory.cantidad_stock -= inventory_movement.cantidad
    
    elif inventory_movement.tipo_movimiento == schemas.TipoMovimiento.SALIDA: 
        inventory.cantidad_stock += inventory_movement.cantidad

    db.delete(inventory_movement)
    db.commit()

    return inventory_movement