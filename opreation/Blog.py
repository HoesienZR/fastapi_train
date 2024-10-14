from sqlalchemy.ext.asyncio import AsyncSession
from schema import post_input,post_output
from queries.posts import PostQueries
from db.model import Post
from uuid  import UUID,uuid4
class BlogOperation:

     def __init__(self, db_session: AsyncSession) -> None:
        self.db_session = db_session

     async def create_post(self,post:post_input.CreatePostInput)->post_output.PostOutput:
        post = Post(#user_id=uuid4(),
                    title=post.title,
                    description=post.description,
                    category = post.category
        )
        await PostQueries.create_post(post=post,db_session=self.db_session)
        return post_output.PostOutput(
                          #user_id = post.user_id,
                          title=post.title,
                          description=post.description,
                          id = post.id,
                          category= post.category
        )
     async def get_all_posts(self):
         posts = await PostQueries.get_all_posts(db_session=self.db_session)
         return posts
     async def get_post(self,post_id:UUID)->post_output.PostOutput:
         post_data = await PostQueries.get_post(db_session=self.db_session,post_id=post_id)
         return post_output.PostOutput(title = post_data.title,
                                       description = post_data.description,
                                       id = post_data.id,
                                       category = post_data.category
                                       )
     async def delete_post(self,post_id:UUID)->None:
         await PostQueries.delete_post(db_session=self.db_session,post_id=post_id)
     async def update_post(self,post:post_input.PostInput)->post_output.PostOutput:
        post = await PostQueries.update_post(db_session=self.db_session,post=post)
        return post_output.PostOutput(title = post.title,
                                      id = post.id,
                                      description=post.description,
                                      category = post.category)
     async def get_post_category(self,category:str)->post_output.PostsOutPut:
        posts = await PostQueries.get_categories_of_posts(db_session=self.db_session,category=category)
        return post_output.PostsOutPut(posts=posts)
     async def get_posts(self,)->post_output.PostsOutPut:
        posts = await PostQueries.get_all_posts(db_session=self.db_session)
        return post_output.PostsOutPut(posts=posts)



