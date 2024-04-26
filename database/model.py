from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

# Создаем базовый класс для декларативных классов таблиц
Base = declarative_base()


class CommentInfo(Base):
    __tablename__ = 'comment_info'

    id = Column(Integer, primary_key=True)
    id_session = Column(Integer, unique=True)
    user_name = Column(String)
    comment = Column(String)
    emotional_coloring = Column(Integer)
    stop_words = Column(Integer)
    tech_issue = Column(Integer)


class Session(Base):
    __tablename__ = 'session_info'

    id = Column(Integer, primary_key=True)
    session_id = Column(Integer)
    start_time = Column(DateTime, default=datetime.utcnow)
    end_time = Column(DateTime, default=datetime.utcnow)
