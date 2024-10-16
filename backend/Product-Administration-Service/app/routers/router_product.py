'''router_product'''
from typing import List
 
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session 

from app import models, schemas
from app.utils import get_db

router = APIRouter(
    prefix= "/products",
    tags= ["Products"]
)

#obtener todos los productos
@router.get("/view_all_product", response_model=List[schemas.Producto])
def obtain_product(db: Session = Depends(get_db)): 
    product = db.query(models.Producto).all()
    return product

#obtener por nombre 
@router.get("/view_product_name/{name_product}", response_model=List[schemas.Producto])
def obtain_product_name(name_product: str, db:Session = Depends(get_db)):
    product = db.query(models.Producto).filter(
        models.Producto.nombre.ilike(f"%{name_product}%")).all()
    if not product: 
        raise HTTPException(status_code= 404, detail="No se encontraron productos con ese nombre"); 

    return product

#crear producto
@router.post("/insert_product/", response_model= schemas.Producto)
def create_product(product: schemas.ProductosBase, db: Session = Depends(get_db)):
    #crear una nueva instancia
    db_product = models.Producto(**product.dict())
    db.add(db_product) #agrega a la nueva instancia
    
    db.commit()
    db.refresh(db_product)
    return db_product

#actualizar producto 
@router.put("/update_product/{product_id}",response_model = None)
def update_product(product_id: int, upd_product: schemas.ProductosBase, db: Session = Depends(get_db)): 
    product = db.query(models.Producto).filter(
        models.Producto.id_producto == product_id).first()
    
    if product is None: 
        raise HTTPException(status=404, detail="Producto no encontrado")
    
    for key, value in upd_product.dict().items():
        setattr(product, key, value)

    db.commit()
    db.refresh(product)
    return product

#eliminar productos
@router.delete("/delete_product/{product_id}",response_model = schemas.Producto)
def delete_product(product_id: int, db: Session = Depends(get_db)): 
    product = db.query(models.Producto).filter(
        models.Producto.id_producto == product_id).first()
    
    if product is None: 
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    db.delete(product)
    db.commit()
    return product


