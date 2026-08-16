from pydantic import BaseModel, StringConstraints
from typing import Annotated
from datetime import datetime

class ProductImageCreate(BaseModel):
    product_id: int
    image_url : Annotated[str, StringConstraints(min_length=2, max_length=512)]
    is_primary : bool


class ProductImageResponse(BaseModel):
    id: int
    product_id: int
    image_url : str
    is_primary : bool
    created_at : datetime
    updated_at : datetime

class ProductImageUpdate(BaseModel):
    product_id : int | None = None
    image_url : Annotated[str | None, StringConstraints(min_length=2, max_length=512)] = None
    is_primary : bool | None = None

class productDictResponse(BaseModel):
    status : str
    message : str
    data: ProductImageResponse