from app.database import engine
from app.models import Role, User, Project, Task, Comment

print("SQLAlchemy models loaded successfully")
print(engine)