from pydantic import BaseModel


class UserResponse(BaseModel):
    user_id: int
    user_name: str
    email: str


    class Config:
        from_attributes = True

        