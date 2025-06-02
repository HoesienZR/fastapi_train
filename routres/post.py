#from idlelib.query import Query

from routres import  UUID ,Annotated

from routres import APIRouter,Body,Depends,status

from routres import AsyncSession

from routres import get_db

from routres import post_input,post_output
from schema.pagination.pagination import  PaginatedResponse

from routres import BlogOperation

from fastapi import Query


router = APIRouter()

@router.get("/post/{item-id}",status_code=status.HTTP_200_OK)
async def get_post(item_id:str,
                   db_session : Annotated[AsyncSession,Depends(get_db)]
                   )->post_output.PostOutput:
    post =  await BlogOperation(db_session=db_session).get_post(item_id)
    """this is routers receive post id then returns post  """
    return post
#TODO data model for get posts need to get fixed it's hard coded and not  flexible
@router.get("/get_posts/",
           # response_model=PaginatedResponse[post_output.PostPagination]
            )
async def get_posts(db_session : Annotated[AsyncSession,Depends(get_db)],
                    limit : int = Query(100,ge = 0),
                    offset : int = Query(0,ge= 0 )

                    )->post_output.PostPagination:
    """this is return all posts"""
    posts = await BlogOperation(db_session=db_session).get_posts(limit,offset)
    return posts
@router.get("/posts_category/{category}",status_code=status.HTTP_200_OK)
async def show_category(category:str,db_session : Annotated[AsyncSession,Depends(get_db)])->post_output.PostsOutPut:
    """this is return post from the same category they are"""
    posts = await BlogOperation(db_session=db_session).get_post_category(category=category)
    return posts
@router.post('/create_post',status_code=status.HTTP_201_CREATED)
async def create_post(
        db_session : Annotated[AsyncSession,Depends(get_db)],
        data:post_input.CreatePostInput=Body()
        )->post_output.PostOutput:
    """this router get title and description form user and make connection
     to data base then create post and return response of post  """
    post = await BlogOperation(db_session).create_post(data)
    return post

@router.delete('/delete_post/{post_id}',status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(db_session : Annotated[AsyncSession,Depends(get_db)],
                      raw_post_id:str
                      ):
    """get post id then delete post  needs to be done"""
    print(raw_post_id)
    await BlogOperation(db_session).delete_post(raw_post_id=raw_post_id)
    return {'id':'8bd3dbb9c5794519bd153d96d5bbaa16',
            'status':'deleted'}
@router.put('/update_post/') #TODO: it's need to filter category it's gets
async def update_post(post:post_input.PostInput,
                      db_session : Annotated[AsyncSession,Depends(get_db)]
                      )->post_output.PostOutput:
    post = await BlogOperation(db_session).update_post(post)
    return post_output.PostOutput(id=post.id,title=post.title,description=post.description,category=post.category)
