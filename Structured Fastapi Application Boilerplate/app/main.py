from fastapi import FastAPI
from app.core.database import Base, engine
from app.api.v1.book import router as book_router

app = FastAPI(title="Book Catalog")

Base.metadata.create_all(bind=engine)

app.include_router(book_router)
