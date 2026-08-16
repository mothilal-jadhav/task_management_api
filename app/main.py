from pathlib import Path
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

from fastapi import FastAPI
from app.routers import users, aut

app = FastAPI(
    title= "TASK MANAGEMENT API",
    version = "1.0.0"
)

app.include_router(users.router)
app.include_router(aut.router)

@app.get("/")
def root():
    return {"messeage": "Task Management API"}