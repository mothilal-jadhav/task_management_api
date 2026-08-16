# task_management_api

the request flow will be 

HTTP Request
     ↓
FastAPI Router
     ↓
Pydantic Schema
     ↓
Service Layer
     ↓
SQLAlchemy
     ↓
MySQL
     ↓
Response

for example for POST/projects we will eventually go 

POST /projects
      ↓
projects router
      ↓
ProjectCreate schema
      ↓
ProjectService
      ↓
SQLAlchemy
      ↓
MySQL

hence, before fastapi, lets build a connection with database through sqlalchemy