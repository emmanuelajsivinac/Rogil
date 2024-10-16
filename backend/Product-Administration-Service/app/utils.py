'''main_utils'''
from .Conexion import SessionLocal

def get_db(): 
    try: 
        db = SessionLocal()
        yield db
    
    finally: 
        db.close()