"""
Incident Intelligence Engine - Main Entrypoint
"""
import uvicorn
from fastapi import FastAPI
from src.api.routes import router as api_router
from src.utils.logger import setup_logging
import os

setup_logging()

app = FastAPI(title="Incident Intelligence Engine")
app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run("src.main:app", host=os.getenv("HOST", "0.0.0.0"), port=int(os.getenv("PORT", 8000)), reload=True)
