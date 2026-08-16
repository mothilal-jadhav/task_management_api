from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Task(Base):
    __tablename__ = "tasks"

    task_id = Column(Integer, primary_key=True, index=True)

    project_id = Column(
        Integer,
        ForeignKey("projects.project_id", ondelete="CASCADE"),
        nullable=True
    )

    assigned_to = Column(
        Integer,
        ForeignKey("users.user_id", ondelete="SET NULL"),
        nullable=True
    )

    title = Column(String(150), nullable=False)
    task_description = Column(Text)
    task_status = Column(String(20), nullable=False)
    task_priority = Column(String(10), nullable=False)

    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    project = relationship("Project", back_populates="tasks")
    assignee = relationship("User")
    comments = relationship("Comment", back_populates="task")