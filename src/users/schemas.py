from pydantic import BaseModel

class User(BaseModel):
    login: str

class CreateUser(User):
    password: str

class Login(User):
    password: str

class ResponseUserLogin(BaseModel):
    success: bool
    accessToken: str
