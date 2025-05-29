from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime

from orm import Base


class User(Base):
    __tablename__ = "app_user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(16))
    password = Column(String(60))
    created_at = Column(DateTime, default=datetime.now)
