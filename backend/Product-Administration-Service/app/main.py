'''main'''
from fastapi import FastAPI
from app import models 
from .Conexion import engine 
from .routers import router_product, router_category, router_supplier, router_inventory, router_movement

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router_product.router)
app.include_router(router_category.router)
app.include_router(router_supplier.router)
app.include_router(router_inventory.router)
app.include_router(router_movement.router)