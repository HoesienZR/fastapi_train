from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship ,MappedColumn,Mapped,mapped_column
from uuid import UUID,uuid4

from .engine import Base


class User(Base):
    __tablename__ = "users"
   # posts: Mapped[list['Post']] = relationship(back_populates='user')
    name:Mapped[str] = mapped_column(String(64))
    password: Mapped[str] = mapped_column(String())
    email: Mapped[str] = mapped_column(String())
    is_active = Column(Boolean, default=True)
    id:Mapped[str] = mapped_column(default_factory = uuid4, primary_key=True)






class Post(Base):
    __tablename__ = "posts"
    title: Mapped[str] = mapped_column(String(50))
    description:Mapped[str] = mapped_column()
  #  user_id : Mapped[UUID] = mapped_column()
   # user:Mapped["User"] = relationship(back_populates='posts')
    id: Mapped[UUID] = mapped_column(primary_key=True, default_factory=uuid4)



