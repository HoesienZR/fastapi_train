from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from db import model

model.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = S()
    try:
        yield db
    finally:
        db.close()