from pydantic import BaseModel, StringConstraints, Field
from typing import Annotated
from datetime import datetime
from pydantic import ConfigDict


class VariantCreate(BaseModel):
    product_id : int
    sku : Annotated[str, StringConstraints(min_length=2, max_length=100)]
    price : float = Field(gt=0)
    discount_price : float | None=Field(default=None, ge=0)
    stock : int = Field(ge=0)
    attributes : str
    is_active : bool | None = None

class VariantResponse(BaseModel):
    id: int
    product_id: int
    sku : str
    price : float 
    discount_price : float | None = None
    stock : int 
    attributes : str
    is_active : bool
    created_at : datetime
    updated_at : datetime

    model_config = ConfigDict(from_attributes=True)


class VariantUpdate(BaseModel):
    product_id: int | None = None
    sku : Annotated[str | None, StringConstraints(min_length=2, max_length=100)] = None
    price : float | None = Field(default=None, gt=0)
    discount_price : float | None = Field(default=None, ge=0)
    stock : int | None = Field(default=None, ge=0)
    attributes : str | None = None
    is_active : bool | None = None