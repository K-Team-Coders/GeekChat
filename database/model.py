from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.orm import declarative_base
from datetime import datetime

# Создаем базовый класс для декларативных классов таблиц
Base = declarative_base()


class CommentInfo(Base):
    __tablename__ = 'comment_info'

    id = Column(Integer, primary_key=True)
    id_session = Column(Integer)
    user_name = Column(String)
    comment = Column(String)
    emotional_coloring = Column(Integer, default=0)
    stop_words = Column(Integer, default=0)
    tech_issue = Column(Integer, default=0)


class Session(Base):
    __tablename__ = 'session_info'

    id = Column(Integer, primary_key=True)
    session_id = Column(Integer)
    start_time = Column(DateTime, default=datetime.utcnow)
    end_time = Column(DateTime, default=datetime.utcnow)


class UserInSession(Base):
    __tablename__ = 'user_in_session'

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer)
    user_name = Column(String, unique=True, index=True)
    count_comment = Column(Integer, default=0)
    positive_comments = Column(Integer, default=0)
    negative_comments = Column(Integer, default=0)
    activity = Column(Float, default=0.0)
    last_activity_update = Column(Integer, default=int(datetime.now().timestamp()))

