## 1. Project Overview

**Project Name:** Task Manager API  
**Version:** 1.0  
**Date:** 2026-04-09

### Summary
This is an Multi user API for a client application to have their tasks created, listed, updated, viewed and deleted"

### Goals
- Authentication - User will have their own username and password to login
- Task Management - Tasks are create, updated, viewed, listed, deleted
- Data Privacy - User should only see their own tasks


## 2. Stakeholders

| Role               | Description                                              |
|--------------------|----------------------------------------------------------|
| Developer          |Builds and maintain the API                               |
| End User           | Individual person who manages their tasks                |
| Client Application | The frontend app that will consume this API in the future|


## 3. Functional Requirements

### 3.1 User Management
| # | Requirement |
|---|---|
| FR-UM-01 | The system shall allow a user to register with a username and password |
| FR-UM-02 | The system shall allow used to Login / Logout of the system|
| FR-UM-03 | The system shall allow user to Password reset / Forgot Password|

### 3.2 Task Management
| # | Requirement |
|---|---|
| FR-TM-01 | The system shall allow a user to create a new task |
| FR-TM-02 | The system shall allow a user to update an existing task|
| FR-TM-03 | The system shall allow a user to delete an existing task|
| FR-TM-04 | The system shall allow a user to view specific task|
| FR-TM-05 | The system shall allow a user to view all the task|

reminder and frequency we can add it later , we can do these task first and then if need we can add these task later


## 4. Non-Functional Requirements

| #      | Category     | Requirement                                                               |
|--------|--------------|---------------------------------------------------------------------------|
| NFR-01 | Performance  |The system shall respond to all API requests within 500ms under normal load|
| NFR-02 | Security     | The system shall have hashed password (not plain text)                    |
| NFR-03 | Scalability  | The system shall support multiple concurrent users                        |
| NFR-04 | Availability | The system shall be available 99.9%                                       |


## 5. Out of Scope

| #     | Feature                         | Notes                                                                                                         |
|-------|---------------------------------|---------------------------------------------------------------------------------------------------------------|
| OS-01 | Task reminder and frequency     | The reminder and frequency of the task will handled at the later stage of the project                         |
| OS-02 | Authentication and Authorisation|Authentication and Authorisation for the user name and password will be added to the project at the later stage|
| OS-03 | Frontend App|Frontend app will designed and developed later                                                                                     |