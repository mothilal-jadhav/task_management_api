from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Project(Base):
    __tablename__ = "projects"

    project_id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(
        Integer,
        ForeignKey("users.user_id", ondelete="SET NULL"),
        nullable=True
    )

    title = Column(String(50), nullable=False)
    created_at = Column(DateTime, nullable=False)

    owner = relationship("User")
    tasks = relationship("Task", back_populates="project")