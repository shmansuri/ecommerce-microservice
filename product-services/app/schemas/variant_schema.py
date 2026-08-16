from pydantic import BaseModel, StringConstraints, Field
from typing import Annotated
from datetime import datetime
from pydantic import ConfigDict
from decimal import Decimal


class VariantCreate(BaseModel):
    product_id : int
    sku : Annotated[str, StringConstraints(min_length=2, max_length=100)]
    price: Decimal = Field(gt=0)
    discount_price: Decimal | None = Field(default=None, ge=0)
    stock: int = Field(default=0, ge=0)
    attributes: dict

class VariantResponse(BaseModel):
    id: int
    product_id: int
    sku : str
    price : Decimal 
    discount_price : Decimal | None = None
    stock : int 
    attributes : dict | None
    is_active : bool
    created_at : datetime
    updated_at : datetime

    model_config = ConfigDict(from_attributes=True)

class VariantUpdate(BaseModel):
    sku: Annotated[str | None, StringConstraints(min_length=2, max_length=100)] = None
    price: Decimal | None = Field(default=None, gt=0)
    discount_price: Decimal | None = Field(default=None, ge=0)
    stock: int | None = Field(default=None, ge=0)
    attributes: dict | None = None
    is_active: bool | None = None


class VariantDictResponse(BaseModel):
    status: str
    message : str
    data: VariantResponse