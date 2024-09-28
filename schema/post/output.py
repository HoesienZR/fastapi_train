from pydantic import BaseModel
from sqlalchemy import Date
from datetime import date

from uuid  import UUID

class PostOutput(BaseModel):
    title:str
    description:str
    id:UUID
