from loguru import logger
from datetime import datetime
from fastapi import FastAPI
from fastApi.manager_connection import ConnectionManager
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.websockets import WebSocketDisconnect, WebSocket
from fastApi.pydantic_model import SessionStart
from database.connector import *

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

manager = ConnectionManager()
session = connect_database()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()

    except WebSocketDisconnect:
        manager.disconnect(websocket)
        logger.info("WebSocket disconnect")


@app.post("/start_status")
async def start_session(request: Session):
    if Session.start is "start":
        time_start = datetime.now()
        new_session = Session(
            session_id=Session.session_id,
            start_time=time_start,
        )
        session.add(new_session)
        session.commit()
    elif Session.stop is "stop":
        session_to_update = session.query(Session).filter_by(id=Session.session_id).first()
        time_end = datetime.now()
        session_to_update.end_time = time_end
        session.commit(session_to_update)
