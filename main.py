from contextlib import asynccontextmanager

from db.engine import Base,ENGINE
from fastapi import FastAPI

import uvicorn

from routres.post import router as post_router
from sqladmin import ModelView , Admin
from db.model import Post
from db.engine import ENGINE


class PostAdmin(ModelView,model=Post):
    column_list = [Post.id,Post.title,Post.category,Post.description]


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Create database tables
    async with ENGINE.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # Shutdown: Dispose of engine
    await ENGINE.dispose()
app  = FastAPI(lifespan=lifespan)
app.include_router(post_router,prefix='/blog')

if __name__ == '__main__':
    admin = Admin(app=app, engine=ENGINE)
    admin.add_view(PostAdmin)
    uvicorn.run(app, host='127.0.0.1', port=8000)
