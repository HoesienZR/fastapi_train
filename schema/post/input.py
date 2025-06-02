import uuid

from pydantic import BaseModel,field_validator
from uuid import UUID
from enum import Enum

class PostCategory(str,Enum):
    Science  = 'Science'
    Computer = 'Computer'
    Mechanic = 'Mechanic'
    Others   =  'Others'
class BasePostInput(BaseModel):
    """schema of post when it will be retrieved """
    id:str
class PostInput(BasePostInput):
    """schema of post when it created """
    title:str
    description:str
    category:str

    @field_validator('category')
    def check_category_field(cls, value):
        print(value)
        if not value in ['Science', 'Computer', 'Mechanic']:
            return 'Others'
        return value

class UpdatePostInput(BasePostInput):
    title:str|None
    description:str|None
    category:str|None



class CreatePostInput(BaseModel):
    #TODO category raw string scchema need to fixed 
    title:str
    description:str
    category:str|None

    @field_validator('category')
    def check_category_field(cls, value):
        print(value)
        if not value in ['Science', 'Computer', 'Mechanic']:
            return 'Others'
        return value
class UpdatePostInput(BasePostInput):
    title:str|None
    description:str|None
    category:PostCategory|None