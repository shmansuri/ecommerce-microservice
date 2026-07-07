from pydantic import BaseModel, EmailStr, StringConstraints
from typing import Annotated

class registerRequested(BaseModel):
    name : Annotated[str, StringConstraints(min_length=2, max_length=100)]
    email : EmailStr
    password: Annotated[str, StringConstraints(min_length=8, max_length=25)]