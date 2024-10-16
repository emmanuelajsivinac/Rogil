'''router_inventory'''
from typing import List 

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app import models, schemas 
from app.utils import get_db

router = APIRouter(
    prefix= "/inventory", 
    tags= ["Inventory"]
)

#obtener todo el inventario
@router.get("/view_all_inventory", response_model=List[schemas.Inventario])
def obtain_inventory(db: Session = Depends(get_db)): 
    inventory = db.query(models.Inventario).all()
    return inventory

#crear inventario 
@router.post("/create_inventory/", response_model= schemas.Inventario)
def create_inventory(inventory: schemas.InventarioBase, db: Session = Depends(get_db)):
    #crear nueva instancia 
    db_inventory = models.Inventario(**inventory.dict())
    db.add(db_inventory) # agrega a la nueva instancia

    db.commit()
    db.refresh(db_inventory)
    return db_inventory

#actualizar inventario 
@router.put("/update_inventory/{inventory_id}", response_model= None)
def update_product(inventory_id: int, upd_inventory: schemas.InventarioBase, db: Session = Depends(get_db)): 
    inventory = db.query(models.Inventario).filter(
        models.Inventario.id_inventario == inventory_id).first()
    
    if inventory is None: 
        raise HTTPException(status_code=404, detail="Inventario no encontrado")
    
    for key, value in upd_inventory.dict().items():
        setattr(inventory, key, value)

    db.commit()
    db.refresh(inventory)
    return inventory

#eliminar productos 
@router.delete("/delete_inventory/{inventory_id}", response_model= schemas.Inventario)
def delete_inventory(inventory_id: int, db: Session = Depends(get_db)):
    inventory = db.query(models.Inventario).filter(
        models.Inventario.id_inventario == inventory_id).first()
    
    if inventory is None: 
        raise HTTPException(status_code=404, detail="Inventario no encontrado")
    
    db.delete(inventory)
    db.commit()
    return inventory