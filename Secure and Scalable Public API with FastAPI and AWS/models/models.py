from sqlalchemy import Column, Integer, String, Text
from db.db import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)

class TranscriptionJob(Base):
    __tablename__ = "transcriptions"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    filename = Column(String, nullable=False)
    status = Column(String, default="pending")
    result = Column(Text, default=None)
