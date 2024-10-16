'''router_category'''
from typing import List

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app  import models, schemas
from app.utils import get_db

router = APIRouter(
    prefix="/category",
    tags=["Category"]
)

#obtener todas las categorias 
@router.get("view_category",response_model=List[schemas.Categoria])
def obtain_category(db: Session = Depends(get_db)): 
    category = db.query(models.Categoria).all()

    return category


#insertar categoria 
@router.post("/insert_category/",response_model= schemas.Categoria)
def create_category(category_p: schemas.CategoriaBase, db: Session = Depends(get_db)): 
    #nueva instancia 
    db_category = models.Categoria(**category_p.dict())
    db.add(db_category) #agregar la instancia
    
    db.commit()
    db.refresh(db_category)
    return db_category

#actualizar categoria
@router.put("/update_category/{category_id}", response_model= None)
def update_category(category_id: int, category_upd: schemas.CategoriaBase, db:Session = Depends(get_db)): 
    category_p = db.query(models.Categoria).filter(
        models.Categoria.id_categoria == category_id).first()
    if category_p is None: 
        raise HTTPException(status_code=404, detail="Categoria no encontrado")
    
    for key, value in category_upd.dict().items(): 
        setattr(category_p, key, value)

    db.commit()
    db.refresh(category_p)
    return category_p

#eliminar categoria 
@router.delete("/delete_category/{category_id}", response_model = schemas.Categoria)
def delete_category(category_id: int, db: Session = Depends(get_db)): 
    category_p = db.query(models.Categoria).filter(
        models.Categoria.id_categoria == category_id).first()
    
    if category_p is None: 
        raise HTTPException(status_code=404, detail="Categoria no encontrado")
    
    db.delete(category_p)
    db.commit()
    return category_p

    
