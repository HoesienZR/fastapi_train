import uuid
from uuid import UUID

from typing import Annotated


from fastapi import APIRouter,Body,Depends,status,Query


from sqlalchemy.ext.asyncio import AsyncSession
from db.engine import get_db
from schema import post_input,post_output
from opreation.Blog import BlogOperation