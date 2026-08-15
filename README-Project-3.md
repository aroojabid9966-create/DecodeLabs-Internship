# Project 3 — Task Management REST API

## Django REST Framework + PostgreSQL

A professional backend project developed using **Django REST Framework** and **PostgreSQL**. The project demonstrates RESTful API development, database integration, serialization, validation, and complete CRUD operations for task management.

---

## Project Overview

The Task Management REST API provides a backend system for creating and managing tasks.

The application allows users to:

- Create tasks
- View all tasks
- View a specific task
- Update tasks
- Partially update tasks
- Delete tasks
- Manage task statuses
- Store task data in a PostgreSQL database

The project follows a RESTful API architecture and uses Django ORM for database communication.

---

## Key Features

- RESTful API development
- Complete CRUD functionality
- PostgreSQL database integration
- Django ORM
- Django REST Framework serializers
- Request validation
- Error handling
- Task status management
- Due date management
- Function-based API views
- API testing with Postman

---

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Django | Web framework |
| Django REST Framework | REST API development |
| PostgreSQL | Database |
| Django ORM | Database operations |
| Postman | API testing |
| Git | Version control |
| GitHub | Project repository |

---

## Project Structure

```text
Project-3/
│
├── config/
│   ├── tasks/
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializer.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   │
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README-Project-3.md

Task Model

The task system stores information such as:

Title — Name of the task
Description — Details about the task
Status — Current state of the task
Due Date — Deadline of the task
Created At — Date and time when the task was created
Task Statuses

The API supports task status values such as:

Pending
In Progress
Completed
API Endpoints
1. Get All Tasks
GET /api/tasks/

Returns a list of all tasks.

2. Create a Task
POST /api/tasks/

Creates a new task.

Example request:

{
    "title": "Project Science",
    "description": "Complete database integration project",
    "status": "In_Progress",
    "due_date": "2026-08-22"
}

Example response:

{
    "id": 2,
    "title": "Project Science",
    "description": "Complete database integration project",
    "status": "In_Progress",
    "due_date": "2026-08-22",
    "created_at": "2026-08-15T09:02:58.561385Z"
}
3. Get a Specific Task
GET /api/tasks/<id>/

Returns the details of a specific task.

Example:

GET /api/tasks/2/
4. Update a Task
PUT /api/tasks/<id>/

Updates the complete task information.

Example:

PUT /api/tasks/2/
5. Partially Update a Task
PATCH /api/tasks/<id>/

Updates selected fields of an existing task without requiring all fields.

Example:

PATCH /api/tasks/2/
6. Delete a Task
DELETE /api/tasks/<id>/

Deletes the selected task from the database.

Example:

DELETE /api/tasks/2/
API Summary
Method	Endpoint	Function
GET	/api/tasks/	Get all tasks
POST	/api/tasks/	Create a task
GET	/api/tasks/<id>/	Get one task
PUT	/api/tasks/<id>/	Update a task
PATCH	/api/tasks/<id>/	Partially update a task
DELETE	/api/tasks/<id>/	Delete a task
Database Integration

The project uses PostgreSQL as the database.

Django ORM is used to communicate between the Django application and PostgreSQL.

The database stores task records and allows the API to perform:

Create
Read
Update
Delete

operations on task data.

Serializers

Django REST Framework serializers are used to:

Convert Django model objects into JSON
Convert incoming JSON data into Python/Django objects
Validate API request data
Save valid data to the database
API Views

The API is implemented using function-based views with Django REST Framework.

The project includes separate functions for:

Task list and creation
Task detail
Task retrieval
Task update
Task partial update
Task deletion
Error Handling

The API handles common errors including:

Invalid request data
Invalid task status
Task not found
Validation errors
Database-related errors

For example, if a requested task does not exist, the API returns an appropriate error response.

API Testing

The API was tested using Postman.

The following operations were tested:

POST     → Create Task
GET      → Retrieve Tasks
GET      → Retrieve Single Task
PUT      → Update Task
PATCH    → Partially Update Task
DELETE   → Delete Task

Successful API requests return appropriate HTTP status codes such as:

200 OK
201 Created
204 No Content
400 Bad Request
404 Not Found
Installation and Setup
1. Clone the Repository
git clone https://github.com/aroojabid9966-create/DecodeLabs-Internship.git

Move into the repository:

cd DecodeLabs-Internship
2. Create a Virtual Environment
python -m venv venv
3. Activate the Virtual Environment

For Windows:

venv\Scripts\activate
4. Install Dependencies
pip install -r requirements.txt
5. Configure the Database

Configure PostgreSQL database settings in the Django project's settings.

Database credentials should be kept secure and should not be committed to GitHub.

6. Run Migrations
python manage.py migrate
7. Start the Development Server
python manage.py runserver

The development server will run at:

http://127.0.0.1:8000/
Testing the API

After starting the server, use Postman to test the endpoints.

Example:

GET
http://127.0.0.1:8000/api/tasks/

Create a task:

POST
http://127.0.0.1:8000/api/tasks/

Access a specific task:

GET
http://127.0.0.1:8000/api/tasks/2/
Security

Sensitive information such as:

Database passwords
Secret keys
Environment variables

should not be committed to GitHub.

The project uses .gitignore to prevent sensitive and unnecessary files from being uploaded.

The virtual environment is also excluded from version control.

Project Status
Completed

The backend and database integration have been implemented with:

Django REST Framework
PostgreSQL
Task model
Serializers
Function-based API views
CRUD operations
API validation
Error handling
Postman testing
Learning Outcomes

This project demonstrates practical experience with:

Django backend development
REST API design
Django REST Framework
PostgreSQL database integration
Django ORM
Serializers
CRUD operations
HTTP methods
API testing
Git and GitHub workflow
Backend project structure
Author

Arooj Fatima

GitHub:

https://github.com/aroojabid9966-create
Project Repository

DecodeLabs Internship Repository

https://github.com/aroojabid9966-create/DecodeLabs-Internship
Project 3

Task Management REST API

Backend + Database Integration

Django REST Framework + PostgreSQL


