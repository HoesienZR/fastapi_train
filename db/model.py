from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,Enum
from sqlalchemy.orm import relationship ,MappedColumn,Mapped,mapped_column
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
    category:Mapped[str] = mapped_column(Enum('Science','Computer','Mechanic','Others',name='category'),default='Others')
    id: Mapped[UUID] = mapped_column(primary_key=True, default_factory=uuid4)



