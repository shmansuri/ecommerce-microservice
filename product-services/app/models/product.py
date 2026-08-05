from sqlalchemy import Column, String, Boolean, Text, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Numeric
from app.core.database import Base
from datetime import datetime


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    category_id = Column(Integer, ForeignKey("categories.id", ondelete="CASCADE"), nullable=False)
    name = Column(String(100), nullable=False)
    slug = Column(String, unique=True, index=True, nullable=False)
    description = Column(Text, nullable=False)
   
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime,  default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    category = relationship('Category', back_populates='products')
    variants = relationship("ProductVariant", back_populates='product', cascade='all, delete-orphan')
    images = relationship("ProductImage", back_populates='product', cascade='all, delete-orphan')