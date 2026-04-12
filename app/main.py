from fastapi import FastAPI

app = FastAPI(
    title="Task Manager API",         
    version="1.0.0",        
    description="A RESTful API for managing tasks"    
)

@app.get("/health")
def health_check():
    return {"status": "ok"}   