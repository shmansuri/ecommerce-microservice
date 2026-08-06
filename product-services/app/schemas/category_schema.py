from pydantic import BaseModel, StringConstraints, ConfigDict
from typing import Annotated
from datetime import datetime


class CategoryCreate(BaseModel):
    name : Annotated[str, StringConstraints(min_length=2, max_length=100)]
    slug : Annotated[str, StringConstraints(min_length=2, max_length=200)]
    description : Annotated[str, StringConstraints(min_length=2, max_length=200)]


class CategoryResponse(BaseModel):
    id: int
    name : str
    slug : str
    description : str
    is_active : bool
    created_at : datetime
    updated_at : datetime

    model_config = ConfigDict(from_attributes=True)


class CategoryUpdate(BaseModel):
    name : Annotated[str | None, StringConstraints(min_length=2, max_length=100)] = None
    slug : Annotated[str | None, StringConstraints(min_length=2, max_length=200)] = None
    description : Annotated[str | None, StringConstraints(min_length=2, max_length=200)] = None
    is_active : bool | None = None
