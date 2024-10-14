from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()
print(f'mysql+pymysql://{os.getenv('USER_DB')}:{os.getenv('PASSWORD_DB')}@{os.getenv('HOST_DB')}:{os.getenv('PORT_DB')}/{os.getenv('DATABASE')}')

DB_URL = f'mysql+pymysql://{os.getenv('USER_DB')}:{os.getenv('PASSWORD_DB')}@{os.getenv('HOST_DB')}:{os.getenv('PORT_DB')}/{os.getenv('DATABASE')}'

engine = create_engine(DB_URL, connect_args={'charset':'utf8mb4'}, pool_pre_ping=True)

sesionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

baseDB = declarative_base()

class Database:
    def __init__(self):
        self.connection = sesionLocal()

    def get_connection(self):
        return self.connection
    
    def close(self):
        self.connection.close()

handlerDB = Database()