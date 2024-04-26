from pydantic import BaseModel


class Session(BaseModel):
    start: str
    session_id: str
    stop: str
