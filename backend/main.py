from fastapi import FastAPI

app = FastAPI() 

@app.get("/login")
async def read_root():
    return {"message": "¡Hola, mundo!"}