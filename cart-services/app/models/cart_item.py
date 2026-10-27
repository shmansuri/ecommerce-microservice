from sqlalchemy import Column, Integer, DateTime, ForeignKey, String, Numeric, CheckConstraint, UniqueConstraint
from app.core.database import Base
from sqlalchemy.orm import relationship
from decimal import Decimal


class CartItem(Base):
    __tablename__ = "cart_items"
    __table_args__ = (
        UniqueConstraint(
            'cart_id',
            'product_id',
            name='uq_cart_product',
        ),
        CheckConstraint(
            'quantity > 0',
            name= 'check_cart_item_quantity',
        ),
    )

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    cart_id = Column(Integer, ForeignKey('carts.id', ondelete='CASCADE' ), nullable=False)
    product_id = Column(Integer, index=True, nullable=False)
    product_name = Column(String, nullable=False)
    quantity = Column(Integer, default=1, nullable=False)
    unit_price = Column(Numeric(10,2), nullable=False)

    cart = relationship('Cart', back_populates='items')