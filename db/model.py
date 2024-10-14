from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,Enum,DateTime
from sqlalchemy.orm import relationship ,MappedColumn,Mapped,mapped_column
from datetime import datetime
from uuid import UUID,uuid4

from .engine import Base


class User(Base):
    """this is a raw model of user will be changed in future"""
    __tablename__ = "users"
   # posts: Mapped[list['Post']] = relationship(back_populates='user')
    name:Mapped[str] = mapped_column(String(64))
    password: Mapped[str] = mapped_column(String())
    email: Mapped[str] = mapped_column(String())
    is_active = Column(Boolean, default=True)
    id:Mapped[str] = mapped_column(default_factory = uuid4, primary_key=True)


class Post(Base):
    """raw model of post  will be changed in future and comment will be added later"""
    __tablename__ = "posts"
    title: Mapped[str] = mapped_column(String(50))
    description:Mapped[str] = mapped_column()
  #  user_id : Mapped[UUID] = mapped_column()
   # user:Mapped["User"] = relationship(back_populates='posts')
    comments: Mapped['Comment'] = relationship(back_populates='comments')
    category:Mapped[str] = mapped_column(Enum('Science','Computer','Mechanic','Others',name='category'),default='Others')
    id: Mapped[UUID] = mapped_column(primary_key=True, default_factory=uuid4)



class Comment(Base):
    __tablename__ = 'comments'
    description:  Mapped[str] = mapped_column()
    post_id: Mapped[UUID] = mapped_column()
    post: Mapped['Post'] = relationship(back_populates='posts')
    date_created: Mapped[datetime] = mapped_column(DateTime,default=datetime)
    id: Mapped[UUID] = mapped_column(primary_key=True, default_factory=uuid4)

