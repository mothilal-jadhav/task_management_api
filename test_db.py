from app.database import engine

try: 
    with engine.connect() as connection:
        print("Database connection succesful")
except Exception as e:
    print("Database Connection failed: ", e)