from pydantic import BaseModel

class UserCreate(BaseModel):
    user_name: str
    email: str
    password: str
    role_id: int
    
class UserResponse(BaseModel):
    user_id: int
    user_name: str
    email: str


    class Config:
        from_attributes = True

