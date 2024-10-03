from pydantic import BaseModel

from uuid import UUID
from enum import Enum
class PostCategory(str,Enum):
    Science  = 'Science'
    Computer = 'Computer'
    Mechanic = 'Mechanic'
    Others   =  'Others'
class BasePostInput(BaseModel):
    """schema of post when it will be retrieved """
    id:UUID
class PostInput(BasePostInput):
    """schema of post when it created """
    title:str
    description:str
class CreatePostInput(BaseModel):
    title:str
    description:str
    category:PostCategory
