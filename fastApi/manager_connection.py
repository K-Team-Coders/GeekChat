import asyncio

from fastapi.websockets import WebSocket
from database.connector import *


class SessionManager:
    def __init__(self):
        self.sessions = {}

    async def connect(self, websocket: WebSocket, session_id: int, user_name: str, db: Session):
        await websocket.accept()
        if session_id not in self.sessions:
            self.sessions[session_id] = {"users": {}, "comments": 0, "positive": 0, "negative": 0}
        self.sessions[session_id]["users"][websocket] = user_name
        # Add user to the database
        db_user = UserInSession(session_id=session_id, user_name=user_name)
        db.add(db_user)
        db.commit()

    def disconnect(self, websocket: WebSocket, session_id: int, db: Session):
        user_name = self.sessions[session_id]["users"][websocket]
        del self.sessions[session_id]["users"][websocket]
        # Delete user from the database
        user_to_delete = db.query(UserInSession).filter_by(user_name=user_name).first()
        db.delete(user_to_delete)
        db.commit()

    async def update_activity(self, session_id: int, interval: int, db: Session):
        while True:
            await asyncio.sleep(interval)
            session_data = self.sessions.get(session_id)
            if session_data:
                current_timestamp = int(datetime.now().timestamp())
                interval_duration = current_timestamp - session_data["last_activity_update"]
                session_data["last_activity_update"] = current_timestamp
                users = session_data["users"]
                total_comments = session_data["comments"]
                total_positive = session_data["positive"]
                total_negative = session_data["negative"]
                for user_ws, user_name in users.items():
                    user = db.query(UserInSession).filter_by(user_name=user_name).first()
                    if user:
                        if interval_duration > 0:
                            user.activity = ((user.positive_comments - user.negative_comments) / user.count_comment) * (
                                        interval_duration / 60) if user.count_comment != 0 else 0
                        else:
                            user.activity = 0
            db.commit()


