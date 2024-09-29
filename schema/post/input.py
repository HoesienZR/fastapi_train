from pydantic import BaseModel
from uuid import UUID

class BasePostInput(BaseModel):
    """schema of post when it will be retrieved """
    id:UUID
class PostInput(BasePostInput):
    """schema of post when it created """
    title:str
    description:str