from contextlib import asynccontextmanager

from db.engine import Base,ENGINE
from fastapi import FastAPI

import uvicorn

from routres.post import router as post_router



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
    uvicorn.run(app, host='127.0.0.1', port=8000)