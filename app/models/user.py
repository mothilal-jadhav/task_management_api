from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from app.database import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)

    role_id = Column(
        Integer,
        ForeignKey("roles.id", ondelete="SET NULL")
    )

    user_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)

    created_at = Column(
        DateTime,
        nullable=False,
        server_default=func.current_timestamp()
    )

    role = relationship("Role")