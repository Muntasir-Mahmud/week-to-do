from fastapi import FastAPI

from src.task import router as task_router


description = """
Todo API
"""

app = FastAPI(
    title="TodoApp",
    description=description,
    version="0.0.1",
    contact={
        "name": "Muntasir Mahmud",
        "url": "http://x-force.example.com/contact/",
    },

)

app.include_router(task_router.router)
