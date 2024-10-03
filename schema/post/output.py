from pydantic import BaseModel
from sqlalchemy import Date
from datetime import date

from enum import Enum
from uuid  import UUID
from .input import PostCategory

class PostOutput(BaseModel):
    """output schema of post that our api routers return """
    title:str
    description:str
    id:UUID
    category:PostCategory