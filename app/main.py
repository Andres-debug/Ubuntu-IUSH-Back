from fastapi import FastAPI
from app.api.routes.v1.endpoints import items
from app.api.routes.v1.endpoints import predictions
from app.db.session import engine
from app.db.base import Base

# Crear todas las tablas
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(items.router, prefix="/api/v1/items", tags=["items"])
app.include_router(predictions.router, prefix="/api/v1/predictions", tags=["Predictions"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI project!"}