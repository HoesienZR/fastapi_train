from pydantic import BaseModel
from sqlalchemy import Date
from datetime import date
from db.model import Post
from enum import Enum
from uuid  import UUID
from .input import PostCategory

class PostOutput(BaseModel):
    """output schema of post that our api routers return """
    title:str
    description:str
    id:UUID
    category:PostCategory|None
class PostsOutPut(BaseModel):
    posts:list[Post]
