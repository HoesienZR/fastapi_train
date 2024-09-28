from sqlalchemy.ext.asyncio import AsyncSession
from db.model import Post
from uuid import UUID
import exceptions
import sqlalchemy as sa

class PostQueries:

    @staticmethod
    async def create_post(post:Post,db_session: AsyncSession)->Post:
        async with db_session as session:
            session.add(post)
            await session.commit()
        return post
    @staticmethod
    async def get_all_posts(db_session: AsyncSession):
        query = sa.select(Post)
        async with db_session as session:
            result = await session.execute(query)
            posts = result.scalars().all()

        return posts
    @staticmethod
    async def get_post(db_session: AsyncSession,post_id:UUID)->Post:
        query = sa.select(Post).where(Post.id == post_id)
        async with db_session as session:
            result  = await session.execute(query)
            post_data = result.scalar()
            if post_data is None:
                raise exceptions.PostNotFound
        return post_data


