from pydantic import BaseModel, Field

class BookBase(BaseModel):
    title: str
    author: str
    published_year: int = Field(..., ge=1, le=2025)
    summary: str | None = None

class BookCreate(BookBase):
    pass

class BookUpdate(BookBase):
    pass

class BookOut(BookBase):
    id: int

    class Config:
        orm_mode = True
