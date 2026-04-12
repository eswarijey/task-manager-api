# Task Manager API
A RESTful Task Manager API built with FastAPI, PostgreSQL, and Docker. A hands-on learning project covering backend development, API design, and AWS deployment

## Overview
Task Manager API is a RESTful API built with FastAPI that allows individual users to create, read, update and delete the task. It is designed as a hands on learning project covering backend development, API design and AWS deployment

## Tech Stack
- **Framework:** FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Validation:** Pydantic
- **Migrations:** Alembic
- **Containerisation:** Docker
- **Deployment:** AWS

## Project Structure
```
task-manager-api/
├── docs/         # Project documentation
│   ├── BRD_Task_Manager_API.md   # Business Requirement Document
│   ├── API_Design.md        # API Design Document
│   └── ERD.md        # Entity Relationship Diagram Document
├── app/       # Project Application
│   ├── main.py     # Entry point of the application
│   ├── models/    # python classes maps to table (database model)
│   ├── schemas/  # Pydantic schema  - structure of data IN and OUT
│   ├── routers/    # API endpoints routes - (tasks.py -> /tasks, users.py -> /users)
│   └── database.py    # Database connection setup
├── tests/   # Unit and Integration testing scripts
├── .env     # environment variable
├── .gitignore  # file to be ignored in git commit
├── docker-compose.yml   # Defines and runs multiple containers together
├── Dockerfile      # Instruction to build Docker image for application
├── requirements.txt     # list of python packages/libraries your projects depends on
└── README.md     # Tells What is this projects is about
```

## API Endpoints
## User Management
| Method | Endpoint | Description |
|---|---|---|
| POST | /users | Register a new user |
| POST | /auth/login | User login |
| POST | /auth/logout | User logout |


## Task Management
| Method | Endpoint | Description |
|---|---|---|
| POST | /tasks | Create a new task |
| PUT | /tasks/{id} | Update task |
| GET | /tasks | list all tasks |
| GET | /tasks/{id} | list a specific task |
| DELETE | /tasks/{id} | delete task |

## Project Status
| Phase | Description | Status |
|---|---|---|
| Phase 0 | Repo & Documentation Setup | ✅ Complete |
| Phase 1 | Implementation Setup | 🔄 In Progress |
| Phase 2 | POC | ⏳ Pending |
| Phase 3 | MVP | ⏳ Pending |
| Phase 4 | Production Ready | ⏳ Pending |
| Phase 5 | AWS Deployment | ⏳ Pending |
