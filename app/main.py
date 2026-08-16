from fastapi import FastAPI

from app.routers import users

app = FastAPI(
    title= "TASK MANAGEMENT API"
    version = "1.0.0"
)

app.include_router(users.router)

@app.get("/")
def root():
    return {"messeage": "Task Management API"}