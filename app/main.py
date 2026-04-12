from fastapi import FastAPI
from app.routers import tasks, users

app = FastAPI(
    title="Task Manager API",         
    version="1.0.0",        
    description="A RESTful API for managing tasks"    
)

app.include_router(users.router)
app.include_router(tasks.router)

@app.get("/health")
def health_check():
    return {"status": "ok"}   