from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.schemas.user import UserResponse, UserCreate



router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/",response_model=list[UserResponse])

def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users

@router.post("/", response_model=UserResponse, status_code=201)
def create_user( user_data: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user_data.email).first()

    if existing_user:
        raise HTTPException(
            status_code=409,
            detail = "emaill already registered"
        )

    user = User(
        user_name = user_data.user_name,
        email = user_data.email,
        password_hash = user_data.password,
        role_id = user_data.role_id
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user



