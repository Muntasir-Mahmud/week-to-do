from sqlalchemy import Column, Integer, String, Float, Text, Boolean, Date, Time
from sqlalchemy.sql import func

from src.db import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    description = Column(Text)
    due_date = Column(Date, server_default=func.now())
    due_time = Column(Time)
    completed = Column(Boolean)
