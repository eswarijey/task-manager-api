# ERD — Task Manager API

## Entities

### User
| Column | Data Type | Constraints |
|---|---|---|
| id | Integer | Primary Key, Auto-increment |
| email | String | Unique, Not Null |
|username|String|Not Null|
|hashed_password|String|NotNull|
|created_at|Datetime|Not Null|
|updated_at|Datetime|Not Null|

### Task
| Column | Data Type | Constraints |
|---|---|---|
|id|Integer|PrimaryKey, Auto-increment|
|title|String|Not Null|
|description|String||
|status|enum|Open, inprogress, pending, completed|
|priority|enum|low, Medium, High|
|due_date|Datetime||
|user_id|integer|foreign Key, Not Null|
|created_at|Datetime|Not Nulll|
|updated_at|Datetime|Not Null|

## Relationships
One User can have many Tasks. The user_id column in the Task table is a Foreign Key referencing id in the User table.
