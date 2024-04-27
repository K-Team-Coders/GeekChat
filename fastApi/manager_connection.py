import asyncio

from fastapi.websockets import WebSocket
from database.connector import *


class SessionManager:
    def __init__(self):
        self.sessions = {}

    async def connect(self, websocket: WebSocket, session_id: int, user_name: str, db: Session):
        await websocket.accept()
        if session_id not in self.sessions:
            self.sessions[session_id] = {"users": set(), "comments": 0, "positive": 0, "negative": 0}
        self.sessions[session_id]["users"].add(user_name)
        # Add user to the database
        db_user = UserInSession(session_id=session_id, user_name=user_name)
        db.add(db_user)
        db.commit()

    def disconnect(self, websocket: WebSocket, session_id: int, db: Session):
        user_name = self.sessions[session_id]["users"].pop()
        if not self.sessions[session_id]["users"]:
            del self.sessions[session_id]
        # Delete user from the database
        user_to_delete = db.query(UserInSession).filter_by(user_name=user_name).first()
        db.delete(user_to_delete)
        db.commit()

    def increment_positive(self, session_id: int):
        if session_id in self.sessions:
            self.sessions[session_id]["positive"] += 1

    def increment_negative(self, session_id: int):
        if session_id in self.sessions:
            self.sessions[session_id]["negative"] += 1

    async def update_activity(self, interval: int, db: Session):
        while True:
            await asyncio.sleep(interval)
            for session_id, session_data in self.sessions.items():
                total_comments = session_data["comments"]
                total_positive = session_data["positive"]
                total_negative = session_data["negative"]
                session = db.query(Session).filter_by(id=session_id).first()
                if session:
                    session.total_comments = total_comments
                    session.total_positive = total_positive
                    session.total_negative = total_negative
                    db.commit()
                    # Calculate activity and update session activity record
                    session_activity = db.query(SessionActivity).filter_by(session_id=session_id).first()
                    if session_activity:
                        session_activity.activity = (total_positive - total_negative) / total_comments if total_comments != 0 else 0
                        db.commit()
