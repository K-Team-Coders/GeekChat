from sqlalchemy import Column, BigInteger, Text

from .sqlalchemy import base

class Messages(base):
    __tablename__ = "messages"

    id = Column(BigInteger, primary_key=True)
    message = Column(Text)
    organisation = Column(Text)
    theme = Column(Text)
    group = Column(Text)