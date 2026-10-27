from pydantic import BaseModel, StringConstraints, ConfigDict
from decimal import Decimal
from typing import Annotated
from datetime import datetime

class OrderCreate(BaseModel):
    user_id : int
    product_id : int
    quantity : int
    total_amount : Decimal
    status : str

class OrderResponse(BaseModel):
    id: int
    user_id : int
    product_id : int
    quantity : int
    total_amount : Decimal
    status: str
    created_at : datetime
    updated_at : datetime 

    model_config = ConfigDict(from_attributes=True)