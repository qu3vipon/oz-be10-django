from pydantic import BaseModel


class UserSignUpRequest(BaseModel):
    username: str
    password: str


class UserLoginRequest(BaseModel):
    username: str
    password: str
