from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src import db

from . import schema
from . import services

router = APIRouter(
    tags=['Tasks'],
    prefix='/tasks'
)


@router.get('/', response_model=List[schema.TaskList])
async def get_all_products(database: Session = Depends(db.get_db)):
    return await services.get_all_tasks(database)
