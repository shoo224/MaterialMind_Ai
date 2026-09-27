from fastapi import FastAPI

from db.database import Base, engine
from models.material import Material
from api.ingestion import router as ingestion_router


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="MaterialMind AI",
    version="1.0.0"
)


app.include_router(ingestion_router)


@app.get("/")
def root():
    return {
        "message": "MaterialMind AI API is running"
    }