from typing import Annotated


from fastapi import APIRouter,Body,Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.engine import get_db
from schema import post_input,post_output
from opreation.Blog import BlogOperation

router = APIRouter()

@router.get("/post/{item_id}")
async def get_post(item_id: int,):
    """this is just get post """
    pass

@router.get("/get_posts/")
async def get_posts():
    """this is return all posts"""
    pass
@router.get("/posts_category/{category}")
async def show_category(category:str):
    """this is return post from the same category they are"""
    pass
@router.post('/create_post')
async def create_post(
        db_session : Annotated[AsyncSession,Depends(get_db)],
        data:post_input.CreatePostInput=Body()
        ):
    """it's create post"""

    post = await BlogOperation(db_session).create_post(data)


@router.delete('/delete_post')
async def delete_post():
    """this is delete post"""
    pass
@router.put('/update_post/{post_id}')
async def update_post(post_id:int):
    """this is update post"""
    pass