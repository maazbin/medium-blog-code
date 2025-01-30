from fastapi import FastAPI
from routers import transcription
from db.db import Base, engine

# Initialize DB
Base.metadata.create_all(bind=engine)

# FastAPI App
app = FastAPI()

# Include Routers
app.include_router(transcription.router, prefix="/api/v1", tags=["Transcription"])
