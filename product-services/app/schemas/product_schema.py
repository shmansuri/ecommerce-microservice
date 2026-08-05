from pydantic import EmailStr, StringConstraints, BaseModel
from typing import Annotated

class ProductCreate(BaseModel):
    pass

class ProductResponse(BaseModel):
    pass