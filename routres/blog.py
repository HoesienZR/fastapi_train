import uuid
from uuid import UUID

from typing import Annotated


from fastapi import APIRouter,Body,Depends,status
from sqlalchemy.ext.asyncio import AsyncSession

from db.engine import get_db
from schema import post_input,post_output
from opreation.Blog import BlogOperation

router = APIRouter()

@router.get("/post/{item-id}",status_code=status.HTTP_200_OK)
async def get_post(item_id:UUID,
                   db_session : Annotated[AsyncSession,Depends(get_db)]
                   )->post_output.PostOutput:
    post =  await BlogOperation(db_session=db_session).get_post(item_id)
    """this is routers receive post id then returns post  """
    return post

@router.get("/get_posts/",)
async def get_posts():
    """this is return all posts"""
    pass
@router.get("/posts_category/{category}")
async def show_category(category:str):
    """this is return post from the same category they are"""
    pass
@router.post('/create_post',status_code=status.HTTP_201_CREATED)
async def create_post(
        db_session : Annotated[AsyncSession,Depends(get_db)],
        data:post_input.PostInput=Body()
        )->post_output.PostOutput:
    """this router get title and description form user and make connection
     to data base then create post and return response of post  """

    post = await BlogOperation(db_session).create_post(data)
    return post



@router.delete('/delete_post/{post_id}',status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(db_session : Annotated[AsyncSession,Depends(get_db)],
                      post_id:UUID
                      ):
    """get post id then delete post  needs to be done"""
    await BlogOperation(db_session).delete_post(post_id=post_id)
@router.put('/update_post/')
async def update_post(post:post_input.PostInput,
                      db_session : Annotated[AsyncSession,Depends(get_db)]
                      )->post_output.PostOutput:
    post = await BlogOperation(db_session).update_post(post)
    return post_output.PostOutput(id=post.id,title=post.title,description=post.description)
