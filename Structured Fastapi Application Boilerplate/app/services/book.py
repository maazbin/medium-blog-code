from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.schemas.book import BookCreate, BookUpdate
from app.crud import book as crud

def get_all_books(db: Session):
    return crud.get_books(db)

def get_book_by_id(db: Session, book_id: int):
    book = crud.get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

def create_new_book(db: Session, book_data: BookCreate):
    return crud.create_book(db, book_data)

def update_existing_book(db: Session, book_id: int, updates: BookUpdate):
    book = crud.get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return crud.update_book(db, book, updates)

def delete_book_by_id(db: Session, book_id: int):
    book = crud.get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    crud.delete_book(db, book)
