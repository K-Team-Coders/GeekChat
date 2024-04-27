from fastapi import FastAPI
from fastApi.manager_connection import ConnectionManager
from fastapi.middleware.cors import CORSMiddleware
from fastapi.websockets import WebSocketDisconnect, WebSocket
from fastApi.pydantic_model import SessionStatus
from database.connector import *
from fastApi.helper_function import *

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
    comment_counter = 0
    positive = 0
    negative = 0
    try:

        while True:
            data = await websocket.receive_text()
            comment_counter += 1
            sentiment = score_calculate_emotion_coloring(data)
            if sentiment == 1:
                positive += 1
            elif sentiment == -1:
                negative += 1
            difference = (positive - negative) / comment_counter if comment_counter != 0 else 0
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        logger.info("WebSocket disconnect")


@app.post("/status")
async def start_session(request: SessionStatus):
    if request.status == "start":
        time_start = datetime.now()
        new_session = Session(
            session_id=request.session_id,
            start_time=time_start,
        )
        session.add(new_session)
        session.commit()
    elif request.status == "stop":
        session_to_update = session.query(Session).filter_by(id=request.session_id).first()
        time_end = datetime.now()
        session_to_update.end_time = time_end
        session.commit(session_to_update)
