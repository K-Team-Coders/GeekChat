from loguru import logger
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from database.sqlalchemy import engine, session, base
from database.models import *

base.metadata.create_all(engine)
current_session = session()

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/add")
def add():
    for query in current_session.query(Messages):
        print(query)
    return JSONResponse({'holacora': "bang"})
