from typing import Any, Coroutine

from sqlalchemy import RowMapping
from sqlalchemy.ext.asyncio import AsyncSession
from db.model import Post,Comment
from uuid import UUID
import exceptions
import sqlalchemy as sa
from sqlalchemy.orm import defer
from queries import transform_uuid
from pydantic import parse_obj_as
from schema.post.output import PostOutput

class PostQueries:

    @staticmethod
    async def create_post(post:Post,db_session: AsyncSession)->Post:
        async with db_session as session:
            session.add(post)
            await session.commit()
        return post
    @staticmethod
    async def get_all_posts(db_session: AsyncSession,limit,offset):
        query = sa.select(Post.id,Post.title,Post.description,Post.category)
        count_query = sa.select(sa.func.count()).select_from(sa.select(Post.id).limit(limit).offset(offset).subquery() )
        async with db_session as session:
            result =   await session.execute(query.limit(limit=limit).offset(offset=offset))
            count  = await session.scalar(count_query)


        return result.mappings().all(),count
    @staticmethod
    async def get_post(db_session: AsyncSession,post_id:str)->Post:
        transformed_post_id = transform_uuid(post_id)
        query = sa.select(Post).where(Post.id == transformed_post_id)
        async with db_session as session:
            result  = await session.execute(query)
            post_data = result.scalar()
            if post_data is None:
                raise exceptions.PostNotFound
        return post_data
    @staticmethod
    async def delete_post(db_session: AsyncSession,raw_post_id:str)->None:
        post_id = transform_uuid(raw_post_id)
        query = sa.delete(Post).where(Post.id == post_id)
        async with db_session as session:
            await session.execute(query)
            await session.commit()
    @staticmethod
    async def update_post(db_session: AsyncSession,
                          post,)-> PostOutput:
        post_uuid = transform_uuid(post.id)
        query = sa.select(Post.id,Post.title,Post.description,Post.category).where(Post.id == post_uuid)
        async with db_session as session:
            result = await session.execute(query)
            post_data = result.mappings().one()

            update_values = {}
            if post.title is not None:
                update_values['title'] = post.title
            else:
                update_values['title'] = post_data['title']
            if post.description is not None:
                update_values['description'] = post.description
            else :
                update_values['description'] = post_data['description']
            if post.category is not None:
                update_values['category'] = post.category
            else :
                update_values['category'] = post_data['category']
            update_query = (sa.update(Post)
                            .where(Post.id == post_uuid)
                            .values(title=update_values['title'],
                            description=update_values['description'],
                            category=update_values['category'],)
                            )
            await session.execute(update_query)
            await session.commit()
            print(post_data.keys())



            return PostOutput(id=post_uuid,
                              description=update_values['description'],
                              category=update_values['category'],
                              title=update_values['title'],)
    @staticmethod
    async def get_categories_of_posts(db_session: AsyncSession,category):
        query = sa.select(Post.id,Post.title,Post.description,Post.category).where(Post.category == category)
        async with db_session as session :
            result = await session.execute(query)
            posts =  result.mappings().all()
        return posts
