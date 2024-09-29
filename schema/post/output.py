from pydantic import BaseModel
from sqlalchemy import Date
from datetime import date

from uuid  import UUID

class PostOutput(BaseModel):
    """output schema of post that our api routers return """
    title:str
    description:str
    id:UUID
