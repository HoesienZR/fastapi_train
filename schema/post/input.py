from pydantic import BaseModel
from uuid import UUID
class CreatePostInput(BaseModel):
    title:str
    description:str
class GetPostInput(BaseModel):
    id:UUID