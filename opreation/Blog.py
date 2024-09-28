from sqlalchemy.ext.asyncio import AsyncSession
from schema import post_input,post_output
from queries.posts import PostQueries
from db.model import Post
from uuid  import UUID,uuid4
class BlogOperation:

     def __init__(self, db_session: AsyncSession) -> None:
        self.db_session = db_session

     async def create_post(self,post:post_input.CreatePostInput
                                )->post_output.PostOutput:
        post = Post(#user_id=uuid4(),
                    title=post.title,
                    description=post.description)
        await PostQueries.create_post(post=post,db_session=self.db_session)
        return post_output.PostOutput(
                          #user_id = post.user_id,
                          title=post.title,
                          description=post.description,
                          id = post.id)
     async def get_all_posts(self):
         posts = await PostQueries.get_all_posts(db_session=self.db_session)
         return posts
     async def get_post(selfs,post_id:UUID)->Post:
         post_data = await PostQueries.get_post(db_session=selfs.db_session,post_id=post_id)
         return post_data






