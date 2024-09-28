from pydantic import BaseModel

class RegisterUser(BaseModel):
    name:str
    password:str
    email:str
    is_active:bool

