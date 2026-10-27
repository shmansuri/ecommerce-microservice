from pydantic import BaseModel, Field, ConfigDict
from typing import List
from datetime import datetime


class CartItemBase(BaseModel):
    product_id : int
    quantity : int = Field(gt=0, description='Quantity Should be greater than 0')

class AddItemRequest(BaseModel):
    product_name : str
    total_price : float = Field(gt=0, description='Total price should be greater than 0')

class UpdateQuantityRequest(BaseModel):
    quantity : int = Field(gt=0, description='Quantity must be greater than 0')


class CartItemResponse(BaseModel):

    model_config = ConfigDict(from_attributes=True)
    id : int
    cart_id : int
    product_id : int
    product_name : str
    quantity : int
    unit_price : float
    total_price : float
   

class CartResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id :int
    user_id : int
    items: List[CartItemResponse] = []
    total_amount : float
    created_at: datetime
    updated_at: datetime

