from sqlalchemy.ext.asyncio import AsyncSession
from db.model import User
import exceptions
from utils.secret import password_manger
import sqlalchemy as sa
from sqlalchemy.exc import IntegrityError
from schema.user.output import RegisterOutput
from utils.jwt import JWTHandler
from schema.jwt import JWTResponsePayload
class UsersOpreation:
    def __init__(self,db_session:AsyncSession)->None:
        self.db_session = db_session

    async def create(self,username:str,password:str)->RegisterOutput:
        pwd = password_manger.hash(password)
        user = User(password = pwd ,username = username)
        async with self.db_session as session :
            try:
                session.add(user)
                await session.commit()
            except IntegrityError:
                raise exceptions.UserAlreadyExists
        return RegisterOutput(username = user.username,id = user.id)
    async def get_user_by_username(self,username:str)->User:
        query =sa.select(User).where(User.username == username)
        async with self.db_session as session:
            user_data = await session.scalar(query)
            if user_data is None:
                raise  exceptions.UserNotFound
            return user_data
    async def upadate_username(self,username_old:str,username_new:str)->User:
        query = sa.select(User).where(User.username == username_old)
        update_query = sa.update(User).where(User.username == username_old).values(username = username_new)

        async with self.db_session as session:
            user_data = await session.scalar(query)
            if user_data is None:
                raise exceptions.UserNotFound
            await session.execute(update_query)
            await session.commit()
            user_data.username = username_new
            return user_data

    async def delete_user_account(self,username,)->None:
        delete_query = sa.delete(User).where(User.username==username ,)
        async with self.db_session as session:
            await session.execute(delete_query)
            await session.commit()
    async def login_user(self,username:str,password:str)->JWTResponsePayload:
        get_user_query = sa.select(User).where(User.username==username,)
        async with self.db_session as session:
            user = await  session.scalar(get_user_query)
            if user is None:
                raise exceptions.PasswordOrUserIncorrect
        if not password_manger.verify(password,user.password):
            raise exceptions.PasswordOrUserIncorrect
        return JWTHandler.generate(username=username)