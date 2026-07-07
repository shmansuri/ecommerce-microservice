from sqlalchemy import Column, String, Float, Integer, Text,Boolean, Date
from app.core.database import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    phone = Column(String, unique=True, nullable=True)
    hashed_password = Column(String)
    is_active = Column(Boolean)
    is_varified = Column(Boolean)
    created_at = Column(Date)
    updated_at = Column(Date)