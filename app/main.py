from fastapi import FastAPI
from app.routers import auth, tasks, users
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="logs/app.log",
)


app = FastAPI(
    title="Task Manager API",
    version="1.0.0",
    description="A RESTful API for managing tasks",
)


app.include_router(users.router, prefix="/api/v1")
app.include_router(tasks.router, prefix="/api/v1")
app.include_router(auth.router, prefix="/api/v1")


@app.get("/health")
def health_check():
    return {"status": "ok"}
