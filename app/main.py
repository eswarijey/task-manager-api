from fastapi import FastAPI
from app.routers import auth, tasks, users

app = FastAPI(
    title="Task Manager API",
    version="1.0.0",
    description="A RESTful API for managing tasks",
)

app.include_router(users.router)
app.include_router(tasks.router)
app.include_router(auth.router)


@app.get("/health")
def health_check():
    return {"status": "ok"}
