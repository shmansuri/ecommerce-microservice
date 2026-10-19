from sqlalchemy import Column, Integer, DateTime, func
from sqlalchemy.orm import relationship
from app.core.database import Base


class Cart(Base):
    __tablename__='carts'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    user_id = Column(Integer, unique=True, index=True,  nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    items = relationship('CartItem', back_populates='cart', cascade='all, delete-orphan', passive_deletes=True, lazy='selectin'                     
)
