from db.engine import Base,ENGINE
from fastapi import FastAPI

import uvicorn

from routres.post import router as blog_router



app = FastAPI()
@app.on_event('startup')
async def init_tables():
    async with ENGINE.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


app.include_router(blog_router,prefix='/blog')

if __name__ == '__main':
    uvicorn.run(app, host='127.0.0.1', port=8000)