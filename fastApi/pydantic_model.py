from pydantic import BaseModel


class SessionStatus(BaseModel):
    status: str
    session_id: int


class User(BaseModel):
    user_name: str
