from sqlalchemy import Column, ForeignKey, String, Integer, DateTime, Numeric, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base


class ProductVariant(Base):
    __tablename__ = 'product_variants'
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('products.id', ondelete='CASCADE'), nullable=False)
    sku = Column(String, unique=True, index=True)
    price = Column(Numeric(10,2), nullable=False)
    discount_price = Column(Numeric(10,2), nullable=True)
    stock = Column(Integer, default=0, nullable=False)
    attributes = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at =Column(DateTime, default=datetime.utcnow,onupdate=datetime.utcnow, nullable=False)
    product = relationship("Product", back_populates='variants')
