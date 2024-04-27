from fastapi import FastAPI
from fastApi.manager_connection import SessionManager
from fastapi.middleware.cors import CORSMiddleware
from fastapi.websockets import WebSocketDisconnect, WebSocket
from fastApi.pydantic_model import SessionStatus, User
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

manager = SessionManager()
session = connect_database()
loop = asyncio.get_event_loop()
loop.create_task(manager.update_activity(session_id=1, interval=60, db=session))


<<<<<<< HEAD
@app.websocket("/ws/{session_id}")
async def websocket_endpoint(websocket: WebSocket, session_id: int, user_name: str):
    await manager.connect(websocket, session_id, user_name, db=session)
    try:
        while True:
            data = await websocket.receive_text()
            session_data = manager.sessions[session_id]
            session_data["comments"] += 1
            # Assume `score_calculate_emotion_coloring` is a placeholder function
            sentiment = score_calculate_emotion_coloring(data)
            if sentiment == 1:
                session_data["positive"] += 1
            elif sentiment == -1:
                session_data["negative"] += 1
            user = session.query(UserInSession).filter_by(user_name=user_name).first()
            if user:
                user.count_comment += 1
                if sentiment == 1:
                    user.positive_comments += 1
                elif sentiment == -1:
                    user.negative_comments += 1
=======
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()

>>>>>>> parent of cf73d46 (fixes)
    except WebSocketDisconnect:
        manager.disconnect(websocket, session_id, session)


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
        new_session_activity = SessionActivity(session_id=request.session_id)
        session.add(new_session_activity)
        session.commit()
    elif request.status == "stop":
        session_to_update = session.query(Session).filter_by(id=request.session_id).first()
        time_end = datetime.now()
        session_to_update.end_time = time_end
        session.commit(session_to_update)
