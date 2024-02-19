from typing import List
from . import models


async def get_all_tasks(database) -> List[models.Task]:
    tasks = database.query(models.Task).all()
    return tasks
