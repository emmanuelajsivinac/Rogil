'''Routers_Suppliers'''
from typing import List

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app import models, schemas
from app.utils import get_db

router = APIRouter(
  prefix="/suppliers",
  tags=["Suppliers"]
)

# obtener Proveedor
@router.get("/viell_all_suppliers/", response_model= List[schemas.Proveedor])
def view_suppliers(db: Session = Depends(get_db)):
  suppliers_p = db.query(models.Proveedor).all()
  return suppliers_p

# insertar Proveedor
@router.post("/insert_suppliers/", response_model=schemas.Proveedor)
def create_suppliers(suppliers_p: schemas.ProveedorBase, db: Session = Depends(get_db)): 
  #crear instancia 
  db_suppliers = models.Proveedor(**suppliers_p.dict())
  db.add(db_suppliers) #agregar la nueva instancia
  db.commit()
  db.refresh(db_suppliers)
  return db_suppliers

#actualizar Proveedor
@router.put("/update_suppliers/{suppliers_id}", response_model=None)
def update_suppliers(suppliers_id: int, proveedor_actualizado: schemas.ProveedorBase, db: Session = Depends(get_db)):
    suppliers_p = db.query(models.Proveedor).filter(
        models.Proveedor.id_proveedor == suppliers_id).first()
    if suppliers_p is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    for key, value in proveedor_actualizado.dict().items():
        setattr(suppliers_p, key, value)

    db.commit()
    db.refresh(suppliers_p)
    return suppliers_p

# eliminar Proveedor
@router.delete("/delete_suppliers/{suppliers_id}", response_model=schemas.Proveedor)
def delete_suppliers(suppliers_id: int, db: Session = Depends(get_db)):
    suppliers_p = db.query(models.Proveedor).filter(
        models.Proveedor.id_proveedor == suppliers_id).first()
    if suppliers_p is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    db.delete(suppliers_p)
    db.commit()
    return suppliers_p