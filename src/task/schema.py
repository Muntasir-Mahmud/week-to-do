from typing import Optional

from pydantic import BaseModel
from datetime import date, time


class TaskBase(BaseModel):
    id: Optional[int]
    name: str
    description: str
    due_date: date
    due_time: time
    completed: bool


class TaskList(TaskBase):

    class Config:
        orm_mode = True
