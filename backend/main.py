from fastapi import FastAPI, Depends
from typing import Annotated
from sqlmodel import Session, SQLModel, create_engine
from contextlib import asynccontextmanager
from config.settings import settings
import models
import requests

connect_args = {"check_same_thread": False}
engine = create_engine(settings.get("database_url"), connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/jobs")
def get_jobs():
    headers = {"Authorization": f"Token {settings.api_key}"}
    r = requests.get("https://findwork.dev/api/jobs/", headers=headers)

    response = r.json()

    return response
