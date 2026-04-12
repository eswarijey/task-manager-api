# API Design — Task Manager API

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
