from pydantic import BaseModel


class Session(BaseModel):
    status: str
    session_id: str