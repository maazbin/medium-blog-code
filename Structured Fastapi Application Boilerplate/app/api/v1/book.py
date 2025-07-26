from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.book import BookCreate, BookUpdate, BookOut
from app.services import book as service

router = APIRouter(prefix="/books", tags=["Books"])

@router.get("/", response_model=list[BookOut])
async def list_books(db: Session = Depends(get_db)):
    return service.get_all_books(db)

@router.get("/{book_id}", response_model=BookOut)
async def get_book(book_id: int, db: Session = Depends(get_db)):
    return service.get_book_by_id(db, book_id)

@router.post("/", response_model=BookOut)
async def create_book(book: BookCreate, db: Session = Depends(get_db)):
    return service.create_new_book(db, book)

@router.put("/{book_id}", response_model=BookOut)
async def update_book(book_id: int, book: BookUpdate, db: Session = Depends(get_db)):
    return service.update_existing_book(db, book_id, book)

@router.delete("/{book_id}", status_code=204)
async def delete_book(book_id: int, db: Session = Depends(get_db)):
    service.delete_book_by_id(db, book_id)
    return JSONResponse (
        status_code=204,
        content={"message" : "Book deleted successfully !"}
    )
