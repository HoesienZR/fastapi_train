from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase,MappedAsDataclass

from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./sql_app.db"

ENGINE = create_async_engine(SQLALCHEMY_DATABASE_URL,
                             echo=True,
                             connect_args={"check_same_thread": False},
)
SESSION_LOCAL = async_sessionmaker(autocommit=False,
                                   autoflush=False,
                                   expire_on_commit=False,
                                   bind=ENGINE
                       )

class Base(DeclarativeBase,MappedAsDataclass):
    pass

async def get_db():
    db = SESSION_LOCAL()
    try :
        yield db
    finally :
       await db.close()


