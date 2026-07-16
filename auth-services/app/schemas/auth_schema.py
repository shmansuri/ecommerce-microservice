from pydantic import BaseModel, EmailStr, StringConstraints, ConfigDict
from typing import Annotated

class RegisterRequested(BaseModel):
    name : Annotated[str, StringConstraints(min_length=2, max_length=100)]
    email : EmailStr
    phone : Annotated[str, StringConstraints(min_length=10, max_length=10)]
    password: Annotated[str, StringConstraints(min_length=8, max_length=25)]


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    email: str
    phone: str | None = None

class RegisterResponse(BaseModel):
    status: str
    message: str
    data: UserResponse



class Login(BaseModel):
    email : str
    password : str
