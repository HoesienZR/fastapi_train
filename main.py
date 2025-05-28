from db.engine import Base,ENGINE
from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn
import logging
from routres.blog import router as blog_router

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting up: Initializing database tables")
    async with ENGINE.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    logger.info("Database tables initialized")
    yield
    logger.info("Shutting down: Disposing database engine")
    await ENGINE.dispose()
app = FastAPI(lifespan=lifespan)
app.include_router(blog_router,prefix='/blog')

if __name__ == '__main__':

    uvicorn.run(app, host='127.0.0.1', port=8000)