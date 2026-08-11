from pydantic import StringConstraints, BaseModel, ConfigDict
from typing import Annotated
from datetime import datetime

class ProductCreate(BaseModel):
    category_id: int
    name : Annotated[str, StringConstraints(min_length=2, max_length=100)]
    slug: Annotated[str, StringConstraints(min_length=2, max_length=200)]
    description: Annotated[str, StringConstraints(min_length=10, max_length=300)]




class ProductResponse(BaseModel):
    id:int
    category_id: int
    name:str
    slug:str
    description:str
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ProductUpdate(BaseModel):
    id:int | None = None
    category_id: int | None = None
    name : Annotated[str | None, StringConstraints(min_length=2, max_length=100)] = None
    slug : Annotated[str | None, StringConstraints(min_length=2, max_length=512)]
    description : Annotated[str | None, StringConstraints(min_length=2, max_length=200)]
    is_active : bool | None = None

class ProductCreateResponse(BaseModel):
    status:str
    message:str
    data: ProductResponse


class PaginationResponse(BaseModel):
    page: int
    limit: int
    total: int
    total_pages: int


class ProductListResponse(BaseModel):
    success: bool
    message: str
    data: list[ProductResponse]
    pagination: PaginationResponse